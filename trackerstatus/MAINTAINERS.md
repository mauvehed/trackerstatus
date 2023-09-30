# Maintainers

This document is intended to assist the maintainers of this repository and software package.

## Updating dependencies via poetry
```bash
poetry update
```

## Updating supported versions of python
Update the tool.poetry.dependencies.python field in `pyproject.toml`

### Update GitHub Actions

### Update pyproject.toml


### Updating requirements.txt
```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

## Releasing a new version

1. Update the value of `version` in pyproject.toml to match the new release number

### Publishing a new version (pypi)

A full documentation reference can be [found here](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04#step-3-building-your-project) (DigitalOcean)

```bash
poetry build

poetry publish
```

This will publish a new package to the official PyPi page at [https://pypi.org/project/trackerstatus/](https://pypi.org/project/trackerstatus/)

### Publish a new version on Github.com

1. [Draft New Release Notes](https://github.com/mauvehed/trackerstatus/releases/new) on Github.com
2. Create a new *Tag* matching the current format (e.g. "v0.1.5")
3. Leave Target set to *main*
4. Set the *Release Title* to the same as the *Tag*
5. Click *Generate Release Notes*
6. Leave *Set as the latest release* checked
7. Click on *Publish Release*