// Package client implements client connection.
package client

import (
	"context"
	"errors"
	"time"

	"github.com/Masterminds/squirrel"
	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
	"github.com/spf13/cast"
	"go.uber.org/zap"
)

const (
	_defaultMaxPoolSize  = 1
	_defaultConnAttempts = 10
	_defaultConnTimeout  = 3 * time.Second
)

type PGClient interface {
	Close()
	Pool() *pgxpool.Pool
	Rollback(ctx context.Context, tx pgx.Tx)
	Builder() squirrel.StatementBuilderType
}

// postgresClient -.
type postgresClient struct {
	logger *zap.Logger

	maxPoolSize  int
	connAttempts int
	connTimeout  time.Duration

	builder squirrel.StatementBuilderType
	pool    *pgxpool.Pool
}

// New -.
func New(url string, opts ...Option) (PGClient, error) {
	pg := &postgresClient{
		maxPoolSize:  _defaultMaxPoolSize,
		connAttempts: _defaultConnAttempts,
		connTimeout:  _defaultConnTimeout,
	}

	for _, opt := range opts {
		opt(pg)
	}

	if pg.logger == nil {
		l, err := zap.NewProduction()
		if err != nil {
			panic(err)
		}
		pg.logger = l
	}

	// builder
	pg.builder = squirrel.StatementBuilder.PlaceholderFormat(squirrel.Dollar)

	// pool
	poolConfig, err := pgxpool.ParseConfig(url)
	if err != nil {
		return nil, err
	}

	poolConfig.MaxConns = cast.ToInt32(2 * pg.maxPoolSize / 2)
	poolConfig.MinConns = cast.ToInt32(pg.maxPoolSize / 2)

	for pg.connAttempts > 0 {
		pg.pool, err = pgxpool.NewWithConfig(context.Background(), poolConfig)
		if err != nil {
			return nil, err
		}
		if err = pg.pool.Ping(context.Background()); err == nil {
			return pg, nil
		}
		pg.logger.Warn("postgres trying connect", zap.Int("attempts_left", pg.connAttempts-1))
		pg.connAttempts--
		time.Sleep(pg.connTimeout)
	}
	return nil, errors.New("postgres connection attempts exceeded")
}

// Close -.
func (p *postgresClient) Close() {
	if p.pool != nil {
		p.pool.Reset()
		p.pool.Close()
	}
}

// Pool -.
func (p *postgresClient) Pool() *pgxpool.Pool {
	return p.pool
}

func (p *postgresClient) Builder() squirrel.StatementBuilderType {
	return p.builder
}

func (p *postgresClient) Rollback(ctx context.Context, tx pgx.Tx) {
	_ = tx.Rollback(ctx)
}
