import pytest
from requests.exceptions import HTTPError, Timeout
from trackerstatus.core import APIClient
from trackerstatus.endpoints.btn import BTNEndpoint
from trackerstatus.core import APIClient
from trackerstatus.endpoints.btn import BTNEndpoint

@pytest.fixture
def api_client():
    """
    Fixture to create an APIClient instance.
    
    Returns:
        APIClient: An instance of the APIClient.
    """
    return APIClient(base_url='https://btn.trackerstatus.info')

@pytest.fixture
def btn_endpoint(api_client):
    """
    Fixture to create a BTNEndpoint instance.
    
    Args:
        api_client (APIClient): An instance of the APIClient.
    
    Returns:
        BTNEndpoint: An instance of the BTNEndpoint.
    """
    return BTNEndpoint(client=api_client)

def test_get_btn_status(btn_endpoint):
    """
    Tests the get_btn_status method of the BTNEndpoint.
    
    Args:
        btn_endpoint (BTNEndpoint): An instance of the BTNEndpoint.
    """
    response = btn_endpoint.get_btn_status()
    assert isinstance(response, dict)
import re

assert 'Website' in response
assert isinstance(response['Website'], str)
assert re.match(r'^https?://', response['Website'])
    assert 'TrackerHTTP' in response
    assert 'TrackerHTTPS' in response
    assert 'IRC' in response
    assert 'Barney' in response
    assert 'CableGuy' in response
    assert 'tweet' in response
    assert 'date' in response['tweet']
    assert 'unix' in response['tweet']
    assert 'message' in response['tweet']

def test_get_btn_latency(btn_endpoint):
    """
    Tests the get_btn_latency method of the BTNEndpoint.
    
    Args:
        btn_endpoint (BTNEndpoint): An instance of the BTNEndpoint.
    """
    response = btn_endpoint.get_btn_latency()
    assert isinstance(response, dict)
    assert 'Website' in response
    assert 'TrackerHTTP' in response
    assert 'TrackerHTTPS' in response
    assert 'IRC' in response
    assert 'Barney' in response
    assert 'CableGuy' in response

def test_get_btn_uptime(btn_endpoint):
    """
    Tests the get_btn_uptime method of the BTNEndpoint.
    
    Args:
        btn_endpoint (BTNEndpoint): An instance of the BTNEndpoint.
    """
    response = btn_endpoint.get_btn_uptime()
    assert isinstance(response, dict)
    assert 'Website' in response
    assert 'TrackerHTTP' in response
    assert 'TrackerHTTPS' in response
    assert 'IRC' in response
    assert 'Barney' in response
    assert 'CableGuy' in response

def test_get_btn_records(btn_endpoint):
    """
    Tests the get_btn_records method of the BTNEndpoint.
    
    Args:
        btn_endpoint (BTNEndpoint): An instance of the BTNEndpoint.
    """
    response = btn_endpoint.get_btn_records()
    assert isinstance(response, dict)
    assert 'Website' in response
    assert 'TrackerHTTP' in response
    assert 'TrackerHTTPS' in response
    assert 'IRC' in response
    assert 'Barney' in response
    assert 'CableGuy' in response

def test_get_btn_downtime(btn_endpoint):
    """
    Tests the get_btn_downtime method of the BTNEndpoint.
    
    Args:
        btn_endpoint (BTNEndpoint): An instance of the BTNEndpoint.
    """
    response = btn_endpoint.get_btn_downtime()
    assert isinstance(response, dict)
    assert 'Website' in response
    assert 'TrackerHTTP' in response
    assert 'TrackerHTTPS' in response
    assert 'IRC' in response
    assert 'Barney' in response
    assert 'CableGuy' in response

def test_get_btn_all(btn_endpoint):
    """
    Tests the get_btn_all method of the BTNEndpoint.
    
    Args:
        btn_endpoint (BTNEndpoint): An instance of the BTNEndpoint.
    """
    response = btn_endpoint.get_btn_all()
    assert isinstance(response, dict)
    assert 'Website' in response
    assert 'TrackerHTTP' in response
    assert 'TrackerHTTPS' in response
    assert 'IRC' in response
    assert 'Barney' in response
    assert 'CableGuy' in response
    assert 'tweet' in response
    assert 'date' in response['tweet']
    assert 'unix' in response['tweet']
    assert 'message' in response['tweet']
