"""
Utility Functions Package
=========================

Provides common utilities for logging, formatting, validation, and
other helper functions used across the MindBridge Coach project.
"""

from .formatters import format_session, format_reflection, format_prompt
from .validators import validate_focus_area, validate_prompt_type
from .logger import get_logger, setup_logging

__all__ = [
    "format_session",
    "format_reflection",
    "format_prompt",
    "validate_focus_area",
    "validate_prompt_type",
    "get_logger",
    "setup_logging",
]
