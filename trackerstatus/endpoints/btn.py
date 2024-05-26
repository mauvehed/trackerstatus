from trackerstatus.core import APIClient

class BTNEndpoint:
    def __init__(self, client: APIClient):
        """
        Initializes the BTNEndpoint with an APIClient instance.
        
        Args:
            client (APIClient): An instance of the APIClient to make HTTP requests.
        """
        self.client = client

    def get_btn_status(self):
        """
        Retrieves the status of all BTN services.
        
        Returns:
            dict: A dictionary containing the status of all BTN services.
        """
        endpoint = 'api/status'
        return self.client.get(endpoint)

    def get_btn_latency(self):
        """
        Retrieves the latency of all BTN services.
        
        Returns:
            dict: A dictionary containing the latency of all BTN services.
        """
        endpoint = 'api/latency'
        return self.client.get(endpoint)

    def get_btn_uptime(self):
        """
        Retrieves the current uptime of all BTN services.
        
        Returns:
            dict: A dictionary containing the current uptime of all BTN services.
        """
        endpoint = 'api/uptime'
        return self.client.get(endpoint)

    def get_btn_records(self):
        """
        Retrieves the best recorded uptime of all BTN services.
        
        Returns:
            dict: A dictionary containing the best recorded uptime of all BTN services.
        """
        endpoint = 'api/records'
        return self.client.get(endpoint)
        
    def get_btn_downtime(self):
        """
        Retrieves the current downtime of all BTN services.
        
        Returns:
            dict: A dictionary containing the current downtime of all BTN services.
        """
        endpoint = 'api/downtime'
        return self.client.get(endpoint)
        
    def get_btn_all(self):
        """
        Retrieves combined data of all BTN services including status, latency, uptime, records, and downtime.
        
        Returns:
            dict: A dictionary containing combined data of all BTN services.
        """
        endpoint = 'api/all'
        return self.client.get(endpoint)
