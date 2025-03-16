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

#### get(endpoint: str, params: Optional[Dict[str, Any]] = None, tracker_prefix: Optional[str] = None) -> Dict[str, Any]

Make a GET request to the specified endpoint.

```python
# For main API
response = client.get('api/list')

# For tracker-specific endpoints (using subdomains)
response = client.get('status', tracker_prefix='btn')  # Uses https://btn.trackerstatus.info/api/status
```

## Endpoints

### StatusEndpoint

Endpoint for retrieving status information for all trackers.

```python
from trackerstatus import StatusEndpoint

status = StatusEndpoint(client)
statuses = status.get_tracker_statuses()
```

#### Methods

##### get_tracker_statuses() -> Dict[str, Dict[str, Any]]

Retrieve the statuses of all trackers from the main API at trackerstatus.info. Updates once per minute as per API documentation.

Returns:
    dict: Status information for all trackers with the following structure:
    ```python
    {
        "tracker_name": {
            "status_code": int,  # 0, 1, or 2
            "status_message": str,  # Human-readable status message
            "details": {  # Optional detailed information
                "Description": str,
                "Services": Dict[str, int],
                "Details": Dict[str, str]
            }
        }
    }
    ```

##### get_status() -> Dict[str, Dict[str, Any]]

Alias for `get_tracker_statuses()`. Returns the same format as above.

### Tracker-Specific Endpoints

All tracker endpoints inherit from `BaseTrackerEndpoint` and provide the following methods. Each tracker has its own subdomain (e.g., btn.trackerstatus.info, ptp.trackerstatus.info) for detailed information.

- `get_status()`: Get current status
  ```python
  {
      "status_code": {
          "Description": str,
          "Details": Dict[str, str]
      }
  }
  ```
- `get_latency()`: Get current latency
  ```python
  {
      "service_name": int  # Latency in milliseconds
  }
  ```
- `get_uptime()`: Get current uptime
  ```python
  {
      "service_name": int  # Uptime in minutes
  }
  ```
- `get_records()`: Get best recorded uptime
  ```python
  {
      "service_name": int  # Best recorded uptime in minutes
  }
  ```
- `get_downtime()`: Get current downtime
  ```python
  {
      "service_name": int  # Current downtime in minutes
  }
  ```
- `get_all()`: Get all information
  ```python
  {
      "status": Dict[str, Any],
      "latency": Dict[str, int],
      "uptime": Dict[str, int],
      "records": Dict[str, int],
      "downtime": Dict[str, int]
  }
  ```

Available tracker endpoints and their subdomains:

- `AREndpoint`: AlphaRatio (ar.trackerstatus.info)
- `BTNEndpoint`: BroadcastTheNet (btn.trackerstatus.info)
- `GGNEndpoint`: GazelleGames (ggn.trackerstatus.info)
- `PTPEndpoint`: PassThePopcorn (ptp.trackerstatus.info)
- `REDEndpoint`: Redacted (red.trackerstatus.info)
- `OPSEndpoint`: Orpheus (ops.trackerstatus.info)
- `NBLEndpoint`: Nebulance (nbl.trackerstatus.info)
- `ANTEndpoint`: Anthelion (ant.trackerstatus.info)

Example usage:

```python
from trackerstatus import BTNEndpoint

btn = BTNEndpoint(client)
status = btn.get_status()  # Uses https://btn.trackerstatus.info/api/status
all_info = btn.get_all()   # Uses https://btn.trackerstatus.info/api/all
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

## Error Handling

The API client may raise the following exceptions:

- `requests.HTTPError`: If the API request fails
- `ValueError`: If the response is not valid JSON
- `TypeError`: If the response is not a dictionary
- `Exception`: For any other unexpected errors

Example error handling:

```python
from trackerstatus import APIClient
import requests

client = APIClient()
try:
    status = client.get("api/list")
except requests.HTTPError as e:
    print(f"API request failed: {e}")
except ValueError as e:
    print(f"Invalid JSON response: {e}")
except TypeError as e:
    print(f"Unexpected response format: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Rate Limiting

The API client implements rate limiting of 1 request per minute as per API requirements. This is handled automatically by the client. When making requests, the client will:

1. Check the time since the last request
2. If less than 60 seconds have passed, wait for the remaining time
3. Make the request
4. Update the last request timestamp

This ensures compliance with the API's rate limiting requirements without requiring any additional configuration.
