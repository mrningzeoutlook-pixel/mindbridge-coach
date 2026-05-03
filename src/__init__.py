"""
MindBridge Coach - AI-Assisted Life Coaching & Reflection Toolkit
===================================================================

A comprehensive AI-powered life coaching framework supporting multiple
evidence-based coaching methodologies including GROW, Ikigai, and SMART goals.

Author: Mary Ma
Email: mary@example.com
License: MIT
"""

__version__ = "0.2.0"
__author__ = "Mary Ma"

from .pipeline import MindBridgePipeline
from .agents.assessment_agent import AssessmentAgent
from .agents.coaching_agent import CoachingAgent
from .agents.reflection_agent import ReflectionAgent

__all__ = [
    "MindBridgePipeline",
    "AssessmentAgent",
    "CoachingAgent",
    "ReflectionAgent",
]
