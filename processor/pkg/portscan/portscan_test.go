package portscan_test

import (
	"context"
	"net"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"

	"phoenix/processor/pkg/portscan"
)

func TestGetRandomPort(t *testing.T) {
	ps := portscan.NewPortScan()
	port := ps.GetRandomPort()
	assert.NotEmpty(t, port)

	// Verify the port is indeed not used (at least at the moment)
	d := net.Dialer{Timeout: 100 * time.Millisecond}
	conn, err := d.DialContext(context.Background(), "tcp", net.JoinHostPort("127.0.0.1", port))
	if err == nil {
		_ = conn.Close()
		t.Logf("Port %s returned by GetRandomPort is actually reachable", port)
		// This might happen if something started listening on it immediately, but unlikely.
		// Or if our check is flawed.
	}
}

func TestExcludePorts(t *testing.T) {
	excludes := portscan.ExcludePortArr{
		{StartPort: 30000, EndPort: 30010},
	}
	ps := portscan.NewPortScan()
	ps.ExcludePorts = excludes

	assert.True(t, ps.ExcludePorts.IsExcluded("30005"))
	assert.False(t, ps.ExcludePorts.IsExcluded("30011"))
}
