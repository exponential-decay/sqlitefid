# -*- coding: utf-8 -*-

"""Version.py

Stores and returns the version of sqlitefid.
"""

from __future__ import absolute_import

__version__ = "v3.0.0rc2"


class SqliteFIDVersion:
    """SqliteFIDVersion."""

    __version__ = __version__

    def getVersion(self):
        """Return version to the caller."""
        return self.__version__
