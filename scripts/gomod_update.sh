#!/bin/bash

cd processor >> /dev/null

rm -rf go.mod
rm -rf go.sum

version="1.25.5"
go install golang.org/dl/go$version@latest && go"$version" download

go"$version" mod init phoenix/processor
go"$version" mod tidy

git add go.mod go.sum
cd - >> /dev/null
