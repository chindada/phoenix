package repository

import (
	"context"
	"fmt"

	"github.com/jackc/pgx/v5"

	"phoenix/processor/pkg/postgres/client"
)

// UserRepository defines the interface for user data access.
type UserRepository interface {
	GetByUsername(ctx context.Context, username string) (*User, error)
	Create(ctx context.Context, user *User) error
	Count(ctx context.Context) (int, error)
}

type userRepo struct {
	client client.PGClient
}

// NewUserRepository creates a new UserRepository.
func NewUserRepository(c client.PGClient) UserRepository {
	return &userRepo{client: c}
}

// GetByUsername fetches a user by their username.
func (r *userRepo) GetByUsername(ctx context.Context, username string) (*User, error) {
	sql, args, err := r.client.Builder().
		Select("username, password_hash, created_at, updated_at").
		From("users").
		Where("username = ?", username).
		ToSql()
	if err != nil {
		return nil, fmt.Errorf("UserRepository.GetByUsername - r.client.Builder: %w", err)
	}

	row := r.client.Pool().QueryRow(ctx, sql, args...)
	var user User
	err = row.Scan(&user.Username, &user.PasswordHash, &user.CreatedAt, &user.UpdatedAt)
	if err != nil {
		if err == pgx.ErrNoRows {
			return nil, nil
		}
		return nil, fmt.Errorf("UserRepository.GetByUsername - row.Scan: %w", err)
	}

	return &user, nil
}

// Create inserts a new user into the database.
func (r *userRepo) Create(ctx context.Context, user *User) error {
	sql, args, err := r.client.Builder().
		Insert("users").
		Columns("username, password_hash, created_at, updated_at").
		Values(user.Username, user.PasswordHash, user.CreatedAt, user.UpdatedAt).
		ToSql()
	if err != nil {
		return fmt.Errorf("UserRepository.Create - r.client.Builder: %w", err)
	}

	_, err = r.client.Pool().Exec(ctx, sql, args...)
	if err != nil {
		return fmt.Errorf("UserRepository.Create - r.client.Pool().Exec: %w", err)
	}

	return nil
}

// Count returns the number of users in the database.
func (r *userRepo) Count(ctx context.Context) (int, error) {
	sql, args, err := r.client.Builder().
		Select("COUNT(*)").
		From("users").
		ToSql()
	if err != nil {
		return 0, fmt.Errorf("UserRepository.Count - r.client.Builder: %w", err)
	}

	var count int
	err = r.client.Pool().QueryRow(ctx, sql, args...).Scan(&count)
	if err != nil {
		return 0, fmt.Errorf("UserRepository.Count - QueryRow.Scan: %w", err)
	}

	return count, nil
}
