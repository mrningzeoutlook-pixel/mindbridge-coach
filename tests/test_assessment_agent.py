"""
Tests for Assessment Agent
===========================

Unit tests for the AssessmentAgent class.
"""

import pytest
from src.agents.assessment_agent import AssessmentAgent, AssessmentResult


class TestAssessmentAgent:
    """Test suite for AssessmentAgent."""

    def setup_method(self):
        """Set up test fixtures."""
        self.agent = AssessmentAgent()

    def test_assess_returns_assessment_result(self):
        """Test that assess() returns an AssessmentResult object."""
        result = self.agent.assess("career-transition")
        assert isinstance(result, AssessmentResult)
        assert result.focus_area == "career-transition"

    def test_assess_with_valid_focus_area(self):
        """Test assessment with different focus areas."""
        test_cases = [
            ("career-transition", "grow"),
            ("purpose", "ikigai"),
            ("goal-setting", "smart"),
            ("life-balance", "wheel"),
            ("unknown-focus", "grow"),  # Default
        ]

        for focus, expected_framework in test_cases:
            result = self.agent.assess(focus)
            assert result.focus_area == focus.lower()
            assert result.recommended_framework == expected_framework

    def test_assess_includes_challenges(self):
        """Test that assessment includes key challenges."""
        result = self.agent.assess("career-transition")
        assert isinstance(result.key_challenges, list)
        assert len(result.key_challenges) > 0

    def test_assess_includes_strengths(self):
        """Test that assessment includes strengths."""
        result = self.agent.assess("purpose-discovery")
        assert isinstance(result.strengths, list)
        assert len(result.strengths) > 0
        assert "self-awareness" in result.strengths

    def test_assess_has_timestamp(self):
        """Test that assessment has a timestamp."""
        result = self.agent.assess("career")
        assert hasattr(result, "assessed_at")
        assert result.assessed_at is not None

    def test_assess_normalizes_focus_area(self):
        """Test that focus area is normalized to lowercase."""
        result = self.agent.assess("CAREER-TRANSITION")
        assert result.focus_area == "career-transition"

        result = self.agent.assess("  Purpose  ")
        assert result.focus_area == "purpose"

    def test_recommend_framework_returns_string(self):
        """Test that _recommend_framework returns a string."""
        framework = self.agent._recommend_framework("career-transition")
        assert isinstance(framework, str)
        assert framework in ["grow", "ikigai", "smart", "wheel"]

    def test_generate_follow_up_questions(self):
        """Test generation of follow-up questions."""
        result = self.agent.assess("career-transition")
        questions = self.agent.generate_follow_up_questions(result)
        assert isinstance(questions, list)
        assert len(questions) > 0
        assert all(isinstance(q, str) for q in questions)


class TestAssessmentResult:
    """Test suite for AssessmentResult dataclass."""

    def test_assessment_result_creation(self):
        """Test creating an AssessmentResult."""
        result = AssessmentResult(
            focus_area="test-focus",
            satisfaction_score=0.7,
            key_challenges=["challenge1"],
            strengths=["strength1"],
            recommended_framework="grow",
        )
        assert result.focus_area == "test-focus"
        assert result.satisfaction_score == 0.7
        assert result.recommended_framework == "grow"
