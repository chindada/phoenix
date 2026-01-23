package middleware

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
	"google.golang.org/protobuf/proto"
)

const ContentTypeProtobuf = "application/x-protobuf"

// Bind binds the request body to the proto message based on Content-Type.
func Bind(c *gin.Context, obj proto.Message) error {
	if c.ContentType() == ContentTypeProtobuf {
		data, err := io.ReadAll(c.Request.Body)
		if err != nil {
			return err
		}
		return proto.Unmarshal(data, obj)
	}
	// Default to JSON
	return c.ShouldBindJSON(obj)
}

// Render writes the proto message to the response based on Accept header.
func Render(c *gin.Context, code int, obj proto.Message) {
	accept := c.GetHeader("Accept")
	if accept == ContentTypeProtobuf {
		data, err := proto.Marshal(obj)
		if err != nil {
			c.AbortWithError(http.StatusInternalServerError, err)
			return
		}
		c.Data(code, ContentTypeProtobuf, data)
		return
	}
	// Default to JSON
	c.JSON(code, obj)
}
