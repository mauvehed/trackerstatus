import pytest
from trackerstatus.core import APIClient
from trackerstatus.endpoints.status import StatusEndpoint

@pytest.fixture
def api_client():
    """
    Fixture to create an APIClient instance.
    
    Returns:
        APIClient: An instance of the APIClient.
    """
    return APIClient(base_url='https://trackerstatus.info')

@pytest.fixture
def status_endpoint(api_client):
    """
    Fixture to create a StatusEndpoint instance.
    
    Args:
        api_client (APIClient): An instance of the APIClient.
    
    Returns:
        StatusEndpoint: An instance of the StatusEndpoint.
    """
    return StatusEndpoint(client=api_client)

def test_get_tracker_statuses(status_endpoint):
    """
    Tests the get_tracker_statuses method of the StatusEndpoint.
    
    Args:
        status_endpoint (StatusEndpoint): An instance of the StatusEndpoint.
    """
    response = status_endpoint.get_tracker_statuses()
    assert isinstance(response, dict)
    assert 'ar' in response
    assert isinstance(response['ar'], dict)
    assert 'URL' in response['ar']
    assert isinstance(response['ar']['URL'], str)
    assert 'Status' in response['ar']
    assert isinstance(response['ar']['Status'], str)
    assert 'URL' in response['ar']
    assert 'Status' in response['ar']
    assert 'Description' in response['ar']
    assert 'tweet' in response['ar']
    assert 'Services' in response['ar']
    assert 'Details' in response['ar']
