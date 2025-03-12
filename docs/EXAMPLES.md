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

# Create a BTN endpoint instance
btn = BTNEndpoint(client)

# Get all information about BTN
info = btn.get_all()

# Print detailed status
print(f"Status: {info['status']['status_code']['Description']}")
print(f"Latency: {info['latency']}")
print(f"Uptime: {info['uptime']}")
print(f"Records: {info['records']}")
print(f"Downtime: {info['downtime']}")
```

## Advanced Usage

### Creating a Status Monitor

```python
from time import sleep
from typing import Dict, Any
from trackerstatus import APIClient, StatusEndpoint, TrackerStatus

def monitor_tracker_status(tracker: str, interval: int = 60) -> None:
    """
    Monitor a specific tracker's status continuously.
<<<<<<< HEAD

    Args:
        tracker: The tracker to monitor (e.g., 'btn', 'ar', etc.)
        interval: Time between checks in seconds (default: 60)
    """
    client = APIClient()
    status_api = StatusEndpoint(client)

    while True:
        try:
            statuses = status_api.get_tracker_statuses()
            tracker_status = statuses.get(tracker)

            if tracker_status:
                status_code = tracker_status['status_code']
                message = tracker_status['status_message']

                if status_code == TrackerStatus.ONLINE:
                    print(f"✅ {tracker.upper()}: {message}")
                elif status_code == TrackerStatus.UNSTABLE:
                    print(f"⚠️ {tracker.upper()}: {message}")
                else:
                    print(f"❌ {tracker.upper()}: {message}")

            sleep(interval)

        except Exception as e:
            print(f"Error monitoring {tracker}: {e}")
            sleep(interval)

# Example usage
monitor_tracker_status('btn')
```

### Creating a Uptime Report

```python
from datetime import datetime
from typing import Dict, Any
from trackerstatus import APIClient, BTNEndpoint

def generate_uptime_report() -> Dict[str, Any]:
    """
    Generate a detailed uptime report for a tracker.

    Returns:
        Dict containing the report data
    """
    client = APIClient()
    btn = BTNEndpoint(client)

    # Get all information
    info = btn.get_all()

    # Calculate uptime percentage
    total_time = sum(info['uptime'].values()) + sum(info['downtime'].values())
    uptime_percentage = (sum(info['uptime'].values()) / total_time * 100) if total_time > 0 else 0

    return {
        'timestamp': datetime.now().isoformat(),
        'status': info['status']['status_code']['Description'],
        'services': {
            service: {
                'uptime': uptime,
                'downtime': info['downtime'].get(service, 0),
                'latency': info['latency'].get(service, 0),
                'best_record': info['records'].get(service, 0)
            }
            for service, uptime in info['uptime'].items()
        },
        'overall_uptime_percentage': round(uptime_percentage, 2)
    }

# Example usage
report = generate_uptime_report()
print(f"Generated at: {report['timestamp']}")
print(f"Overall Status: {report['status']}")
print(f"Overall Uptime: {report['overall_uptime_percentage']}%")
print("\nService Details:")
for service, details in report['services'].items():
    print(f"\n{service}:")
    print(f"  Uptime: {details['uptime']} minutes")
    print(f"  Downtime: {details['downtime']} minutes")
    print(f"  Latency: {details['latency']}ms")
    print(f"  Best Record: {details['best_record']} minutes")
```

### Error Handling and Retries

```python
from time import sleep
from typing import Optional, Dict, Any
from trackerstatus import APIClient, StatusEndpoint
import requests

def get_tracker_status_with_retry(
    tracker: str,
    max_retries: int = 3,
    retry_delay: int = 60
) -> Optional[Dict[str, Any]]:
    """
    Get tracker status with automatic retries on failure.

    Args:
        tracker: The tracker to check
        max_retries: Maximum number of retry attempts
        retry_delay: Delay between retries in seconds

    Returns:
        Dict containing status information or None if all retries fail
    """
    client = APIClient()
    status_api = StatusEndpoint(client)

    for attempt in range(max_retries):
        try:
            statuses = status_api.get_tracker_statuses()
            return statuses.get(tracker)

        except requests.HTTPError as e:
            print(f"HTTP Error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                sleep(retry_delay)

        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    return None

# Example usage
status = get_tracker_status_with_retry('btn')
if status:
    print(f"BTN Status: {status['status_message']}")
else:
    print("Failed to get BTN status after all retries")
```

### Monitoring Multiple Trackers

```python
from typing import Dict, List, Any
from trackerstatus import APIClient, StatusEndpoint, TrackerStatus

def monitor_multiple_trackers(trackers: List[str]) -> Dict[str, Any]:
    """
    Monitor multiple trackers and generate a summary.

    Args:
        trackers: List of tracker codes to monitor

    Returns:
        Dict containing monitoring results
    """
    client = APIClient()
    status_api = StatusEndpoint(client)

    results = {
        'online': [],
        'unstable': [],
        'offline': [],
        'unknown': []
    }

    try:
        statuses = status_api.get_tracker_statuses()

        for tracker in trackers:
            status = statuses.get(tracker)
            if not status:
                results['unknown'].append(tracker)
                continue

            status_code = status['status_code']
            if status_code == TrackerStatus.ONLINE:
                results['online'].append(tracker)
            elif status_code == TrackerStatus.UNSTABLE:
                results['unstable'].append(tracker)
            elif status_code == TrackerStatus.OFFLINE:
                results['offline'].append(tracker)
            else:
                results['unknown'].append(tracker)

    except Exception as e:
        print(f"Error monitoring trackers: {e}")

    return results

# Example usage
trackers_to_monitor = ['btn', 'ar', 'ggn', 'ptp', 'red', 'ops']
results = monitor_multiple_trackers(trackers_to_monitor)

print("\nTracker Status Summary:")
print(f"Online: {', '.join(results['online'])}")
print(f"Unstable: {', '.join(results['unstable'])}")
print(f"Offline: {', '.join(results['offline'])}")
print(f"Unknown: {', '.join(results['unknown'])}")
```

## Best Practices

1. **Rate Limiting**: The library handles rate limiting automatically, but be mindful when making multiple requests in quick succession.

2. **Error Handling**: Always implement proper error handling as shown in the examples above.

3. **Resource Management**: The `APIClient` uses a session object for better performance. Create one instance and reuse it.

4. **Type Hints**: The library provides type hints for better IDE support and code quality.

5. **Status Interpretation**: Use the `TrackerStatus` enum for status comparisons rather than raw numbers.

These examples demonstrate various ways to use the library effectively. You can combine and modify them based on your specific needs.
||||||| 08b962c
=======
    
    Args:
        tracker: The tracker to monitor (e.g., 'btn', 'ar', etc.)
        interval: Time between checks in seconds (default: 60)
    """
    client = APIClient()
    status_api = StatusEndpoint(client)
    
    while True:
        try:
            statuses = status_api.get_tracker_statuses()
            tracker_status = statuses.get(tracker)
            
            if tracker_status:
                status_code = tracker_status['status_code']
                message = tracker_status['status_message']
                
                if status_code == TrackerStatus.ONLINE:
                    print(f"✅ {tracker.upper()}: {message}")
                elif status_code == TrackerStatus.UNSTABLE:
                    print(f"⚠️ {tracker.upper()}: {message}")
                else:
                    print(f"❌ {tracker.upper()}: {message}")
            
            sleep(interval)
            
        except Exception as e:
            print(f"Error monitoring {tracker}: {e}")
            sleep(interval)

# Example usage
monitor_tracker_status('btn')
```

### Creating a Uptime Report

```python
from datetime import datetime
from typing import Dict, Any
from trackerstatus import APIClient, BTNEndpoint

def generate_uptime_report() -> Dict[str, Any]:
    """
    Generate a detailed uptime report for a tracker.
    
    Returns:
        Dict containing the report data
    """
    client = APIClient()
    btn = BTNEndpoint(client)
    
    # Get all information
    info = btn.get_all()
    
    # Calculate uptime percentage
    total_time = sum(info['uptime'].values()) + sum(info['downtime'].values())
    uptime_percentage = (sum(info['uptime'].values()) / total_time * 100) if total_time > 0 else 0
    
    return {
        'timestamp': datetime.now().isoformat(),
        'status': info['status']['status_code']['Description'],
        'services': {
            service: {
                'uptime': uptime,
                'downtime': info['downtime'].get(service, 0),
                'latency': info['latency'].get(service, 0),
                'best_record': info['records'].get(service, 0)
            }
            for service, uptime in info['uptime'].items()
        },
        'overall_uptime_percentage': round(uptime_percentage, 2)
    }

# Example usage
report = generate_uptime_report()
print(f"Generated at: {report['timestamp']}")
print(f"Overall Status: {report['status']}")
print(f"Overall Uptime: {report['overall_uptime_percentage']}%")
print("\nService Details:")
for service, details in report['services'].items():
    print(f"\n{service}:")
    print(f"  Uptime: {details['uptime']} minutes")
    print(f"  Downtime: {details['downtime']} minutes")
    print(f"  Latency: {details['latency']}ms")
    print(f"  Best Record: {details['best_record']} minutes")
```

### Error Handling and Retries

```python
from time import sleep
from typing import Optional, Dict, Any
from trackerstatus import APIClient, StatusEndpoint
import requests

def get_tracker_status_with_retry(
    tracker: str,
    max_retries: int = 3,
    retry_delay: int = 60
) -> Optional[Dict[str, Any]]:
    """
    Get tracker status with automatic retries on failure.
    
    Args:
        tracker: The tracker to check
        max_retries: Maximum number of retry attempts
        retry_delay: Delay between retries in seconds
        
    Returns:
        Dict containing status information or None if all retries fail
    """
    client = APIClient()
    status_api = StatusEndpoint(client)
    
    for attempt in range(max_retries):
        try:
            statuses = status_api.get_tracker_statuses()
            return statuses.get(tracker)
            
        except requests.HTTPError as e:
            print(f"HTTP Error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                sleep(retry_delay)
                
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    return None

# Example usage
status = get_tracker_status_with_retry('btn')
if status:
    print(f"BTN Status: {status['status_message']}")
else:
    print("Failed to get BTN status after all retries")
```

### Monitoring Multiple Trackers

```python
from typing import Dict, List, Any
from trackerstatus import APIClient, StatusEndpoint, TrackerStatus

def monitor_multiple_trackers(trackers: List[str]) -> Dict[str, Any]:
    """
    Monitor multiple trackers and generate a summary.
    
    Args:
        trackers: List of tracker codes to monitor
        
    Returns:
        Dict containing monitoring results
    """
    client = APIClient()
    status_api = StatusEndpoint(client)
    
    results = {
        'online': [],
        'unstable': [],
        'offline': [],
        'unknown': []
    }
    
    try:
        statuses = status_api.get_tracker_statuses()
        
        for tracker in trackers:
            status = statuses.get(tracker)
            if not status:
                results['unknown'].append(tracker)
                continue
                
            status_code = status['status_code']
            if status_code == TrackerStatus.ONLINE:
                results['online'].append(tracker)
            elif status_code == TrackerStatus.UNSTABLE:
                results['unstable'].append(tracker)
            elif status_code == TrackerStatus.OFFLINE:
                results['offline'].append(tracker)
            else:
                results['unknown'].append(tracker)
                
    except Exception as e:
        print(f"Error monitoring trackers: {e}")
        
    return results

# Example usage
trackers_to_monitor = ['btn', 'ar', 'ggn', 'ptp', 'red', 'ops']
results = monitor_multiple_trackers(trackers_to_monitor)

print("\nTracker Status Summary:")
print(f"Online: {', '.join(results['online'])}")
print(f"Unstable: {', '.join(results['unstable'])}")
print(f"Offline: {', '.join(results['offline'])}")
print(f"Unknown: {', '.join(results['unknown'])}")
```

## Best Practices

1. **Rate Limiting**: The library handles rate limiting automatically, but be mindful when making multiple requests in quick succession.

2. **Error Handling**: Always implement proper error handling as shown in the examples above.

3. **Resource Management**: The `APIClient` uses a session object for better performance. Create one instance and reuse it.

4. **Type Hints**: The library provides type hints for better IDE support and code quality.

5. **Status Interpretation**: Use the `TrackerStatus` enum for status comparisons rather than raw numbers.

These examples demonstrate various ways to use the library effectively. You can combine and modify them based on your specific needs. 
>>>>>>> origin/main
