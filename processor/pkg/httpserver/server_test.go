package httpserver_test

import (
	"context"
	"net/http"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"phoenix/processor/pkg/httpserver"
)

func TestServer(t *testing.T) {
	handler := http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(http.StatusOK)
	})

	s := httpserver.New(handler, httpserver.Port("0")) // Use random port
	err := s.Start()
	require.NoError(t, err)

	port := s.GetListenPort()
	assert.NotEqual(t, "0", port)
	assert.NotEmpty(t, port)

	// Test if reachable
	ctx := context.Background()
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, "http://localhost:"+port, nil)
	require.NoError(t, err)

	resp, err := http.DefaultClient.Do(req)
	require.NoError(t, err)

	if err == nil {
		assert.Equal(t, http.StatusOK, resp.StatusCode)
		_ = resp.Body.Close()
	}
	err = s.Shutdown()
	assert.NoError(t, err)
}

func TestServerRandomPort(t *testing.T) {
	handler := http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(http.StatusOK)
	})

	s := httpserver.New(handler)
	err := s.StartWithRandomPort()
	require.NoError(t, err)
	defer func() {
		_ = s.Shutdown()
	}()

	port := s.GetListenPort()
	assert.NotEmpty(t, port)
	assert.NotEqual(t, "80", port) // default port is 80
}
