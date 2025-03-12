# API Reference

## APIClient

The main client for interacting with the trackerstatus.info API.

```python
from trackerstatus import APIClient

client = APIClient()
```

### Parameters

- `base_url` (str, optional): Base URL for the API. Defaults to "https://trackerstatus.info"

### Methods

#### get(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]

Make a GET request to the specified endpoint.

```python
response = client.get('api/list')
```

## Endpoints

### StatusEndpoint

Endpoint for retrieving status information for all trackers.

```python
from trackerstatus import StatusEndpoint

status = StatusEndpoint(client)
statuses = status.get_tracker_statuses()
```

### Tracker-Specific Endpoints

All tracker endpoints inherit from `BaseTrackerEndpoint` and provide the following methods:

- `get_status()`: Get current status
- `get_latency()`: Get current latency
- `get_uptime()`: Get current uptime
- `get_records()`: Get best recorded uptime
- `get_downtime()`: Get current downtime
- `get_all()`: Get all information

Available tracker endpoints:

- `AREndpoint`: AlphaRatio
- `BTNEndpoint`: BroadcastTheNet
- `GGNEndpoint`: GazelleGames
- `PTPEndpoint`: PassThePopcorn
- `REDEndpoint`: Redacted
- `OPSEndpoint`: Orpheus

Example usage:

```python
from trackerstatus import BTNEndpoint

btn = BTNEndpoint(client)
status = btn.get_status()
all_info = btn.get_all()
```

## Status Codes

The API uses the following status codes:

- `0`: Offline - no response over the past 3 minutes
- `1`: Online - perfect response over the past 3 minutes
- `2`: Unstable - intermittent responses over the past 3 minutes

These are available as the `TrackerStatus` enum:

```python
from trackerstatus import TrackerStatus

if status == TrackerStatus.ONLINE:
    print("Service is online!")
```

## Rate Limiting

The API client implements rate limiting of 1 request per minute as per API requirements. This is handled automatically by the client.
