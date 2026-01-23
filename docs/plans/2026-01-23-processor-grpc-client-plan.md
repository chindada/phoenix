# Processor gRPC Client & REST Gateway Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement a production-ready gRPC client with connection pooling and a REST API Gateway with JWT auth and Protobuf support in the Go processor.

**Architecture:**

- `internal/client`: Handles gRPC connections to Python Provider.
- `internal/gateway`: Exposes REST API using Gin.
- `cmd/phoenix`: Wires them together.

**Tech Stack:** Go 1.25+, Gin, gRPC-Go, Golang-JWT.

---

## Task 1: Project Structure & Dependencies

**Files:**

- Modify: `processor/go.mod`
- Create: `processor/internal/client/client.go` (placeholder)
- Create: `processor/internal/gateway/server.go` (placeholder)

***Step 1: Initialize Modules***

Run command to add dependencies:

```bash
cd processor
go get -u google.golang.org/grpc
go get -u github.com/gin-gonic/gin
go get -u github.com/golang-jwt/jwt/v5
go get -u github.com/grpc-ecosystem/go-grpc-middleware
go get -u github.com/grpc-ecosystem/go-grpc-prometheus
```

***Step 2: Create Directory Structure***

```bash
mkdir -p processor/internal/client
mkdir -p processor/internal/gateway
```

***Step 3: Commit***

```bash
git add processor/go.mod processor/go.sum
git commit -m "chore: add dependencies for grpc client and gin gateway"
```

---

## Task 2: gRPC Client - Interface & Types

**Files:**

- Create: `processor/internal/client/interface.go`
- Create: `processor/internal/client/mock_client.go` (for testing)

***Step 1: Define Interface***
Define `ShioajiClient` interface matching `pb.ShioajiProviderClient` but with `Close()` method.

***Step 2: Generate Mocks***
If `mockgen` is available, use it. Otherwise, create a manual mock struct in `mock_client.go` that implements `ShioajiClient`.

***Step 3: Commit***

```bash
git add processor/internal/client/interface.go processor/internal/client/mock_client.go
git commit -m "feat(client): define ShioajiClient interface and mock"
```

---

## Task 3: gRPC Client - Connection Pool Implementation

**Files:**

- Create: `processor/internal/client/pool.go`
- Test: `processor/internal/client/pool_test.go`

***Step 1: Write Failing Test (Pool Creation)***
Create `pool_test.go` checking if `NewClient` creates the specified number of connections.

***Step 2: Implement Client Struct***
In `pool.go`:

```go
package client

import (
    "context"
    "sync"
    "google.golang.org/grpc"
    "phoenix/processor/pkg/pb"
)

type Config struct {
    Target   string
    PoolSize int
}

type Client struct {
    conns []*grpc.ClientConn
    // ... logic for round robin
}
```

***Step 3: Implement Round Robin Selection***
Add logic to select next connection index atomically.

***Step 4: Implement gRPC Method Wrappers***
Implement `Login`, `PlaceOrder`, etc. calling the underlying `pb.NewShioajiProviderClient(conn)`.

***Step 5: Verify Tests***
Run `go test ./processor/internal/client/...`

***Step 6: Commit***

```bash
git add processor/internal/client/
git commit -m "feat(client): implement grpc connection pool"
```

---

## Task 4: REST Gateway - Auth Middleware

**Files:**

- Create: `processor/internal/gateway/middleware/auth.go`
- Test: `processor/internal/gateway/middleware/auth_test.go`

***Step 1: Write Failing Test***
Test middleware rejects request without header. Test it accepts valid JWT.

***Step 2: Implement JWT Logic***
Use `golang-jwt/jwt/v5`. Secret should be configurable (env var).

***Step 3: Implement Gin Middleware***
Extract "Bearer " token. Validate. Set `user_id` in context. Abort with 401 if invalid.

***Step 4: Verify Tests***
Run tests.

***Step 5: Commit***

```bash
git add processor/internal/gateway/middleware/
git commit -m "feat(gateway): implement jwt auth middleware"
```

---

## Task 5: REST Gateway - Content Negotiation

**Files:**

- Create: `processor/internal/gateway/middleware/proto.go`
- Test: `processor/internal/gateway/middleware/proto_test.go`

***Step 1: Write Test***
Test sending `application/json` -> receives JSON.
Test sending `application/x-protobuf` -> receives Proto bytes.

***Step 2: Implement Handler Utilities***
Create helper function `Bind(c *gin.Context, obj proto.Message)` and `Render(c *gin.Context, obj proto.Message)`.

- `Bind`: Check `Content-Type`. If `x-protobuf`, `proto.Unmarshal`. Else `c.ShouldBindJSON`.
- `Render`: Check `Accept`. If `x-protobuf`, `proto.Marshal` + write bytes. Else `c.JSON`.

***Step 3: Verify Tests***

***Step 4: Commit***

```bash
git add processor/internal/gateway/middleware/
git commit -m "feat(gateway): implement protobuf content negotiation"
```

---

## Task 6: REST Gateway - Handlers (Login)

**Files:**

- Create: `processor/internal/gateway/handler/auth.go`
- Modify: `processor/internal/gateway/router.go`

***Step 1: Implement Login Handler***

- Bind `pb.LoginRequest`.
- Call `client.Login`.
- On success, generate JWT.
- Return `{"token": "...", "account": ...}` (JSON) or Proto response with injected token (if we extend Proto, otherwise just return the Proto response and let client handle token separately? -> *Decision: Return a custom struct wrapping the response for JSON, or headers for Proto? For simplicity, let's put Token in a Header `X-Auth-Token` for both formats.*)

***Step 2: Register Route***
`POST /api/v1/login`

***Step 3: Commit***

```bash
git add processor/internal/gateway/
git commit -m "feat(gateway): implement login handler"
```

---

## Task 7: REST Gateway - Handlers (Trading)

**Files:**

- Create: `processor/internal/gateway/handler/trade.go`
- Modify: `processor/internal/gateway/router.go`

***Step 1: Implement Generic Proxy Handler***
Since we map 1:1, we can create a pattern.

- `PlaceOrder`: Bind `pb.PlaceOrderRequest`. Call `client.PlaceOrder`. Render `pb.Trade`.
- `ListAccounts`: Bind Empty. Call `client.ListAccounts`. Render `pb.ListAccountsResponse`.

***Step 2: Register Routes***
`POST /api/v1/orders`
`GET /api/v1/accounts`
etc.

***Step 3: Commit***

```bash
git add processor/internal/gateway/
git commit -m "feat(gateway): implement trading handlers"
```

---

## Task 8: Main Integration

**Files:**

- Modify: `processor/cmd/phoenix/main.go`

***Step 1: Update Main***

- Load Config (Env vars).
- Initialize `client.NewClient`.
- Initialize `gateway.New(client)`.
- `gateway.Run(":8080")`.

***Step 2: Run & Verify***
Manual run to check startup.

***Step 3: Commit***

```bash
git add processor/cmd/phoenix/main.go
git commit -m "feat: wire up grpc client and rest gateway"
```
