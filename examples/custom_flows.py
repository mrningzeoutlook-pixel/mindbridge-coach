"""
Example: Custom Coaching Flow
==============================

This example demonstrates how to create a custom coaching flow
tailored to specific needs.
"""

from src.agents.assessment_agent import AssessmentAgent
from src.agents.coaching_agent import CoachingAgent
from src.agents.reflection_agent import ReflectionAgent


def custom_career_transition():
    """A custom coaching flow for career transition."""
    print("=" * 60)
    print("Custom Career Transition Coaching")
    print("=" * 60)

    assessment = AssessmentAgent()
    coaching = CoachingAgent()
    reflection = ReflectionAgent()

    # Assessment
    print("\n--- Step 1: Self-Assessment ---")
    result = assessment.assess("career-transition")
    print(f"Focus: {result.focus_area}")
    print(f"Framework: {result.recommended_framework}")

    # Coaching
    print("\n--- Step 2: Coaching with GROW ---")
    guidance = coaching.coach(
        {"focus_area": result.focus_area},
        "grow"
    )
    for step in guidance.steps:
        print(f"\n{step.stage}:")
        print(f"  Prompt: {step.prompt}")
        print(f"  Tip: {step.tips}")

    # Specific follow-up questions for career transition
    print("\n--- Additional Career Questions ---")
    questions = [
        "What skills from your current role transfer to your new path?",
        "Who in your network could support this transition?",
        "What is the minimum viable step you could take this week?",
        "What fears are holding you back? How can you address them?",
    ]
    for q in questions:
        print(f"  - {q}")

    # Reflection
    print("\n--- Step 3: Reflection ---")
    guide = reflection.reflect("goal-review")
    print(f"Type: {guide.reflection_type}")
    print(f"Guidance: {guide.guidance}")
    for prompt in guide.prompts:
        print(f"  {prompt.order}. {prompt.question}")


def custom_life_balance():
    """A custom coaching flow for life balance."""
    print("\n" + "=" * 60)
    print("Custom Life Balance Coaching")
    print("=" * 60)

    assessment = AssessmentAgent()
    coaching = CoachingAgent()

    # Assessment
    result = assessment.assess("life-balance")
    print(f"\nRecommended Framework: {result.recommended_framework}")

    # Coaching
    guidance = coaching.coach(
        {"focus_area": result.focus_area},
        "grow"
    )

    print(f"\nFramework: {guidance.framework}")
    print("Wheel of Life Areas to Consider:")
    wheel_areas = [
        ("Career", "How satisfied are you with your work life?"),
        ("Finance", "How secure do you feel financially?"),
        ("Health", "How would you rate your physical health?"),
        ("Family", "How are your family relationships?"),
        ("Relationships", "How fulfilling are your friendships?"),
        ("Growth", "Are you learning and growing?"),
        ("Fun", "Are you making time for enjoyment?"),
        ("Environment", "Does your environment support you?"),
    ]
    for area, question in wheel_areas:
        print(f"  - {area}: {question}")

    print("\nUse a scale of 0-10 to rate each area,")
    print("then focus coaching on the areas with lowest scores.")


if __name__ == "__main__":
    custom_career_transition()
    custom_life_balance()
