"""
SunPy's LightCurve module provides a datatype for 1D time series data.

The objects also include data downloaders for their specific instruments, they
also support instantiation from files such as csv.
"""
from __future__ import absolute_import

__author__ = "Keith Hughitt"
__email__ = "keith.hughitt@nasa.gov"

from sunpy.lightcurve.lightcurve import GenericLightCurve
from sunpy.lightcurve.sources.eve import *
from sunpy.lightcurve.sources.goes import *
from sunpy.lightcurve.sources.lyra import *
from sunpy.lightcurve.sources.logical import *
