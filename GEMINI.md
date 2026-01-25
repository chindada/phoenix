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
* **Provider**: Python 3.10+, `shioaji`, `grpcio`, `pytest`, `mypy`, `pyright`, `ruff`, `pylint`
* **Processor**: Go 1.25+, `gin-gonic`, `grpc-go`, `golangci-lint-v2`, `gofumpt`
* **Tools**: `make`, `protoc`

## Development Workflow

### Prerequisites

* Python 3.10+
* Go 1.25+
* Protobuf Compiler (`protoc`) with Go plugins (`protoc-gen-go`, `protoc-gen-go-grpc`)

### Build and Run Commands

Use the `Makefile` for common tasks:

* **Setup**: `make install` (Creates Python venv and installs dependencies)
* **Code Generation**: `make codegen` (Generates gRPC code for both Python and Go, and Swagger docs)
  * `make codegen-py`: Python only
  * `make codegen-go`: Go only
  * `make swagger`: Generate Swagger documentation for the Go API
* **Linting**: `make lint` (Runs comprehensive linting for both Python and Go)
  * `make lint-py`: Python only (ruff, pylint, mypy, pyright)
  * `make lint-go`: Go only (gofumpt, golangci-lint-v2 for both darwin and linux)
* **Testing**: `make test` (Runs all tests, currently defaults to Go tests)
  * `make test-go`: Go tests using `go test`
* **Formatting**: `make format` (Formats Python code with `ruff`; Go uses `gofumpt` via linter)
* **Type Checking**: `make type-check` (Runs `mypy` and `pyright` on Python code)
* **Run Provider**: `make run-provider` (Starts the Python gRPC server)
* **Build Processor**: `make build-go` (Compiles the Go server to `processor/bin/processor`)

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
│       ├── provider.py   # gRPC server entry point
│       └── shioaji_client.py
└── processor/            # Go REST API Gateway
    ├── go.mod
    ├── bin/              # Compiled binaries
    ├── cmd/phoenix/      # Go entry point (main.go)
    ├── internal/         # Internal application logic
    │   ├── client/       # gRPC client wrapper
    │   ├── gateway/      # REST server implementation (Gin)
    │   └── repository/   # Data access layer
    ├── migrations/       # SQL migrations for the database
    └── pkg/              # Shared packages
        ├── eventbus/     # Internal event system
        ├── log/          # Structured logging
        ├── pb/           # Generated Go gRPC code
        └── postgres/     # Embedded Postgres launcher and migrator
```

### Conventions

* **Linting**: The project enforces strict linting. Always run `make lint` before committing.
  * Python: Uses `ruff` (formatting/linting), `pylint`, `mypy`, and `pyright`.
  * Go: Uses `gofumpt` and `golangci-lint-v2` with cross-platform checks (darwin/linux).
* **gRPC**: Changes to the API should be made in `protos/v1/provider.proto` first, followed by `make codegen`.
* **API Documentation**: Go REST API uses Swagger. Run `make swagger` to update documentation.
* **Env Vars**:
  * `PROVIDER_ADDR`: Address of the gRPC provider (default: `localhost:50051`).
  * `PORT`: Port for the Go REST server (default: `:8080`).
  * `SJ_LOG_PATH`: Path for Shioaji logs (Python).
  * `SJ_CONTRACTS_PATH`: Path for Shioaji contracts data (Python).
