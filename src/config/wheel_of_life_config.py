"""
Wheel of Life Configuration
===========================

The Wheel of Life is a coaching tool that provides a visual representation
of different areas of your life. It helps identify areas of balance and
imbalance, and serves as a starting point for deeper coaching conversations.

The typical areas include career, finance, health, family, relationships,
personal growth, fun/recreation, and physical environment.
"""

WHEEL_OF_LIFE_CONFIG = {
    "name": "Wheel of Life",
    "description": (
        "The Wheel of Life provides a holistic view of your life satisfaction "
        "across multiple domains. By rating each area, you can identify "
        "imbalances and prioritize where to focus your coaching attention."
    ),
    "origin": "Popularized by Paul J. Meyer in the 1960s as part of success coaching",
    "best_for": [
        "Holistic life satisfaction assessment",
        "Identifying imbalances between life areas",
        "Prioritizing coaching focus areas",
        "Yearly or quarterly life reviews",
        "Understanding overall well-being",
    ],
    "areas": [
        {
            "id": "career",
            "name": "Career",
            "description": "Your professional life, job satisfaction, and career growth",
            "questions": [
                "How satisfied are you with your current role?",
                "Are you growing professionally?",
                "Do you feel valued at work?",
            ],
        },
        {
            "id": "finance",
            "name": "Finance",
            "description": "Your financial health, stability, and relationship with money",
            "questions": [
                "Do you have financial security?",
                "Are you managing your money well?",
                "Do you feel in control of your finances?",
            ],
        },
        {
            "id": "health",
            "name": "Health",
            "description": "Your physical health, fitness, and energy levels",
            "questions": [
                "How is your physical health?",
                "Do you have enough energy for daily life?",
                "Are you taking care of your body?",
            ],
        },
        {
            "id": "family",
            "name": "Family",
            "description": "Your relationship with family members and family life",
            "questions": [
                "Are your family relationships healthy?",
                "Do you spend quality time with family?",
                "Is there harmony in your family life?",
            ],
        },
        {
            "id": "relationships",
            "name": "Relationships",
            "description": "Your friendships, romantic relationship, and social connections",
            "questions": [
                "Do you have meaningful relationships?",
                "Are you giving and receiving support?",
                "Do you feel connected to others?",
            ],
        },
        {
            "id": "growth",
            "name": "Growth",
            "description": "Your personal development, learning, and self-improvement",
            "questions": [
                "Are you learning and growing?",
                "Do you have goals for personal development?",
                "Are you challenging yourself?",
            ],
        },
        {
            "id": "fun",
            "name": "Fun & Recreation",
            "description": "Your leisure activities, hobbies, and enjoyment of life",
            "questions": [
                "Are you having fun regularly?",
                "Do you have hobbies that bring you joy?",
                "Are you making time for play?",
            ],
        },
        {
            "id": "environment",
            "name": "Environment",
            "description": "Your physical surroundings, living space, and environment",
            "questions": [
                "Is your living space comfortable?",
                "Do you feel good in your environment?",
                "Is your surroundings supportive of your goals?",
            ],
        },
    ],
    "scale": {
        "min": 0,
        "max": 10,
        "labels": {
            0: "Completely unsatisfied",
            5: "Neutral / Average",
            10: "Completely satisfied",
        },
    },
    "tips": [
        "Rate honestly, not based on where you think you 'should' be",
        "Look for patterns - low scores may be related",
        "Focus on 1-2 areas at a time for improvement",
        "Revisit regularly to track changes over time",
    ],
}
