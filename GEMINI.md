# Project Context: Phoenix

Phoenix is a polyglot trading system wrapper that exposes the Shioaji API (Taiwanese stock trading) via a standardized gRPC interface and a RESTful API gateway.

## Architecture

The system consists of two main components:

1. **Provider (Python)**:
    * Acts as the backend service interacting directly with the Shioaji trading API.
    * Implements a gRPC server defined in `protos/v1/provider.proto`.
    * Handles authentication, order management, and market data retrieval.
    * Located in `provider/`.

2. **Processor (Go)**:
    * Acts as the API Gateway / Frontend.
    * Exposes a RESTful API using the Gin framework.
    * Translates HTTP requests into gRPC calls to the Provider.
    * Located in `processor/`.

## Key Technologies

* **Communication**: gRPC (Protocol Buffers v3)
* **Provider**: Python 3, `shioaji`, `grpcio`
* **Processor**: Go 1.25+, `gin-gonic`, `grpc-go`
* **Tools**: `make`, `protoc`, `ruff`, `mypy`, `golangci-lint`

## Development Workflow

### Prerequisites

* Python 3.10+
* Go 1.25+
* Protobuf Compiler (`protoc`) with Go plugins (`protoc-gen-go`, `protoc-gen-go-grpc`)

### Build and Run Commands

Use the `Makefile` for common tasks:

* **Setup**: `make install` (Creates Python venv and installs dependencies)
* **Code Generation**: `make codegen` (Generates gRPC code for both Python and Go)
  * `make codegen-py`: Python only
  * `make codegen-go`: Go only
* **Linting**: `make lint` (Runs `ruff` and `golangci-lint`)
  * `make lint-py`: Python only
  * `make lint-go`: Go only
* **Formatting**: `make format` (Formats Python code with `ruff`; Go uses `goimports` via linter)
* **Type Checking**: `make type-check` (Runs `mypy` on Python code)
* **Run Provider**: `make run-server` (Starts the Python gRPC server)
* **Build Processor**: `make build-go` (Compiles the Go server to `processor/bin/server`)

### Project Structure

```text
phoenix/
├── Makefile              # Central task runner
├── protos/               # gRPC service definitions
│   └── v1/
│       └── provider.proto
├── provider/             # Python gRPC server (Shioaji wrapper)
│   ├── requirements.txt
│   └── src/
│       ├── server.py     # gRPC server entry point
│       └── shioaji_client.py
└── processor/            # Go REST API Gateway
    ├── go.mod
    ├── cmd/server/       # Go entry point
    ├── internal/         # Internal application logic
    │   ├── client/       # gRPC client wrapper
    │   └── server/       # REST server implementation (Gin)
    └── pkg/pb/           # Generated Go gRPC code
```

### Conventions

* **Linting**: The project enforces strict linting. Always run `make lint` before committing.
  * Python: Uses `ruff` for linting and formatting.
  * Go: Uses `golangci-lint` v2 with strict settings (including `modernize`, `golines`, `goimports`).
* **gRPC**: Changes to the API should be made in `protos/v1/provider.proto` first, followed by `make codegen`.
* **Env Vars**:
  * `PROVIDER_ADDR`: Address of the gRPC provider (default: `localhost:50051`).
  * `PORT`: Port for the Go REST server (default: `:8080`).
