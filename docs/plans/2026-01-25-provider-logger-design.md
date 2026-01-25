# Design Document: Provider Logger Implementation

## Overview
Implement a structured logger for the Python Provider that mirrors the behavior and configuration of the Go Processor's logger (`processor/pkg/log/log.go`). This ensures consistent log formats, levels, and rotation across the polyglot system.

## Configuration
The logger will be configured via environment variables:
- `LOG_LEVEL`: Logging level (default: `info`).
- `LOG_DISABLE_CONSOLE`: If set, disables console logging.
- `LOG_DISABLE_FILE`: If set, disables file logging.

## Components

### 1. Console Logging
- **Library**: `colorlog`
- **Format**: Human-readable with color-coded levels.
- **Time Format**: `YYYY/MM/DD HH:MM:SS.mmm`.
- **Target**: `stdout`.

### 2. File Logging
- **Library**: `python-json-logger` + standard `logging.handlers.RotatingFileHandler`.
- **Format**: JSON (structured logging).
- **Location**: `../logs/provider.log` (relative to the executable).
- **Rotation**:
  - Max Size: 500 MB.
  - Max Backups: 3.
  - Compression: (Handled manually or via standard library if available, otherwise omitted for simplicity).

### 3. API
- Expose a global logger instance similar to `zap.L()` in Go.
- Integration with `logging` standard library for compatibility with third-party packages.

## Dependencies
Add to `provider/requirements.txt`:
- `colorlog`
- `python-json-logger`

## Testing
- Verify environment variables override defaults.
- Verify log file creation and JSON format.
- Verify console output coloring.
