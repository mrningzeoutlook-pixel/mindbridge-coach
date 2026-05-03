"""
Tests for Coaching Agent
========================

Unit tests for the CoachingAgent class.
"""

import pytest
from src.agents.coaching_agent import CoachingAgent, CoachingGuidance, CoachingStep


class TestCoachingAgent:
    """Test suite for CoachingAgent."""

    def setup_method(self):
        """Set up test fixtures."""
        self.agent = CoachingAgent()
        self.sample_assessment = {
            "focus_area": "career-transition",
            "recommended_framework": "grow",
        }

    def test_coach_returns_guidance_object(self):
        """Test that coach() returns a CoachingGuidance object."""
        guidance = self.agent.coach(self.sample_assessment, "grow")
        assert isinstance(guidance, CoachingGuidance)

    def test_coach_with_grow_framework(self):
        """Test coaching with GROW framework."""
        guidance = self.agent.coach(self.sample_assessment, "grow")
        assert guidance.framework == "GROW Model"
        assert len(guidance.steps) == 4

    def test_coach_with_ikigai_framework(self):
        """Test coaching with Ikigai framework."""
        guidance = self.agent.coach(self.sample_assessment, "ikigai")
        assert guidance.framework == "Ikigai Framework"
        assert len(guidance.steps) == 4

    def test_coach_with_smart_framework(self):
        """Test coaching with SMART framework."""
        guidance = self.agent.coach(self.sample_assessment, "smart")
        assert guidance.framework == "SMART Goals"
        assert len(guidance.steps) == 5

    def test_coach_invalid_framework_defaults_to_grow(self):
        """Test that invalid framework falls back to GROW."""
        guidance = self.agent.coach(self.sample_assessment, "invalid")
        assert guidance.framework == "GROW Model"

    def test_coach_steps_have_required_fields(self):
        """Test that coaching steps have all required fields."""
        guidance = self.agent.coach(self.sample_assessment, "grow")
        for step in guidance.steps:
            assert hasattr(step, "stage")
            assert hasattr(step, "prompt")
            assert hasattr(step, "tips")
            assert hasattr(step, "order")
            assert isinstance(step.stage, str)
            assert isinstance(step.prompt, str)

    def test_coach_sets_focus_area(self):
        """Test that coaching guidance includes focus area."""
        guidance = self.agent.coach(self.sample_assessment, "grow")
        assert guidance.focus_area == "career-transition"

    def test_coach_has_estimated_duration(self):
        """Test that coaching guidance has estimated duration."""
        guidance = self.agent.coach(self.sample_assessment, "grow")
        assert guidance.estimated_duration_minutes > 0

    def test_generate_tips_returns_string(self):
        """Test that _generate_tips returns a string."""
        tip = self.agent._generate_tips("Goal", "grow")
        assert isinstance(tip, str)
        assert len(tip) > 0

    def test_get_framework_info(self):
        """Test getting framework information."""
        info = self.agent.get_framework_info("grow")
        assert isinstance(info, dict)
        assert "name" in info
        assert "description" in info
        assert "steps" in info
        assert info["name"] == "GROW Model"

    def test_estimate_duration(self):
        """Test duration estimation for different frameworks."""
        assert self.agent._estimate_duration("grow") == 30
        assert self.agent._estimate_duration("ikigai") == 45
        assert self.agent._estimate_duration("smart") == 25


class TestCoachingGuidance:
    """Test suite for CoachingGuidance dataclass."""

    def test_coaching_guidance_creation(self):
        """Test creating a CoachingGuidance object."""
        steps = [
            CoachingStep(stage="Goal", prompt="What do you want?", tips="Be specific", order=1),
        ]
        guidance = CoachingGuidance(
            framework="Test Framework",
            focus_area="test",
            steps=steps,
        )
        assert guidance.framework == "Test Framework"
        assert guidance.focus_area == "test"
        assert len(guidance.steps) == 1
