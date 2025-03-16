import time
from typing import Any, Dict, Optional

import requests


class APIClient:
    """
    Client for interacting with the trackerstatus.info API.
    Implements rate limiting (1 request per minute) as per API requirements.
    """

    def __init__(self, base_url: str = "https://trackerstatus.info"):
        """
        Initialize the API client.

        Args:
            base_url (str): Base URL for the API. Defaults to https://trackerstatus.info
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.last_request_time: Optional[float] = None

    def _enforce_rate_limit(self) -> None:
        """Enforce the 1 request per minute rate limit."""
        if self.last_request_time:
            elapsed = time.time() - self.last_request_time
            if elapsed < 60:  # Wait if less than 60 seconds since last request
                time.sleep(60 - elapsed)

    def _construct_url(
        self, endpoint: str, tracker_prefix: Optional[str] = None
    ) -> str:
        """
        Construct the full URL for an API endpoint.

        Args:
            endpoint (str): The API endpoint to construct the URL for
            tracker_prefix (str, optional): The tracker prefix for subdomain-based URLs

        Returns:
            str: The full URL
        """
        # If it's already a full URL, return it
        if endpoint.startswith(("http://", "https://")):
            return endpoint

        # For tracker-specific endpoints, use the subdomain
        if tracker_prefix:
            base = f"https://{tracker_prefix}.trackerstatus.info"
        else:
            base = self.base_url

        # Join with the base URL and ensure api/ prefix
        endpoint = endpoint.lstrip("/")
        if not endpoint.startswith("api/"):
            endpoint = f"api/{endpoint}"

        return f"{base}/{endpoint}"

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        tracker_prefix: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Make a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to query
            params (dict, optional): Query parameters to include
            tracker_prefix (str, optional): The tracker prefix for subdomain-based URLs

        Returns:
            dict: JSON response from the API

        Raises:
            requests.HTTPError: If the request fails
            ValueError: If the response is not valid JSON
            TypeError: If the response is not a dictionary
        """
        self._enforce_rate_limit()

        url = self._construct_url(endpoint, tracker_prefix)

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, dict):
                raise TypeError("API response must be a dictionary")
            self.last_request_time = time.time()
            return data
        except (requests.HTTPError, ValueError, TypeError) as err:
            raise err
        except Exception as err:
            raise Exception(f"An error occurred: {err}") from err
