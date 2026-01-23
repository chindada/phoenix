package launcher

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"time"

	"go.uber.org/zap"
)

type backupManager struct {
	*executor

	logger *zap.Logger

	process  ProcessManager
	migrator Migrator

	backupRoot    string
	port          string
	dbName        string
	listenAddress string
}

func (b *backupManager) getListenAddress() string {
	if b.listenAddress == "*" {
		return localhost
	}
	return b.listenAddress
}

func (b *backupManager) createBackupPath(name string) (string, error) {
	if name == "" {
		return "", errors.New("backup name is required")
	}
	path := filepath.Join(b.backupRoot, name)
	if err := os.MkdirAll(path, os.ModePerm); err != nil {
		return "", err
	}
	if err := os.Chmod(path, os.ModePerm); err != nil {
		return "", err
	}
	return path, nil
}

func (b *backupManager) Backup(auto bool, req BackupRequest) error {
	running, err := b.process.IsRunning()
	if err != nil {
		return err
	}
	if !running {
		err = b.process.StartDB()
		if err != nil {
			return err
		}
		defer func() {
			err = b.process.StopDB()
			if err != nil {
				panic(err)
			}
		}()
	}
	name := fmt.Sprintf("%s-%s", b.dbName, time.Now().Format(defaultDateLayout))
	if auto {
		if err = b.deleteAutoBackup(); err != nil {
			return err
		}
	}
	backUpPath, err := b.createBackupPath(name)
	if err != nil {
		return err
	}
	args := []string{}
	args = append(args, "-Fd")
	args = append(args, "-f", backUpPath)
	args = append(args, "-p", b.port)
	args = append(args, "-h", b.getListenAddress())
	args = append(args, "-U", defaultUser)
	args = append(args, b.dbName)
	cmd := b.newCMD(b.getCliDump(), args...)
	err = cmd.Start()
	if err != nil {
		return err
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	meta, err := b.newMeta(auto, req)
	if err != nil {
		return err
	}
	metaPath := filepath.Join(backUpPath, backupMetaFile)
	content, err := json.Marshal(meta)
	if err != nil {
		return err
	}
	if err = os.WriteFile(metaPath, content, 0o600); err != nil {
		return err
	}
	return nil
}

func (b *backupManager) DeleteBackup(name string) error {
	backups, err := b.ListBackups()
	if err != nil {
		return err
	}
	backup, ok := b.backupsToMap(backups)[name]
	if !ok {
		return fmt.Errorf("backup:%s not found", name)
	}
	return os.RemoveAll(backup.Path)
}

func (b *backupManager) deleteAutoBackup() error {
	backups, err := b.ListBackups()
	if err != nil {
		return err
	}
	for _, bu := range backups {
		meta, lErr := b.loadMeta(bu.Path)
		if lErr != nil {
			return lErr
		}
		if strings.HasPrefix(meta.Name, fmt.Sprintf("%s-auto-", b.dbName)) {
			if err = os.RemoveAll(bu.Path); err != nil {
				return err
			}
		}
	}
	return nil
}

func (b *backupManager) RestoreDatabase(name string) error {
	if name == "" {
		return errors.New("name is required")
	}
	backups, err := b.ListBackups()
	if err != nil {
		return err
	}
	backup, ok := b.backupsToMap(backups)[name]
	if !ok {
		return fmt.Errorf("backup:%s not found", name)
	}
	meta, err := b.newMeta(false, BackupRequest{})
	if err != nil {
		return err
	}
	if meta.Migration < backup.MigrationVersion {
		return fmt.Errorf("backup migration:%d is greater than current:%d", backup.MigrationVersion, meta.Migration)
	}
	if err = b.process.ClearDB(); err != nil {
		return err
	}
	if err = b.process.InitDataDir(); err != nil {
		return err
	}
	err = b.process.StartDB()
	if err != nil {
		return err
	}
	defer func() {
		err = b.process.StopDB()
		if err != nil {
			panic(err)
		}
	}()
	args := []string{}
	args = append(args, "-U", defaultUser)
	args = append(args, "-h", b.getListenAddress())
	args = append(args, "-p", b.port)
	args = append(args, "-C")
	args = append(args, "-d", dbNameRoot)
	args = append(args, backup.Path)
	cmd := b.newCMD(b.getCliRestore(), args...)
	b.logger.Info("restoring database", zap.String("name", name))
	err = cmd.Start()
	if err != nil {
		return err
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	b.logger.Info("database restored")
	return nil
}

func (b *backupManager) backupsToMap(backups []Backup) map[string]*Backup {
	result := map[string]*Backup{}
	for i, bu := range backups {
		result[bu.Name] = &backups[i]
	}
	return result
}

func (b *backupManager) ListBackups() ([]Backup, error) {
	files, err := os.ReadDir(b.backupRoot)
	if err != nil {
		return nil, err
	}
	result := []Backup{}
	for _, f := range files {
		if f.IsDir() {
			meta, lErr := b.loadMeta(filepath.Join(b.backupRoot, f.Name()))
			if lErr != nil {
				continue
			}
			createTime, pErr := time.ParseInLocation(
				defaultDateLayout,
				meta.BackupTime,
				time.Local,
			)
			if pErr != nil {
				return nil, pErr
			}
			bu := Backup{
				Name:             meta.Name,
				Path:             filepath.Join(b.backupRoot, f.Name()),
				CreatedAt:        createTime,
				MigrationVersion: meta.Migration,
				BackupRequest: BackupRequest{
					Note:    meta.Note,
					Version: meta.Version,
				},
			}
			result = append(result, bu)
		}
	}
	return result, nil
}

func (b *backupManager) loadMeta(dataPath string) (*metaData, error) {
	metaPath := filepath.Join(dataPath, backupMetaFile)
	metaFile, err := os.ReadFile(metaPath)
	if err != nil {
		return nil, err
	}
	meta := metaData{}
	if err = json.Unmarshal(metaFile, &meta); err != nil {
		return nil, err
	}
	if meta.DBName != b.dbName {
		return nil, errors.New("invalid database name in meta")
	}
	return &meta, nil
}

func (b *backupManager) newMeta(auto bool, req BackupRequest) (*metaData, error) {
	mig, err := b.migrator.CurrentMigrationVersion()
	if err != nil {
		return nil, err
	}
	now := time.Now().Format(defaultDateLayout)
	name := fmt.Sprintf("%s-%s", b.dbName, now)
	if auto {
		name = fmt.Sprintf("%s-auto-%s", b.dbName, now)
	}
	return &metaData{
		Name:       name,
		Migration:  mig,
		BackupTime: now,
		DBName:     b.dbName,
		Note:       req.Note,
		Version:    req.Version,
	}, nil
}
