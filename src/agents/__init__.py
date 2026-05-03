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

from .assessment_agent import AssessmentAgent
from .coaching_agent import CoachingAgent
from .reflection_agent import ReflectionAgent
from .pipeline import MindBridgePipeline

__all__ = [
    "AssessmentAgent",
    "CoachingAgent",
    "ReflectionAgent",
    "MindBridgePipeline",
]
