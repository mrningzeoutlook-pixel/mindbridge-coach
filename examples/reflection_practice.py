"""
Example: Reflection Practice
=============================

This example demonstrates how to use MindBridge Coach for
reflection exercises.
"""

from src.agents.pipeline import MindBridgePipeline


def main():
    """Run reflection exercises."""
    print("=" * 60)
    print("MindBridge Coach - Reflection Practice Example")
    print("=" * 60)

    # Initialize the pipeline
    pipeline = MindBridgePipeline()

    # Daily reflection
    print("\n>>> Daily Reflection...\n")
    output = pipeline.reflect("daily")
    print(output)

    # Weekly reflection
    print("\n>>> Weekly Reflection...\n")
    output = pipeline.reflect("weekly")
    print(output)

    # Monthly reflection
    print("\n>>> Monthly Reflection...\n")
    output = pipeline.reflect("monthly")
    print(output)

    # Gratitude practice
    print("\n>>> Gratitude Practice...\n")
    output = pipeline.reflect("gratitude")
    print(output)


if __name__ == "__main__":
    main()
