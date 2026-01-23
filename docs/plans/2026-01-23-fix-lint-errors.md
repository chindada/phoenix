# Fix Lint Errors Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Fix all 27 linting errors reported by `make lint-darwin` in the `processor` module.

**Architecture:** Refactor code to comply with `golangci-lint` rules including `errcheck`, `goimports`, `golines`, `gosec`, `intrange`, `modernize`, `noctx`, `protogetter`, and `testpackage`.

**Tech Stack:** Go 1.25+, golangci-lint v2

---

## Task 1: Fix Test Package Names (`testpackage`)

**Files:**

- Modify: `processor/internal/client/pool_test.go`
- Modify: `processor/internal/gateway/middleware/auth_test.go`
- Modify: `processor/internal/gateway/middleware/proto_test.go`

***Step 1: Verify current state***
Run: `make lint-darwin` (verify `testpackage` errors exist)

***Step 2: Rename packages***

- In `pool_test.go`: Change `package client` to `package client_test` and import `phoenix/processor/internal/client`.
- In `auth_test.go` & `proto_test.go`: Change `package middleware` to `package middleware_test` and import `phoenix/processor/internal/gateway/middleware`.

***Step 3: Verify Fix***
Run: `make lint-darwin`
Expected: `testpackage` errors gone.

***Step 4: Commit***

```bash
git add processor/internal
git commit -m "fix(lint): use _test package suffix for test files"
```

---

## Task 2: Fix HTTP Request Context (`noctx`)

**Files:**

- Modify: `processor/internal/gateway/middleware/auth_test.go`
- Modify: `processor/internal/gateway/middleware/proto_test.go`

***Step 1: Verify current state***
Run: `make lint-darwin` (verify `noctx` errors exist)

***Step 2: Use NewRequestWithContext***

- Replace `http.NewRequest(...)` with `http.NewRequestWithContext(context.Background(), ...)`

***Step 3: Verify Fix***
Run: `make lint-darwin`
Expected: `noctx` errors gone.

***Step 4: Commit***

```bash
git add processor/internal/gateway/middleware
git commit -m "fix(lint): use http.NewRequestWithContext in tests"
```

---

## Task 3: Fix Proto Getters (`protogetter`)

**Files:**

- Modify: `processor/internal/gateway/middleware/proto_test.go`

***Step 1: Verify current state***
Run: `make lint-darwin` (verify `protogetter` errors exist)

***Step 2: Use Getters***

- Replace `reqObj.ApiKey` with `reqObj.GetApiKey()`

***Step 3: Verify Fix***
Run: `make lint-darwin`
Expected: `protogetter` errors gone.

***Step 4: Commit***

```bash
git add processor/internal/gateway/middleware/proto_test.go
git commit -m "fix(lint): use proto getter methods"
```

---

## Task 4: Fix Loops and Modernize (`intrange`, `modernize`)

**Files:**

- Modify: `processor/internal/client/pool.go`
- Modify: `processor/internal/gateway/middleware/auth.go`

***Step 1: Verify current state***
Run: `make lint-darwin` (verify `intrange` and `modernize` errors exist)

***Step 2: Modernize Loops in `pool.go`***

- Replace `for i := 0; i < cfg.PoolSize; i++` with `for range cfg.PoolSize` (or `for _ = range cfg.PoolSize` depending on Go version, strictly Go 1.22+ supports integer range).
- *Correction*: `for i := range cfg.PoolSize` if `i` is used.

***Step 3: Modernize Interface in `auth.go`***

- Replace `interface{}` with `any`

***Step 4: Verify Fix***
Run: `make lint-darwin`
Expected: `intrange` and `modernize` errors gone.

***Step 5: Commit***

```bash
git add processor/internal
git commit -m "fix(lint): modernize loops and use any"
```

---

## Task 5: Fix Logic Errors (`errcheck`, `gosec`)

**Files:**

- Modify: `processor/internal/gateway/middleware/proto.go`
- Modify: `processor/internal/client/pool.go`

***Step 1: Verify current state***
Run: `make lint-darwin` (verify `errcheck` and `gosec` errors exist)

***Step 2: Handle Errors***

- In `proto.go`: explicitly ignore error `_ = c.AbortWithError(...)` or handle it.
- In `pool.go`: explicitly ignore close error `_ = conns[j].Close()` or log it.

***Step 3: Verify Fix***
Run: `make lint-darwin`
Expected: `errcheck` and `gosec` errors gone.

***Step 4: Commit***

```bash
git add processor/internal
git commit -m "fix(lint): handle unchecked errors"
```

---

## Task 6: Fix Formatting (`goimports`, `golines`)

**Files:**

- Modify: `processor/internal/client/pool.go`
- Modify: `processor/internal/client/pool_test.go`
- Modify: `processor/internal/client/wrappers.go`
- Modify: `processor/internal/gateway/handler/auth.go`
- Modify: `processor/internal/gateway/handler/trade.go`
- Modify: `processor/internal/gateway/middleware/auth_test.go`
- Modify: `processor/internal/gateway/middleware/proto_test.go`
- Modify: `processor/internal/gateway/router.go`
- Modify: `processor/internal/gateway/server.go`

***Step 1: Verify current state***
Run: `make lint-darwin` (verify formatting errors exist)

***Step 2: Fix Imports and Lines***

- Group imports correctly (std lib, then 3rd party, then local).
- Split long line in `wrappers.go`.

***Step 3: Verify Fix***
Run: `make lint-darwin`
Expected: All errors gone.

***Step 4: Commit***

```bash
git add processor
git commit -m "fix(lint): formatting and imports"
```
