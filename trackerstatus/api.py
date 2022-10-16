'''Module for the trackerstatus class'''
import requests

API_ALL_SITES_URL = 'https://trackerstatus.info/api/list/'

class Trackerstatus:
    '''Fetches data from the trackerstatus.info API

    Args:
        site_name (str): The site name to fetch data for
                         Must match 'all', 'ar', 'btn', 'ggn', 'ptp', 'red', or 'ops'

    Returns:
        dict: The data retrieved from the API
    '''
    def __init__(self, site_name):
        '''Initialize the class'''
        self.site_name = site_name
        self.data = ''
        if site_name == 'all':
            self.get_sites_all_api()

    def get_site_api(self, api_type='all'):
        '''Get the API data as specified by the api_type

        Args:
            api_type (str): The API type to fetch data for
                            Must match 'status', 'latency', 'uptime', 'records', 'downtime' or 'all'
                            If no value is specified, 'all' is used as value

        Returns:
            dict: The data retreived from the API
        '''
        api_site_url = f'https://{self.site_name}.trackerstatus.info/api/{api_type}/'
        response_is = requests.get(api_site_url,timeout=15)
        if response_is.status_code == 200:
            self.data = response_is.json()
        return self.data

    def get_sites_all_api(self):
        '''Get the top level /api/all/ sites API data'''
        response_is = requests.get(API_ALL_SITES_URL,timeout=15)
        if response_is.status_code == 200:
            self.data = response_is.json()
        return self.data

    def get_site_status(self):
        '''Get the site status API data'''
        return self.get_site_api('status')

    def get_site_latency(self):
        '''Get the site latency API data'''
        return self.get_site_api('latency')

    def get_site_uptime(self):
        '''Get the site uptime API data'''
        return self.get_site_api('uptime')

    def get_site_records(self):
        '''Get the site records API data'''
        return self.get_site_api('records')

    def get_site_downtime(self):
        '''Get the site downtime API data'''
        return self.get_site_api('downtime')

    def get_site_all(self):
        '''Get the site all API data'''
        return self.get_site_api('all')
