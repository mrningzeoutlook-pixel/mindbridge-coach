"""
Tests for Utilities
===================

Unit tests for utility functions.
"""

import pytest
from src.utils.formatters import (
    format_session,
    format_reflection,
    format_prompt,
    truncate_text,
    format_progress_bar,
)
from src.utils.validators import (
    validate_focus_area,
    validate_prompt_type,
    validate_framework,
    validate_score,
    validate_non_empty,
    get_valid_options,
)


class TestFormatters:
    """Tests for formatting utilities."""

    def test_format_session(self):
        """Test session formatting."""
        steps = [
            {"stage": "Goal", "prompt": "Test?", "tips": "Be good"},
        ]
        output = format_session("test-focus", "GROW Model", steps, 30)
        assert "test-focus" in output
        assert "GROW Model" in output
        assert "30" in output

    def test_format_reflection(self):
        """Test reflection formatting."""
        prompts = ["Question 1?", "Question 2?"]
        output = format_reflection("daily", prompts, "Guidance", "Tip")
        assert "Daily" in output
        assert "1. Question 1?" in output
        assert "2. Question 2?" in output

    def test_format_prompt(self):
        """Test prompt formatting."""
        output = format_prompt("Test question?", "general")
        assert output == "Test question?"

        output = format_prompt("Test?", "growth", True, 1)
        assert "1. Test?" in output
        assert "growth" in output

    def test_truncate_text(self):
        """Test text truncation."""
        text = "This is a very long text that should be truncated"
        result = truncate_text(text, 20)
        assert len(result) <= 23  # 20 + "..."
        assert result.endswith("...")

        # Short text should not be truncated
        short = "Short"
        assert truncate_text(short, 20) == short

    def test_format_progress_bar(self):
        """Test progress bar formatting."""
        bar = format_progress_bar(4, 10)
        assert "40%" in bar
        assert "[" in bar
        assert "]" in bar

        # Edge cases
        bar = format_progress_bar(0, 10)
        assert "0%" in bar

        bar = format_progress_bar(10, 10)
        assert "100%" in bar


class TestValidators:
    """Tests for validation utilities."""

    def test_validate_focus_area_valid(self):
        """Test validation of valid focus areas."""
        is_valid, msg = validate_focus_area("career-transition")
        assert is_valid is True
        assert msg == ""

    def test_validate_focus_area_invalid(self):
        """Test validation of invalid focus areas."""
        is_valid, msg = validate_focus_area("invalid-area")
        assert is_valid is False
        assert len(msg) > 0

    def test_validate_prompt_type_valid(self):
        """Test validation of valid prompt types."""
        is_valid, msg = validate_prompt_type("daily")
        assert is_valid is True

        is_valid, msg = validate_prompt_type("weekly")
        assert is_valid is True

    def test_validate_prompt_type_invalid(self):
        """Test validation of invalid prompt types."""
        is_valid, msg = validate_prompt_type("invalid")
        assert is_valid is False

    def test_validate_framework_valid(self):
        """Test validation of valid frameworks."""
        for framework in ["grow", "ikigai", "smart"]:
            is_valid, msg = validate_framework(framework)
            assert is_valid is True

    def test_validate_framework_invalid(self):
        """Test validation of invalid frameworks."""
        is_valid, msg = validate_framework("unknown")
        assert is_valid is False

    def test_validate_score(self):
        """Test score validation."""
        is_valid, msg = validate_score(5)
        assert is_valid is True

        is_valid, msg = validate_score(15)
        assert is_valid is False

        is_valid, msg = validate_score(-1)
        assert is_valid is False

    def test_validate_non_empty(self):
        """Test non-empty validation."""
        is_valid, msg = validate_non_empty("hello")
        assert is_valid is True

        is_valid, msg = validate_non_empty("")
        assert is_valid is False

        is_valid, msg = validate_non_empty("  ")
        assert is_valid is False

    def test_get_valid_options(self):
        """Test getting valid options."""
        options = get_valid_options()
        assert "focus_areas" in options
        assert "prompt_types" in options
        assert "frameworks" in options
        assert isinstance(options["focus_areas"], list)
        assert isinstance(options["prompt_types"], list)
        assert isinstance(options["frameworks"], list)
