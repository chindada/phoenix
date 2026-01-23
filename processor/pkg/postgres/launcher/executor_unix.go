//go:build !windows

package launcher

import (
	"context"
	"os/exec"
	"os/user"
	"strconv"
	"syscall"

	"github.com/spf13/cast"
)

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
