//go:build windows

package launcher

import (
	"context"
	"os/exec"
	"syscall"
)

func (e *executor) newCMD(command string, args ...string) *exec.Cmd {
	cmd := exec.CommandContext(context.Background(), command, args...)
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
	if e.verbose {
		stderr, _ := cmd.StderrPipe()
		stdout, _ := cmd.StdoutPipe()
		e.pipeStderr(stderr)
		e.pipeStdout(stdout)
	}
	return cmd
}

func (e *executor) newCMDWithoutSetSTD(command string, args ...string) *exec.Cmd {
	return exec.CommandContext(context.Background(), command, args...)
}
