"""
GROW Model Configuration
========================

The GROW model is one of the most widely-used coaching frameworks,
developed by John Whitmore in the 1980s. It provides a structured
approach to goal setting and problem solving.

The four stages:
- Goal: Define what you want to achieve
- Reality: Understand your current situation
- Options: Explore all possible paths
- Will: Commit to specific actions
"""

GROW_CONFIG = {
    "name": "GROW Model",
    "description": (
        "The GROW model provides a structured approach to coaching "
        "by guiding you through four key areas: Goal, Reality, Options, "
        "and Will. It helps you move from where you are to where you want to be."
    ),
    "origin": "Developed by John Whitmore, popularized in the 1980s-1990s",
    "best_for": [
        "Career decisions and transitions",
        "Solving specific problems",
        "Making choices when uncertain",
        "Personal goal setting",
        "Breaking through obstacles",
    ],
    "steps": [
        {
            "stage": "Goal",
            "prompt": "What do you really want? Be specific and vivid.",
            "description": "Define your ideal outcome clearly",
            "questions": [
                "What do you want to achieve?",
                "What would success look like?",
                "What is your timeline?",
                "How will you know when you've achieved it?",
            ],
        },
        {
            "stage": "Reality",
            "prompt": "Where are you right now in relation to this goal?",
            "description": "Assess your current situation honestly",
            "questions": [
                "What is your current situation?",
                "What have you already tried?",
                "What is working well?",
                "What challenges are you facing?",
            ],
        },
        {
            "stage": "Options",
            "prompt": "What could you do? List all possibilities, even wild ones.",
            "description": "Explore all possible paths forward",
            "questions": [
                "What options do you have?",
                "What have others done in similar situations?",
                "What would you do if you had more resources?",
                "What would you do if there were no obstacles?",
            ],
        },
        {
            "stage": "Will",
            "prompt": "What will you commit to doing? By when?",
            "description": "Create your action plan with commitments",
            "questions": [
                "What will you do?",
                "When will you start?",
                "What obstacles might you face?",
                "How will you measure progress?",
                "Who can support you?",
            ],
        },
    ],
    "tips": [
        "Be as specific as possible with your goals",
        "Be honest about your current reality",
        "Don't filter options too early",
        "Make commitments specific and time-bound",
    ],
}
