//go:build windows

package command

import (
	"context"
	"os/exec"
	"syscall"
)

func NewCMD(command string, arg ...string) *exec.Cmd {
	c := exec.CommandContext(context.Background(), command, arg...)
	c.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
	return c
}
