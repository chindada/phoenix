# DEBUG

- .vscode/settings.json

```json
{
    "python.analysis.extraPaths": [
        "./provider/src"
    ]
}
```

- .vscode/launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "processor",
            "type": "go",
            "request": "launch",
            "debugAdapter": "dlv-dap",
            "mode": "exec",
            "preLaunchTask": "build processor",
            "program": "${workspaceFolder}/processor/bin/processor",
            "console": "integratedTerminal",
            "internalConsoleOptions": "neverOpen",
            "env": {
                "SHIOAJI_API_KEY": "AmeUuVs6ca9BdLw6rwF7GMRjeu1dGX64YSrEbYqh8VmE",
                "SHIOAJI_SECRET_KEY": "DvkA9cDKuFrzuitxDD42gERPoo6YgkhF4Pbaz3Xqw8QT",
            },
        },
        {
            "name": "provider",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/provider/src/provider.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "SJ_LOG_PATH": "${workspaceFolder}/provider/logs/shioaji.log",
                "SJ_CONTRACTS_PATH": "${workspaceFolder}/provider/data",
            },
            "python": "${command:python.interpreterPath}",
            "pythonArgs": [
                "-BO"
            ],
            "preLaunchTask": "Check venv",
            "internalConsoleOptions": "neverOpen",
        }
    ],
    "compounds": [
        {
            "name": "integrated",
            "configurations": [
                "provider",
                "processor"
            ],
            "stopAll": true
        }
    ]
}
```

- .vscode/tasks.json

```json
{
    "version": "2.0.0",
    "cwd": "${workspaceFolder}",
    "type": "shell",
    "presentation": {
        "close": true
    },
    "tasks": [
        {
            "label": "build processor",
            "command": "go",
            "args": [
                "build",
                "-o",
                "./bin/processor",
                "-gcflags=all=\"-N -l\"",
                "-tags",
                "debug",
                "./cmd/phoenix/main.go",
            ],
            "options": {
                "cwd": "${workspaceFolder}/processor"
            }
        },
        {
            "label": "Check venv",
            "command": "",
            "args": [
                "source",
                ".venv/bin/activate;",
            ],
        },
    ]
}
```
