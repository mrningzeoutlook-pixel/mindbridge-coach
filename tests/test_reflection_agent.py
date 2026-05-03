"""
Tests for Reflection Agent
==========================

Unit tests for the ReflectionAgent class.
"""

import pytest
from src.agents.reflection_agent import ReflectionAgent, ReflectionGuide, ReflectionPrompt


class TestReflectionAgent:
    """Test suite for ReflectionAgent."""

    def setup_method(self):
        """Set up test fixtures."""
        self.agent = ReflectionAgent()

    def test_reflect_returns_guide_object(self):
        """Test that reflect() returns a ReflectionGuide object."""
        guide = self.agent.reflect("weekly")
        assert isinstance(guide, ReflectionGuide)

    def test_reflect_daily_prompts(self):
        """Test daily reflection prompts."""
        guide = self.agent.reflect("daily")
        assert guide.reflection_type == "daily"
        assert len(guide.prompts) >= 4

    def test_reflect_weekly_prompts(self):
        """Test weekly reflection prompts."""
        guide = self.agent.reflect("weekly")
        assert guide.reflection_type == "weekly"
        assert len(guide.prompts) >= 5

    def test_reflect_monthly_prompts(self):
        """Test monthly reflection prompts."""
        guide = self.agent.reflect("monthly")
        assert guide.reflection_type == "monthly"
        assert len(guide.prompts) >= 5

    def test_reflect_invalid_type_defaults_to_weekly(self):
        """Test that invalid reflection type falls back to weekly."""
        guide = self.agent.reflect("invalid-type")
        assert guide.reflection_type == "weekly"

    def test_reflect_prompts_have_required_fields(self):
        """Test that prompts have all required fields."""
        guide = self.agent.reflect("gratitude")
        for prompt in guide.prompts:
            assert hasattr(prompt, "question")
            assert hasattr(prompt, "order")
            assert hasattr(prompt, "category")
            assert isinstance(prompt.question, str)
            assert isinstance(prompt.order, int)

    def test_reflect_has_guidance(self):
        """Test that reflection guide has guidance text."""
        guide = self.agent.reflect("daily")
        assert hasattr(guide, "guidance")
        assert isinstance(guide.guidance, str)
        assert len(guide.guidance) > 0

    def test_reflect_has_tip(self):
        """Test that reflection guide has a tip."""
        guide = self.agent.reflect("daily")
        assert hasattr(guide, "tip")
        assert isinstance(guide.tip, str)
        assert len(guide.tip) > 0

    def test_reflect_has_timestamp(self):
        """Test that reflection guide has a timestamp."""
        guide = self.agent.reflect("weekly")
        assert hasattr(guide, "created_at")
        assert guide.created_at is not None

    def test_reflect_normalizes_type(self):
        """Test that reflection type is normalized."""
        guide = self.agent.reflect("DAILY")
        assert guide.reflection_type == "daily"

        guide = self.agent.reflect("  Weekly  ")
        assert guide.reflection_type == "weekly"

    def test_generate_insight_questions(self):
        """Test generation of insight questions."""
        questions = self.agent.generate_insight_questions("weekly")
        assert isinstance(questions, list)
        assert len(questions) > 0
        assert all(isinstance(q, str) for q in questions)

    def test_identify_patterns(self):
        """Test pattern identification from history."""
        history = [
            {"reflection": "I felt stressed about work"},
            {"reflection": "Work was challenging today"},
        ]
        patterns = self.agent.identify_patterns(history)
        assert isinstance(patterns, dict)
        assert "recurring_themes" in patterns


class TestReflectionGuide:
    """Test suite for ReflectionGuide dataclass."""

    def test_reflection_guide_creation(self):
        """Test creating a ReflectionGuide object."""
        prompts = [
            ReflectionPrompt(question="Test?", order=1, category="test"),
        ]
        guide = ReflectionGuide(
            reflection_type="test",
            prompts=prompts,
            guidance="Test guidance",
            tip="Test tip",
        )
        assert guide.reflection_type == "test"
        assert len(guide.prompts) == 1
        assert guide.guidance == "Test guidance"
        assert guide.tip == "Test tip"
