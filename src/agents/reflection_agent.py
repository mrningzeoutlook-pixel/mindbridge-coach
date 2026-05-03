"""
Reflection Agent - Agent 3 of the MindBridge Three-Layer Architecture
=====================================================================

This agent facilitates deep self-reflection and helps identify
behavioral patterns and growth opportunities.

Key Responsibilities:
- Generate contextually appropriate reflection prompts
- Facilitate pattern recognition and insights
- Support daily, weekly, and monthly reflection practices
- Encourage continuous self-awareness and growth
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

from ..config import REFLECTION_PROMPTS


@dataclass
class ReflectionPrompt:
    """Represents a single reflection prompt."""
    question: str
    order: int
    category: str = "general"


@dataclass
class ReflectionGuide:
    """Data class representing a reflection exercise."""
    reflection_type: str
    prompts: List[ReflectionPrompt]
    guidance: str
    tip: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class ReflectionAgent:
    """
    Agent 3: Facilitate reflection and identify patterns.

    This agent generates thoughtful reflection prompts and helps users
    develop deeper self-awareness through structured journaling and
    contemplation exercises.

    Reflection Types:
    - daily: Quick daily check-ins for ongoing awareness
    - weekly: Deeper weekly reviews for learning and planning
    - monthly: Comprehensive monthly reflections for big-picture perspective
    - goal-review: Specific prompts for reviewing progress on goals
    - gratitude: Focused gratitude practice prompts

    Example:
        >>> agent = ReflectionAgent()
        >>> reflection = agent.reflect("weekly")
        >>> print(f"Generated {len(reflection.prompts)} prompts")
        'Generated 5 prompts'
    """

    # Extended reflection prompts beyond the basic ones
    EXTENDED_PROMPTS = {
        "daily": [
            {"question": "What was the best moment of today?", "category": "highlight"},
            {"question": "What challenged you today?", "category": "growth"},
            {"question": "What are you grateful for right now?", "category": "gratitude"},
            {"question": "What would you do differently tomorrow?", "category": "improvement"},
            {"question": "How did you take care of yourself today?", "category": "self-care"},
        ],
        "weekly": [
            {"question": "What were your top 3 wins this week?", "category": "success"},
            {"question": "What drained your energy this week?", "category": "drain"},
            {"question": "What gave you energy this week?", "category": "energy"},
            {"question": "What is one thing you want to focus on next week?", "category": "planning"},
            {"question": "How did you move toward your goals this week?", "category": "progress"},
            {"question": "What did you learn about yourself this week?", "category": "insight"},
        ],
        "monthly": [
            {"question": "What theme emerged this month?", "category": "theme"},
            {"question": "What did you learn about yourself?", "category": "growth"},
            {"question": "What habits served you well? Which didn't?", "category": "habits"},
            {"question": "What are you most proud of this month?", "category": "pride"},
            {"question": "What do you want to let go of as you enter the next month?", "category": "release"},
            {"question": "How have you grown compared to last month?", "category": "progress"},
        ],
        "goal-review": [
            {"question": "What progress have you made on your goal?", "category": "progress"},
            {"question": "What obstacles have you encountered?", "category": "challenges"},
            {"question": "What support do you need?", "category": "support"},
            {"question": "Is this goal still meaningful to you?", "category": "relevance"},
            {"question": "What will you do differently going forward?", "category": "adjustment"},
        ],
        "gratitude": [
            {"question": "What is something you're grateful for today?", "category": "gratitude"},
            {"question": "Who is someone you appreciate in your life?", "category": "people"},
            {"question": "What is a challenge you're grateful for?", "category": "growth"},
            {"question": "What simple pleasure did you enjoy recently?", "category": "pleasure"},
            {"question": "What ability or skill are you thankful to have?", "category": "strengths"},
        ],
    }

    # Guidance messages for different reflection types
    GUIDANCE_MESSAGES = {
        "daily": "Daily reflection helps build self-awareness over time. "
                 "Keep it brief but honest. This is for you, not for perfection.",
        "weekly": "Weekly reflection is an opportunity to pause and see the bigger picture. "
                  "Look for patterns across your days and celebrate progress.",
        "monthly": "Monthly reflection is for perspective. Consider both achievements and "
                   "setbacks as information, not judgment.",
        "goal-review": "Goal reviews help you course-correct and stay aligned with what "
                       "matters most. Be honest but compassionate with yourself.",
        "gratitude": "Gratitude practice shifts focus from what's lacking to what's present. "
                     "Even small things count.",
    }

    def reflect(self, prompt_type: str) -> ReflectionGuide:
        """
        Generate reflection prompts and pattern insights.

        Args:
            prompt_type: Type of reflection to generate.
                        Options: "daily", "weekly", "monthly", "goal-review", "gratitude"

        Returns:
            ReflectionGuide containing prompts and guidance

        Example:
            >>> agent = ReflectionAgent()
            >>> reflection = agent.reflect("weekly")
            >>> print(reflection.guidance)
            'Weekly reflection is an opportunity to pause...'
        """
        # Normalize prompt type
        prompt_key = prompt_type.lower().strip()
        prompts_data = self.EXTENDED_PROMPTS.get(prompt_key, self.EXTENDED_PROMPTS["weekly"])
        prompts = [
            ReflectionPrompt(
                question=p["question"],
                order=idx,
                category=p.get("category", "general")
            )
            for idx, p in enumerate(prompts_data, 1)
        ]

        reflection = ReflectionGuide(
            reflection_type=prompt_key,
            prompts=prompts,
            guidance=self.GUIDANCE_MESSAGES.get(prompt_key, self.GUIDANCE_MESSAGES["weekly"]),
            tip=self._get_tip(prompt_key),
        )

        print(f"[Reflection] Generated {prompt_key} reflection ({len(prompts)} prompts)")
        return reflection

    def _get_tip(self, prompt_type: str) -> str:
        """
        Get helpful tip for the reflection type.

        Args:
            prompt_type: The type of reflection

        Returns:
            Helpful tip string
        """
        tips = {
            "daily": "Try to write at least 2-3 sentences for each prompt. "
                     "Depth of reflection matters more than breadth.",
            "weekly": "Aim for 10-15 minutes for this reflection. "
                     "It's a complete check-in, not a marathon.",
            "monthly": "This reflection may take 30-60 minutes. "
                       "Find a quiet space where you won't be interrupted.",
            "goal-review": "Be specific about what worked and what didn't. "
                          "Vague reflections lead to vague adjustments.",
            "gratitude": "If you're struggling, start with one small thing. "
                         "Fresh sheets, a good meal, a moment of peace - it all counts.",
        }
        return tips.get(prompt_type, tips["daily"])

    def identify_patterns(self, reflection_history: List[Dict]) -> Dict[str, str]:
        """
        Identify patterns from reflection history.

        This is a simplified pattern recognition that would be enhanced
        with actual AI processing in a full implementation.

        Args:
            reflection_history: List of past reflection entries

        Returns:
            Dictionary of identified patterns and insights
        """
        patterns = {
            "recurring_themes": [],
            "growth_areas": [],
            "energy_patterns": [],
            "insights": [],
        }

        # Placeholder for actual pattern recognition logic
        # In a full implementation, this would analyze text and extract themes

        return patterns

    def generate_insight_questions(self, reflection_type: str) -> List[str]:
        """
        Generate deeper insight questions based on reflection type.

        Args:
            reflection_type: The type of reflection being done

        Returns:
            List of deeper follow-up questions
        """
        questions = [
            "What does this reveal about your values?",
            "What would you do if you weren't afraid?",
            "What advice would you give to a friend in your situation?",
        ]

        if reflection_type == "weekly":
            questions.extend([
                "What pattern do you notice across this week?",
                "What is one small win you might be overlooking?",
            ])

        return questions
