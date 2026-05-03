"""
MindBridge Coach - AI-Assisted Life Coaching & Reflection Toolkit
Helping people find clarity, set meaningful goals, and navigate life transitions.
"""

import os
import json
import argparse
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class CoachingSession:
    """Represents a coaching session with context."""
    focus_area: str
    current_state: str
    desired_state: str
    created_at: str


# Coaching frameworks
FRAMEWORKS = {
    "grow": {
        "name": "GROW Model",
        "steps": [
            {"stage": "Goal", "prompt": "What do you really want? Be specific and vivid."},
            {"stage": "Reality", "prompt": "Where are you right now in relation to this goal?"},
            {"stage": "Options", "prompt": "What could you do? List all possibilities, even wild ones."},
            {"stage": "Will", "prompt": "What will you commit to doing? By when?"},
        ],
    },
    "ikigai": {
        "name": "Ikigai Framework",
        "steps": [
            {"stage": "Passion", "prompt": "What do you love doing? What makes you lose track of time?"},
            {"stage": "Mission", "prompt": "What does the world need that you care about?"},
            {"stage": "Vocation", "prompt": "What can you be paid for? What skills do people value?"},
            {"stage": "Profession", "prompt": "What are you good at? What comes naturally to you?"},
        ],
    },
    "smart": {
        "name": "SMART Goals",
        "steps": [
            {"stage": "Specific", "prompt": "What exactly do you want to achieve? Define it precisely."},
            {"stage": "Measurable", "prompt": "How will you know you have achieved it? What are the metrics?"},
            {"stage": "Achievable", "prompt": "Is this realistic? What resources do you need?"},
            {"stage": "Relevant", "prompt": "Why does this matter to you? How does it align with your values?"},
            {"stage": "Time-bound", "prompt": "By when will you achieve this? Set a clear deadline."},
        ],
    },
}

REFLECTION_PROMPTS = {
    "daily": [
        "What was the best moment of today?",
        "What challenged you today?",
        "What are you grateful for right now?",
        "What would you do differently tomorrow?",
    ],
    "weekly": [
        "What were your top 3 wins this week?",
        "What drained your energy this week?",
        "What gave you energy this week?",
        "What is one thing you want to focus on next week?",
        "How did you move toward your goals this week?",
    ],
    "monthly": [
        "What theme emerged this month?",
        "What did you learn about yourself?",
        "What habits served you well? Which didn't?",
        "What are you most proud of this month?",
        "What do you want to let go of as you enter the next month?",
    ],
}


class AssessmentAgent:
    """Agent 1: Guide self-assessment and identify current state."""

    def assess(self, focus_area: str) -> dict:
        """Run a guided self-assessment.

        Args:
            focus_area: The area of life the user wants to focus on

        Returns:
            Assessment results
        """
        assessment = {
            "focus_area": focus_area,
            "satisfaction_score": 0.5,  # Placeholder - would come from user input
            "key_challenges": ["clarity", "direction", "confidence"],
            "strengths": ["self-awareness", "willingness to grow", "resilience"],
            "recommended_framework": self._recommend_framework(focus_area),
        }
        print(f"[Assessment] Focus: {focus_area}, Recommended: {assessment['recommended_framework']}")
        return assessment

    def _recommend_framework(self, focus_area: str) -> str:
        """Recommend a coaching framework based on the focus area."""
        framework_map = {
            "career-transition": "grow",
            "purpose": "ikigai",
            "goal-setting": "smart",
            "life-balance": "grow",
            "self-discovery": "ikigai",
        }
        return framework_map.get(focus_area, "grow")


class CoachingAgent:
    """Agent 2: Generate personalized coaching guidance."""

    def coach(self, assessment: dict, framework_name: str) -> dict:
        """Generate coaching guidance using the selected framework.

        Args:
            assessment: Assessment results from AssessmentAgent
            framework_name: Name of the coaching framework to use

        Returns:
            Coaching session with guided prompts and insights
        """
        framework = FRAMEWORKS.get(framework_name, FRAMEWORKS["grow"])

        guidance = {
            "framework": framework["name"],
            "focus_area": assessment["focus_area"],
            "steps": [],
        }

        for step in framework["steps"]:
            guidance["steps"].append({
                "stage": step["stage"],
                "prompt": step["prompt"],
                "tips": f"Take your time with this {step['stage'].lower()} stage. Be honest with yourself.",
            })

        print(f"[Coaching] Generated {framework['name']} guidance for {assessment['focus_area']}")
        return guidance


class ReflectionAgent:
    """Agent 3: Facilitate reflection and identify patterns."""

    def reflect(self, prompt_type: str) -> dict:
        """Generate reflection prompts and pattern insights.

        Args:
            prompt_type: Type of reflection (daily, weekly, monthly)

        Returns:
            Reflection prompts and guidance
        """
        prompts = REFLECTION_PROMPTS.get(prompt_type, REFLECTION_PROMPTS["weekly"])

        reflection = {
            "type": prompt_type,
            "prompts": prompts,
            "guidance": "There are no wrong answers. Write freely and honestly. "
                       "The goal is self-awareness, not perfection.",
            "tip": "Try to write at least 2-3 sentences for each prompt. "
                   "Depth of reflection matters more than breadth.",
        }
        print(f"[Reflection] Generated {prompt_type} reflection ({len(prompts)} prompts)")
        return reflection


class MindBridgePipeline:
    """Main pipeline orchestrating all agents for life coaching sessions."""

    def __init__(self):
        self.assessment_agent = AssessmentAgent()
        self.coaching_agent = CoachingAgent()
        self.reflection_agent = ReflectionAgent()

    def session(self, focus: str) -> str:
        """Run a full coaching session.

        Args:
            focus: Focus area for the coaching session

        Returns:
            Formatted coaching session output
        """
        print("\n" + "=" * 60)
        print("MindBridge Coach - AI-Assisted Life Coaching")
        print("=" * 60)

        # Step 1: Assessment
        print("\n[Step 1/3] Running self-assessment...")
        assessment = self.assessment_agent.assess(focus)

        # Step 2: Coaching
        print("\n[Step 2/3] Generating coaching guidance...")
        guidance = self.coaching_agent.coach(assessment, assessment["recommended_framework"])

        # Format output
        separator = "-" * 40
        output = f"\n\n  Coaching Session: {focus.upper()}\n"
        output += f"  Framework: {guidance['framework']}\n\n"

        for step in guidance["steps"]:
            output += f"  {separator}\n"
            output += f"  {step['stage'].upper()}\n"
            output += f"  {separator}\n"
            output += f"  {step['prompt']}\n\n"
            output += f"  Tip: {step['tips']}\n\n"

        print("[Step 3/3] Session complete!")
        return output

    def reflect(self, prompt_type: str) -> str:
        """Run a reflection exercise.

        Args:
            prompt_type: Type of reflection (daily, weekly, monthly)

        Returns:
            Formatted reflection prompts
        """
        print("\n" + "=" * 60)
        print(f"MindBridge Coach - {prompt_type.title()} Reflection")
        print("=" * 60)

        reflection = self.reflection_agent.reflect(prompt_type)

        output = f"\n\n  {prompt_type.title()} Reflection\n\n"
        output += f"  {reflection['guidance']}\n\n"
        for i, prompt in enumerate(reflection["prompts"], 1):
            output += f"  {i}. {prompt}\n\n"
        output += f"  Tip: {reflection['tip']}\n"

        return output


def main():
    parser = argparse.ArgumentParser(description="MindBridge Coach - AI-Assisted Life Coaching")
    parser.add_argument("command", choices=["session", "reflect"],
                       help="Command: start a coaching session or reflection exercise")
    parser.add_argument("--focus", default="career-transition",
                       help="Focus area for coaching session")
    parser.add_argument("--prompt", default="weekly", choices=["daily", "weekly", "monthly"],
                       help="Reflection prompt type")

    args = parser.parse_args()

    pipeline = MindBridgePipeline()

    if args.command == "session":
        output = pipeline.session(args.focus)
        print(output)
    elif args.command == "reflect":
        output = pipeline.reflect(args.prompt)
        print(output)


if __name__ == "__main__":
    main()
