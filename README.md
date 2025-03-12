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

- [API Reference](docs/api.md) - Detailed API documentation
- [Examples](docs/EXAMPLES.md) - Various usage examples and best practices
- [Changelog](CHANGELOG.md) - Version history and changes

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
from trackerstatus import APIClient

# Create an API client
client = APIClient()

# Check a specific tracker's status
status = client.get_status("ar")  # AlphaRatio
print(f"Status: {status.status}")
print(f"Latency: {status.latency}ms")
print(f"Uptime: {status.uptime}%")

# Or check all trackers
for tracker in ["ar", "btn", "ggn", "ptp", "red", "ops"]:
    status = client.get_status(tracker)
    print(f"{tracker.upper()}: {status.status}")
```

For more detailed examples, see the [examples documentation](docs/EXAMPLES.md).

## Documentation

- [API Reference](docs/api.md)
- [Examples](EXAMPLES.md)
- [Changelog](CHANGELOG.md)

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
