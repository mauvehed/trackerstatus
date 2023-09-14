# Maintainers

This document is intended to assist the maintainers of this repository and software package.

## Updating dependencies via poetry

```bash
poetry update

poetry export --without-hashes --format=requirements.txt > requirements.txt
```

## Updating supported versions of python

### Update GitHub Actions

### Update pyproject.toml

### Updating requirements.txt

## Releasing a new version

1. Update the value of `version` in pyproject.toml to match the new release number

## Publishing a new version (pypi)

A full documentation reference can be [found here](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-3-building-your-project) (DigitalOcean)

```bash
poetry build

poetry publish
```

This will publish a new package to the official PyPi page at [https://pypi.org/project/trackerstatus/](https://pypi.org/project/trackerstatus/)
