// Package log provides a common logger package using uber-go/zap.
package log

import (
	"fmt"
	"os"
	"path/filepath"
	"time"

	"github.com/ilyakaznacheev/cleanenv"
	"github.com/moby/term"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
	"gopkg.in/natefinch/lumberjack.v2"
)

type envSetting struct {
	Level          string `env:"LOG_LEVEL"           env-default:"info"`
	DisableConsole bool   `env:"LOG_DISABLE_CONSOLE"`
	DisableFile    bool   `env:"LOG_DISABLE_FILE"`
}

func init() {
	cfg := readEnv()
	setup(cfg)
}

func setup(cfg *envSetting) {
	level, err := zapcore.ParseLevel(cfg.Level)
	if err != nil {
		level = zapcore.InfoLevel
	}

	var cores []zapcore.Core
	if !cfg.DisableFile {
		if fc, fcErr := newFileCore(level); fcErr == nil {
			cores = append(cores, fc)
		}
	}
	if !cfg.DisableConsole {
		cores = append(cores, newConsoleCore(level))
	}

	var logger *zap.Logger
	if len(cores) > 0 {
		logger = zap.New(zapcore.NewTee(cores...), zap.AddCaller())
	} else {
		logger = zap.NewNop()
	}
	zap.ReplaceGlobals(logger)
}

func newFileCore(level zapcore.Level) (zapcore.Core, error) {
	ex, err := os.Executable()
	if err != nil {
		return nil, err
	}
	folder := filepath.Join(filepath.Clean(filepath.Dir(ex)), "..", "logs")
	if err = os.MkdirAll(folder, 0o750); err != nil {
		return nil, err
	}

	filename := filepath.Join(folder, fmt.Sprintf("%s.log", filepath.Base(ex)))
	w := zapcore.AddSync(&lumberjack.Logger{
		Filename:   filename,
		MaxSize:    500, // MB
		MaxAge:     28,  // days
		MaxBackups: 3,
		Compress:   true,
	})
	encCfg := zap.NewProductionEncoderConfig()
	encCfg.EncodeTime = func(ts time.Time, encoder zapcore.PrimitiveArrayEncoder) {
		encoder.AppendString(ts.Local().Format("2006/01/02 15:04:05.000"))
	}
	return zapcore.NewCore(zapcore.NewJSONEncoder(encCfg), w, level), nil
}

func newConsoleCore(level zapcore.Level) zapcore.Core {
	encCfg := zap.NewProductionEncoderConfig()
	encCfg.EncodeTime = func(ts time.Time, encoder zapcore.PrimitiveArrayEncoder) {
		encoder.AppendString(ts.Local().Format("2006/01/02 15:04:05.000"))
	}

	// We are writing to Stdout, so check if Stdout is a terminal
	coloringEnabled := os.Getenv("NO_COLOR") == "" && os.Getenv("TERM") != "xterm-mono"
	if term.IsTerminal(os.Stdout.Fd()) && coloringEnabled {
		encCfg.EncodeLevel = zapcore.CapitalColorLevelEncoder
	}
	return zapcore.NewCore(zapcore.NewConsoleEncoder(encCfg), zapcore.AddSync(os.Stdout), level)
}

func readEnv() *envSetting {
	cfg := &envSetting{}
	if err := cleanenv.ReadEnv(cfg); err != nil {
		cfg.DisableConsole = false
		cfg.DisableFile = false
		cfg.Level = "info"
	}
	return cfg
}

func L() *zap.Logger {
	return zap.L()
}

func S() *zap.SugaredLogger {
	return zap.S()
}

func Get() *zap.Logger {
	return zap.L()
}

func GetSugar() *zap.SugaredLogger {
	return zap.S()
}
