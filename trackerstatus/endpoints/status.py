from trackerstatus.core import APIClient

class StatusEndpoint:
    def __init__(self, client: APIClient):
        """
        Initializes the StatusEndpoint with an APIClient instance.

        Args:
            client (APIClient): An instance of the APIClient to make HTTP requests.
        """
        self.client = client

    def get_tracker_statuses(self):
        """
        Retrieves the statuses of all trackers.

        Returns:
            dict: A dictionary containing the statuses of all trackers.
        """
        endpoint = 'api/list'
        return self.client.get(endpoint)
