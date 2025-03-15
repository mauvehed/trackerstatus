from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class StatusEndpoint(BaseTrackerEndpoint):
    """
    Endpoint for retrieving status information for all trackers.
    This endpoint provides an overview of all monitored services.
    """

    def __init__(self, client: APIClient):
        """
        Initializes the StatusEndpoint with an APIClient instance.

        Args:
            client (APIClient): An instance of the APIClient to make HTTP requests.
        """
        super().__init__(client)

    def get_tracker_statuses(self) -> Dict[str, Any]:
        """
        Retrieve the statuses of all trackers.
        Updates once per minute as per API documentation.

        Returns:
            dict: Status information for all trackers with human-readable interpretations
        """
        data = self.client.get("api/list")

        # Add human-readable status interpretations
        interpreted_data = {}
        for tracker, status in data.items():
            if isinstance(status, dict):
                status_code = (
                    2
                    if status.get("Status") == "unstable"
                    else 1 if status.get("Status") == "online" else 0
                )
            else:
                status_code = status
            interpreted_data[tracker] = {
                "status_code": status_code,
                "status_message": self.interpret_status(status_code),
                "details": status if isinstance(status, dict) else None,
            }

        return interpreted_data

    def get_status(self) -> Dict[str, Any]:
        """
        Alias for get_tracker_statuses() to conform to BaseTrackerEndpoint interface.

        Returns:
            dict: Status information for all trackers
        """
        return self.get_tracker_statuses()
