"""
Tests for Configuration Modules
===============================

Unit tests for the coaching framework configurations.
"""

import pytest
from src.config import (
    GROW_CONFIG,
    IKIGAI_CONFIG,
    SMART_CONFIG,
    WHEEL_OF_LIFE_CONFIG,
    REFLECTION_PROMPTS,
)


class TestGROWConfig:
    """Tests for GROW Model configuration."""

    def test_grow_config_structure(self):
        """Test that GROW config has required keys."""
        assert "name" in GROW_CONFIG
        assert "description" in GROW_CONFIG
        assert "steps" in GROW_CONFIG
        assert "best_for" in GROW_CONFIG

    def test_grow_has_four_steps(self):
        """Test that GROW has 4 steps."""
        assert len(GROW_CONFIG["steps"]) == 4

    def test_grow_step_stages(self):
        """Test GROW step stages are correct."""
        stages = [step["stage"] for step in GROW_CONFIG["steps"]]
        assert stages == ["Goal", "Reality", "Options", "Will"]


class TestIkigaiConfig:
    """Tests for Ikigai configuration."""

    def test_ikigai_config_structure(self):
        """Test that Ikigai config has required keys."""
        assert "name" in IKIGAI_CONFIG
        assert "description" in IKIGAI_CONFIG
        assert "steps" in IKIGAI_CONFIG
        assert "components" in IKIGAI_CONFIG

    def test_ikigai_has_four_components(self):
        """Test that Ikigai has 4 components."""
        assert len(IKIGAI_CONFIG["steps"]) == 4
        assert len(IKIGAI_CONFIG["components"]) == 4

    def test_ikigai_component_names(self):
        """Test Ikigai component names."""
        component_ids = list(IKIGAI_CONFIG["components"].keys())
        assert "passion" in component_ids
        assert "mission" in component_ids
        assert "vocation" in component_ids
        assert "profession" in component_ids


class TestSMARTConfig:
    """Tests for SMART Goals configuration."""

    def test_smart_config_structure(self):
        """Test that SMART config has required keys."""
        assert "name" in SMART_CONFIG
        assert "description" in SMART_CONFIG
        assert "criteria" in SMART_CONFIG

    def test_smart_has_five_criteria(self):
        """Test that SMART has 5 criteria."""
        assert len(SMART_CONFIG["steps"]) == 5
        assert len(SMART_CONFIG["criteria"]) == 5

    def test_smart_criteria_letters(self):
        """Test SMART criteria letters."""
        letters = [c["letter"] for c in SMART_CONFIG["criteria"].values()]
        assert letters == ["S", "M", "A", "R", "T"]


class TestWheelOfLifeConfig:
    """Tests for Wheel of Life configuration."""

    def test_wheel_config_structure(self):
        """Test that Wheel of Life config has required keys."""
        assert "name" in WHEEL_OF_LIFE_CONFIG
        assert "description" in WHEEL_OF_LIFE_CONFIG
        assert "areas" in WHEEL_OF_LIFE_CONFIG
        assert "scale" in WHEEL_OF_LIFE_CONFIG

    def test_wheel_has_eight_areas(self):
        """Test that Wheel of Life has 8 areas."""
        assert len(WHEEL_OF_LIFE_CONFIG["areas"]) == 8

    def test_wheel_scale_bounds(self):
        """Test Wheel of Life scale."""
        scale = WHEEL_OF_LIFE_CONFIG["scale"]
        assert scale["min"] == 0
        assert scale["max"] == 10


class TestReflectionPrompts:
    """Tests for reflection prompts."""

    def test_reflection_prompts_structure(self):
        """Test that reflection prompts has required keys."""
        assert "daily" in REFLECTION_PROMPTS
        assert "weekly" in REFLECTION_PROMPTS
        assert "monthly" in REFLECTION_PROMPTS

    def test_daily_prompts_count(self):
        """Test daily prompts count."""
        assert len(REFLECTION_PROMPTS["daily"]) >= 4

    def test_weekly_prompts_count(self):
        """Test weekly prompts count."""
        assert len(REFLECTION_PROMPTS["weekly"]) >= 5

    def test_monthly_prompts_count(self):
        """Test monthly prompts count."""
        assert len(REFLECTION_PROMPTS["monthly"]) >= 5

    def test_prompts_have_questions(self):
        """Test that prompts have question field."""
        for prompt_type, prompts in REFLECTION_PROMPTS.items():
            for prompt in prompts:
                assert "question" in prompt
                assert isinstance(prompt["question"], str)
