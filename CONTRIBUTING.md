# Contributing to GRC Platform

Thank you for your interest in contributing to the Integrated Governance, Risk & Compliance Platform! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and professional in all interactions. We are committed to providing a welcoming and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear, descriptive title
   - Detailed description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots or logs if applicable
   - Your environment (OS, Python version, etc.)

### Suggesting Features

1. **Check existing issues** for similar suggestions
2. **Create a new issue** with:
   - Clear, descriptive title
   - Detailed description of the feature
   - Use cases and benefits
   - Any relevant examples or mockups

### Code Contributions

#### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/techmahindrahero-png/riskmanagement.git
cd riskmanagement

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt
cd frontend && npm install && cd ..
```

#### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Write tests for new features
   - Update documentation

3. **Code Style Guidelines**
   - Backend: Follow PEP 8 (use `black` for formatting)
   - Frontend: Follow standard React conventions
   - Use meaningful variable/function names
   - Keep functions small and focused

4. **Testing**
   ```bash
   # Backend tests
   cd backend
   pytest tests/ -v --cov
   
   # Frontend tests
   cd frontend
   npm test
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```
   
   Follow conventional commits:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `style:` for formatting
   - `refactor:` for code refactoring
   - `test:` for tests
   - `chore:` for maintenance

6. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   
   Create a PR with:
   - Clear title and description
   - Reference related issues
   - List any breaking changes
   - Include screenshots if UI changes

### Pull Request Process

1. **PR Requirements**
   - Must pass all tests
   - Code review approval
   - No merge conflicts
   - Updated documentation
   - Meaningful commit history

2. **Review Process**
   - Maintainers will review your PR
   - Address feedback promptly
   - Update your changes based on review
   - Maintain respectful communication

3. **Merge Criteria**
   - Tests passing
   - At least one approval
   - No unresolved comments
   - Documentation updated

## Development Workflow

### Frontend Development

```bash
cd frontend
npm start  # Runs on http://localhost:3000
```

### Backend Development

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Database Migrations

```bash
cd backend
alembic revision --autogenerate -m "description"
alembic upgrade head
```

## Project Structure

- **backend/** - FastAPI application
  - `app/models/` - Database models
  - `app/schemas/` - Pydantic schemas
  - `app/routers/` - API endpoints
  - `app/services/` - Business logic
  - `tests/` - Unit tests

- **frontend/** - React application
  - `src/components/` - Reusable components
  - `src/pages/` - Page components
  - `src/services/` - API services
  - `src/contexts/` - React contexts

## Testing

### Backend Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test
pytest tests/test_auth.py

# Run with verbose output
pytest -v
```

### Frontend Testing

```bash
# Run tests
npm test

# Run with coverage
CI=true npm test -- --coverage
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to Python functions
- Add JSDoc comments to React components
- Update API documentation in code comments
- Keep CONTRIBUTING.md current

## Commit Message Guidelines

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example:**
```
feat(risk-assessment): add AI-powered risk scoring

Implemented machine learning model for automatic risk scoring
based on historical data and current assessments.

Closes #123
```

## Release Process

1. Update version numbers
2. Update CHANGELOG.md
3. Create release branch
4. Tag release with version
5. Create GitHub release
6. Deploy to production

## Questions or Need Help?

- Open an issue with `[QUESTION]` tag
- Check existing documentation
- Contact maintainers

Thank you for contributing! 🎉
