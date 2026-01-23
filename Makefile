.PHONY: install codegen codegen-go run-server clean-venv venv lint format type-check install-lint-go lint-go

PROTO_DIR = ./protos/v1
PROVIDER_DIR = ./provider
PROCESSOR_DIR = ./processor
GO_PB_DIR = $(PROCESSOR_DIR)/pkg/pb
SRC_DIR = $(PROVIDER_DIR)/src
VENV = $(shell pwd)/.venv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python
PIP = $(BIN)/pip

$(VENV):
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip

venv: $(VENV)

install:
	@$(PIP) install -r $(PROVIDER_DIR)/requirements.txt

codegen: codegen-py codegen-go

codegen-py:
	@$(PYTHON) -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(SRC_DIR) --pyi_out=$(SRC_DIR) --grpc_python_out=$(SRC_DIR) $(PROTO_DIR)/provider.proto

codegen-go:
	@protoc -I$(PROTO_DIR) \
		--go_out=$(GO_PB_DIR) --go_opt=paths=source_relative \
		--go-grpc_out=$(GO_PB_DIR) --go-grpc_opt=paths=source_relative \
		$(PROTO_DIR)/provider.proto

lint: lint-py lint-go

lint-py: type-check type-check-pyright
	@$(BIN)/ruff format --exclude $(SRC_DIR)/*_pb2.py --exclude $(SRC_DIR)/*_pb2.pyi --exclude $(SRC_DIR)/*_pb2_grpc.py
	@$(BIN)/ruff check --fix $(PROVIDER_DIR) --exclude $(SRC_DIR)/*_pb2.py --exclude $(SRC_DIR)/*_pb2.pyi --exclude $(SRC_DIR)/*_pb2_grpc.py
	@$(BIN)/pylint --rcfile=$(PROVIDER_DIR)/.pylintrc $(PROVIDER_DIR)

lint-go:
	@echo "Linting all platforms..."
	@cd $(PROCESSOR_DIR); gofumpt -l -w .
	@cd $(PROCESSOR_DIR); golangci-lint-v2 fmt ./...
	make lint-windows
	make lint-darwin
	make lint-linux

lint-windows:
	@echo "Linting for windows..."
	@cd $(PROCESSOR_DIR); CGO_ENABLED=0 GOOS=windows GOARCH=amd64 golangci-lint-v2 run --config ./.golangci.yml  ./...

lint-darwin:
	@echo "Linting for darwin..."
	@cd $(PROCESSOR_DIR); CGO_ENABLED=0 GOOS=darwin GOARCH=arm64 golangci-lint-v2 run --config ./.golangci.yml  ./...

lint-linux:
	@echo "Linting for linux..."
	@cd $(PROCESSOR_DIR); CGO_ENABLED=0 GOOS=linux GOARCH=amd64 golangci-lint-v2 run --config ./.golangci.yml  ./...


type-check:
	@$(BIN)/mypy $(PROVIDER_DIR) --exclude $(SRC_DIR)/*_pb2.py --exclude $(SRC_DIR)/*_pb2.pyi --exclude $(SRC_DIR)/*_pb2_grpc.py --disable-error-code=import-untyped

type-check-pyright:
	@cd $(PROVIDER_DIR) && $(BIN)/pyright

run-server:
	@SJ_LOG_PATH=$(shell pwd)/logs/shioaji.log SJ_CONTRACTS_PATH=$(shell pwd)/$(PROVIDER_DIR)/data $(PYTHON) $(SRC_DIR)/server.py

clean-venv:
	@rm -rf $(VENV)

migrate-create-phoenix:
	@go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@latest
	@migrate create -ext sql -dir migrations/phoenix -tz "Asia/Taipei" -seq -digits 4 'phoenix'
