package launcher

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"strings"
	"sync"
	"syscall"

	"go.uber.org/zap"
)

type processManager struct {
	*executor

	logger *zap.Logger
	mutex  sync.Mutex

	port          string
	dbName        string
	listenAddress string
	enableLog     bool

	socketPath      string
	exporterProcess *exec.Cmd
}

func (p *processManager) Logger() *zap.Logger {
	return p.logger
}

func (p *processManager) GetSocketPath() string {
	return p.socketPath
}

func (p *processManager) RunExporter() error {
	_ = os.Setenv("DATA_SOURCE_URI", fmt.Sprintf("%s:%s/postgres?sslmode=disable", p.getListenAddress(), p.port))
	_ = os.Setenv("DATA_SOURCE_USER", defaultUser)
	_ = os.Setenv("DATA_SOURCE_PASS", defaultPass)
	args := []string{"--log.level=error"}
	cmd := p.newCMD(p.getCliExport(), args...)
	err := cmd.Start()
	if err != nil {
		return err
	}
	p.exporterProcess = cmd
	return nil
}

func (p *processManager) getListenAddress() string {
	if p.listenAddress == "*" {
		return localhost
	}
	return p.listenAddress
}

func (p *processManager) InitDB(start bool) error {
	err := p.InitDataDir()
	if err != nil {
		return err
	}
	if err = p.StartDB(); err != nil {
		return err
	} else if err = p.createDB(); err != nil {
		return err
	}
	if !start {
		return p.StopDB()
	}
	return nil
}

func (p *processManager) InitDataDir() error {
	p.mutex.Lock()
	defer p.mutex.Unlock()

	if err := p.writePWfile(); err != nil {
		return err
	}
	args := []string{
		"-D", p.GetDataPath(),
		"-U", defaultUser,
		"-E", "UTF8",
		"--no-locale",
		fmt.Sprintf("--pwfile=./%s", filePWD),
	}
	cmd := p.newCMD(p.getCliInitDB(), args...)
	p.logger.Info("initializing database...")
	err := cmd.Start()
	if err != nil {
		return err
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	if err = os.Remove(filePWD); err != nil {
		return err
	}
	p.logger.Info("database initialized")
	return nil
}

func (p *processManager) createDB() error {
	args := []string{
		"-U", defaultUser,
		"-h", p.getListenAddress(),
		"-p", p.port,
		"-c", fmt.Sprintf("CREATE DATABASE %s", p.dbName),
	}
	cmd := p.newCMD(p.getCliPsql(), args...)
	p.logger.Info("creating database...")
	err := cmd.Start()
	if err != nil {
		return err
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	p.logger.Info("database created")
	return nil
}

func (p *processManager) IsRunning() (bool, error) {
	p.mutex.Lock()
	defer p.mutex.Unlock()

	args := []string{
		"-D", p.GetDataPath(),
		"status",
	}
	cmd := p.newCMDWithoutSetSTD(p.getCliPGCtl(), args...)
	output, _ := cmd.Output()
	outputStr := string(output)
	if strings.Contains(outputStr, "PID") {
		p.extractSocketPath(outputStr)
		return true, nil
	}
	return false, nil
}

func (p *processManager) extractSocketPath(input string) {
	for line := range strings.SplitSeq(input, "\n") {
		for word := range strings.FieldsSeq(line) {
			re := regexp.MustCompile(`"(\S+)=(\S+)"`)
			matches := re.FindStringSubmatch(word)
			if len(matches) > 2 && matches[1] == "unix_socket_directories" {
				_, err := os.Stat(matches[2])
				if err == nil {
					p.socketPath = filepath.Clean(matches[2])
					return
				}
			}
		}
	}
}

func (p *processManager) StartDB() error {
	running, err := p.IsRunning()
	if err != nil {
		return err
	} else if running {
		p.logger.Info("database already running")
		return nil
	}
	p.mutex.Lock()
	defer p.mutex.Unlock()

	opts := p.serverOption()
	args := []string{}
	args = append(args, "-D", p.GetDataPath())
	args = append(args, "-o", opts)
	if p.enableLog {
		args = append(args, "-l", filepath.Join(p.GetDataPath(), fileLog))
	}
	args = append(args, "-s", "-w", "start")
	cmd := p.newCMD(p.getCliPGCtl(), args...)
	p.logger.Info("starting database...")
	err = cmd.Start()
	if err != nil {
		return err
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	p.extractSocketPath(opts)
	p.logger.Info("database started")
	return nil
}

func (p *processManager) StopDB() error {
	running, err := p.IsRunning()
	if err != nil {
		return err
	} else if !running {
		p.logger.Info("database already stopped")
		return nil
	}

	if p.exporterProcess != nil {
		p.logger.Info("stopping exporter...")
		_ = p.exporterProcess.Process.Signal(syscall.SIGTERM)
	}

	p.mutex.Lock()
	defer p.mutex.Unlock()

	args := []string{}
	args = append(args, "-D", p.GetDataPath())
	args = append(args, "-o", p.serverOption())
	if p.enableLog {
		args = append(args, "-l", filepath.Join(p.GetDataPath(), fileLog))
	}
	args = append(args, "-w", "stop")
	cmd := p.newCMD(p.getCliPGCtl(), args...)
	p.logger.Info("stopping database...")
	err = cmd.Start()
	if err != nil {
		return err
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	p.socketPath = ""
	p.logger.Info("database stopped")
	return nil
}

func (p *processManager) ClearDB() error {
	running, err := p.IsRunning()
	if err != nil {
		return err
	}
	if running {
		if err = p.StopDB(); err != nil {
			return err
		}
	}

	p.mutex.Lock()
	defer p.mutex.Unlock()

	if err = os.RemoveAll(p.GetDataPath()); err != nil {
		return err
	}
	return nil
}

func (p *processManager) writePWfile() error {
	f, err := os.Create(filePWD)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = fmt.Fprintf(f, "%s\n", defaultPass)
	if err != nil {
		return err
	}
	return nil
}

func (p *processManager) DatabaseAlreadyExists() bool {
	p.mutex.Lock()
	defer p.mutex.Unlock()

	path := filepath.Join(p.GetDataPath(), fileConfig)
	_, err := os.Stat(path)
	return err == nil
}
