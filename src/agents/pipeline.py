"""
MindBridge Coach - Main Pipeline
================================

This module contains the main MindBridgePipeline class that orchestrates
the three-agent coaching system.

The Pipeline Architecture:
1. Assessment Agent - Gathers user context and recommends framework
2. Coaching Agent - Generates personalized coaching guidance
3. Reflection Agent - Facilitates ongoing self-reflection

Usage:
    >>> from mindbridge_coach import MindBridgePipeline
    >>> pipeline = MindBridgePipeline()
    >>> output = pipeline.session("career-transition")
"""

from .assessment_agent import AssessmentAgent
from .coaching_agent import CoachingAgent
from .reflection_agent import ReflectionAgent


class MindBridgePipeline:
    """
    Main pipeline orchestrating all agents for life coaching sessions.

    This pipeline coordinates the three-agent system to provide a
    complete coaching experience:

    1. Assessment - Understand current situation and recommend framework
    2. Coaching - Generate structured guidance using selected framework
    3. Reflection - Facilitate ongoing self-awareness

    Example:
        >>> pipeline = MindBridgePipeline()
        >>> session_output = pipeline.session("career-transition")
        >>> print(session_output)  # doctest: +SKIP

        Coaching Session: CAREER-TRANSITION
        ────────────────────────────────────────
        GOAL
        ────────────────────────────────────────
        What do you really want? Be specific and vivid.
        ...
    """

    def __init__(self):
        """Initialize the pipeline with all three agents."""
        self.assessment_agent = AssessmentAgent()
        self.coaching_agent = CoachingAgent()
        self.reflection_agent = ReflectionAgent()

    def session(self, focus: str) -> str:
        """
        Run a full coaching session.

        This method executes the complete coaching pipeline:
        1. Self-assessment to understand current state
        2. Framework-based coaching guidance
        3. Formatted session output

        Args:
            focus: Focus area for the coaching session.
                  Common values: "career-transition", "purpose",
                  "goal-setting", "life-balance", "self-discovery"

        Returns:
            Formatted coaching session output as a string

        Example:
            >>> pipeline = MindBridgePipeline()
            >>> output = pipeline.session("purpose-discovery")
            >>> assert "PURPOSE" in output or "Ikigai" in output
        """
        print("\n" + "=" * 60)
        print("MindBridge Coach - AI-Assisted Life Coaching")
        print("Empowering you to find your own answers")
        print("=" * 60)

        # Step 1: Assessment
        print("\n[Step 1/3] Running self-assessment...")
        assessment = self.assessment_agent.assess(focus)

        # Step 2: Coaching
        print("\n[Step 2/3] Generating coaching guidance...")
        guidance = self.coaching_agent.coach(assessment, assessment.recommended_framework)

        # Format output
        output = self._format_coaching_session(focus, guidance)

        print("\n[Step 3/3] Session complete!")
        print(f"Estimated duration: {guidance.estimated_duration_minutes} minutes")

        return output

    def _format_coaching_session(self, focus: str, guidance) -> str:
        """
        Format the coaching session into readable output.

        Args:
            focus: The focus area for the session
            guidance: The coaching guidance object

        Returns:
            Formatted session string
        """
        separator = "-" * 40
        output = f"\n\n  Coaching Session: {focus.upper()}\n"
        output += f"  Framework: {guidance.framework}\n"
        output += f"  Estimated Duration: {guidance.estimated_duration_minutes} minutes\n\n"

        for step in guidance.steps:
            output += f"  {separator}\n"
            output += f"  {step.stage.upper()}\n"
            output += f"  {separator}\n"
            output += f"  {step.prompt}\n\n"
            output += f"  Tip: {step.tips}\n\n"

        output += "  " + separator + "\n"
        output += "  Remember: Take your time with each section.\n"
        output += "  There are no right or wrong answers.\n"
        output += "  " + separator + "\n"

        return output

    def reflect(self, prompt_type: str) -> str:
        """
        Run a reflection exercise.

        This method generates a guided reflection with prompts
        tailored to the specified frequency.

        Args:
            prompt_type: Type of reflection to generate.
                        Options: "daily", "weekly", "monthly",
                        "goal-review", "gratitude"

        Returns:
            Formatted reflection prompts as a string

        Example:
            >>> pipeline = MindBridgePipeline()
            >>> output = pipeline.reflect("weekly")
            >>> assert "Reflection" in output
        """
        print("\n" + "=" * 60)
        print(f"MindBridge Coach - {prompt_type.title()} Reflection")
        print("Take a moment to be present with yourself")
        print("=" * 60)

        reflection = self.reflection_agent.reflect(prompt_type)

        output = self._format_reflection(reflection)

        return output

    def _format_reflection(self, reflection) -> str:
        """
        Format reflection into readable output.

        Args:
            reflection: The reflection guide object

        Returns:
            Formatted reflection string
        """
        output = f"\n\n  {reflection.reflection_type.title()} Reflection\n\n"
        output += f"  {reflection.guidance}\n\n"
        output += "  " + "-" * 40 + "\n\n"

        for prompt in reflection.prompts:
            output += f"  {prompt.order}. {prompt.question}\n\n"

        output += "  " + "-" * 40 + "\n"
        output += f"  Tip: {reflection.tip}\n"

        return output

    def full_experience(self, focus: str, reflection_type: str = "weekly") -> str:
        """
        Run a complete coaching experience with both session and reflection.

        This combines the coaching session with a follow-up reflection
        for a comprehensive self-development experience.

        Args:
            focus: Focus area for the coaching session
            reflection_type: Type of reflection to include

        Returns:
            Complete coaching experience output
        """
        session_output = self.session(focus)
        reflection_output = self.reflect(reflection_type)

        return f"{session_output}\n\n{'=' * 60}\n\n{reflection_output}"


def main():
    """CLI entry point for MindBridge Coach."""
    import argparse

    parser = argparse.ArgumentParser(
        description="MindBridge Coach - AI-Assisted Life Coaching",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Start a career coaching session:
    python -m src.pipeline session --focus career-transition

  Run a weekly reflection:
    python -m src.pipeline reflect --prompt weekly

  Run a full coaching experience:
    python -m src.pipeline full --focus purpose --reflection monthly
        """
    )

    parser.add_argument(
        "command",
        choices=["session", "reflect", "full"],
        help="Command: session (coaching), reflect (reflection), full (both)"
    )
    parser.add_argument(
        "--focus",
        default="career-transition",
        help="Focus area for coaching session (default: career-transition)"
    )
    parser.add_argument(
        "--prompt",
        default="weekly",
        choices=["daily", "weekly", "monthly", "goal-review", "gratitude"],
        help="Reflection prompt type (default: weekly)"
    )

    args = parser.parse_args()

    pipeline = MindBridgePipeline()

    if args.command == "session":
        output = pipeline.session(args.focus)
        print(output)
    elif args.command == "reflect":
        output = pipeline.reflect(args.prompt)
        print(output)
    elif args.command == "full":
        output = pipeline.full_experience(args.focus, args.prompt)
        print(output)


if __name__ == "__main__":
    main()
