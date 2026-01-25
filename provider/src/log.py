"""
Logging configuration for the provider.
"""

import logging
import os
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

import colorlog
from pythonjsonlogger import json


class CustomJsonFormatter(json.JsonFormatter):
    """
    Custom JSON formatter that adds a timestamp and ensures the level is uppercase.
    """

    def add_fields(self, log_data, record, message_dict):
        """
        Add custom fields to the JSON log record.
        """
        super().add_fields(log_data, record, message_dict)
        if not log_data.get("timestamp"):
            now = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]
            log_data["timestamp"] = now
        if log_data.get("level"):
            log_data["level"] = log_data["level"].upper()
        else:
            log_data["level"] = record.levelname


def SetupLogger():
    """
    Configures and returns the global logger.
    """
    log_level_str = os.getenv("LOG_LEVEL", "info").upper()
    level = getattr(logging, log_level_str, logging.INFO)

    disable_console = os.getenv("LOG_DISABLE_CONSOLE", "false").lower() == "true"
    disable_file = os.getenv("LOG_DISABLE_FILE", "false").lower() == "true"

    log = logging.getLogger()
    log.setLevel(level)

    # Remove existing handlers
    for handler in log.handlers[:]:
        log.removeHandler(handler)

    if not disable_console:
        console_handler = logging.StreamHandler(sys.stdout)
        coloring_enabled = (
            os.getenv("NO_COLOR") == "" and os.getenv("TERM") != "xterm-mono"
        )

        if sys.stdout.isatty() and coloring_enabled:
            formatter = colorlog.ColoredFormatter(
                "%(log_color)s%(asctime)s.%(msecs)03d %(levelname)-8s%(reset)s %(message)s",
                datefmt="%Y/%m/%d %H:%M:%S",
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
            )
        else:
            formatter = logging.Formatter(
                "%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
                datefmt="%Y/%m/%d %H:%M:%S",
            )

        console_handler.setFormatter(formatter)
        log.addHandler(console_handler)

    if not disable_file:
        try:
            base_dir = Path(__file__).resolve().parent.parent
            log_dir = base_dir / "logs"
            log_dir.mkdir(parents=True, exist_ok=True)
            log_file = log_dir / "provider.log"
            file_handler = RotatingFileHandler(
                log_file, maxBytes=500 * 1024 * 1024, backupCount=3
            )
            file_formatter = CustomJsonFormatter(
                "%(timestamp)s %(level)s %(name)s %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            log.addHandler(file_handler)
        except Exception as exc:
            print(f"Failed to setup file logging: {exc}", file=sys.stderr)
    return log


logger = SetupLogger()


def L():
    """
    Returns the global logger instance.
    """
    return logger


def S():
    """
    Returns the global logger instance (Sugared equivalent).
    """
    return logger
