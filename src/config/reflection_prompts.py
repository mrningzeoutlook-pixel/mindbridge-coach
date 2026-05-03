"""
Reflection Prompts Configuration
================================

Contains structured reflection prompts for daily, weekly, and monthly
reflection practices. These prompts are designed to encourage
self-awareness, gratitude, and continuous growth.
"""

REFLECTION_PROMPTS = {
    "daily": [
        {
            "question": "What was the best moment of today?",
            "category": "highlight",
            "purpose": "Notice what brings you joy and satisfaction",
        },
        {
            "question": "What challenged you today?",
            "category": "growth",
            "purpose": "Identify opportunities for learning and growth",
        },
        {
            "question": "What are you grateful for right now?",
            "category": "gratitude",
            "purpose": "Cultivate appreciation and positive focus",
        },
        {
            "question": "What would you do differently tomorrow?",
            "category": "improvement",
            "purpose": "Commit to continuous improvement",
        },
        {
            "question": "How did you take care of yourself today?",
            "category": "self-care",
            "purpose": "Track self-care practices",
        },
    ],
    "weekly": [
        {
            "question": "What were your top 3 wins this week?",
            "category": "success",
            "purpose": "Celebrate progress and acknowledge achievements",
        },
        {
            "question": "What drained your energy this week?",
            "category": "drain",
            "purpose": "Identify energy drains to address",
        },
        {
            "question": "What gave you energy this week?",
            "category": "energy",
            "purpose": "Discover what energizes you",
        },
        {
            "question": "What is one thing you want to focus on next week?",
            "category": "planning",
            "purpose": "Set priorities for the coming week",
        },
        {
            "question": "How did you move toward your goals this week?",
            "category": "progress",
            "purpose": "Track momentum and motivation",
        },
        {
            "question": "What did you learn about yourself this week?",
            "category": "insight",
            "purpose": "Deepen self-awareness",
        },
    ],
    "monthly": [
        {
            "question": "What theme emerged this month?",
            "category": "theme",
            "purpose": "Identify patterns and overarching narratives",
        },
        {
            "question": "What did you learn about yourself?",
            "category": "growth",
            "purpose": "Recognize personal development",
        },
        {
            "question": "What habits served you well? Which didn't?",
            "category": "habits",
            "purpose": "Evaluate habits and routines",
        },
        {
            "question": "What are you most proud of this month?",
            "category": "pride",
            "purpose": "Celebrate achievements large and small",
        },
        {
            "question": "What do you want to let go of as you enter the next month?",
            "category": "release",
            "purpose": "Practice letting go of what no longer serves",
        },
        {
            "question": "How have you grown compared to last month?",
            "category": "progress",
            "purpose": "Recognize growth over time",
        },
    ],
    "goal_review": [
        {
            "question": "What progress have you made on your goal?",
            "category": "progress",
            "purpose": "Assess advancement toward objectives",
        },
        {
            "question": "What obstacles have you encountered?",
            "category": "challenges",
            "purpose": "Identify barriers and challenges",
        },
        {
            "question": "What support do you need?",
            "category": "support",
            "purpose": "Recognize when to ask for help",
        },
        {
            "question": "Is this goal still meaningful to you?",
            "category": "relevance",
            "purpose": "Reassess alignment with values",
        },
        {
            "question": "What will you do differently going forward?",
            "category": "adjustment",
            "purpose": "Plan for course correction",
        },
    ],
    "gratitude": [
        {
            "question": "What is something you're grateful for today?",
            "category": "gratitude",
            "purpose": "Daily gratitude practice",
        },
        {
            "question": "Who is someone you appreciate in your life?",
            "category": "people",
            "purpose": "Express appreciation for relationships",
        },
        {
            "question": "What is a challenge you're grateful for?",
            "category": "growth",
            "purpose": "Find value in difficulties",
        },
        {
            "question": "What simple pleasure did you enjoy recently?",
            "category": "pleasure",
            "purpose": "Appreciate everyday joys",
        },
        {
            "question": "What ability or skill are you thankful to have?",
            "category": "strengths",
            "purpose": "Recognize your capabilities",
        },
    ],
    "evening": [
        {
            "question": "What am I grateful for today?",
            "category": "gratitude",
        },
        {
            "question": "What did I accomplish today?",
            "category": "accomplishment",
        },
        {
            "question": "What could I have done better?",
            "category": "improvement",
        },
        {
            "question": "What am I looking forward to tomorrow?",
            "category": "anticipation",
        },
    ],
    "morning": [
        {
            "question": "How am I feeling right now?",
            "category": "awareness",
        },
        {
            "question": "What is my intention for today?",
            "category": "intention",
        },
        {
            "question": "What is the most important thing I need to do today?",
            "category": "priority",
        },
        {
            "question": "How will I take care of myself today?",
            "category": "self-care",
        },
    ],
}
