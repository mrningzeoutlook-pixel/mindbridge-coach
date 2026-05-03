"""
Ikigai Framework Configuration
===============================

Ikigai is a Japanese concept meaning "reason for being" or "purpose in life."
It helps you find your unique purpose by exploring the intersection of
four key areas.

The four components:
- Passion (What you love) - Activities that bring you joy
- Mission (What the world needs) - How you contribute to others
- Vocation (What you can be paid for) - Your marketable skills
- Profession (What you're good at) - Your natural talents

Your Ikigai sits at the intersection of all four.
"""

IKIGAI_CONFIG = {
    "name": "Ikigai Framework",
    "description": (
        "Ikigai is a Japanese concept that helps you find your reason for being. "
        "It explores four key questions: What you love, what you're good at, "
        "what the world needs, and what you can be paid for. Your ikigai "
        "is found where all four intersect."
    ),
    "origin": "Japanese concept, popularized by Hector Garcia and Francesc Miralles in 'Ikigai: The Japanese Secret to a Long and Happy Life'",
    "best_for": [
        "Finding life purpose and meaning",
        "Career direction and reinvention",
        "Major life transitions",
        "Discovering what truly matters",
        "Creating a balanced life",
    ],
    "components": {
        "passion": {
            "name": "Passion",
            "question": "What do you love doing? What makes you lose track of time?",
            "description": "Activities that bring you joy and energize you",
            "reflection": [
                "What activities make you feel alive?",
                "What would you do even if you weren't paid?",
                "What topics do you constantly want to learn about?",
                "What brings you flow state?",
            ],
        },
        "mission": {
            "name": "Mission",
            "question": "What does the world need that you care about?",
            "description": "How you contribute to others and the world",
            "reflection": [
                "What problems in the world do you feel strongly about?",
                "What would you change if you could?",
                "What cause would you volunteer for?",
                "How do you want to be remembered?",
            ],
        },
        "vocation": {
            "name": "Vocation",
            "question": "What can you be paid for? What skills do people value?",
            "description": "Your marketable skills and expertise",
            "reflection": [
                "What skills do people often ask for your help with?",
                "What have you been trained to do?",
                "What expertise have you developed over time?",
                "What problems can you solve for others?",
            ],
        },
        "profession": {
            "name": "Profession",
            "question": "What are you good at? What comes naturally to you?",
            "description": "Your natural talents and strengths",
            "reflection": [
                "What do people compliment you on?",
                "What comes easily to you but difficult for others?",
                "What have you always been good at?",
                "What would your friends say you're great at?",
            ],
        },
    },
    "steps": [
        {"stage": "Passion", "prompt": "What do you love doing? What makes you lose track of time?"},
        {"stage": "Mission", "prompt": "What does the world need that you care about?"},
        {"stage": "Vocation", "prompt": "What can you be paid for? What skills do people value?"},
        {"stage": "Profession", "prompt": "What are you good at? What comes naturally to you?"},
    ],
    "tips": [
        "Start with what you love - passion often leads to other areas",
        "Look for patterns across all four areas",
        "Your ikigai may evolve over time - that's normal",
        "Small ikigais (daily pleasures) matter as much as big ones",
    ],
}
