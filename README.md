# trackerstatus

[![PyPI](https://img.shields.io/pypi/v/trackerstatus.svg)](https://pypi.org/project/trackerstatus/)
[![Python Version](https://img.shields.io/pypi/pyversions/trackerstatus.svg)](https://pypi.org/project/trackerstatus/)
[![License](https://img.shields.io/pypi/l/trackerstatus.svg)](https://github.com/mauvehed/trackerstatus/blob/main/LICENSE)

A Python wrapper for the [trackerstatus.info](https://trackerstatus.info) API and its tracker-specific endpoints. This library provides a simple interface to monitor the status of various trackers and their services.

## Features

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

## Installation

### Using pip

```bash
pip install trackerstatus
```

### Using poetry

```bash
poetry add trackerstatus
```

## Usage

### Basic Usage

```python
from trackerstatus import APIClient, StatusEndpoint

# Initialize the client
client = APIClient()

# Get status for all trackers
status_api = StatusEndpoint(client)
all_statuses = status_api.get_tracker_statuses()

# Print status of each tracker
for tracker, info in all_statuses.items():
    print(f"{tracker}: {info['status_message']}")
```

### Tracker-Specific Endpoints

```python
from trackerstatus import APIClient, BTNEndpoint

# Initialize the client
client = APIClient()

# Create a BTN endpoint instance
btn = BTNEndpoint(client)

# Get current status
status = btn.get_status()

# Get latency information
latency = btn.get_latency()

# Get uptime statistics
uptime = btn.get_uptime()

# Get all information at once
all_info = btn.get_all()
```

### Available Endpoints

Each tracker endpoint (`AREndpoint`, `BTNEndpoint`, `GGNEndpoint`, `PTPEndpoint`, `REDEndpoint`, `OPSEndpoint`) provides these methods:

- `get_status()`: Current status of all services
- `get_latency()`: Current response latency
- `get_uptime()`: Current uptime in minutes
- `get_records()`: Best recorded uptime
- `get_downtime()`: Current downtime
- `get_all()`: Combined data from all endpoints

### Status Codes

All status responses use these codes:
- `0`: Offline (no response over past 3 minutes)
- `1`: Online (perfect response over past 3 minutes)
- `2`: Unstable (intermittent responses over past 3 minutes)

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/mauvehed/trackerstatus.git
cd trackerstatus

# Install development dependencies
pip install -e ".[dev,test]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=trackerstatus

# Run tests and watch for changes
pytest-watch
```

### Code Style

The project uses:
- Black for code formatting
- isort for import sorting
- mypy for type checking
- pylint for linting

Run formatters:
```bash
black .
isort .
```

Run type checking:
```bash
mypy trackerstatus tests
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the test suite
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [trackerstatus.info](https://trackerstatus.info) for providing the API
- All tracker-specific status pages:
  - [ar.trackerstatus.info](https://ar.trackerstatus.info)
  - [btn.trackerstatus.info](https://btn.trackerstatus.info)
  - [ggn.trackerstatus.info](https://ggn.trackerstatus.info)
  - [ptp.trackerstatus.info](https://ptp.trackerstatus.info)
  - [red.trackerstatus.info](https://red.trackerstatus.info)
  - [ops.trackerstatus.info](https://ops.trackerstatus.info)
