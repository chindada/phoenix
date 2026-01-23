# Processor Authentication & User Management Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transition the Processor to use a local PostgreSQL database for user authentication and establish a system-wide gRPC connection to the Provider on startup.

**Architecture:** 
1. The Processor starts a local PostgreSQL instance via its `launcher` package.
2. A `users` table stores hashed credentials.
3. At startup, the Processor performs a "System Login" to the Provider using env vars.
4. `/api/v1/login` validates credentials against the local database and issues a JWT.

**Tech Stack:** Go, PostgreSQL (pgx, squirrel, golang-migrate), gRPC, JWT, bcrypt.

---

### Task 1: Database Schema Migration

**Files:**
- Modify: `processor/migrations/phoenix/0001_phoenix.up.sql`
- Modify: `processor/migrations/phoenix/0001_phoenix.down.sql`

**Step 1: Update UP migration**
```sql
BEGIN;

CREATE TABLE IF NOT EXISTS users (
    username      TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMIT;
```

**Step 2: Update DOWN migration**
```sql
BEGIN;

DROP TABLE IF EXISTS users;

COMMIT;
```

**Step 3: Commit**
```bash
git add processor/migrations/phoenix/0001_phoenix.*.sql
git commit -m "feat: add users table migration"
```

---

### Task 2: User Repository Implementation

**Files:**
- Create: `processor/internal/repository/user.go`
- Create: `processor/internal/repository/model.go`

**Step 1: Define User model**
```go
package repository

import "time"

type User struct {
    Username     string
    PasswordHash string
    CreatedAt    time.Time
    UpdatedAt    time.Time
}
```

**Step 2: Implement UserRepository**
```go
package repository

import (
    "context"
    "phoenix/processor/pkg/postgres/client"
)

type UserRepository interface {
    GetByUsername(ctx context.Context, username string) (*User, error)
    Create(ctx context.Context, user *User) error
    Count(ctx context.Context) (int, error)
}

type userRepo struct {
    client client.PGClient
}

func NewUserRepository(c client.PGClient) UserRepository {
    return &userRepo{client: c}
}

// Implement methods using squirrel and pgx...
```

**Step 3: Write tests for UserRepository**
- Use a real PG instance started by launcher in tests if possible, or mock PGClient.

**Step 4: Commit**
```bash
git add processor/internal/repository/
git commit -m "feat: implement user repository"
```

---

### Task 3: Startup Integration (main.go)

**Files:**
- Modify: `processor/cmd/phoenix/main.go`

**Step 1: Initialize DB Launcher and Migrator**
- Call `launcher.New()` with `DBName("mojave")`.
- Call `l.InitDB(true)`.
- Call `l.MigrateScheme(nil)`.

**Step 2: System Login to Provider**
- Read `SHIOAJI_API_KEY` and `SHIOAJI_SECRET_KEY`.
- Call `grpcClient.Login(ctx, &pb.LoginRequest{...})`.

**Step 3: Seed Admin User**
- Check `userRepo.Count()`.
- If 0, `userRepo.Create(...)` with hashed "admin" password.

**Step 4: Commit**
```bash
git add processor/cmd/phoenix/main.go
git commit -m "feat: integrate database and system login at startup"
```

---

### Task 4: Refactor Auth Handler

**Files:**
- Modify: `processor/internal/gateway/handler/auth.go`
- Modify: `processor/internal/gateway/router.go`
- Modify: `processor/internal/gateway/server.go`

**Step 1: Update Handler struct and Login method**
- Add `UserRepository` to `Handler`.
- Change `Login` to accept `username`/`password`.
- Verify password with `bcrypt.CompareHashAndPassword`.

**Step 2: Update Router and Server to inject Repository**

**Step 3: Commit**
```bash
git add processor/internal/gateway/
git commit -m "feat: refactor login handler to use local database"
```

---

### Task 5: Verification

**Step 1: Run full system**
- `make run-server` (Provider)
- `make build-go && ./processor/bin/server` (Processor)

**Step 2: Test Login**
- `curl -X POST http://localhost:8080/api/v1/login -d '{"username":"admin", "password":"admin"}'`
- Verify `X-Auth-Token` is returned.

**Step 3: Test Protected Route**
- `curl -H "X-Auth-Token: <token>" http://localhost:8080/api/v1/accounts`
- Verify it returns accounts from the system-logged-in Shioaji account.
