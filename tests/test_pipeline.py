"""
Tests for MindBridge Pipeline
==============================

Unit tests for the MindBridgePipeline class.
"""

import pytest
from src.agents.pipeline import MindBridgePipeline


class TestMindBridgePipeline:
    """Test suite for MindBridgePipeline."""

    def setup_method(self):
        """Set up test fixtures."""
        self.pipeline = MindBridgePipeline()

    def test_pipeline_initialization(self):
        """Test that pipeline initializes with all agents."""
        assert hasattr(self.pipeline, "assessment_agent")
        assert hasattr(self.pipeline, "coaching_agent")
        assert hasattr(self.pipeline, "reflection_agent")

    def test_session_returns_string(self):
        """Test that session() returns a string."""
        output = self.pipeline.session("career-transition")
        assert isinstance(output, str)

    def test_session_contains_focus_area(self):
        """Test that session output contains the focus area."""
        output = self.pipeline.session("career-transition")
        assert "CAREER-TRANSITION" in output

    def test_session_contains_framework(self):
        """Test that session output contains the framework name."""
        output = self.pipeline.session("career-transition")
        assert "GROW" in output

    def test_session_with_purpose_focus(self):
        """Test session with purpose focus area."""
        output = self.pipeline.session("purpose")
        assert "PURPOSE" in output or "Ikigai" in output

    def test_session_with_smart_focus(self):
        """Test session with goal-setting focus."""
        output = self.pipeline.session("goal-setting")
        assert "SMART" in output

    def test_reflect_returns_string(self):
        """Test that reflect() returns a string."""
        output = self.pipeline.reflect("weekly")
        assert isinstance(output, str)

    def test_reflect_contains_prompts(self):
        """Test that reflection output contains prompts."""
        output = self.pipeline.reflect("daily")
        assert "Reflection" in output
        assert "1." in output  # Prompt numbering

    def test_reflect_different_types(self):
        """Test reflection with different prompt types."""
        for prompt_type in ["daily", "weekly", "monthly", "gratitude"]:
            output = self.pipeline.reflect(prompt_type)
            assert isinstance(output, str)
            assert prompt_type.title() in output

    def test_full_experience_returns_string(self):
        """Test that full_experience() returns a string."""
        output = self.pipeline.full_experience("career-transition")
        assert isinstance(output, str)

    def test_full_experience_contains_both(self):
        """Test that full experience contains both session and reflection."""
        output = self.pipeline.full_experience("purpose", "weekly")
        assert "PURPOSE" in output
        assert "Reflection" in output

    def test_format_coaching_session(self):
        """Test formatting of coaching session."""
        mock_guidance = self.pipeline.coaching_agent.coach(
            {"focus_area": "test"},
            "grow"
        )
        output = self.pipeline._format_coaching_session("test", mock_guidance)
        assert isinstance(output, str)
        assert "TEST" in output

    def test_format_reflection(self):
        """Test formatting of reflection."""
        mock_reflection = self.pipeline.reflection_agent.reflect("weekly")
        output = self.pipeline._format_reflection(mock_reflection)
        assert isinstance(output, str)
        assert "Weekly" in output
