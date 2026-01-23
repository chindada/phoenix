package phoenix

import "embed"

//go:embed *.sql
var Asset embed.FS
