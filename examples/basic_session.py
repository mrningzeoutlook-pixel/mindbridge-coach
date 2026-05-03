"""
Example: Basic Coaching Session
================================

This example demonstrates how to use MindBridge Coach for a basic
coaching session.
"""

from src.agents.pipeline import MindBridgePipeline


def main():
    """Run a basic coaching session."""
    print("=" * 60)
    print("MindBridge Coach - Basic Session Example")
    print("=" * 60)

    # Initialize the pipeline
    pipeline = MindBridgePipeline()

    # Run a career transition coaching session
    print("\n>>> Starting a career transition coaching session...\n")
    output = pipeline.session("career-transition")
    print(output)

    # Run a purpose discovery session
    print("\n>>> Starting a purpose discovery session...\n")
    output = pipeline.session("purpose")
    print(output)

    # Run a goal-setting session
    print("\n>>> Starting a SMART goal-setting session...\n")
    output = pipeline.session("goal-setting")
    print(output)


if __name__ == "__main__":
    main()
