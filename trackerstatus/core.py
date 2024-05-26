import requests

class APIClient:
    def __init__(self, base_url):
        """
        Initializes the APIClient with a base URL.

        Args:
            base_url (str): The base URL for the API endpoints.
        """
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        """
        Makes a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the GET request to.
            params (dict, optional): URL parameters to append to the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        url = f'{self.base_url}/{endpoint}'
        response = self.session.get(url, params=params)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise SystemExit(f'HTTP error occurred: {http_err}')
        except Exception as err:
            raise SystemExit(f'Other error occurred: {err}')
        return response.json()
