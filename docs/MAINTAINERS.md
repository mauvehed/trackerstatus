# Maintainers Guide

This document outlines the responsibilities and procedures for maintainers of the TrackerStatus project.

## Responsibilities

1. Review pull requests
2. Merge approved changes
3. Release new versions
4. Maintain documentation
5. Monitor issues
6. Ensure code quality

## CI/CD Pipeline

Our GitHub Actions workflow:
- Runs on every push and pull request
- Tests against Python 3.9-3.12
- Performs code quality checks
- Generates coverage reports

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create and push tag
4. GitHub Actions will:
   - Run tests
   - Build package
   - Create GitHub release
   - Publish to PyPI

## Code Quality Standards

Ensure all code:
1. Has type hints
2. Passes mypy checks
3. Follows black formatting
4. Has test coverage
5. Has documentation

## Documentation

Keep updated:
1. README.md
2. API documentation
3. Contributing guide
4. Installation instructions
5. Usage examples

## Releasing a new version

Releases are automated via the `release.yml` GitHub Action. When a new git tag is created that matches the `v*.*.*` format, the following will occur:

1. Requirements files are generated and committed
1. A new Release is created on GitHub with the following artifacts:
   - Distribution files
   - Requirements files
1. The release notes are auto created
1. A python package is published to [PyPI](https://pypi.org/project/trackerstatus/)

To create a new release:

1. Update the `version` in `pyproject.toml`.
1. Push a new tag following the format `v*.*.*` (e.g., `v1.2.3`).

   ```bash
   git tag v1.2.3
   git push origin v1.2.3
   ```

### Updating supported versions of python

#### Update GitHub Actions

1. Update `python-version` matrix in `.github/workflows/ci.yml`
2. Update `python-version` in `.github/workflows/release.yml`
3. Update `tool.poetry.dependencies.python` field in pyproject.toml

## CI/CD Workflows

The project uses several GitHub Actions workflows:

1. `ci.yml`: Handles continuous integration
   - Runs tests across Python 3.9-3.12
   - Performs code quality checks (black, isort, mypy, pylint)
   - Generates and uploads coverage reports
   - Runs on push, pull request, and manual trigger

2. `release.yml`: Handles releases and publishing
   - Triggered by version tags
   - Generates requirements files
   - Creates GitHub releases
   - Publishes to PyPI

3. `codeql-analysis.yml`: Security scanning
   - Performs CodeQL analysis for Python
   - Runs on push, pull request, and weekly schedule
   - Identifies potential security vulnerabilities

4. `dependency-review.yml`: Dependency security
   - Reviews dependency changes in pull requests
   - Identifies known vulnerabilities
   - Prevents merging of vulnerable dependencies

## Development Tools

### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality. The configuration is in `.pre-commit-config.yaml` and includes:

- Code formatting (black)
- Import sorting (isort)
- Type checking (mypy)
- Linting (pylint)
- Various other code quality checks

To update pre-commit hooks to their latest versions:

```bash
pre-commit autoupdate
```

### Code Quality Tools

The project uses several code quality tools configured in `setup.cfg`:

- `flake8`: Code style enforcement
- `mypy`: Type checking
- `pytest`: Testing configuration
- `coverage`: Test coverage settings
- `isort`: Import sorting

## Miscellaneous Tasks

### Updating Dependencies via Poetry

```bash
poetry update
```

### Updating (dev-)requirements.txt

The `requirements.txt` and `dev-requirements.txt` files are automatically updated during the release process via the `release.yml` workflow.
