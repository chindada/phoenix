package launcher

import "go.uber.org/zap"

type Option func(*Config)

func DBName(dbName string) Option {
	return func(c *Config) {
		if dbName != "" {
			c.DBName = dbName
		}
	}
}

func Listen(listen string) Option {
	return func(c *Config) {
		if listen != "" {
			c.ListenAddress = listen
		}
	}
}

func Port(port string) Option {
	return func(c *Config) {
		if port != "" {
			c.Port = port
		}
	}
}

func AddLogger(base *zap.Logger) Option {
	return func(c *Config) {
		c.Logger = base
	}
}

func BinaryRoot(root string) Option {
	return func(c *Config) {
		c.BinaryRoot = root
	}
}

func Verbose() Option {
	return func(c *Config) {
		c.Verbose = true
	}
}

func EnableLog() Option {
	return func(c *Config) {
		c.EnableLog = true
	}
}
