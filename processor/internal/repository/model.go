package repository

import "time"

// User represents a user record in the database.
type User struct {
	Username     string
	PasswordHash string
	CreatedAt    time.Time
	UpdatedAt    time.Time
}
