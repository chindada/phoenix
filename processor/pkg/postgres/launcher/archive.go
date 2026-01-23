package launcher

import (
	"archive/zip"
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
)

type archiver struct {
	backupManager BackupManager
	backupRoot    string
	dbName        string
}

func (a *archiver) Zip(zipName, sourceDir string) error {
	zipFile, err := os.Create(zipName)
	if err != nil {
		return err
	}
	defer func() { _ = zipFile.Close() }()

	zipWriter := zip.NewWriter(zipFile)
	defer func() { _ = zipWriter.Close() }()

	err = filepath.Walk(sourceDir,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if !info.IsDir() {
				zippedFile, oErr := os.Open(path)
				if oErr != nil {
					return oErr
				}
				defer func() { _ = zippedFile.Close() }()

				zipPath := strings.TrimPrefix(
					path,
					fmt.Sprintf("%s%s", filepath.Dir(sourceDir), string(os.PathSeparator)),
				)
				w1, oErr := zipWriter.Create(strings.ReplaceAll(zipPath, "\\", "/"))
				if oErr != nil {
					return oErr
				}
				if _, cErr := io.Copy(w1, zippedFile); cErr != nil {
					return cErr
				}
			}
			return nil
		},
	)
	if err != nil {
		return err
	}
	return nil
}

func (a *archiver) LoadBackupArchiveFile(path string) error {
	backUpName, err := a.archiveIsValid(path)
	if err != nil {
		return err
	}
	createdPath, err := a.createBackupPath(backUpName)
	if err != nil {
		return errors.New("cannot create backup directory")
	}
	archive, err := zip.OpenReader(path)
	if err != nil {
		return err
	}
	defer func() {
		_ = archive.Close()
	}()
	for _, f := range archive.File {
		dstFile, oErr := os.OpenFile(
			filepath.Join(createdPath, filepath.Base(f.Name)),
			os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode(),
		)
		if oErr != nil {
			return oErr
		}
		fileInArchive, oErr := f.Open()
		if oErr != nil {
			return oErr
		}
		for {
			_, err = io.CopyN(dstFile, fileInArchive, 1024)
			if err != nil {
				if errors.Is(err, io.EOF) {
					break
				}
				return err
			}
		}
		_ = dstFile.Close()
		_ = fileInArchive.Close()
	}
	return nil
}

func (a *archiver) createBackupPath(name string) (string, error) {
	if name == "" {
		return "", errors.New("backup name is required")
	}
	path := filepath.Join(a.backupRoot, name)
	if err := os.MkdirAll(path, os.ModePerm); err != nil {
		return "", err
	}
	if err := os.Chmod(path, os.ModePerm); err != nil {
		return "", err
	}
	return path, nil
}

func (a *archiver) archiveIsValid(path string) (string, error) {
	archive, err := zip.OpenReader(path)
	if err != nil {
		return "", err
	}
	defer func() {
		_ = archive.Close()
	}()
	backUpName := ""
	for _, f := range archive.File {
		if f.FileInfo().IsDir() {
			return "", errors.New("invalid backup archive: directory found")
		}
		if filepath.Base(f.Name) == backupMetaFile {
			r, e := f.Open()
			if e != nil {
				return "", e
			}
			buf := bytes.NewBuffer(nil)
			_, e = buf.ReadFrom(r)
			if e != nil {
				return "", e
			}
			_ = r.Close()
			meta := metaData{}
			if e = json.Unmarshal(buf.Bytes(), &meta); e != nil {
				return "", e
			}
			if meta.DBName != a.dbName {
				return "", errors.New("invalid database name in meta")
			}
			backUpName = meta.Name
			break
		}
	}
	if backUpName == "" {
		return "", errors.New("invalid backup archive")
	}
	if a.backupExists(backUpName) {
		return "", errors.New("backup already exists")
	}
	return backUpName, nil
}

func (a *archiver) backupExists(name string) bool {
	backups, err := a.backupManager.ListBackups()
	if err != nil {
		return false
	}
	for _, b := range backups {
		if b.Name == name {
			return true
		}
	}
	return false
}
