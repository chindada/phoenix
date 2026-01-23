package repository

import (
	"errors"
	"time"
)

// ErrNotFound is returned when a record is not found in the database.
var ErrNotFound = errors.New("not found")

// User represents a user record in the database.
type User struct {
	Username     string
	PasswordHash string
	CreatedAt    time.Time
	UpdatedAt    time.Time
}
