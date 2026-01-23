//go:build !windows

package command

import (
	"context"
	"os/exec"
)

func NewCMD(command string, arg ...string) *exec.Cmd {
	return exec.CommandContext(context.Background(), command, arg...)
}
