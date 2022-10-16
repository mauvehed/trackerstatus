'''Module for the trackerstatus class'''
import requests

API_ALL_SITES_URL = 'https://trackerstatus.info/api/list/'

class Trackerstatus:
    '''Fetches data from the trackerstatus.info API

    Args:
        site_name (str): The site name to fetch data for
                         Must match 'all', 'ar', 'btn', 'ggn', 'ptp', 'red', or 'ops'

    Returns:
        dict: The data from the API
    '''
    def __init__(self, site_name):
        '''Initialize the class'''
        self.site_name = site_name
        self.data = ''
        if site_name == 'all':
            self.get_sites_all_api()

    def get_site_api(self, api_type):
        '''Get the API data

        api_type can be one of the following:
        - status
        - latency
        - uptime
        - records
        - downtime
        - all
        '''
        api_site_url = f'https://{self.site_name}.trackerstatus.info/api/{api_type}/'
        response_is = requests.get(api_site_url,timeout=15)
        if response_is.status_code == 200:
            self.data = response_is.json()
        return self.data

    def get_sites_all_api(self):
        '''Get the top level /api/all/ sites API data'''
        self.data = requests.get(API_ALL_SITES_URL,timeout=15).json()
        return self.data
