"""
SMART Goals Configuration
=========================

SMART is an acronym for a goal-setting framework that ensures objectives
are well-defined and achievable. While its exact origins are debated,
it's widely used in personal and professional development.

The five criteria:
- Specific: Clear and well-defined
- Measurable: Has quantifiable criteria
- Achievable: Realistic given resources
- Relevant: Aligned with broader goals
- Time-bound: Has a deadline
"""

SMART_CONFIG = {
    "name": "SMART Goals",
    "description": (
        "SMART goals provide a proven framework for setting objectives "
        "that are clear, achievable, and measurable. By ensuring your "
        "goals meet these five criteria, you dramatically increase your "
        "likelihood of success."
    ),
    "origin": "Popularized by George Doran, Arthur Miller, and James Cunningham in 1981",
    "best_for": [
        "Converting vague aspirations into actionable goals",
        "Project planning and milestones",
        "Professional development objectives",
        "Habit formation",
        "Breaking down large goals into steps",
    ],
    "criteria": {
        "specific": {
            "letter": "S",
            "name": "Specific",
            "question": "What exactly do you want to achieve? Define it precisely.",
            "description": "Your goal should be clear and well-defined",
            "prompts": [
                "What do you want to accomplish?",
                "Why is this goal important?",
                "Who is involved?",
                "Where will this happen?",
                "What are the requirements and constraints?",
            ],
        },
        "measurable": {
            "letter": "M",
            "name": "Measurable",
            "question": "How will you know you have achieved it? What are the metrics?",
            "description": "Your goal should have clear criteria for success",
            "prompts": [
                "How much? How many?",
                "How will you measure progress?",
                "What is your target number or benchmark?",
                "What evidence will prove you've achieved it?",
            ],
        },
        "achievable": {
            "letter": "A",
            "name": "Achievable",
            "question": "Is this realistic? What resources do you need?",
            "description": "Your goal should be attainable given your resources",
            "prompts": [
                "Is this goal realistic given your current situation?",
                "What skills or resources do you need?",
                "How can you accomplish this goal?",
                "Have others achieved similar goals?",
            ],
        },
        "relevant": {
            "letter": "R",
            "name": "Relevant",
            "question": "Why does this matter to you? How does it align with your values?",
            "description": "Your goal should align with broader objectives",
            "prompts": [
                "Does this goal align with your values?",
                "Is this the right time for this goal?",
                "How does this fit with other goals?",
                "Who else benefits from this achievement?",
            ],
        },
        "time_bound": {
            "letter": "T",
            "name": "Time-bound",
            "question": "By when will you achieve this? Set a clear deadline.",
            "description": "Your goal should have a clear timeline",
            "prompts": [
                "What is your deadline?",
                "What can you do today? This week? This month?",
                "What obstacles might affect your timeline?",
                "How will you stay on track?",
            ],
        },
    },
    "steps": [
        {"stage": "Specific", "prompt": "What exactly do you want to achieve? Define it precisely."},
        {"stage": "Measurable", "prompt": "How will you know you have achieved it? What are the metrics?"},
        {"stage": "Achievable", "prompt": "Is this realistic? What resources do you need?"},
        {"stage": "Relevant", "prompt": "Why does this matter to you? How does it align with your values?"},
        {"stage": "Time-bound", "prompt": "By when will you achieve this? Set a clear deadline."},
    ],
    "examples": [
        {
            "vague": "I want to get fit",
            "smart": "I will exercise for 30 minutes, 4 times per week, for the next 3 months, to improve my cardiovascular health and reach a resting heart rate of 70 bpm.",
        },
        {
            "vague": "I want to save money",
            "smart": "I will save $500 per month into a high-yield savings account, automatically transferred on the 1st of each month, to build a 6-month emergency fund of $12,000 by December 2026.",
        },
    ],
    "tips": [
        "Use the 5W1H method (What, Why, Who, Where, Which, How) to make goals specific",
        "Define at least 2-3 measurable indicators of success",
        "Stretch goals are good, but impossible goals lead to frustration",
        "Without a deadline, goals easily drift - set a specific date",
    ],
}
