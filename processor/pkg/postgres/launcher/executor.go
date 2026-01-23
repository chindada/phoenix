package launcher

import (
	"io"
	"os"
	"path/filepath"
)

type executor struct {
	binaryRoot string
	verbose    bool
}

const (
	cliInitDB  = "initdb"
	cliPsql    = "psql"
	cliPGCtl   = "pg_ctl"
	cliDump    = "pg_dump"
	cliRestore = "pg_restore"
)

const (
	cliExport = "postgres_exporter"
)

func (e *executor) getCliInitDB() string {
	if e.binaryRoot == "" {
		return cliInitDB
	}
	return filepath.Join(e.binaryRoot, cliInitDB)
}

func (e *executor) getCliPsql() string {
	if e.binaryRoot == "" {
		return cliPsql
	}
	return filepath.Join(e.binaryRoot, cliPsql)
}

func (e *executor) getCliPGCtl() string {
	if e.binaryRoot == "" {
		return cliPGCtl
	}
	return filepath.Join(e.binaryRoot, cliPGCtl)
}

func (e *executor) getCliDump() string {
	if e.binaryRoot == "" {
		return cliDump
	}
	return filepath.Join(e.binaryRoot, cliDump)
}

func (e *executor) getCliRestore() string {
	if e.binaryRoot == "" {
		return cliRestore
	}
	return filepath.Join(e.binaryRoot, cliRestore)
}

func (e *executor) getCliExport() string {
	if e.binaryRoot == "" {
		return cliExport
	}
	return filepath.Join(e.binaryRoot, cliExport)
}

func (e *executor) pipeStdout(src io.ReadCloser) {
	go func() {
		_, _ = io.Copy(os.Stdout, src)
	}()
}

func (e *executor) pipeStderr(src io.ReadCloser) {
	go func() {
		_, _ = io.Copy(os.Stderr, src)
	}()
}
