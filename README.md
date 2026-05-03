# MindBridge Coach

AI-assisted life coaching and reflection toolkit. Helping people find clarity, set meaningful goals, and navigate life transitions with structured self-reflection and AI-guided conversations.

## Problem

Many people feel stuck, overwhelmed, or directionless but cannot access professional coaching. Traditional life coaching costs $150-500 per session, making it inaccessible for most. Meanwhile, self-help books lack personalization and accountability.

## Solution

MindBridge provides an AI-assisted coaching framework that:

1. **Assessment** - Guided self-reflection exercises to identify current state and desires
2. **Goal Setting** - SMART goal framework with AI-optimized goal breakdown
3. **Action Planning** - Step-by-step action plans with milestone tracking
4. **Reflection** - Weekly guided reflection prompts and progress review
5. **Pattern Recognition** - AI identifies behavioral patterns and limiting beliefs

## Architecture

```
User Input (journal / answers / goals)
     |
     v
[Assessment Agent] --> Understand current situation
     |
     v
[Coaching Agent] --> Generate personalized guidance
     |
     v
[Reflection Agent] --> Facilitate self-discovery
     |
     v
Output: Personalized coaching insights
```

## Tech Stack

- **Python 3.11+** - Core runtime
- **AI Agents** - Multi-step coaching conversation pipeline
- **Prompt Engineering** - Therapeutic and coaching frameworks in prompts

## Quick Start

```bash
# Clone the repository
git clone https://github.com/mrningzeoutlook-pixel/mindbridge-coach.git
cd mindbridge-coach

# Install dependencies
pip install -r requirements.txt

# Start a coaching session
python mindbridge.py session --focus "career-transition"

# Run a reflection exercise
python mindbridge.py reflect --prompt weekly
```

## Coaching Frameworks

- **GROW Model** - Goal, Reality, Options, Will
- **SMART Goals** - Specific, Measurable, Achievable, Relevant, Time-bound
- **Ikigai** - Finding purpose at the intersection of passion, mission, vocation, profession
- **Wheel of Life** - Holistic life satisfaction assessment

## Roadmap

- [x] Core coaching conversation engine
- [x] Assessment and reflection frameworks
- [ ] Session memory and continuity
- [ ] Progress tracking dashboard
- [ ] Community sharing (anonymous)
- [ ] Integration with journaling apps

## License

MIT License

---

Empowering people to find their own answers.
