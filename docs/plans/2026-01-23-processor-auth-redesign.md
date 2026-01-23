# Design: Processor Authentication & User Management

**Date:** 2026-01-23
**Status:** Approved
**Topic:** Transitioning Processor's `/api/v1/login` to use a local database and establishing a system-wide Provider session.

## Overview
Currently, the Processor's `/api/v1/login` proxies Shioaji credentials directly to the Provider. We want to move to a model where:
1. The **Processor** manages its own users in a PostgreSQL database.
2. The **Provider** connection is established once by the Processor at startup using system environment variables.
3. Users authenticate against the Processor to get a JWT, which authorizes them to use the already-connected Shioaji session.

## Architecture & Components

### 1. Database Schema
We will use the existing `pkg/postgres/launcher` and `golang-migrate` to manage the schema.
- **Table:** `users`
    - `username` (TEXT, PK)
    - `password_hash` (TEXT, NOT NULL)
    - `created_at` (TIMESTAMPTZ, DEFAULT NOW())
    - `updated_at` (TIMESTAMPTZ, DEFAULT NOW())

### 2. Startup Lifecycle (main.go)
1. **Initialize Database:** Start PostgreSQL using `launcher.New(...)`. Run `MigrateScheme(nil)`.
2. **System Login:** Read `SHIOAJI_API_KEY` and `SHIOAJI_SECRET_KEY` from environment variables. Call `grpcClient.Login(...)` immediately.
3. **Seed Admin:** If the `users` table is empty, create a default user `admin` with a hashed password.
4. **Dependency Injection:** Initialize `UserRepository` and pass it to the Gateway/Handlers.

### 3. Data Access (internal/repository)
- **UserRepository Interface:**
    - `GetByUsername(ctx, username) (*User, error)`
    - `Create(ctx, user) error`
- **Implementation:** Uses `squirrel` for SQL building and `pgxpool` for execution.

### 4. Authentication Flow
- **POST /api/v1/login**:
    - Request Body: `{ "username": "...", "password": "..." }`
    - Logic:
        1. Fetch user from DB.
        2. Compare hash using `bcrypt`.
        3. Issue JWT if successful.
- **JWT Middleware**: Continues to validate the token but no longer checks for provider session state (as the provider is globally connected).

## Environment Variables
- `SHIOAJI_API_KEY`: Required for system login.
- `SHIOAJI_SECRET_KEY`: Required for system login.
- `DB_NAME`: Database name (e.g., `mojave`).
- `JWT_SECRET`: Used for signing tokens.

## Implementation Plan
1. Update migrations.
2. Implement `UserRepository`.
3. Update `main.go` for DB and System Login.
4. Refactor `handler.Login` to use the repository.
5. Verify with integration tests.
