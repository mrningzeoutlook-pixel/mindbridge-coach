"""
Validation Utilities
====================

Provides validation functions for user inputs and configuration
values to ensure data integrity.
"""

from typing import List, Tuple


# Valid focus areas
VALID_FOCUS_AREAS = [
    "career-transition",
    "career",
    "purpose",
    "purpose-discovery",
    "goal-setting",
    "goals",
    "productivity",
    "life-balance",
    "balance",
    "self-discovery",
    "relationships",
    "health",
    "finance",
]

# Valid reflection prompt types
VALID_PROMPT_TYPES = [
    "daily",
    "weekly",
    "monthly",
    "goal-review",
    "gratitude",
    "evening",
    "morning",
]

# Valid coaching frameworks
VALID_FRAMEWORKS = [
    "grow",
    "ikigai",
    "smart",
    "wheel",
]


def validate_focus_area(focus_area: str) -> Tuple[bool, str]:
    """
    Validate a focus area input.

    Args:
        focus_area: The focus area string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not focus_area:
        return False, "Focus area cannot be empty"

    focus_lower = focus_area.lower().strip()

    # Check for exact match
    if focus_lower in VALID_FOCUS_AREAS:
        return True, ""

    # Check for partial match
    for valid_area in VALID_FOCUS_AREAS:
        if valid_area in focus_lower or focus_lower in valid_area:
            return True, ""

    # Suggest similar
    suggestions = []
    for valid_area in VALID_FOCUS_AREAS:
        if any(word in valid_area for word in focus_lower.split("-")):
            suggestions.append(valid_area)

    if suggestions:
        return False, f"Unknown focus area. Did you mean: {', '.join(suggestions[:3])}?"

    return False, f"Unknown focus area. Valid options: {', '.join(VALID_FOCUS_AREAS[:5])}..."


def validate_prompt_type(prompt_type: str) -> Tuple[bool, str]:
    """
    Validate a reflection prompt type.

    Args:
        prompt_type: The prompt type string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not prompt_type:
        return False, "Prompt type cannot be empty"

    prompt_lower = prompt_type.lower().strip()

    if prompt_lower in VALID_PROMPT_TYPES:
        return True, ""

    # Suggest closest match
    for valid_type in VALID_PROMPT_TYPES:
        if valid_type.startswith(prompt_lower[:3]):
            return False, f"Did you mean '{valid_type}'?"

    return False, f"Unknown prompt type. Valid options: {', '.join(VALID_PROMPT_TYPES)}"


def validate_framework(framework: str) -> Tuple[bool, str]:
    """
    Validate a coaching framework name.

    Args:
        framework: The framework string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not framework:
        return False, "Framework cannot be empty"

    framework_lower = framework.lower().strip()

    if framework_lower in VALID_FRAMEWORKS:
        return True, ""

    # Normalize common variations
    if framework_lower in ["wheel of life", "wheel-of-life"]:
        return True, ""

    return False, f"Unknown framework. Valid options: {', '.join(VALID_FRAMEWORKS)}"


def validate_score(score: float, min_val: float = 0.0, max_val: float = 10.0) -> Tuple[bool, str]:
    """
    Validate a numeric score within a range.

    Args:
        score: The score to validate
        min_val: Minimum valid value
        max_val: Maximum valid value

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(score, (int, float)):
        return False, "Score must be a number"

    if score < min_val or score > max_val:
        return False, f"Score must be between {min_val} and {max_val}"

    return True, ""


def validate_non_empty(value: str, field_name: str = "Value") -> Tuple[bool, str]:
    """
    Validate that a string is not empty.

    Args:
        value: The string to validate
        field_name: Name of the field for error message

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not value or not value.strip():
        return False, f"{field_name} cannot be empty"

    return True, ""


def validate_length(
    value: str,
    min_length: int = 0,
    max_length: int = 10000,
    field_name: str = "Value"
) -> Tuple[bool, str]:
    """
    Validate string length.

    Args:
        value: The string to validate
        min_length: Minimum required length
        max_length: Maximum allowed length
        field_name: Name of the field for error message

    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(value) < min_length:
        return False, f"{field_name} must be at least {min_length} characters"

    if len(value) > max_length:
        return False, f"{field_name} must be no more than {max_length} characters"

    return True, ""


def get_valid_options() -> dict:
    """
    Get all valid options for user selection.

    Returns:
        Dictionary of valid option categories and their values
    """
    return {
        "focus_areas": VALID_FOCUS_AREAS,
        "prompt_types": VALID_PROMPT_TYPES,
        "frameworks": VALID_FRAMEWORKS,
    }
