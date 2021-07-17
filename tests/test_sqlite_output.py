# -*- coding: utf-8 -*-

from __future__ import absolute_import

import collections
import sqlite3
import sys

import pytest

from sqlitefid.libs.DROIDLoaderClass import DROIDLoader
from sqlitefid.libs.GenerateBaselineDBClass import GenerateBaselineDB

if sys.version_info[0] == 3:
    PY3 = True
else:
    PY3 = False


FIDDatabase = collections.namedtuple("FIDDatabase", "baseline cursor")


@pytest.fixture()
def database():
    """Create a baseline database for each of the tests below.

    :returns: Yielded named tuple containing a baseline db object
        (GenerateBaselineDB) and database cursor object (sqlite3.Cursor)
    """
    basedb = GenerateBaselineDB("export.csv")
    basedb.tooltype = "droid"
    basedb.dbname = "file::memory:?cache=shared"
    connection = FIDDatabase(basedb, basedb.dbsetup())
    yield connection


def test_base_db(database):
    """Ensure that the baseline database is created correctly."""

    basedb = database.baseline
    cursor = database.cursor


def test_droid_setup(database):
    """Ensure that the initial data for a DROID database is correct."""

    basedb = database.baseline
    cursor = database.cursor

    droid_loader = DROIDLoader(basedb, True)
    droid_loader.setupNamespaceConstants(cursor, "filename-♖♗♘♙♚♛♜♝♞♟.csv")

    res = cursor.execute("SELECT * from NSDATA").fetchall()

    assert res[0][0] == 1
    assert res[0][1] == "pronom"
    if PY3:
        assert res[0][2] == "filename-♖♗♘♙♚♛♜♝♞♟.csv"
    else:
        assert res[0][2].encode("utf8") == "filename-♖♗♘♙♚♛♜♝♞♟.csv"

    assert droid_loader.NS_DETAILS == "filename-♖♗♘♙♚♛♜♝♞♟.csv"


def test_sqlite_output_droid():
    assert True


def test_sqlite_output_sf():
    assert True
