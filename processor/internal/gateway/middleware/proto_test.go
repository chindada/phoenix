package middleware_test

import (
	"bytes"
	"context"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/gin-gonic/gin"
	"google.golang.org/protobuf/proto"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

func TestBind(t *testing.T) {
	gin.SetMode(gin.TestMode)

	t.Run("JSON", func(t *testing.T) {
		w := httptest.NewRecorder()
		c, _ := gin.CreateTestContext(w)

		jsonBody := `{"api_key": "123", "secret_key": "abc"}`
		req, _ := http.NewRequestWithContext(
			context.Background(),
			http.MethodPost,
			"/",
			bytes.NewBufferString(jsonBody),
		)
		req.Header.Set("Content-Type", "application/json")
		c.Request = req

		var reqObj pb.LoginRequest
		if err := middleware.Bind(c, &reqObj); err != nil {
			t.Fatalf("Bind() error = %v", err)
		}
		if reqObj.GetApiKey() != "123" {
			t.Errorf("ApiKey = %v, want 123", reqObj.GetApiKey())
		}
	})

	t.Run("Proto", func(t *testing.T) {
		w := httptest.NewRecorder()
		c, _ := gin.CreateTestContext(w)

		protoObj := &pb.LoginRequest{ApiKey: "123", SecretKey: "abc"}
		data, _ := proto.Marshal(protoObj)
		req, _ := http.NewRequestWithContext(context.Background(), http.MethodPost, "/", bytes.NewBuffer(data))
		req.Header.Set("Content-Type", "application/x-protobuf")
		c.Request = req

		var reqObj pb.LoginRequest
		if err := middleware.Bind(c, &reqObj); err != nil {
			t.Fatalf("Bind() error = %v", err)
		}
		if reqObj.GetApiKey() != "123" {
			t.Errorf("ApiKey = %v, want 123", reqObj.GetApiKey())
		}
	})
}

func TestRender(t *testing.T) {
	gin.SetMode(gin.TestMode)
	respObj := &pb.LoginResponse{} // just empty for now

	t.Run("JSON", func(t *testing.T) {
		w := httptest.NewRecorder()
		c, _ := gin.CreateTestContext(w)
		req, _ := http.NewRequestWithContext(context.Background(), http.MethodGet, "/", nil)
		req.Header.Set("Accept", "application/json")
		c.Request = req

		middleware.Render(c, http.StatusOK, respObj)
		if w.Header().Get("Content-Type") != "application/json; charset=utf-8" {
			t.Errorf("Content-Type = %v, want %v", w.Header().Get("Content-Type"), "application/json; charset=utf-8")
		}
	})

	t.Run("Proto", func(t *testing.T) {
		w := httptest.NewRecorder()
		c, _ := gin.CreateTestContext(w)
		req, _ := http.NewRequestWithContext(context.Background(), http.MethodGet, "/", nil)
		req.Header.Set("Accept", "application/x-protobuf")
		c.Request = req

		middleware.Render(c, http.StatusOK, respObj)
		if w.Header().Get("Content-Type") != "application/x-protobuf" {
			t.Errorf("Content-Type = %v, want %v", w.Header().Get("Content-Type"), "application/x-protobuf")
		}
	})
}
