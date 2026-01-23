// Package portscan package portscan
package portscan

import (
	"context"
	"crypto/rand"
	"math/big"
	"net"
	"strconv"
	"time"
)

const (
	_target       = "127.0.0.1"
	_minPort      = 30000
	_maxPortRange = 30000
	_maxRetries   = 100
)

func (p *PortScan) GetRandomPort() string {
	// If ExcludePorts is nil, we assume we haven't scanned yet.
	if p.ExcludePorts == nil {
		_, _ = p.Scan()
	}

	for range _maxRetries {
		randomOffset, _ := rand.Int(rand.Reader, big.NewInt(_maxPortRange))
		port := randomOffset.Int64() + _minPort
		portStr := strconv.FormatInt(port, 10)

		if p.ExcludePorts.IsExcluded(portStr) {
			continue
		}

		if !p.GetPortIsUsed(portStr) {
			return portStr
		}
	}
	return ""
}

func (p *PortScan) GetPortIsUsed(port string) bool {
	d := net.Dialer{Timeout: 500 * time.Millisecond}
	conn, err := d.DialContext(context.Background(), "tcp", net.JoinHostPort(_target, port))
	if err != nil {
		return false
	}
	if conn != nil {
		_ = conn.Close()
		return true
	}
	return false
}
