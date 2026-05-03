# Contributing to MindBridge Coach

Thank you for your interest in contributing to MindBridge Coach! This project empowers people to find clarity, set meaningful goals, and navigate life transitions with structured self-reflection and AI-guided conversations.

## Quick Links

- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- pip (Python package manager)

### Fork the Repository

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/mindbridge-coach.git
   cd mindbridge-coach
   ```

### Install Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

## Development Setup

### Project Structure

```
mindbridge-coach/
├── src/
│   ├── agents/          # Three-agent coaching system
│   │   ├── assessment_agent.py
│   │   ├── coaching_agent.py
│   │   ├── reflection_agent.py
│   │   └── pipeline.py
│   ├── config/          # Coaching framework configurations
│   │   ├── grow_config.py
│   │   ├── ikigai_config.py
│   │   └── ...
│   └── utils/           # Utility functions
├── tests/               # pytest test suite
├── docs/                # Documentation
└── examples/            # Usage examples
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_assessment_agent.py

# Run with verbose output
pytest -v
```

### Code Style

We use standard Python conventions (PEP 8) with some modifications:

- Line length: 100 characters
- Use type hints where possible
- Docstrings for all public functions and classes

```bash
# Format code
black src/ tests/

# Check linting
ruff check src/ tests/
```

## Making Changes

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Write code following our style guidelines
- Add tests for new functionality
- Update documentation as needed
- Keep commits atomic and well-described

### 3. Commit Your Changes

```bash
git add .
git commit -m "feat: Add new coaching framework support"
```

#### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

### 4. Push to GitHub

```bash
git push origin feature/your-feature-name
```

### 5. Create a Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template
5. Submit!

## Pull Request Process

### PR Requirements

- [ ] Code follows our style guidelines
- [ ] Tests pass locally (`pytest`)
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages are clear and follow our format

### PR Description Template

```markdown
## Summary
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested your changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
```

## Adding New Coaching Frameworks

Want to add a new coaching framework? Here's how:

1. Create a new config file in `src/config/`:
   ```python
   # src/config/my_framework_config.py
   MY_FRAMEWORK_CONFIG = {
       "name": "My Framework",
       "description": "Description...",
       "steps": [
           {"stage": "Stage 1", "prompt": "..."},
           # ...
       ],
   }
   ```

2. Register it in `src/config/__init__.py`

3. Add tests in `tests/test_config.py`

4. Update documentation

## Reporting Issues

### Bug Reports

- Use the GitHub issue tracker
- Include Python version, OS, and relevant dependencies
- Provide minimal reproduction steps
- Include expected vs actual behavior

### Feature Requests

- Describe the problem you're trying to solve
- Explain how this feature would help users
- Provide examples if possible

## Community

- **Discord**: Join our community for discussions
- **GitHub Discussions**: Ask questions and share ideas
- **Twitter**: Follow us for updates

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to MindBridge Coach! Every contribution helps empower people on their journey of self-discovery and growth.
