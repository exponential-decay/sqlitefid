# -*- coding: utf-8 -*-

from __future__ import absolute_import

import collections
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

    res = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()

    assert res == [("FILEDATA",), ("IDDATA",), ("IDRESULTS",), ("NSDATA",)]

    res = cursor.execute("PRAGMA table_info(FILEDATA)").fetchall()

    assert res == [
        (0, "FILE_ID", "integer", 0, None, 1),
        (1, "INPUT_ID", "integer", 0, None, 0),
        (2, "PARENT_ID", "integer", 0, None, 0),
        (3, "URI", "", 0, None, 0),
        (4, "URI_SCHEME", "", 0, None, 0),
        (5, "FILE_PATH", "", 0, None, 0),
        (6, "DIR_NAME", "", 0, None, 0),
        (7, "NAME", "", 0, None, 0),
        (8, "SIZE", "integer", 0, None, 0),
        (9, "TYPE", "", 0, None, 0),
        (10, "EXT", "", 0, None, 0),
        (11, "LAST_MODIFIED", "TIMESTAMP", 0, None, 0),
        (12, "YEAR", "INTEGER", 0, None, 0),
        (13, "HASH", "", 0, None, 0),
        (14, "ERROR", "", 0, None, 0),
    ]

    res = cursor.execute("PRAGMA table_info(IDDATA)").fetchall()

    assert res == [
        (0, "ID_ID", "integer", 0, None, 1),
        (1, "NS_ID", "integer", 0, None, 0),
        (2, "METHOD", "", 0, None, 0),
        (3, "STATUS", "", 0, None, 0),
        (4, "ID", "", 0, None, 0),
        (5, "BASIS", "", 0, None, 0),
        (6, "MIME_TYPE", "", 0, None, 0),
        (7, "FORMAT_NAME", "", 0, None, 0),
        (8, "FORMAT_VERSION", "", 0, None, 0),
        (9, "EXTENSION_MISMATCH", "boolean", 0, None, 0),
        (10, "WARNING", "", 0, None, 0),
    ]

    res = cursor.execute("PRAGMA table_info(IDRESULTS)").fetchall()

    assert res == [
        (0, "FILE_ID", "INTEGER", 0, None, 1),
        (1, "ID_ID", "INTEGER", 0, None, 2),
    ]

    res = cursor.execute("PRAGMA table_info(NSDATA)").fetchall()

    assert res == [
        (0, "NS_ID", "INTEGER", 0, None, 1),
        (1, "NS_NAME", "", 0, None, 0),
        (2, "NS_DETAILS", "", 0, None, 0),
    ]

    res = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type = 'index';"
    ).fetchall()

    assert res == [("sqlite_autoindex_IDRESULTS_1",), ("HASH",), ("NAME",), ("PUID",)]

    basedb.timestamp = "timestamp_value"
    basedb.hashtype = "hashtype_value"
    basedb.tooltype = "identification_tool"

    basedb.createDBMD(cursor)

    res = cursor.execute("PRAGMA table_info(DBMD)").fetchall()

    assert res == [
        (0, "TIMESTAMP", "TIMESTAMP", 0, None, 0),
        (1, "HASH_TYPE", "", 0, None, 0),
        (2, "TOOL_TYPE", "", 0, None, 0),
    ]

    res = cursor.execute("SELECT * from DBMD").fetchall()

    assert res == [("timestamp_value", "hashtype_value", "identification_tool")]


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
