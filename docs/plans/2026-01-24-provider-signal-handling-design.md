# Design: Provider Signal Handling (SIGQUIT/SIGINT/SIGTERM)

## Goal
Implement graceful shutdown for the Python Provider when receiving system signals (`SIGINT`, `SIGTERM`, `SIGQUIT`). Specifically, ensure that the Shioaji client logs out before the process terminates.

## Architecture
- **Signal Module**: Use Python's built-in `signal` module to intercept OS signals.
- **Unified Handler**: A single handler will manage `SIGINT` (Ctrl+C), `SIGTERM` (standard kill), and `SIGQUIT` (Ctrl+\).
- **Graceful Sequence**:
    1. Intercept Signal.
    2. Check if logged in.
    3. Call `client.logout()` if necessary.
    4. Call `server.stop(0)` to terminate the gRPC server.

## Implementation Details
- The `serve()` function in `provider/src/provider.py` will be modified.
- A closure or a helper object will be used to give the signal handler access to both the `ShioajiService` instance and the `grpc.Server` instance.
- Signal registration will occur before `server.start()`.

## Error Handling
- Wrap `client.logout()` in a try-except block to prevent logout errors from blocking the server shutdown.
- Log all shutdown steps for visibility.

## Testing
- Manual verification:
    - Run `make run-provider`.
    - Send `SIGINT` (Ctrl+C) and verify logout log.
    - Send `SIGQUIT` (Ctrl+\) and verify logout log.
