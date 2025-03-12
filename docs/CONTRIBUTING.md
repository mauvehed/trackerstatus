# Contributing to TrackerStatus

Thank you for considering contributing to TrackerStatus! This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Development Setup](#development-setup)
1. [Running Tests](#running-tests)
1. [Code Style](#code-style)
1. [CI/CD Pipeline](#cicd-pipeline)
1. [Making Changes](#making-changes)
1. [Pull Request Process](#pull-request-process)

## Development Setup

1. **Fork and Clone the Repository**

   Fork the repository on GitHub and clone your fork locally:

   ```sh
   git clone https://github.com/your-username/trackerstatus.git
   cd trackerstatus
   ```

2. **Install Python 3.9 or higher**

   Ensure you have Python 3.9 or higher installed on your system.

3. **Install Poetry (dependency management tool)**

   Poetry is used for managing project dependencies and virtual environments. Install it using the following command:

   ```sh
   poetry install
   ```

4. **Install dependencies**

   Use Poetry to install the project dependencies:

   ```sh
   poetry install
   ```

5. **Install pre-commit hooks**

   Install pre-commit hooks to ensure code quality:

   ```sh
   pre-commit install
   ```

   This will run the following checks before each commit:
   - Code formatting (black)
   - Import sorting (isort)
   - Type checking (mypy)
   - Linting (pylint)
   - Various other code quality checks

## Running Tests

All new code should have appropriate coverage for functionality. To run the tests, use pytest:

```bash
poetry run pytest
```

This will discover and run all tests in the tests directory.

For more detailed output, you can use:

```sh
pytest -v  # Verbose output
pytest -vv # Very verbose output
pytest --cov=trackerstatus  # With coverage report
```

## Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **mypy**: Type checking
- **pylint**: Linting

These are all configured in `pyproject.toml` and run automatically via pre-commit hooks.

## CI/CD Pipeline

Our GitHub Actions workflow:
- Tests against Python 3.9-3.12
- Runs on Ubuntu latest
- Checks code formatting and linting
- Runs all tests with coverage

## Making Changes

1. **Create a new branch**

   Create a new branch for your feature or bug fix:

   ```sh
   git checkout -b feature/your-feature-name
   ```

2. **Make changes**

   Make your changes in the new branch.

3. **Write/update tests**

   Ensure that your changes are covered by tests.

4. **Run pre-commit hooks**

   Run the pre-commit hooks to ensure code quality:

   ```sh
   pre-commit run --all-files
   ```

5. **Push changes**

   Push your changes to your fork:

   ```sh
   git push origin feature/your-feature-name
   ```

6. **Open a pull request**

   Open a pull request on GitHub from your fork to the main repository.

## Pull Request Process

1. **Update documentation if needed**

   Ensure that any changes to the code or functionality are reflected in the documentation.

2. **Add tests for new features**

   If you've added new functionality, make sure to add tests for it.

3. **Ensure CI passes**

   Before merging, ensure that all CI checks pass.

4. **Get review approval**

   Pull requests must be reviewed and approved by at least one maintainer.

5. **Maintainer will merge**

   Once all checks are passed and review is approved, the maintainer will merge the pull request.
