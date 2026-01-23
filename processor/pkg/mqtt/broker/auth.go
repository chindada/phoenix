package broker

import (
	"bytes"
	"net"
	"strings"

	mqtt "github.com/mochi-mqtt/server/v2"
	"github.com/mochi-mqtt/server/v2/packets"
)

type Authenticator func(userName, password string) error

type authHook struct {
	mqtt.HookBase

	authenticator Authenticator
}

// newAuthHook returns a new auth hook.
func newAuthHook(authenticator Authenticator) mqtt.Hook {
	return &authHook{
		authenticator: authenticator,
	}
}

// ID returns the ID of the hook.
func (h *authHook) ID() string {
	return "auth-hook"
}

// Provides indicates which hook methods this hook provides.
func (h *authHook) Provides(b byte) bool {
	base := []byte{
		mqtt.OnConnectAuthenticate,
		mqtt.OnACLCheck,
	}
	return bytes.Contains(base, []byte{b})
}

// OnConnectAuthenticate -.
func (h *authHook) OnConnectAuthenticate(cl *mqtt.Client, pk packets.Packet) bool {
	clientID := cl.ID
	userName := string(cl.Properties.Username)
	if strings.Compare(clientID, userName) != 0 {
		return false
	}
	password := string(pk.Connect.Password)
	if err := h.authenticator(userName, password); err != nil {
		return false
	}
	return true
}

// OnACLCheck -.
func (h *authHook) OnACLCheck(cl *mqtt.Client, topic string, _ bool) bool {
	if topic == "" || strings.Compare(topic, "#") == 0 {
		return false
	}
	if strings.HasPrefix(topic, "$SYS") && h.remoteIsLocal(cl) {
		return true
	}
	userName := string(cl.Properties.Username)
	if strings.Compare(cl.ID, userName) != 0 {
		return false
	}
	if strings.HasPrefix(topic, userName) {
		return true
	}
	return false
}

func (h *authHook) remoteIsLocal(cl *mqtt.Client) bool {
	resolveAddr, err := net.ResolveTCPAddr("tcp", cl.Net.Remote)
	if err != nil {
		return false
	}
	ifaces, err := net.Interfaces()
	if err != nil {
		return false
	}
	for _, i := range ifaces {
		addrs, aErr := i.Addrs()
		if aErr != nil {
			return false
		}
		for _, addr := range addrs {
			if v, ok := addr.(*net.IPNet); ok {
				if v.IP.To4() == nil {
					continue
				}
				if v.IP.Equal(resolveAddr.IP) {
					return true
				}
			}
		}
	}
	return false
}
