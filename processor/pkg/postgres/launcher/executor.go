package launcher

import (
	"context"
	"io"
	"os"
	"os/exec"
	"os/user"
	"path/filepath"
	"strconv"
	"syscall"

	"github.com/spf13/cast"
)

type executor struct {
	binaryRoot string
	verbose    bool
}

const (
	cliInitDB  = "initdb"
	cliPsql    = "psql"
	cliPGCtl   = "pg_ctl"
	cliDump    = "pg_dump"
	cliRestore = "pg_restore"
)

const (
	cliExport = "postgres_exporter"
)

func (e *executor) getCliInitDB() string {
	if e.binaryRoot == "" {
		return cliInitDB
	}
	return filepath.Join(e.binaryRoot, cliInitDB)
}

func (e *executor) getCliPsql() string {
	if e.binaryRoot == "" {
		return cliPsql
	}
	return filepath.Join(e.binaryRoot, cliPsql)
}

func (e *executor) getCliPGCtl() string {
	if e.binaryRoot == "" {
		return cliPGCtl
	}
	return filepath.Join(e.binaryRoot, cliPGCtl)
}

func (e *executor) getCliDump() string {
	if e.binaryRoot == "" {
		return cliDump
	}
	return filepath.Join(e.binaryRoot, cliDump)
}

func (e *executor) getCliRestore() string {
	if e.binaryRoot == "" {
		return cliRestore
	}
	return filepath.Join(e.binaryRoot, cliRestore)
}

func (e *executor) getCliExport() string {
	if e.binaryRoot == "" {
		return cliExport
	}
	return filepath.Join(e.binaryRoot, cliExport)
}

func (e *executor) pipeStdout(src io.ReadCloser) {
	go func() {
		_, _ = io.Copy(os.Stdout, src)
	}()
}

func (e *executor) pipeStderr(src io.ReadCloser) {
	go func() {
		_, _ = io.Copy(os.Stderr, src)
	}()
}

func (e *executor) getPosgresUser() *user.User {
	u, err := user.Lookup(defaultUser)
	if err != nil {
		return nil
	}
	return u
}

func (e *executor) getCMDCrendential() *syscall.Credential {
	u := e.getPosgresUser()
	if u == nil {
		return nil
	}
	uid, err := strconv.Atoi(u.Uid)
	if err != nil {
		return nil
	}
	gid, err := strconv.Atoi(u.Gid)
	if err != nil {
		return nil
	}
	return &syscall.Credential{Uid: cast.ToUint32(uid), Gid: cast.ToUint32(gid)}
}

func (e *executor) newCMD(command string, args ...string) *exec.Cmd {
	cmd := exec.CommandContext(context.Background(), command, args...)
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Credential: e.getCMDCrendential(),
	}
	if e.verbose {
		stderr, _ := cmd.StderrPipe()
		stdout, _ := cmd.StdoutPipe()
		e.pipeStderr(stderr)
		e.pipeStdout(stdout)
	}
	return cmd
}

func (e *executor) newCMDWithoutSetSTD(command string, args ...string) *exec.Cmd {
	cmd := exec.CommandContext(context.Background(), command, args...)
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Credential: e.getCMDCrendential(),
	}
	return cmd
}
