# Contributing to TrackerStatus

Thank you for your interest in contributing to the TrackerStatus project! This document provides guidelines for setting up the project for local development, testing, and building the package.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up the Project](#setting-up-the-project)
3. [Running Tests](#running-tests)
4. [Type Checking](#type-checking)
5. [Building the Package](#building-the-package)
6. [Submitting Changes](#submitting-changes)

## Prerequisites

Ensure you have the following software installed on your machine:

- [Python](https://www.python.org/downloads/) (version 3.9 or higher)
- [Poetry](https://python-poetry.org/docs/#installation) (version 1.1.0 or higher)
- [Git](https://git-scm.com/)

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

## Developer Expectations

### Running Tests

All new code should have appropriate coverage for functionality. To run the tests, use pytest:

```sh
pytest
```

This will discover and run all tests in the tests directory.

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
    pip install dist/trackerstatus-0.1.0-py3-none-any.whl
    ```

    Replace `trackerstatus-0.1.0-py3-none-any.whl` with the actual filename of the built package in dist/

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

4. **Push Changes**

    Push your changes to your fork:

    ```sh
    git push origin feature/your-feature-name
    ```

5. **Open a Pull Request**

    Open a pull request on GitHub from your fork to the main repository.
