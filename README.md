# Phoenix

Phoenix is a polyglot trading system wrapper designed to expose the **Shioaji** API (Taiwanese stock trading) via a standardized gRPC interface and a RESTful API gateway.

## Architecture

The system is split into two primary services:

1. **Provider (Python)**
    * **Role**: Backend service that interfaces directly with the Shioaji trading API.
    * **Tech**: Python 3.10+, `grpcio`, `shioaji`.
    * **Communication**: gRPC server defined in `protos/v1/provider.proto`.

2. **Processor (Go)**
    * **Role**: API Gateway and frontend facade.
    * **Tech**: Go 1.25+, Gin Framework, gRPC client.
    * **Communication**: Translates RESTful HTTP requests into gRPC calls to the Provider.

## Prerequisites

* **Python**: 3.10 or higher
* **Go**: 1.25 or higher
* **Protobuf Compiler**: `protoc` with `protoc-gen-go` and `protoc-gen-go-grpc` plugins installed.
* **Make**: For running build tasks.

## Getting Started

### 1. Installation

Initialize the Python environment and install dependencies:

```bash
make install
```

### 2. Code Generation

If you modify `protos/v1/provider.proto`, regenerate the gRPC code for both services:

```bash
make codegen
```

### 3. Running the System

**Start the Provider (Python gRPC Server):**

```bash
make run-server
```

**Build and Run the Processor (Go API Gateway):**

```bash
make build-go
./processor/bin/server
```

By default:

* Provider listens on `localhost:50051` (configurable via `PROVIDER_ADDR`)
* Processor listens on port `8080` (configurable via `PORT`)

## Development

### Linting & Formatting

The project enforces strict code quality standards.

* **Run all linters**: `make lint`
* **Python**: Uses `ruff`, `pylint`, `mypy`, and `pyright`.
* **Go**: Uses `golangci-lint` and `gofumpt`.

### Testing

* **Run all tests**: `make test`
* **Python only**: `make test-py`
* **Go only**: `make test-go`

## Project Structure

```text
phoenix/
├── protos/       # Shared gRPC service definitions
├── provider/     # Python backend (Shioaji wrapper)
└── processor/    # Go API Gateway (REST -> gRPC)
```

## IDE Setup

### VS Code

For correct Python auto-completion and analysis, ensure your analysis paths are configured correctly.
See `DEBUG.md` for `settings.json` examples.
