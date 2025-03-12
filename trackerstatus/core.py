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

    def _construct_url(self, endpoint: str) -> str:
        """
        Construct the full URL for an API endpoint.

        Args:
            endpoint (str): The API endpoint to construct the URL for

        Returns:
            str: The full URL
        """
        # If it's already a full URL, return it
        if endpoint.startswith(("http://", "https://")):
            return endpoint

        # Otherwise, join it with the base URL
        return f'{self.base_url}/{endpoint.lstrip("/")}'

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to query
            params (dict, optional): Query parameters to include

        Returns:
            dict: JSON response from the API

        Raises:
            requests.HTTPError: If the request fails
            ValueError: If the response is not valid JSON
            TypeError: If the response is not a dictionary
        """
        self._enforce_rate_limit()

        url = self._construct_url(endpoint)

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
