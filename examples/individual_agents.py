"""
Example: Using Individual Agents
=================================

This example demonstrates how to use each agent individually
for more control over the coaching process.
"""

from src.agents.assessment_agent import AssessmentAgent
from src.agents.coaching_agent import CoachingAgent
from src.agents.reflection_agent import ReflectionAgent


def main():
    """Demonstrate individual agent usage."""
    print("=" * 60)
    print("MindBridge Coach - Individual Agents Example")
    print("=" * 60)

    # Initialize agents
    assessment = AssessmentAgent()
    coaching = CoachingAgent()
    reflection = ReflectionAgent()

    # Step 1: Assessment
    print("\n[Step 1] Assessment...")
    result = assessment.assess("career-transition")
    print(f"Focus Area: {result.focus_area}")
    print(f"Recommended Framework: {result.recommended_framework}")
    print(f"Key Challenges: {result.key_challenges}")
    print(f"Strengths: {result.strengths}")

    # Step 2: Coaching with recommended framework
    print("\n[Step 2] Coaching...")
    guidance = coaching.coach(
        {"focus_area": result.focus_area},
        result.recommended_framework
    )
    print(f"Framework: {guidance.framework}")
    print(f"Steps: {len(guidance.steps)}")

    for step in guidance.steps:
        print(f"  - {step.stage}: {step.prompt}")

    # Step 3: Reflection
    print("\n[Step 3] Reflection...")
    reflection_guide = reflection.reflect("weekly")
    print(f"Type: {reflection_guide.reflection_type}")
    print(f"Guidance: {reflection_guide.guidance}")
    print(f"Prompts ({len(reflection_guide.prompts)}):")
    for prompt in reflection_guide.prompts:
        print(f"  {prompt.order}. {prompt.question}")

    # Bonus: Get framework info
    print("\n[Bonus] Framework Information...")
    info = coaching.get_framework_info("grow")
    print(f"Name: {info['name']}")
    print(f"Description: {info['description']}")
    print(f"Best for: {info['best_for']}")


if __name__ == "__main__":
    main()
