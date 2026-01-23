# gRPC to REST API Expansion Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Expose all 30+ Provider gRPC services as RESTful API endpoints in the Processor, organized by domain.

**Architecture:**
- Split `processor/internal/gateway/handler` into domain-specific files (`auth.go`, `account.go`, `order.go`, etc.) to improve maintainability.
- Map each gRPC RPC to a REST endpoint in `processor/internal/gateway/router.go`.
- Use the existing `client.ShioajiClient` interface.
- Implement handlers using `gin.Context` to bind JSON/Params and call gRPC methods.

**Tech Stack:** Go, Gin, gRPC

---

### Task 1: Refactor Handler Structure

**Files:**
- Modify: `processor/internal/gateway/handler/handler.go` (New file for common struct)
- Move: `processor/internal/gateway/handler/auth.go` -> `processor/internal/gateway/handler/auth.go` (Keep but clean up)
- Move: `processor/internal/gateway/handler/trade.go` -> Split content into `account.go`, `order.go`, `trade.go`

**Step 1: Create Handler Struct in `handler.go`**
Extract the `Handler` struct and factory from `auth.go`/`trade.go` into a common file to avoid circular deps or duplication if we were to separate packages (but here we stay in `handler` package).

```go
// processor/internal/gateway/handler/handler.go
package handler

import (
    "phoenix/processor/internal/client"
    "phoenix/processor/internal/repository"
)

type Handler struct {
    client   client.ShioajiClient
    userRepo repository.UserRepository
    secret   string
}

func New(client client.ShioajiClient, userRepo repository.UserRepository, secret string) *Handler {
    return &Handler{
        client:   client,
        userRepo: userRepo,
        secret:   secret,
    }
}
```

**Step 2: Clean up `auth.go`**
Remove `Handler` struct definition from `auth.go`.

**Step 3: Create `account.go` and move `ListAccounts`**
Create `processor/internal/gateway/handler/account.go` and move `ListAccounts` there.

**Step 4: Create `order.go` and move `PlaceOrder`, `CancelOrder`**
Create `processor/internal/gateway/handler/order.go`.

**Step 5: Create `trade.go` and move `ListTrades`**
Keep `ListTrades` in `trade.go` but remove others.

**Step 6: Create `position.go` and move `ListPositions`**
Create `processor/internal/gateway/handler/position.go`.

**Step 7: Verify compilation**
Run `go build ./processor/...`

---

### Task 2: Implement Auth & Account Handlers

**Files:**
- Modify: `processor/internal/gateway/handler/auth.go`
- Modify: `processor/internal/gateway/handler/account.go`
- Modify: `processor/internal/gateway/router.go`

**Step 1: Add Auth RPCs to `auth.go`**
Implement:
- `Logout`: `POST /api/v1/logout`
- `ActivateCA`: `POST /api/v1/ca/activate`
- `GetCAExpireTime`: `GET /api/v1/ca/expire`

**Step 2: Add Account RPCs to `account.go`**
Implement:
- `GetUsage`: `GET /api/v1/usage`
- `GetAccountBalance`: `GET /api/v1/accounts/balance`
- `GetSettlements`: `GET /api/v1/accounts/settlements`
- `GetMargin`: `GET /api/v1/accounts/margin`
- `GetTradingLimits`: `GET /api/v1/accounts/limits`

**Step 3: Register Routes in `router.go`**
Add the new endpoints to the router.

**Step 4: Verify**
Compile and check for errors.

---

### Task 3: Implement Order Handlers

**Files:**
- Modify: `processor/internal/gateway/handler/order.go`
- Modify: `processor/internal/gateway/router.go`

**Step 1: Add Order RPCs**
Implement:
- `PlaceComboOrder`: `POST /api/v1/orders/combo`
- `UpdateOrder`: `PUT /api/v1/orders`
- `CancelComboOrder`: `POST /api/v1/orders/combo/cancel`
- `UpdateStatus`: `POST /api/v1/orders/status`
- `UpdateComboStatus`: `POST /api/v1/orders/combo/status`

**Step 2: Register Routes**
Add endpoints to `router.go`.

---

### Task 4: Implement Trade Handlers

**Files:**
- Modify: `processor/internal/gateway/handler/trade.go`
- Modify: `processor/internal/gateway/router.go`

**Step 1: Add Trade RPCs**
Implement:
- `ListComboTrades`: `GET /api/v1/trades/combo`
- `GetOrderDealRecords`: `GET /api/v1/trades/deals`
- `SubscribeTrade`: `POST /api/v1/trades/subscribe`
- `UnsubscribeTrade`: `POST /api/v1/trades/unsubscribe`

**Step 2: Register Routes**
Add endpoints to `router.go`.

---

### Task 5: Implement Position Handlers

**Files:**
- Modify: `processor/internal/gateway/handler/position.go`
- Modify: `processor/internal/gateway/router.go`

**Step 1: Add Position RPCs**
Implement:
- `ListPositionDetail`: `GET /api/v1/positions/detail`
- `ListProfitLoss`: `GET /api/v1/positions/pnl`
- `ListProfitLossDetail`: `GET /api/v1/positions/pnl/detail`
- `ListProfitLossSummary`: `GET /api/v1/positions/pnl/summary`

**Step 2: Register Routes**
Add endpoints to `router.go`.

---

### Task 6: Implement Market Data Handlers

**Files:**
- Create: `processor/internal/gateway/handler/market.go`
- Modify: `processor/internal/gateway/router.go`

**Step 1: Create `market.go`**
Implement:
- `GetSnapshots`: `GET /api/v1/market/snapshots`
- `GetTicks`: `GET /api/v1/market/ticks`
- `GetKbars`: `GET /api/v1/market/kbars`
- `GetDailyQuotes`: `GET /api/v1/market/daily-quotes`
- `GetScanners`: `GET /api/v1/market/scanners`
- `GetPunish`: `GET /api/v1/market/punish`
- `GetNotice`: `GET /api/v1/market/notice`
- `FetchContracts`: `POST /api/v1/market/contracts/fetch`

**Step 2: Register Routes**
Add endpoints to `router.go`.

---

### Task 7: Implement Stock Reserve Handlers

**Files:**
- Create: `processor/internal/gateway/handler/reserve.go`
- Modify: `processor/internal/gateway/router.go`

**Step 1: Create `reserve.go`**
Implement:
- `GetStockReserveSummary`: `GET /api/v1/reserve/stock/summary`
- `GetStockReserveDetail`: `GET /api/v1/reserve/stock/detail`
- `ReserveStock`: `POST /api/v1/reserve/stock`
- `GetEarmarkingDetail`: `GET /api/v1/reserve/earmarking`
- `ReserveEarmarking`: `POST /api/v1/reserve/earmarking`
- `CreditEnquires`: `GET /api/v1/reserve/credit`
- `GetShortStockSources`: `GET /api/v1/reserve/short-sources`

**Step 2: Register Routes**
Add endpoints to `router.go`.

---

### Task 8: Final Verification

**Files:**
- Test: `processor/internal/gateway/server_test.go` (Create integration test if possible, or reliance on unit tests)

**Step 1: Run Lint**
`make lint-go`

**Step 2: Build**
`make build-go`

**Step 3: Commit**
`git add .`
`git commit -m "feat: expand REST API to cover all gRPC services"`
