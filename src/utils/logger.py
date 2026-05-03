"""
Logging Utilities
================

Provides logging configuration and helper functions for the
MindBridge Coach project.
"""

import logging
import sys
from typing import Optional


def setup_logging(
    level: str = "INFO",
    format_string: Optional[str] = None,
    log_to_file: bool = False,
    log_file: str = "mindbridge.log"
) -> logging.Logger:
    """
    Set up logging configuration for the project.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format_string: Custom format string for log messages
        log_to_file: Whether to also log to a file
        log_file: Path to log file if log_to_file is True

    Returns:
        Configured logger instance
    """
    if format_string is None:
        format_string = "[%(asctime)s] %(levelname)s - %(name)s: %(message)s"

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=format_string,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[]
    )

    # Get logger for this project
    logger = logging.getLogger("mindbridge")

    # Clear any existing handlers
    logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    console_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(console_handler)

    # File handler if requested
    if log_to_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(format_string))
        logger.addHandler(file_handler)

    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance for a specific module.

    Args:
        name: Name of the module (typically __name__)

    Returns:
        Logger instance
    """
    if name:
        return logging.getLogger(f"mindbridge.{name}")
    return logging.getLogger("mindbridge")


class LoggerMixin:
    """
    Mixin class to add logging capability to any class.

    Usage:
        class MyClass(LoggerMixin):
            def __init__(self):
                self.setup_logger()

        obj = MyClass()
        obj.logger.info("This is a log message")
    """

    _logger: Optional[logging.Logger] = None

    def setup_logger(self, name: Optional[str] = None):
        """
        Initialize the logger for this instance.

        Args:
            name: Optional name for the logger
        """
        if name is None:
            name = self.__class__.__name__

        self._logger = logging.getLogger(f"mindbridge.{name}")

    @property
    def logger(self) -> logging.Logger:
        """
        Get the logger instance.

        Returns:
            Logger instance, initializing if necessary
        """
        if self._logger is None:
            self._logger = logging.getLogger(f"mindbridge.{self.__class__.__name__}")
        return self._logger


def log_entry_exit(func):
    """
    Decorator to log function entry and exit.

    Usage:
        @log_entry_exit
        def my_function(arg1, arg2):
            # function body
            pass
    """
    import functools
    import logging

    logger = logging.getLogger("mindbridge")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Entering {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"Exiting {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise

    return wrapper
