"""
Example: Full Coaching Experience
==================================

This example demonstrates how to run a complete coaching experience
combining both coaching sessions and reflection exercises.
"""

from src.agents.pipeline import MindBridgePipeline


def main():
    """Run a full coaching experience."""
    print("=" * 60)
    print("MindBridge Coach - Full Experience Example")
    print("=" * 60)
    print("\nThis example combines a coaching session with")
    print("a follow-up reflection exercise.\n")

    # Initialize the pipeline
    pipeline = MindBridgePipeline()

    # Define the coaching focus
    focus_area = "purpose"
    reflection_type = "monthly"

    # Run the full experience
    output = pipeline.full_experience(focus_area, reflection_type)
    print(output)

    # Suggested journal prompts after the session
    print("\n" + "=" * 60)
    print("Suggested Follow-Up Questions")
    print("=" * 60)
    print("""
After completing this coaching experience, consider journaling about:

1. What insights did you gain about yourself?
2. What surprised you during the reflection?
3. What one action will you take this week based on this session?
4. What support do you need to follow through?
5. How will you measure progress on your goal?
    """)


if __name__ == "__main__":
    main()
