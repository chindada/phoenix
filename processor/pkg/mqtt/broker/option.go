package broker

import "go.uber.org/zap"

type Option func(*mqBkr)

func AddLogger(base *zap.Logger) Option {
	return func(c *mqBkr) {
		c.logger = base
	}
}

func AddAuthenticator(authenticator Authenticator) Option {
	return func(c *mqBkr) {
		err := c.server.AddHook(newAuthHook(authenticator), nil)
		if err != nil {
			panic(err)
		}
	}
}

func Port(port string) Option {
	return func(c *mqBkr) {
		c.port = port
	}
}
