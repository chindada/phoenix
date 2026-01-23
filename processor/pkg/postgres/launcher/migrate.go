package launcher

import (
	"context"
	"errors"
	"fmt"
	"net"
	"time"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/source"
	"github.com/golang-migrate/migrate/v4/source/iofs"
	"github.com/jackc/pgx/v5"
	"go.uber.org/zap"

	phoenixMigrate "phoenix/processor/migrations/phoenix"
	"phoenix/processor/pkg/postgres/client"

	// postgres driver.
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const (
	_defaultAttempts = 20
	_defaultWait     = time.Second
)

type migrator struct {
	logger  *zap.Logger
	process ProcessManager

	port          string
	dbName        string
	listenAddress string
}

func (m *migrator) getListenAddress() string {
	if m.listenAddress == "*" {
		return localhost
	}
	return m.listenAddress
}

func (m *migrator) getFullPath() string {
	return fmt.Sprintf("postgres://%s:%s@%s/%s",
		defaultUser,
		defaultPass,
		net.JoinHostPort(m.getListenAddress(), m.port),
		m.dbName,
	)
}

func (m *migrator) getMigrationSource() (source.Driver, error) {
	switch m.dbName {
	case dbNamePhoenix:
		return iofs.New(phoenixMigrate.Asset, ".")
	default:
		panic("invalid database name")
	}
}

func (m *migrator) MigrateScheme(step *int) error {
	running, err := m.process.IsRunning()
	if err != nil {
		return err
	}
	if !running {
		err = m.process.StartDB()
		if err != nil {
			return err
		}
		defer func() {
			err = m.process.StopDB()
			if err != nil {
				panic(err)
			}
		}()
	}
	migInstance := &migrate.Migrate{}
	attempts := _defaultAttempts
	path := fmt.Sprintf("postgres://postgres:password@%s/%s%s",
		net.JoinHostPort(m.getListenAddress(), m.port), m.dbName, "?sslmode=disable")
	d, err := m.getMigrationSource()
	if err != nil {
		return err
	}
	for attempts > 0 {
		migInstance, err = migrate.NewWithSourceInstance("iofs", d, path)
		if err == nil {
			break
		}

		m.logger.Info("migrate trying to connect postgres", zap.Int("attempts_left", attempts))
		time.Sleep(_defaultWait)
		attempts--
	}
	if err != nil {
		return fmt.Errorf("postgres connect error in migrate: %w", err)
	}

	defer func() {
		_, _ = migInstance.Close()
	}()

	return m.migrate(migInstance, step)
}

func (m *migrator) migrate(migInstance *migrate.Migrate, step *int) error {
	if step == nil {
		err := migInstance.Up()
		if err != nil {
			if errors.Is(err, migrate.ErrNoChange) {
				m.logger.Info("migrate no change")
				return nil
			}
			return fmt.Errorf("migrate db error: %w", err)
		}
		m.logger.Info("migrate success")
		return nil
	}
	current, dirty, err := migInstance.Version()
	if err != nil && !errors.Is(err, migrate.ErrNilVersion) {
		return fmt.Errorf("migrate db error: %w", err)
	} else if dirty {
		return errors.New("database is dirty")
	}
	if current > 0 && *step < 0 && int(current)+*step < 0 {
		return errors.New("step is too small")
	}
	return migInstance.Steps(*step)
}

func (m *migrator) CurrentMigrationVersion() (int, error) {
	running, err := m.process.IsRunning()
	if err != nil {
		return 0, err
	}
	if !running {
		err = m.process.StartDB()
		if err != nil {
			return 0, err
		}
		defer func() {
			err = m.process.StopDB()
			if err != nil {
				panic(err)
			}
		}()
	}
	c, err := client.New(
		m.getFullPath(),
		client.MaxPoolSize(1),
		client.AddLogger(m.logger),
	)
	if err != nil {
		return 0, err
	}
	defer c.Close()
	sql, args, err := c.Builder().
		Select("version, dirty").
		From(migrationTable).
		ToSql()
	if err != nil {
		return 0, err
	}
	row := c.Pool().QueryRow(context.Background(), sql, args...)
	var mig int
	var dirty bool
	if err = row.Scan(&mig, &dirty); err != nil {
		if errors.Is(err, pgx.ErrNoRows) {
			return 0, nil
		}
		return 0, err
	}
	if dirty {
		return 0, errors.New("database is dirty")
	}
	return mig, nil
}
