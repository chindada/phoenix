// Package eventbus provides a singleton, routed, publish-subscribe event bus.
package eventbus

import (
	"errors"
	"sync"

	"github.com/asaskevich/EventBus"
)

var (
	singleton *Bus
	once      sync.Once
)

// Bus is a wrapper around EventBus with hierarchical routing.
type Bus struct {
	bus    EventBus.Bus
	routes sync.Map // map[string]*Bus
}

// Get returns the singleton bus or a routed sub-bus.
func Get(route ...string) *Bus {
	once.Do(func() {
		singleton = &Bus{
			bus: EventBus.New(),
		}
	})

	if len(route) == 0 {
		return singleton
	}

	current := singleton
	for _, r := range route {
		v, ok := current.routes.Load(r)
		if !ok {
			newBus := &Bus{
				bus: EventBus.New(),
			}
			// LoadOrStore handles the race condition where another goroutine might have created it
			actual, _ := current.routes.LoadOrStore(r, newBus)
			v = actual
		}
		// Safe type assertion
		if b, isBus := v.(*Bus); isBus {
			current = b
		}
	}
	return current
}

// Publish publishes an event to a specific topic.
func (c *Bus) Publish(topic string, arg ...any) {
	c.bus.Publish(topic, arg...)
}

// SubscribeAsync subscribes to a topic asynchronously.
// Transactional determines whether subsequent callbacks for a topic are
// run serially (true) or concurrently (false).
func (c *Bus) SubscribeAsync(topic string, transactional bool, fn ...any) error {
	if len(fn) == 0 {
		return errors.New("fn length must be greater than 0")
	}

	for i := range fn {
		err := c.bus.SubscribeAsync(topic, fn[i], transactional)
		if err != nil {
			return err
		}
	}
	return nil
}

// Subscribe subscribes to a topic synchronously.
func (c *Bus) Subscribe(topic string, fn ...any) error {
	if len(fn) == 0 {
		return errors.New("fn length must be greater than 0")
	}

	for i := range fn {
		err := c.bus.Subscribe(topic, fn[i])
		if err != nil {
			return err
		}
	}
	return nil
}

// Unsubscribe unsubscribes from a topic.
func (c *Bus) Unsubscribe(topic string, fn ...any) error {
	if len(fn) == 0 {
		return errors.New("fn length must be greater than 0")
	}

	for i := len(fn) - 1; i >= 0; i-- {
		err := c.bus.Unsubscribe(topic, fn[i])
		if err != nil {
			return err
		}
	}
	return nil
}
