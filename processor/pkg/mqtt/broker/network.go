package broker

import (
	"context"
	"net"
	"time"
)

func getPortIsUsed(port string) bool {
	dialer := &net.Dialer{
		Timeout: 500 * time.Millisecond,
	}
	conn, err := dialer.DialContext(context.Background(), "tcp", net.JoinHostPort("127.0.0.1", port))
	if err != nil && conn != nil {
		return false
	}
	if conn != nil {
		defer func() {
			if err = conn.Close(); err != nil {
				return
			}
		}()
		return true
	}
	cfg := &net.ListenConfig{}
	ln, err := cfg.Listen(context.Background(), "tcp", net.JoinHostPort("", port))
	if err != nil {
		return true
	}
	if ln != nil {
		defer func() {
			if err = ln.Close(); err != nil {
				return
			}
		}()
	}
	return false
}
