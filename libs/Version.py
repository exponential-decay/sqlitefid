# -*- coding: utf-8 -*-

"""Version.py

Stores and returns the version of sqlitefid.
"""

from __future__ import absolute_import


class SqliteFIDVersion:
    """SqliteFIDVersion."""

    version = "sqlitefid-2.0.1"

    def getVersion(self):
        """Return version to the caller."""
        return self.version
