"""
Coaching Agent - Agent 2 of the MindBridge Three-Layer Architecture
====================================================================

This agent generates personalized coaching guidance using various
evidence-based coaching frameworks.

Key Responsibilities:
- Select appropriate coaching framework based on assessment
- Generate structured coaching steps and prompts
- Provide tips and guidance for each coaching stage
- Adapt coaching style to user's focus area
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

from ..config import GROW_CONFIG, IKIGAI_CONFIG, SMART_CONFIG


@dataclass
class CoachingStep:
    """Represents a single step in a coaching framework."""
    stage: str
    prompt: str
    tips: str
    order: int


@dataclass
class CoachingGuidance:
    """Data class representing coaching guidance from the agent."""
    framework: str
    focus_area: str
    steps: List[CoachingStep]
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    estimated_duration_minutes: int = 30


class CoachingAgent:
    """
    Agent 2: Generate personalized coaching guidance.

    This agent uses evidence-based coaching frameworks to guide users
    through structured self-reflection and action planning.

    Supported Frameworks:
    - GROW Model (Goal, Reality, Options, Will)
    - Ikigai (Passion, Mission, Vocation, Profession)
    - SMART Goals (Specific, Measurable, Achievable, Relevant, Time-bound)

    Example:
        >>> agent = CoachingAgent()
        >>> assessment = AssessmentAgent().assess("career-transition")
        >>> guidance = agent.coach(assessment, "grow")
        >>> print(guidance.framework)
        'GROW Model'
    """

    # Framework registry
    FRAMEWORKS = {
        "grow": GROW_CONFIG,
        "ikigai": IKIGAI_CONFIG,
        "smart": SMART_CONFIG,
    }

    # Framework descriptions for user education
    FRAMEWORK_DESCRIPTIONS = {
        "grow": "The GROW model is one of the most widely-used coaching frameworks. "
                "It provides a structured approach to goal setting and problem solving.",
        "ikigai": "Ikigai is a Japanese concept meaning 'reason for being.' "
                  "It helps you find your unique purpose by exploring four key areas.",
        "smart": "SMART goals ensure your objectives are well-defined and achievable. "
                 "This framework is particularly effective for concrete, measurable goals.",
    }

    def coach(self, assessment: dict, framework_name: str) -> CoachingGuidance:
        """
        Generate coaching guidance using the selected framework.

        Args:
            assessment: Assessment results from AssessmentAgent containing
                      focus_area and other relevant information
            framework_name: Name of the coaching framework to use.
                           Options: "grow", "ikigai", "smart"

        Returns:
            CoachingGuidance object containing structured coaching steps

        Example:
            >>> agent = CoachingAgent()
            >>> assessment = {"focus_area": "career-transition", "recommended_framework": "grow"}
            >>> guidance = agent.coach(assessment, "grow")
            >>> len(guidance.steps)
            4
        """
        # Normalize framework name
        framework_key = framework_name.lower().strip()
        framework_config = self.FRAMEWORKS.get(framework_key, GROW_CONFIG)

        steps = []
        for idx, step_config in enumerate(framework_config["steps"], 1):
            step = CoachingStep(
                stage=step_config["stage"],
                prompt=step_config["prompt"],
                tips=self._generate_tips(step_config["stage"], framework_key),
                order=idx,
            )
            steps.append(step)

        guidance = CoachingGuidance(
            framework=framework_config["name"],
            focus_area=assessment["focus_area"],
            steps=steps,
            estimated_duration_minutes=self._estimate_duration(framework_key),
        )

        print(f"[Coaching] Generated {framework_config['name']} guidance for {assessment['focus_area']}")
        return guidance

    def _generate_tips(self, stage: str, framework: str) -> str:
        """
        Generate helpful tips for the current coaching stage.

        Args:
            stage: The current coaching stage name
            framework: The framework being used

        Returns:
            Helpful tip string for the user
        """
        tip_templates = {
            "grow": {
                "Goal": "Be as specific as possible. Instead of 'I want to be happier', "
                        "try 'I want to feel satisfied with my work 4 days out of 5'.",
                "Reality": "Be honest about where you are now. This isn't about judgment, "
                           "it's about starting from an accurate foundation.",
                "Options": "Don't filter too early. Write down every idea, even ones that seem impossible. "
                           "You can evaluate later.",
                "Will": "Be specific about what you'll do AND when. 'I'll exercise for 30 minutes "
                        "every Tuesday and Thursday morning' is better than 'I'll exercise more'.",
            },
            "ikigai": {
                "Passion": "Think about activities that make you feel alive, not just competent. "
                           "What would you do even if you weren't paid for it?",
                "Mission": "Consider both local and global impact. What change do you want to see in your community?",
                "Vocation": "Think about skills that come naturally to you and that others value. "
                            "What do people often ask for your help with?",
                "Profession": "What can you actually be compensated for? Consider both traditional "
                              "and emerging opportunities.",
            },
            "smart": {
                "Specific": "Use the 5W1H method: What, Why, Who, Where, Which, How. "
                            "The more specific, the easier to measure.",
                "Measurable": "Define concrete criteria for success. How will you know when you've achieved this?",
                "Achievable": "Be honest about your resources and constraints. Ambitious is good, impossible is not.",
                "Relevant": "Connect this goal to your broader life direction. Why does this matter NOW?",
                "Time-bound": "Set a specific deadline. Without time pressure, goals easily drift.",
            },
        }

        return tip_templates.get(framework, {}).get(
            stage,
            f"Take your time with this {stage.lower()} stage. Be honest with yourself."
        )

    def _estimate_duration(self, framework: str) -> int:
        """
        Estimate the duration of a coaching session in minutes.

        Args:
            framework: The framework being used

        Returns:
            Estimated minutes for the session
        """
        durations = {
            "grow": 30,
            "ikigai": 45,
            "smart": 25,
        }
        return durations.get(framework, 30)

    def get_framework_info(self, framework_name: str) -> Dict[str, str]:
        """
        Get detailed information about a specific framework.

        Args:
            framework_name: Name of the framework

        Returns:
            Dictionary with framework details
        """
        framework_key = framework_name.lower().strip()
        config = self.FRAMEWORKS.get(framework_key, GROW_CONFIG)

        return {
            "name": config["name"],
            "description": self.FRAMEWORK_DESCRIPTIONS.get(framework_key, ""),
            "steps": [step["stage"] for step in config["steps"]],
            "best_for": self._get_framework_best_for(framework_key),
        }

    def _get_framework_best_for(self, framework: str) -> str:
        """Get recommendation text for when to use a framework."""
        recommendations = {
            "grow": "Best for: Career decisions, solving specific problems, making choices when uncertain.",
            "ikigai": "Best for: Finding life purpose, career direction, major life transitions.",
            "smart": "Best for: Converting vague aspirations into actionable goals.",
        }
        return recommendations.get(framework, "")
