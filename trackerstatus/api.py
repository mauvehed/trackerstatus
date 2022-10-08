'''Module for the trackerstatus class'''
import requests

API_ALL_SITES_URL = 'https://trackerstatus.info/api/list/'

class Trackerstatus:
    '''Class for the trackerstatus command'''
    def __init__(self):
        '''Initialize the class'''
        self.data = ''

    def get_allsites_api_all(self):
        '''Get the top level /api/all/ sites API data'''
        self.data = requests.get(API_ALL_SITES_URL,timeout=15).json()
        return self.data

    def get_site_api_all(self, site_name):
        '''Get the site specific /api/all/ API data'''
        api_site_all_url = f'https://{site_name}.trackerstatus.info/api/all/'
        self.data = requests.get(api_site_all_url,timeout=15).json()
        return self.data

    def get_site_api_status(self, site_name):
        '''Get the site specific /api/status/ API data'''
        api_site_status_url = f'https://{site_name}.trackerstatus.info/api/status/'
        self.data = requests.get(api_site_status_url,timeout=15).json()
        return self.data

    def get_site_api_latency(self, site_name):
        '''Get the site specific /api/latency/ API data'''
        api_site_latency_url = f'https://{site_name}.trackerstatus.info/api/latency/'
        self.data = requests.get(api_site_latency_url,timeout=15).json()
        return self.data

    def get_site_api_uptime(self, site_name):
        '''Get the site specific /api/uptime/ API data'''
        api_site_uptime_url = f'https://{site_name}.trackerstatus.info/api/uptime/'
        self.data = requests.get(api_site_uptime_url,timeout=15).json()
        return self.data

    def get_site_api_records(self, site_name):
        '''Get the site specific /api/records/ API data'''
        api_site_records_url = f'https://{site_name}.trackerstatus.info/api/records/'
        self.data = requests.get(api_site_records_url,timeout=15).json()
        return self.data

    def get_site_api_downtime(self, site_name):
        '''Get the site specific /api/downtime/ API data'''
        api_site_downtime_url = f'https://{site_name}.trackerstatus.info/api/downtime/'
        self.data = requests.get(api_site_downtime_url,timeout=15).json()
        return self.data
