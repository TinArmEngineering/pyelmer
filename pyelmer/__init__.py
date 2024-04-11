"""A python interface to Elmer."""

from . import elmer

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
