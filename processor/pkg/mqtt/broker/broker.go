// Package broker package broker
package broker

import (
	"crypto/tls"
	"fmt"
	"io"
	"log/slog"
	"os"
	"sync"
	"time"

	"github.com/google/uuid"
	mqtt "github.com/mochi-mqtt/server/v2"
	"github.com/mochi-mqtt/server/v2/listeners"
	"github.com/mochi-mqtt/server/v2/packets"
	"go.uber.org/zap"
)

const (
	_defaultPort = "18883"
)

type Bkr interface {
	Serve() error
	Close() error
	Publish(topic string, payload []byte) error
	Subscribe(topic string, callbackFn mqtt.InlineSubFn) int
	Unsubscribe(id int)
	DisconnectClient(clientID string) error
}

type mqBkr struct {
	logger *zap.Logger

	server *mqtt.Server

	subscriptionID     int
	subscriptionTopic  map[int]string
	subscriptionIDLock sync.Mutex

	port string
}

func New(opts ...Option) (Bkr, error) {
	m := &mqBkr{
		subscriptionTopic: make(map[int]string),
		server: mqtt.New(&mqtt.Options{
			InlineClient:             true,
			Logger:                   slog.New(slog.NewTextHandler(io.Discard, nil)),
			ClientNetWriteBufferSize: 4096,
			ClientNetReadBufferSize:  4096,
			SysTopicResendInterval:   10,
		}),
	}
	for _, opt := range opts {
		opt(m)
	}
	if m.port == "" {
		m.port = _defaultPort
	}
	crt, err := m.readCerts()
	if err != nil {
		return nil, err
	}
	cfg := listeners.Config{
		ID:      uuid.NewString(),
		Address: fmt.Sprintf(":%s", m.port),
		TLSConfig: &tls.Config{
			InsecureSkipVerify: true,
			Certificates:       []tls.Certificate{*crt},
		},
	}
	tcp := listeners.NewTCP(cfg)
	err = m.server.AddListener(tcp)
	if err != nil {
		return nil, err
	}
	return m, nil
}

func (m *mqBkr) readCerts() (*tls.Certificate, error) {
	crtBytes, err := os.ReadFile("certs/moldlink-center.com.crt")
	if err != nil {
		return nil, err
	}
	keyBytes, err := os.ReadFile("certs/moldlink-center.com.key")
	if err != nil {
		return nil, err
	}
	cert, err := tls.X509KeyPair(crtBytes, keyBytes)
	if err != nil {
		return nil, err
	}
	return &cert, nil
}

func (m *mqBkr) Serve() error {
	if m.logger == nil {
		l, err := zap.NewProduction()
		if err != nil {
			return err
		}
		m.logger = l
	}
	errChan := make(chan error)
	go func() {
		err := m.server.Serve()
		if err != nil {
			errChan <- err
		}
	}()
	ticker := time.NewTicker(time.Second)
	for {
		select {
		case err := <-errChan:
			return err
		case <-ticker.C:
			if getPortIsUsed(m.port) {
				m.logger.Info("MQTT Serve On", zap.String("port", m.port))
				return nil
			}
		}
	}
}

func (m *mqBkr) Close() error {
	return m.server.Close()
}

func (m *mqBkr) DisconnectClient(clientID string) error {
	cl, ok := m.server.Clients.Get(clientID)
	if !ok {
		return nil
	}
	return m.server.DisconnectClient(cl, packets.CodeDisconnect)
}

func (m *mqBkr) getSubscriptionID(topic string) int {
	m.subscriptionIDLock.Lock()
	defer m.subscriptionIDLock.Unlock()
	m.subscriptionID++
	m.subscriptionTopic[m.subscriptionID] = topic
	return m.subscriptionID
}

func (m *mqBkr) getTopic(id int) string {
	if id < 0 {
		return ""
	}
	m.subscriptionIDLock.Lock()
	defer m.subscriptionIDLock.Unlock()
	topic, ok := m.subscriptionTopic[id]
	if !ok {
		return ""
	}
	delete(m.subscriptionTopic, id)
	return topic
}

func (m *mqBkr) Publish(topic string, payload []byte) error {
	return m.server.Publish(topic, payload, false, 1)
}

func (m *mqBkr) Subscribe(topic string, callbackFn mqtt.InlineSubFn) int {
	id := m.getSubscriptionID(topic)
	err := m.server.Subscribe(topic, id, callbackFn)
	if err != nil {
		return -1
	}
	return id
}

func (m *mqBkr) Unsubscribe(id int) {
	topic := m.getTopic(id)
	if topic == "" {
		return
	}
	err := m.server.Unsubscribe(topic, id)
	if err != nil {
		m.logger.Error("Unsubscribe error", zap.Error(err))
	}
}
