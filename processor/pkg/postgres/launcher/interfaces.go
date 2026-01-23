package launcher

import (
	"errors"
	"time"

	"go.uber.org/zap"
)

var ErrDatabaseAlreadyExists = errors.New("database already exists")

// ProcessManager manages the lifecycle of the postgres process.
type ProcessManager interface {
	InitDB(start bool) error
	InitDataDir() error
	StartDB() error
	StopDB() error
	IsRunning() (bool, error)
	ClearDB() error
	DatabaseAlreadyExists() bool
	GetDataPath() string
	GetSocketPath() string
	RunExporter() error
}

// BackupManager manages database backups and restorations.
type BackupManager interface {
	Backup(auto bool, req BackupRequest) error
	RestoreDatabase(name string) error
	ListBackups() ([]Backup, error)
	DeleteBackup(name string) error
}

// Migrator manages database migrations.
type Migrator interface {
	MigrateScheme(step *int) error
	CurrentMigrationVersion() (int, error)
}

// Archiver handles zip archiving of data.
type Archiver interface {
	Zip(zipName, sourceDir string) error
	LoadBackupArchiveFile(path string) error
}

// Launcher composes all management interfaces.
type Launcher interface {
	ProcessManager
	BackupManager
	Migrator
	Archiver
	Logger() *zap.Logger
}

type Backup struct {
	BackupRequest

	Name             string
	Path             string
	MigrationVersion int
	CreatedAt        time.Time
}

type BackupRequest struct {
	Note    string
	Version string
}

type metaData struct {
	DBName     string `json:"db_name"`
	Name       string `json:"name"`
	Note       string `json:"note"`
	Version    string `json:"version"`
	Migration  int    `json:"migration"`
	BackupTime string `json:"backup_time"`
}
