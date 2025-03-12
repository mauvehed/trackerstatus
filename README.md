# trackerstatus
[![PyPI](https://img.shields.io/pypi/v/trackerstatus.svg)](https://pypi.org/project/trackerstatus/)
[![Python Version](https://img.shields.io/pypi/pyversions/trackerstatus.svg)](https://pypi.org/project/trackerstatus/)
[![License](https://img.shields.io/pypi/l/trackerstatus.svg)](https://github.com/mauvehed/trackerstatus/blob/main/LICENSE)

[![CodeQL](https://github.com/mauvehed/trackerstatus/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/codeql-analysis.yml)
[![CI](https://github.com/mauvehed/trackerstatus/actions/workflows/ci.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/ci.yml)
[![Release](https://github.com/mauvehed/trackerstatus/actions/workflows/release.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/release.yml)

A Python wrapper for the [trackerstatus.info](https://trackerstatus.info) API and its tracker-specific endpoints. This library provides a simple interface to monitor the status of various trackers and their services.
- Rate-limited API client (1 request per minute as per API requirements)
- Support for all tracker-specific endpoints:
  - AlphaRatio (AR)
  - BroadcastTheNet (BTN)
  - GazelleGames (GGN)
  - PassThePopcorn (PTP)
  - Redacted (RED)
  - Orpheus (OPS)
  - Nebulance (NBL)
  - Anthelion (ANT)
- Comprehensive status information including:
  - Current status
  - Latency metrics
  - Uptime statistics
  - Record uptimes
  - Downtime tracking
- Type hints and detailed documentation
- Extensive test coverage

## Documentation

The project includes comprehensive documentation:

- [API Reference](https://github.com/mauvehed/trackerstatus/blob/main/docs/API.md) - Detailed API documentation
- [Examples](https://github.com/mauvehed/trackerstatus/blob/main/docs/EXAMPLES.md) - Various usage examples and best practices
- [Changelog](https://github.com/mauvehed/trackerstatus/blob/main/CHANGELOG.md) - Version history and changes

## Features

- Check tracker status and response times
- Support for multiple tracker protocols (HTTP, HTTPS, UDP)
- Detailed status information including:
  - Response time
  - Status code
  - Error messages
  - Protocol information
- Easy-to-use API
- Comprehensive documentation

## Installation

```bash
pip install trackerstatus
```

## Quick Start

```python
from trackerstatus import APIClient, StatusEndpoint

# Create an API client
client = APIClient()

# Get overall status of all trackers
status_endpoint = StatusEndpoint(client)
all_statuses = status_endpoint.get_status()
print("Overall Status:")
for tracker, info in all_statuses.items():
    print(f"{tracker.upper()}: {info['status_message']}")
    if info['details']:
        details = info['details']
        print(f"  Description: {details.get('Description', 'N/A')}")
        print(f"  Services: {details.get('Services', {})}")
        print(f"  Last Update: {details.get('tweet', {}).get('date', 'N/A')}")
```

For more detailed examples, see the [examples documentation](https://github.com/mauvehed/trackerstatus/blob/main/docs/EXAMPLES.md).

## Documentation

- [API Reference](https://github.com/mauvehed/trackerstatus/blob/main/docs/API.md)
- [Examples](https://github.com/mauvehed/trackerstatus/blob/main/docs/EXAMPLES.md)
- [Changelog](https://github.com/mauvehed/trackerstatus/blob/main/CHANGELOG.md)

## Development

This project uses Poetry for dependency management and development tools:

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Format code
poetry run black .
poetry run isort .

# Type checking
poetry run mypy .
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/mauvehed/trackerstatus/blob/main/LICENSE) file for details.
