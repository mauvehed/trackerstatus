# Maintainers

This document is intended to assist the maintainers of this repository and software package with various tasks.

## Releasing a new version

Releases are automated via the `create-new-release.yml` GitHub Action. When a new git tag is created that matches the `v*.*.*` format, the following will occur:

1. A new Release is created on GitHub
1. The release notes are auto created
1. A python package is published to [PyPI](https://pypi.org/project/trackerstatus/).

To create a new release:

1. Update the `version` in `pyproject.toml`.
1. Push a new tag following the format `v*.*.*` (e.g., `v1.2.3`).

   ```bash
   git tag v1.2.3
   git push origin v1.2.3
   ```

### Updating supported versions of python

#### Update GitHub Actions

1. Update `python-version` in `.github/workflows/create-new-release.yml`
1. Update `python-version` in `.github/workflows/generate-requirements.yml`
1. Update `python-version` in `.github/workflows/mypy-linting.yml`
1. Update `python-version` in `.github/workflows/pytestts-coverage.yml`
1. Update `python-version` in `.sourcery.yaml`
1. Update `tool.poetry.dependencies.python` field in pyproject.toml

## Miscellaneous Tasks

### Updating Dependencies via Poetry

```bash
poetry update
```

### Updating (dev-)requirements.txt

The `requirements.txt` and `dev-requirements.txt` files are automatically updated on any changes to `pyproject.toml` or `poetry.lock` via a GitHub Actions workflow.
