"""
Formatting Utilities
====================

Provides formatting functions for coaching sessions, reflections,
and prompts to ensure consistent and readable output.
"""

from typing import List, Dict, Any
from datetime import datetime


def format_session(
    focus: str,
    framework: str,
    steps: List[Dict[str, str]],
    estimated_duration: int = 30
) -> str:
    """
    Format a coaching session into readable output.

    Args:
        focus: The focus area for the session
        framework: The coaching framework being used
        steps: List of step dictionaries with 'stage', 'prompt', 'tips' keys
        estimated_duration: Estimated session duration in minutes

    Returns:
        Formatted session string
    """
    separator = "-" * 40
    output = f"\n\n  Coaching Session: {focus.upper()}\n"
    output += f"  Framework: {framework}\n"
    output += f"  Estimated Duration: {estimated_duration} minutes\n\n"

    for step in steps:
        output += f"  {separator}\n"
        output += f"  {step['stage'].upper()}\n"
        output += f"  {separator}\n"
        output += f"  {step['prompt']}\n\n"
        output += f"  Tip: {step.get('tips', '')}\n\n"

    output += f"  {separator}\n"
    output += "  Remember: Take your time with each section.\n"
    output += "  There are no right or wrong answers.\n"
    output += f"  {separator}\n"

    return output


def format_reflection(
    reflection_type: str,
    prompts: List[str],
    guidance: str,
    tip: str
) -> str:
    """
    Format reflection prompts into readable output.

    Args:
        reflection_type: Type of reflection (daily, weekly, monthly)
        prompts: List of reflection prompt questions
        guidance: Overall guidance for the reflection
        tip: Helpful tip for the reflection practice

    Returns:
        Formatted reflection string
    """
    output = f"\n\n  {reflection_type.title()} Reflection\n\n"
    output += f"  {guidance}\n\n"
    output += "  " + "-" * 40 + "\n\n"

    for idx, prompt in enumerate(prompts, 1):
        output += f"  {idx}. {prompt}\n\n"

    output += "  " + "-" * 40 + "\n"
    output += f"  Tip: {tip}\n"

    return output


def format_prompt(
    question: str,
    category: str = "general",
    include_number: bool = False,
    number: int = 0
) -> str:
    """
    Format a single reflection prompt.

    Args:
        question: The reflection question
        category: Category of the prompt
        include_number: Whether to include question number
        number: Question number if include_number is True

    Returns:
        Formatted prompt string
    """
    if include_number:
        return f"{number}. {question} [{category}]"
    return question


def format_framework_table(frameworks: Dict[str, Any]) -> str:
    """
    Format framework information as a markdown table.

    Args:
        frameworks: Dictionary of framework configurations

    Returns:
        Markdown-formatted table string
    """
    output = "| Framework | Best For | Duration |\n"
    output += "|-----------|----------|-----------|\n"

    for key, config in frameworks.items():
        best_for = config.get("best_for", ["General coaching"])
        if isinstance(best_for, list):
            best_for = "; ".join(best_for[:2])
        output += f"| {config['name']} | {best_for} | ~{30 if 'grow' in key else 45} min |\n"

    return output


def format_timestamp(dt: datetime = None) -> str:
    """
    Format a datetime as a readable timestamp.

    Args:
        dt: Datetime to format (defaults to now)

    Returns:
        Formatted timestamp string
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def format_progress_bar(current: float, total: float, width: int = 20) -> str:
    """
    Format a simple text-based progress bar.

    Args:
        current: Current progress value
        total: Total value
        width: Width of the progress bar in characters

    Returns:
        Progress bar string like "[####----] 40%"
    """
    if total == 0:
        percentage = 0
    else:
        percentage = min(int((current / total) * 100), 100)

    filled = int((current / total) * width) if total > 0 else 0
    bar = "=" * filled + "-" * (width - filled)

    return f"[{bar}] {percentage}%"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: Text to truncate
        max_length: Maximum length including suffix
        suffix: Suffix to add when truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
