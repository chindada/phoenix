# Design Document: Unix Domain Socket (UDS) Support for Provider-Processor IPC

## Overview
This document outlines the design for implementing Unix Domain Socket (UDS) support for the Inter-Process Communication (IPC) between the Phoenix Processor (Go) and the Phoenix Provider (Python). This change aims to reduce latency and overhead for local deployments.

## Architecture
Both services will utilize a shared configuration pattern to determine the gRPC transport layer.

### 1. Configuration Strategy
A single environment variable, `PROVIDER_ADDR`, will be used by both components.
- **TCP (Default):** `PROVIDER_ADDR=localhost:50051`
- **UDS:** `PROVIDER_ADDR=unix:///tmp/phoenix.sock`

## Components

### 1. Provider (Python gRPC Server)
The Python server entry point (`provider/src/server.py`) will be updated to:
- Detect the address type from `PROVIDER_ADDR`.
- If a UDS path is provided (starting with `unix:`):
    - Parse the file path.
    - Check if the socket file exists and `os.unlink()` it to ensure a clean bind.
    - Bind the gRPC server using the `unix:` scheme.
- If a TCP address is provided, bind normally.

### 2. Processor (Go gRPC Client)
The Go client wrapper (`processor/internal/client/client.go`) and the main entry point (`processor/cmd/phoenix/main.go`) will:
- Pass the `PROVIDER_ADDR` string directly to `grpc.NewClient`.
- `grpc-go` natively handles the `unix://` scheme, so no specific socket-handling code is required in the dialer.

## Implementation Details

### Provider Logic (Python)
```python
def serve():
    addr = os.getenv("PROVIDER_ADDR", "localhost:50051")
    if addr.startswith("unix:"):
        # Handle unix:///path/to/socket vs unix:/path/to/socket
        path = addr.replace("unix://", "").replace("unix:", "")
        if os.path.exists(path):
            os.remove(path)
            logging.info("Removed existing socket file: %s", path)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # ... registration ...
    server.add_insecure_port(addr)
    server.start()
```

### Processor Logic (Go)
The current implementation in `processor/internal/client/pool.go` already uses `grpc.NewClient(cfg.Target, opts...)`. Since `cfg.Target` is passed through from `PROVIDER_ADDR`, no changes are needed to the connection logic.

## Verification Plan
1. **Manual Integration Test:**
    - Set `PROVIDER_ADDR=unix:///tmp/phoenix.test.sock`.
    - Start Provider.
    - Verify `/tmp/phoenix.test.sock` exists.
    - Start Processor.
    - Execute a `Login` request via the Processor API and verify gRPC response.
2. **Backward Compatibility:**
    - Unset `PROVIDER_ADDR` or set to `localhost:50051`.
    - Verify both services still communicate over TCP.
