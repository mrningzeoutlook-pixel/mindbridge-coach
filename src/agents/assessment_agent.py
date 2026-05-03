"""
Assessment Agent - Agent 1 of the MindBridge Three-Layer Architecture
=====================================================================

This agent is responsible for guiding self-assessment and identifying
the user's current state across various life domains.

Key Responsibilities:
- Evaluate satisfaction levels in different life areas
- Identify key challenges and strengths
- Recommend appropriate coaching frameworks based on focus area
- Gather baseline information for personalized coaching
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict
from datetime import datetime


@dataclass
class AssessmentResult:
    """Data class representing the results of a self-assessment."""
    focus_area: str
    satisfaction_score: float  # 0.0 to 1.0
    key_challenges: List[str]
    strengths: List[str]
    recommended_framework: str
    assessed_at: str = field(default_factory=lambda: datetime.now().isoformat())


class AssessmentAgent:
    """
    Agent 1: Guide self-assessment and identify current state.

    This agent helps users gain clarity about their current situation
    by asking targeted questions and analyzing their responses to
    recommend the most suitable coaching framework.

    Example:
        >>> agent = AssessmentAgent()
        >>> result = agent.assess("career-transition")
        >>> print(result.recommended_framework)
        'grow'
    """

    # Mapping of focus areas to recommended frameworks
    FRAMEWORK_MAP = {
        "career-transition": "grow",
        "career": "grow",
        "purpose": "ikigai",
        "purpose-discovery": "ikigai",
        "goal-setting": "smart",
        "goals": "smart",
        "productivity": "smart",
        "life-balance": "wheel",
        "balance": "wheel",
        "self-discovery": "ikigai",
        "relationships": "grow",
        "health": "grow",
        "finance": "smart",
    }

    # Common challenges by focus area
    CHALLENGE_TEMPLATES = {
        "career": ["clarity on next steps", "confidence in abilities", "work-life balance"],
        "purpose": ["finding meaning", "feeling stuck", "lack of direction"],
        "goals": ["accountability", "time management", "motivation"],
        "balance": ["overwhelm", "prioritization", "energy management"],
    }

    # Default strengths to help users identify their resources
    DEFAULT_STRENGTHS = [
        "self-awareness",
        "willingness to grow",
        "resilience",
        "openness to feedback",
    ]

    def assess(self, focus_area: str) -> AssessmentResult:
        """
        Run a guided self-assessment.

        Args:
            focus_area: The area of life the user wants to focus on.
                       Common values: "career-transition", "purpose",
                       "goal-setting", "life-balance", "self-discovery"

        Returns:
            AssessmentResult containing the assessment data

        Example:
            >>> agent = AssessmentAgent()
            >>> result = agent.assess("career-transition")
            >>> result.focus_area
            'career-transition'
        """
        focus_lower = focus_area.lower().strip()

        # Determine challenges based on focus area
        key_challenges = self._get_challenges(focus_lower)

        # Get recommended framework
        recommended_framework = self._recommend_framework(focus_lower)

        assessment = AssessmentResult(
            focus_area=focus_lower,
            satisfaction_score=0.5,  # Placeholder - would come from user input in future
            key_challenges=key_challenges,
            strengths=self.DEFAULT_STRENGTHS.copy(),
            recommended_framework=recommended_framework,
        )

        print(f"[Assessment] Focus: {focus_lower}, Recommended: {recommended_framework}")
        return assessment

    def _recommend_framework(self, focus_area: str) -> str:
        """
        Recommend a coaching framework based on the focus area.

        Args:
            focus_area: The focus area to match against known patterns

        Returns:
            Framework name string
        """
        return self.FRAMEWORK_MAP.get(focus_area, "grow")

    def _get_challenges(self, focus_area: str) -> List[str]:
        """
        Get typical challenges for the given focus area.

        Args:
            focus_area: The focus area to get challenges for

        Returns:
            List of challenge strings
        """
        for key, challenges in self.CHALLENGE_TEMPLATES.items():
            if key in focus_area:
                return challenges.copy()
        return ["clarity", "direction", "confidence"]  # Default challenges

    def assess_wheel_of_life(self) -> Dict[str, float]:
        """
        Generate a wheel of life assessment template.

        Returns:
            Dictionary mapping life areas to scores (0-10)
        """
        return {
            "career": 5,
            "finance": 5,
            "health": 5,
            "family": 5,
            "relationships": 5,
            "growth": 5,
            "fun": 5,
            "environment": 5,
        }

    def generate_follow_up_questions(self, assessment: AssessmentResult) -> List[str]:
        """
        Generate follow-up questions based on assessment results.

        Args:
            assessment: The assessment result to generate questions for

        Returns:
            List of follow-up questions
        """
        questions = [
            f"What specifically would you like to change about your {assessment.focus_area}?",
            "On a scale of 1-10, how urgent is this for you right now?",
            "What have you already tried to address this?",
        ]

        if assessment.recommended_framework == "ikigai":
            questions.append("What activities make you lose track of time?")
            questions.append("What do you think the world needs more of?")

        return questions
