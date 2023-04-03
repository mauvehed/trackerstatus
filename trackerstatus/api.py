'''Module for the trackerstatus class'''
import requests

API_ALL_SITES_URL = 'https://trackerstatus.info/api/list/'

class Trackerstatus:
    """
    This library is a wrapper for the (*.)trackerstatus.info/api/
    API endpoints.  The API endpoints are documented at
    https://trackerstatus.info/api/
    """
    def __init__(self, site_name='all'):
        """Initialize the default state for the class

        Args:
            site_name (str, optional): Defaults to 'all'.
                This value represents one of the defined sites monitored by Trackerstatus
                Must be one of 'all', 'ar', 'btn', 'ggn', 'ptp', 'red', or 'ops'

        Returns:
            dict: The data retrieved from the API
        """
        self.site_name = site_name
        self.data = ''
        if site_name == 'all':
            self.get_sites_all_api()

    def get_site_api(self, api_type='all'):
        """Get the API data for the specific api_type

        Args:
            api_type (str, optional):  Defaults to 'all'.
                The API type to fetch data for
                Must be one of 'status', 'latency', 'uptime', 'records', 'downtime' or 'all'

        Returns:
            dict: The data retrieved from the API
        """
        api_site_url = f'https://{self.site_name}.trackerstatus.info/api/{api_type}/'
        return self._extracted_from_get_sites_all_api(api_site_url)


    def get_sites_all_api(self):
        """Get the top level /api/list/ sites API data

        https://trackerstatus.info/api/list/

        Returns:
            dict: The data retrieved from the API
        """
        return self._extracted_from_get_sites_all_api(API_ALL_SITES_URL)

    def _extracted_from_get_sites_all_api(self, api_site_url):
        """Get the API data for the specific api_site_url
        
        Args:
            api_site_url (str, optional):  Defaults to 'all'.
        
            The API type to fetch data for
            Must be one of 'status', 'latency', 'uptime', 'records', 'downtime' or 'all'
        
        Returns:
            dict: The data retrieved from the API
        """
        response_is = requests.get(api_site_url, timeout=15)
        if response_is.status_code == 200:
            self.data = response_is.json()
        return self.data

    def get_site_status(self):
        """Get the site status API data

        https://*.trackerstatus.info/api/status/

        Returns:
            dict: The data retrieved from the API
        """
        return self.get_site_api('status')

    def get_site_latency(self):
        """Get the site latency API data

        https://*.trackerstatus.info/api/latency/

        Returns:
            dict: The data retrieved from the API
        """
        return self.get_site_api('latency')

    def get_site_uptime(self):
        """Get the site uptime API data

        https://*.trackerstatus.info/api/uptime/

        Returns:
            dict: The data retrieved from the API
        """
        return self.get_site_api('uptime')

    def get_site_records(self):
        """Get the site records API data

        https://*.trackerstatus.info/api/records/

        Returns:
            dict: The data retrieved from the API
        """
        return self.get_site_api('records')

    def get_site_downtime(self):
        """Get the site downtime API data

        https://*.trackerstatus.info/api/downtime/

        Returns:
            dict: The data retrieved from the API
        """
        return self.get_site_api('downtime')

    def get_site_all(self):
        """Get the site all API data

        https://*.trackerstatus.info/api/all/

        Returns:
            dict: The data retrieved from the API
        """

        return self.get_site_api('all')
