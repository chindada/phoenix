package launcher

import (
	"errors"
	"os"
	"path/filepath"

	"go.uber.org/zap"
)

type Config struct {
	DBName        string
	ListenAddress string
	Port          string
	Logger        *zap.Logger
	BinaryRoot    string
	Verbose       bool
	EnableLog     bool
}

type launcher struct {
	ProcessManager
	BackupManager
	Migrator
	Archiver

	logger *zap.Logger
}

func (l *launcher) Logger() *zap.Logger {
	return l.logger
}

func New(opts ...Option) (Launcher, error) {
	cfg := &Config{
		ListenAddress: defaultListenAddress,
		Port:          defaultPort,
	}

	ex, err := os.Executable()
	if err != nil {
		return nil, err
	}
	// default backup root relative to executable
	backupRoot := filepath.Join(filepath.Dir(ex), "..", "db_backup")

	for _, opt := range opts {
		opt(cfg)
	}

	if cfg.Logger == nil {
		l, zErr := zap.NewProduction()
		if zErr != nil {
			return nil, zErr
		}
		cfg.Logger = l
	}

	if cfg.DBName == "" {
		return nil, errors.New("database name is required")
	}
	if cfg.DBName != dbNameMojave && cfg.DBName != dbNameVentura {
		return nil, errors.New("invalid database name")
	}

	// Create backup root if not exists
	if err = os.MkdirAll(backupRoot, os.ModePerm); err != nil {
		return nil, err
	}
	if err = os.Chmod(backupRoot, os.ModePerm); err != nil {
		return nil, err
	}

	exec := &executor{
		binaryRoot: cfg.BinaryRoot,
		verbose:    cfg.Verbose,
	}

	pm := &processManager{
		executor:      exec,
		logger:        cfg.Logger,
		port:          cfg.Port,
		dbName:        cfg.DBName,
		listenAddress: cfg.ListenAddress,
		enableLog:     cfg.EnableLog,
	}

	mig := &migrator{
		logger:        cfg.Logger,
		process:       pm,
		port:          cfg.Port,
		dbName:        cfg.DBName,
		listenAddress: cfg.ListenAddress,
	}

	bm := &backupManager{
		executor:      exec,
		logger:        cfg.Logger,
		process:       pm,
		migrator:      mig,
		backupRoot:    backupRoot,
		port:          cfg.Port,
		dbName:        cfg.DBName,
		listenAddress: cfg.ListenAddress,
	}

	ar := &archiver{
		backupManager: bm,
		backupRoot:    backupRoot,
		dbName:        cfg.DBName,
	}

	return &launcher{
		ProcessManager: pm,
		BackupManager:  bm,
		Migrator:       mig,
		Archiver:       ar,
		logger:         cfg.Logger,
	}, nil
}
