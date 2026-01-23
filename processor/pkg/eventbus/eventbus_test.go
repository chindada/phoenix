package eventbus_test

import (
	"sync"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"phoenix/processor/pkg/eventbus"
)

func TestGet(t *testing.T) {
	b1 := eventbus.Get()
	b2 := eventbus.Get()
	assert.Equal(t, b1, b2, "Get() should return singleton")

	b3 := eventbus.Get("route1")
	assert.NotEqual(t, b1, b3, "Get('route1') should return different bus")

	b4 := eventbus.Get("route1")
	assert.Equal(t, b3, b4, "Get('route1') should return same bus instance")

	b5 := eventbus.Get("route1", "subroute")
	assert.NotEqual(t, b3, b5, "Get('route1', 'subroute') should be different from parent")
}

func TestPubSub(t *testing.T) {
	b := eventbus.Get("test_pubsub")
	var wg sync.WaitGroup
	wg.Add(1)

	var received string
	err := b.Subscribe("topic", func(arg string) {
		received = arg
		wg.Done()
	})
	require.NoError(t, err)

	b.Publish("topic", "hello")

	done := make(chan struct{})
	go func() {
		wg.Wait()
		close(done)
	}()

	select {
	case <-done:
		assert.Equal(t, "hello", received)
	case <-time.After(1 * time.Second):
		t.Fatal("timeout waiting for event")
	}
}

func TestUnsubscribe(t *testing.T) {
	b := eventbus.Get("test_unsub")
	count := 0
	handler := func() {
		count++
	}

	err := b.Subscribe("topic", handler)
	require.NoError(t, err)

	b.Publish("topic")

	err = b.Unsubscribe("topic", handler)
	require.NoError(t, err)

	b.Publish("topic")

	assert.Equal(t, 1, count)
}
