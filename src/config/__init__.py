"""
Configuration Package - Coaching Framework Definitions
=====================================================

Contains structured definitions for various coaching frameworks
including GROW, Ikigai, SMART goals, and more.
"""

from .grow_config import GROW_CONFIG
from .ikigai_config import IKIGAI_CONFIG
from .smart_config import SMART_CONFIG
from .wheel_of_life_config import WHEEL_OF_LIFE_CONFIG
from .reflection_prompts import REFLECTION_PROMPTS

__all__ = [
    "GROW_CONFIG",
    "IKIGAI_CONFIG",
    "SMART_CONFIG",
    "WHEEL_OF_LIFE_CONFIG",
    "REFLECTION_PROMPTS",
]
