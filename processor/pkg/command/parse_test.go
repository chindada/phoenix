package command_test

import (
	"context"
	"os/exec"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"phoenix/processor/pkg/command"
)

func TestRunAndParse(t *testing.T) {
	// echo -e "line1\nline2" (but echo -e is not portable, use printf)
	ctx := context.Background()
	cmd := exec.CommandContext(ctx, "printf", "line1\nline2")
	lines, err := command.RunAndParse(cmd)
	require.NoError(t, err)
	assert.Equal(t, []string{"line1", "line2"}, lines)
}
