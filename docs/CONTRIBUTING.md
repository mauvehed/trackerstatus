# Contributing to TrackerStatus

Thank you for your interest in contributing to the TrackerStatus project! This document provides guidelines for setting up the project for local development, testing, and building the package.

## Table of Contents

1. [Setting Up the Project](#setting-up-the-project)
1. [Development Tools](#development-tools)
1. [Running Tests](#running-tests)
1. [Type Checking](#type-checking)
1. [Building the Package](#building-the-package)
1. [Submitting Changes](#submitting-changes)
1. [CI/CD](#cicd)

## Setting Up the Project

1. **Fork and Clone the Repository**

   Fork the repository on GitHub and clone your fork locally:

   ```sh
   git clone https://github.com/your-username/trackerstatus.git
   cd trackerstatus
   ```

2. **Install Dependencies**

   Use Poetry to install the project dependencies:

   ```sh
   poetry install
   ```

3. **Activate the Virtual Environment**

   Activate the virtual environment created by Poetry:

   ```sh
   poetry shell
   ```

4. **Set up Pre-commit Hooks**

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

## Development Tools

The project uses several tools to maintain code quality:

### Code Quality Tools

All tools are configured in `setup.cfg`:

- **flake8**: Code style enforcement
- **mypy**: Type checking
- **pytest**: Testing configuration
- **coverage**: Test coverage settings
- **isort**: Import sorting

### Pre-commit Hooks

The pre-commit configuration is in `.pre-commit-config.yaml`. To update hooks to their latest versions:

```sh
pre-commit autoupdate
```

### Security Checks

The project includes several security measures:

1. **CodeQL Analysis**
   - Performs static analysis for security vulnerabilities
   - Runs automatically on pull requests
   - Weekly scheduled scans

2. **Dependency Review**
   - Checks for known vulnerabilities in dependencies
   - Prevents merging of vulnerable packages
   - Runs on all pull requests

## Developer Expectations

### Running Tests

All new code should have appropriate coverage for functionality. To run the tests, use pytest:

```sh
pytest
```

This will discover and run all tests in the tests directory.

For more detailed output, you can use:

```sh
pytest -v  # Verbose output
pytest -vv # Very verbose output
pytest --cov=trackerstatus  # With coverage report
```

### Type Checking

All new code is expected to adhere to mypy standards. To ensure type correctness, use mypy:

```sh
mypy trackerstatus tests
```

This checks all Python files in the trackerstatus and tests directories for type correctness.

## Building the Package

To build the package for local testing, follow these steps:

1. **Build the Package**

   Use Poetry to build the package:

   ```sh
   poetry build
   ```

   This will create the distribution files in the dist directory.

2. **Install the Package Locally**

   You can install the built package locally to test it:

   ```sh
   pip install dist/trackerstatus-1.0.0-py3-none-any.whl
   ```

   Replace `trackerstatus-1.0.0-py3-none-any.whl` with the actual filename of the built package in dist/

## Submitting Changes

1. **Create a Branch**

   Create a new branch for your feature or bug fix:

   ```sh
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**

   Make your changes in the new branch.

3. **Commit Changes**

   Commit your changes with a descriptive commit message:

   ```sh
   git add .
   git commit -m "Add your descriptive commit message here"
   ```

   Note: The pre-commit hooks will run automatically and may modify your commit if code style issues are found.

4. **Push Changes**

   Push your changes to your fork:

   ```sh
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

   Open a pull request on GitHub from your fork to the main repository.

## CI/CD

The project uses GitHub Actions for continuous integration and deployment:

1. **Continuous Integration** (`ci.yml`)
   - Runs on every push and pull request
   - Tests against Python 3.8-3.12
   - Performs code quality checks
   - Generates and uploads coverage reports

2. **Release Process** (`release.yml`)
   - Triggered by version tags
   - Generates requirements files
   - Creates GitHub releases
   - Publishes to PyPI

3. **Security Checks**
   - CodeQL analysis for security vulnerabilities
   - Dependency review for known vulnerabilities
   - Weekly security scans

All pull requests must pass the CI checks before they can be merged.
