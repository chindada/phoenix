package log_test

import (
	"testing"

	"github.com/stretchr/testify/assert"

	"phoenix/processor/pkg/log"
)

func TestLog(t *testing.T) {
	// Just verify we can call L() and S() without panic
	l := log.L()
	assert.NotNil(t, l)
	l.Info("test info log")

	s := log.S()
	assert.NotNil(t, s)
	s.Info("test sugar log")

	// Test deprecated
	assert.Equal(t, l, log.Get())
	assert.Equal(t, s, log.GetSugar())
}
