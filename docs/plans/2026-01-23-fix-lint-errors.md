# Fix Lint Errors Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Resolve all linting errors reported by `make lint` in the Go processor component.

**Architecture:** 
- Refactor `main.go` to reduce cognitive and cyclomatic complexity by extracting initialization logic into smaller functions.
- Improve error handling in repositories by using `errors.Is` and sentinel errors.
- Clean up minor linting issues like variable shadowing and outdated type syntax.

**Tech Stack:** Go 1.25+, zap, pgx, gin

---

### Task 1: Fix Repository Lint Errors

**Files:**
- Modify: `processor/internal/repository/user.go`
- Modify: `processor/internal/repository/model.go` (to add ErrNotFound)
- Modify: `processor/internal/gateway/handler/auth.go` (to handle new error)

**Step 1: Define ErrNotFound in model.go**
Add `var ErrNotFound = errors.New("not found")` to `processor/internal/repository/model.go`.

**Step 2: Update GetByUsername in user.go**
- Import `errors`.
- Use `errors.Is(err, pgx.ErrNoRows)`.
- Return `nil, ErrNotFound` instead of `nil, nil`.

**Step 3: Update Login handler in auth.go**
- Import `errors` and `phoenix/processor/internal/repository`.
- Update error check to handle `repository.ErrNotFound`.

**Step 4: Verify with Lint**
Run: `make lint-go`
Expected: `user.go` errors resolved.

**Step 5: Commit**
```bash
git add processor/internal/repository/user.go processor/internal/repository/model.go processor/internal/gateway/handler/auth.go
git commit -m "refactor: improve repository error handling and fix lint errors"
```

---

### Task 2: Fix Auth Handler Minor Lint Errors

**Files:**
- Modify: `processor/internal/gateway/handler/auth.go`

**Step 1: Fix shadowed err**
Rename the inner `err` in `bcrypt.CompareHashAndPassword` check.

**Step 2: Replace interface{} with any**
Change `[]interface{}{}` to `[]any{}`.

**Step 3: Verify with Lint**
Run: `make lint-go`
Expected: `auth.go` errors resolved.

**Step 4: Commit**
```bash
git add processor/internal/gateway/handler/auth.go
git commit -m "refactor: fix shadowed variable and modernize type syntax in auth handler"
```

---

### Task 3: Refactor Main to Reduce Complexity

**Files:**
- Modify: `processor/cmd/phoenix/main.go`

**Step 1: Fix perfsprint error**
Change `fmt.Sprintf("postgres://...")` to just the string literal.

**Step 2: Extract DB Initialization**
Create `initDB(log *zap.Logger) (*launcher.Launcher, error)` function.

**Step 3: Extract Admin Seeding**
Create `seedAdminUser(ctx context.Context, repo repository.UserRepository) error` function.

**Step 4: Extract gRPC Client Initialization**
Create `initGRPCClient(ctx context.Context, addr string, key, secret string) (*client.Client, error)` function.

**Step 5: Re-assemble Main**
Clean up `main` by calling the extracted functions.

**Step 6: Verify with Lint**
Run: `make lint-go`
Expected: `main.go` complexity and perfsprint errors resolved.

**Step 7: Commit**
```bash
git add processor/cmd/phoenix/main.go
git commit -m "refactor: reduce main function complexity and fix lint errors"
```

---

### Task 4: Final Verification

**Step 1: Run all tests**
Run: `make test-go` (Wait, I should check if there is a make test-go)
Run: `go test ./processor/...`

**Step 2: Run final lint**
Run: `make lint`

**Step 3: Commit**
```bash
git commit --allow-empty -m "chore: final verification of lint fixes"
```