"""
trackerstatus - A Python wrapper for the trackerstatus.info API
"""

from trackerstatus.core import APIClient
from trackerstatus.endpoints.ant import ANTEndpoint
from trackerstatus.endpoints.ar import AREndpoint
from trackerstatus.endpoints.base import BaseTrackerEndpoint, TrackerStatus
from trackerstatus.endpoints.btn import BTNEndpoint
from trackerstatus.endpoints.ggn import GGNEndpoint
from trackerstatus.endpoints.nbl import NBLEndpoint
from trackerstatus.endpoints.ops import OPSEndpoint
from trackerstatus.endpoints.ptp import PTPEndpoint
from trackerstatus.endpoints.red import REDEndpoint
from trackerstatus.endpoints.status import StatusEndpoint

__version__ = "1.0.10"
__all__ = [
    "APIClient",
    "TrackerStatus",
    "BaseTrackerEndpoint",
    "StatusEndpoint",
    "AREndpoint",
    "BTNEndpoint",
    "GGNEndpoint",
    "PTPEndpoint",
    "REDEndpoint",
    "OPSEndpoint",
    "NBLEndpoint",
    "ANTEndpoint",
]
