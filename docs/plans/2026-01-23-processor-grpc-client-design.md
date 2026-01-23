# Processor gRPC Client & REST Gateway Design

## Goal

Implement a robust gRPC client in the Go `processor` to communicate with the Python `provider` (Shioaji wrapper), and expose this functionality via a RESTful API Gateway using Gin.

## Architecture

1. **gRPC Client (`internal/client`)**:
    * **Multi-Connection Pool**: Manages a pool of `grpc.ClientConn` to support high concurrency and avoid head-of-line blocking during streaming.
    * **Interface**: Defines a `ShioajiClient` interface mirroring the Proto definition for testability.
    * **Retries**: Uses standard gRPC `service_config` for exponential backoff on transient failures.
    * **Metrics**: Prometheus interceptors for monitoring.

2. **REST Gateway (`internal/gateway`)**:
    * **Framework**: Gin (high performance).
    * **Content Negotiation**: Supports both JSON (`application/json`) and Protobuf (`application/x-protobuf`) for requests and responses.
    * **Authentication**: JWT-based session management for the Gateway itself.
    * **Mapping**: Maps REST endpoints (e.g., `POST /orders`) directly to gRPC methods using generated Proto structs.

## Components

### 1. gRPC Client (`internal/client`)

* **Struct**: `Client` containing `[]*grpc.ClientConn`.
* **Configuration**:
  * `Target`: Provider address (e.g., `localhost:50051`).
  * `PoolSize`: Number of connections (default: 5).
  * `RetryPolicy`: Standard JSON service config.
* **Method**: `New(cfg Config) (*Client, error)`
* **Method**: `Execute(ctx, method, req, reply)` - generic wrapper or specific methods for `Login`, `PlaceOrder`, etc.

### 2. REST Gateway (`internal/gateway`)

* **Struct**: `Gateway` containing `*gin.Engine` and `client.ShioajiClient`.
* **Auth Middleware**: Extracts `Authorization: Bearer <token>`, validates JWT.
* **Protobuf Middleware/Handler**:
  * Checks `Content-Type` to bind request (JSON vs Proto).
  * Checks `Accept` to render response (JSON vs Proto).
* **Endpoints**:
  * `POST /api/v1/login` -> `client.Login` -> Returns JWT + Account info.
  * `GET /api/v1/accounts` -> `client.ListAccounts`
  * `POST /api/v1/orders` -> `client.PlaceOrder`
  * (and so on for all Proto methods).

## Data Flow

1. **Request**: Client sends HTTP request (JSON or Proto).
2. **Gateway**:
    * Validates JWT (except login).
    * Deserializes body to Proto Struct.
    * Selects a gRPC connection from pool.
    * Calls Provider via gRPC.
3. **Provider**: Executes Shioaji action. Returns Proto response.
4. **Gateway**:
    * Receives Proto response.
    * Serializes to JSON or Proto based on `Accept` header.
    * Returns HTTP 200/400/500.

## Error Handling

* **gRPC Errors**: Converted to standard HTTP status codes.
  * `INVALID_ARGUMENT` -> 400 Bad Request
  * `UNAUTHENTICATED` -> 401 Unauthorized
  * `UNAVAILABLE` -> 503 Service Unavailable
  * Default -> 500 Internal Server Error
* **Response Body**: consistent JSON error format `{"error": "message", "code": 123}` for JSON clients.

## Testing

* **Unit Tests**: Mock `ShioajiClient` interface to test Gateway handlers without running the Provider.
* **Integration Tests**: Test the real Client against a mock gRPC server.
