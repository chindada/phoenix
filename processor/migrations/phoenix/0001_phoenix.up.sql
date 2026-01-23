BEGIN;

CREATE TABLE IF NOT EXISTS users (
    username      TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMIT;