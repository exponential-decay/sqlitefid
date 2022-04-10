# -*- coding: utf-8 -*-

"""Version.py

Stores and returns the version of sqlitefid.
"""

from __future__ import absolute_import


class SqliteFIDVersion:
    """SqliteFIDVersion."""

    __version__ = "v2.0.3"

    def getVersion(self):
        """Return version to the caller."""
        return self.__version__
