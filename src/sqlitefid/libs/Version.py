# -*- coding: utf-8 -*-

"""Version.py

Stores and returns the version of sqlitefid.
"""

__version__ = "v4.0.0rc1"


class SqliteFIDVersion:
    """SqliteFIDVersion."""

    __version__ = __version__

    def getVersion(self):
        """Return version to the caller."""
        return self.__version__
