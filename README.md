# trackerstatus

[![PyPI](https://img.shields.io/pypi/v/trackerstatus.svg)](https://pypi.org/project/trackerstatus/)
[![Python Version](https://img.shields.io/pypi/pyversions/trackerstatus.svg)](https://github.com/mauvehed/yourIP/actions/workflows/main.yml)
[![CodeQL](https://github.com/mauvehed/trackerstatus/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/codeql-analysis.yml)
[![Pylint](https://github.com/mauvehed/trackerstatus/actions/workflows/pylint.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/pylint.yml)

A Python library for interacting with the [trackerstatus.info](https://trackerstatus.info) API. Trackerstatus.info provides real-time status updates and historical data for various trackers, helping users monitor and analyze tracker performance.

## Installation

### Pip

```bash
pip install trackerstatus
```

### Poetry

```bash
poetry add trackerstatus
```

## Resources

* Github repo: [https://github.com/mauvehed/trackerstatus/](https://github.com/mauvehed/trackerstatus/)
* Pip package: [https://pypi.org/project/trackerstatus/](https://pypi.org/project/trackerstatus/)

## Usage

### Initialization

First, you need to initialize the APIClient and the specific endpoint class you want to use.

```python
from trackerstatus.core import APIClient
from trackerstatus.endpoints.btn import BTNEndpoint
from trackerstatus.endpoints.status import StatusEndpoint

# Initialize the APIClient
client = APIClient(base_url='https://btn.trackerstatus.info')

# Initialize the BTN endpoint
btn_api = BTNEndpoint(client=client)

# Initialize the Status endpoint
status_api = StatusEndpoint(client=client)
```

#### Fetching All Tracker Statuses

```python
statuses = status_api.get_tracker_statuses()
print(statuses)
```

#### Fetching BTN Status

To get the status of all BTN services use:

```python
status = btn_api.get_btn_status()
print("Status:", status)
```

#### Fetching BTN Latency
To get the latency of all BTN services:

```python
latency = btn_api.get_btn_latency()
print("Latency:", latency)
```

#### Fetching BTN Uptime

To get the current uptime of all BTN services:

```python
uptime = btn_api.get_btn_uptime()
print("Uptime:", uptime)
```

#### Fetching BTN Records

To get the best recorded uptime of all BTN services:

```python
records = btn_api.get_btn_records()
print("Records:", records)
```

#### Fetching BTN Downtime

To get the current downtime of all BTN services:

```python
downtime = btn_api.get_btn_downtime()
print("Downtime:", downtime)
```

#### Fetching All BTN Data

To get all combined data of BTN services including status, latency, uptime, records, and downtime:

```python
all_data = btn_api.get_btn_all()
print("All Data:", all_data)
```

#### Fetching Tracker Statuses
To get the statuses of all trackers:

```python
tracker_statuses = status_api.get_tracker_statuses()
print("Tracker Statuses:", tracker_statuses)
```

## Running Tests

To run tests, you can use pytest. Make sure you have all development dependencies installed:

```bash
poetry install
pytest
```

