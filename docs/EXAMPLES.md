# Examples

This document provides various examples of how to use the `trackerstatus` library in different scenarios.

## Basic Usage

### Checking All Tracker Statuses

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

### Monitoring a Specific Tracker

```python
from trackerstatus import APIClient, BTNEndpoint

# Initialize the client
client = APIClient()

# Create BTN endpoint (uses btn.trackerstatus.info)
btn = BTNEndpoint(client)

# Get current status
status = btn.get_status()
print(f"Status: {status['status_code']['Description']}")

# Get all information
all_info = btn.get_all()
print("\nDetailed Information:")
print(f"Status: {all_info['status']['status_code']['Description']}")
print(f"Latency: {all_info['latency']}")
print(f"Uptime: {all_info['uptime']}")
```

### Using Different Tracker Endpoints

```python
from trackerstatus import (
    APIClient,
    AREndpoint,    # ar.trackerstatus.info
    BTNEndpoint,   # btn.trackerstatus.info
    GGNEndpoint,   # ggn.trackerstatus.info
    PTPEndpoint,   # ptp.trackerstatus.info
    REDEndpoint,   # red.trackerstatus.info
    OPSEndpoint,   # ops.trackerstatus.info
    NBLEndpoint,   # nbl.trackerstatus.info
    ANTEndpoint    # ant.trackerstatus.info
)

client = APIClient()

# Create endpoints
ar = AREndpoint(client)
btn = BTNEndpoint(client)
ggn = GGNEndpoint(client)
ptp = PTPEndpoint(client)
red = REDEndpoint(client)
ops = OPSEndpoint(client)
nbl = NBLEndpoint(client)
ant = ANTEndpoint(client)

# Get status for each tracker
trackers = [ar, btn, ggn, ptp, red, ops, nbl, ant]
for tracker in trackers:
    status = tracker.get_status()
    # Get tracker name from the class name
    name = tracker.__class__.__name__.replace('Endpoint', '')
    print(f"{name}: {status['status_code']['Description']}")
```

## Advanced Usage

### Creating a Status Monitor

```python
from time import sleep
from typing import Dict, Any
from trackerstatus import APIClient, BTNEndpoint, TrackerStatus

def monitor_tracker_status(interval: int = 60) -> None:
    """
    Monitor BTN's status continuously.

    Args:
        interval: Time between checks in seconds (default: 60)
    """
    client = APIClient()
    btn = BTNEndpoint(client)

    while True:
        try:
            status = btn.get_status()
            description = status['status_code']['Description']
            details = status['status_code']['Details']

            print(f"\nBTN Status: {description}")
            print("Service Status:")
            for service, status_code in details.items():
                if int(status_code) == TrackerStatus.ONLINE:
                    print(f"✅ {service}")
                elif int(status_code) == TrackerStatus.UNSTABLE:
                    print(f"⚠️ {service}")
                else:
                    print(f"❌ {service}")

            sleep(interval)

        except Exception as e:
            print(f"Error monitoring BTN: {e}")
            sleep(interval)

# Example usage
monitor_tracker_status()
```

### Creating a Multi-Tracker Monitor

```python
from time import sleep
from typing import Dict, List, Any
from trackerstatus import (
    APIClient, TrackerStatus,
    AREndpoint, BTNEndpoint, GGNEndpoint, PTPEndpoint,
    REDEndpoint, OPSEndpoint, NBLEndpoint, ANTEndpoint
)

def monitor_all_trackers(interval: int = 60) -> None:
    """
    Monitor all trackers continuously.

    Args:
        interval: Time between checks in seconds (default: 60)
    """
    client = APIClient()

    # Create all tracker endpoints
    trackers = [
        AREndpoint(client),
        BTNEndpoint(client),
        GGNEndpoint(client),
        PTPEndpoint(client),
        REDEndpoint(client),
        OPSEndpoint(client),
        NBLEndpoint(client),
        ANTEndpoint(client)
    ]

    while True:
        try:
            print("\nTracker Status Report:")
            print("=" * 50)

            for tracker in trackers:
                name = tracker.__class__.__name__.replace('Endpoint', '')
                status = tracker.get_status()
                description = status['status_code']['Description']

                print(f"\n{name}:")
                print(f"Status: {description}")

                if 'Details' in status['status_code']:
                    print("Services:")
                    for service, code in status['status_code']['Details'].items():
                        status_icon = "✅" if int(code) == TrackerStatus.ONLINE else "❌"
                        print(f"{status_icon} {service}")

            print("\n" + "=" * 50)
            sleep(interval)

        except Exception as e:
            print(f"Error in monitoring: {e}")
            sleep(interval)

# Example usage
monitor_all_trackers()
```

## Best Practices

1. **Rate Limiting**: The library handles rate limiting automatically (1 request per minute), but be mindful when monitoring multiple trackers.

2. **Error Handling**: Always implement proper error handling as shown in the examples above.

3. **Resource Management**: Create one `APIClient` instance and reuse it across all tracker endpoints.

4. **URL Structure**: Each tracker has its own subdomain (e.g., btn.trackerstatus.info). The library handles this automatically when you use the appropriate endpoint class.

5. **Status Codes**: Use the `TrackerStatus` enum for comparing status codes:
   ```python
   from trackerstatus import TrackerStatus

   if int(status_code) == TrackerStatus.ONLINE:
       print("Service is online!")
   elif int(status_code) == TrackerStatus.UNSTABLE:
       print("Service is unstable!")
   else:  # TrackerStatus.OFFLINE
       print("Service is offline!")
   ```

These examples demonstrate various ways to use the library effectively. You can combine and modify them based on your specific needs.
