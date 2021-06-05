# -*- coding: utf-8 -*-

"""Version.py

Stores and returns the version of sqlitefid.
"""

from __future__ import absolute_import


class SqliteFIDVersion:
    """SqliteFIDVersion."""

    version = "sqlitefid-1.0.0"  # need something reasonable here...

    def getVersion(self):
        """Return version to the caller."""
        return self.version
