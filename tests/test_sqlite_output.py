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


@pytest.fixture(scope="function")
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


DROID_CSV = u""""ID","PARENT_ID","URI","FILE_PATH","NAME","METHOD","STATUS","SIZE","TYPE","EXT","LAST_MODIFIED","EXTENSION_MISMATCH","SHA1_HASH","FORMAT_COUNT","PUID","MIME_TYPE","FORMAT_NAME","FORMAT_VERSION"
"2","0","file:////10.1.4.222/format-corpus/","\\10.1.4.222\\format-corpus","format-corpus",,"Done","","Folder",,"2014-02-28T15:49:11","false",,"",,"","",""
"3","2","file:////10.1.4.222/format-corpus/video/","\\10.1.4.222\\format-corpus\\video","video",,"Done","","Folder",,"2014-02-28T15:48:47","false",,"",,"","",""
"4","3","file:////10.1.4.222/format-corpus/video/Quicktime/","\\10.1.4.222\\format-corpus\\video\\Quicktime","Quicktime",,"Done","","Folder",,"2014-02-28T15:48:59","false",,"",,"","",""
"5","4","file:////10.1.4.222/format-corpus/video/Quicktime/apple-intermediate-codec.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\apple-intermediate-codec.mov","apple-intermediate-codec.mov","Signature","Done","319539","File","mov","2014-02-18T16:58:16","false","d097cf36467373f52b974542d48bec134279fa3f","1","x-fmt/384","video/quicktime","Quicktime",""
"6","4","file:////10.1.4.222/format-corpus/video/Quicktime/animation.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\animation.mov","animation.mov","Signature","Done","1020209","File","mov","2014-02-18T16:58:16","false","edb5226b963f449ce58054809149cb812bdf8c0a","1","x-fmt/384","video/quicktime","Quicktime",""
"7","4","file:////10.1.4.222/format-corpus/video/Quicktime/apple-prores-422-hq.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\apple-prores-422-hq.mov","apple-prores-422-hq.mov","Signature","Done","701111","File","mov","2014-02-18T16:58:16","false","484591affcae8ef5d896289db75503b603092ef8","1","x-fmt/384","video/quicktime","Quicktime",""
"8","4","file:////10.1.4.222/format-corpus/video/Quicktime/apple-prores-422-lt.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\apple-prores-422-lt.mov","apple-prores-422-lt.mov","Signature","Done","476503","File","mov","2014-02-18T16:58:16","false","4dacced1685746d8e39bb6dc36d01bf2a60a17e2","1","x-fmt/384","video/quicktime","Quicktime",""
"9","4","file:////10.1.4.222/format-corpus/video/Quicktime/apple-prores-422-proxy.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\apple-prores-422-proxy.mov","apple-prores-422-proxy.mov","Signature","Done","242855","File","mov","2014-02-18T16:58:16","false","0e18911984ac1cd4721b4d3c9e0914cc98da3ab4","1","x-fmt/384","video/quicktime","Quicktime",""
"10","4","file:////10.1.4.222/format-corpus/video/Quicktime/apple-prores-422.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\apple-prores-422.mov","apple-prores-422.mov","Signature","Done","564775","File","mov","2014-02-18T16:58:16","false","faf81ab4a815cf0cd7c9b01d8ea950971d38dad1","1","x-fmt/384","video/quicktime","Quicktime",""
"11","4","file:////10.1.4.222/format-corpus/video/Quicktime/dv-dvchd-ntsc-interlaced.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\dv-dvchd-ntsc-interlaced.mov","dv-dvchd-ntsc-interlaced.mov","Signature","Done","3001365","File","mov","2014-02-18T16:58:16","false","b9d45fd2e79a83c69afe95d89a846b96bf1778b7","1","x-fmt/384","video/quicktime","Quicktime",""
"12","4","file:////10.1.4.222/format-corpus/video/Quicktime/dv-dvchd-ntsc-progressive.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\dv-dvchd-ntsc-progressive.mov","dv-dvchd-ntsc-progressive.mov","Signature","Done","3001365","File","mov","2014-02-18T16:58:16","false","a9caed081ab55ff1ea1b32d3eb30dab2841a9785","1","x-fmt/384","video/quicktime","Quicktime",""
"13","4","file:////10.1.4.222/format-corpus/video/Quicktime/🖤dv-pal-progressive.mov","\\10.1.4.222\\format-corpus\\video\\Quicktime\\🖤dv-pal-progressive.mov","🖤dv-pal-progressive.mov","Signature","Done","3601749","File","mov","2014-02-18T16:58:16","false","7955c4e67b84f67bab77eff241a81ceba0177bf4","1","x-fmt/384","video/quicktime","Quicktime",""
529,525,"file:/home/govdocs_selected/PUB_2/281480.pub","/home/govdocs_selected/PUB_2/281480.pub","281480.pub","Extension","Done",1962,"File","pub","2012-07-26T23:18:55","false","e902a454e50b042a6853616c25d59cc1",1,"x-fmt/252",,"Microsoft Publisher",2,"x-fmt/253",,"Microsoft Publisher",95,"x-fmt/254",,"Microsoft Publisher",97,"x-fmt/255",,"Microsoft Publisher",98,"x-fmt/256",,"Microsoft Publisher",2000,"x-fmt/257",,"Microsoft Publisher",2002,,,,,,,,,,,,
2828,2824,"file:/home/govdocs_selected/DOC_131/921227.doc","/home/govdocs_selected/DOC_131/921227.doc","921227.doc","Extension","Done",28160,"File","doc","2012-07-26T23:23:43","false","99cebaa113805dc0dd31c2bb3059ea43",9,"x-fmt/2",,"Microsoft Word for Macintosh Document",6,"x-fmt/42",,"Wordperfect Secondary File",5,"x-fmt/43",,"Wordperfect Secondary File","5.1/5.2","x-fmt/129","application/msword","Microsoft Word for Macintosh Document","X","x-fmt/131",,"Stationery for Mac OS X",,"x-fmt/273","application/msword","Microsoft Word for MS-DOS Document",3,"x-fmt/329",,"Interleaf Document",,"fmt/609","application/msword","Microsoft Word (Generic)","6.0-2003","fmt/754","application/msword","Microsoft Word Document (Password Protected)","97-2003"
2831,2824,"file:/home/govdocs_selected/DOC_131/804888.doc","/home/govdocs_selected/DOC_131/804888.doc","804888.doc","Extension","Done",4352,"File","doc","2012-07-26T23:23:43","false","85c533a640ac715c1c79f29561d19063",9,"x-fmt/2",,"Microsoft Word for Macintosh Document",6,"x-fmt/42",,"Wordperfect Secondary File",5,"x-fmt/43",,"Wordperfect Secondary File","5.1/5.2","x-fmt/129","application/msword","Microsoft Word for Macintosh Document","X","x-fmt/131",,"Stationery for Mac OS X",,"x-fmt/273","application/msword","Microsoft Word for MS-DOS Document",3,"x-fmt/329",,"Interleaf Document",,"fmt/609","application/msword","Microsoft Word (Generic)","6.0-2003","fmt/754","application/msword","Microsoft Word Document (Password Protected)","97-2003"
4691,4687,"file:/home/govdocs_selected/HTML_102/374362.rtf","/home/govdocs_selected/HTML_102/374362.rtf","374362.rtf","Signature","Done",16934,"File","rtf","2012-07-26T23:20:06","true","5cba46515944f50566b5d961457866cc",2,"fmt/45","application/rtf, text/rtf","Rich Text Format","1.0-1.4","fmt/96","text/html","Hypertext Markup Language",,,,,,,,,,,,,,,,,,,,,,,,,,,,,
4692,4687,"file:/home/govdocs_selected/HTML_102/374355.rtf","/home/govdocs_selected/HTML_102/374355.rtf","374355.rtf","Signature","Done",10994,"File","rtf","2012-07-26T23:20:06","true","e692ac078285d2e9367aeb746cc0de31",2,"fmt/50","application/rtf, text/rtf","Rich Text Format","1.5-1.6","fmt/99","text/html","Hypertext Markup Language",4,,,,,,,,,,,,,,,,,,,,,,,,,,,,
4977,4974,"file:/home/govdocs_selected/DOC_127/696918.doc","/home/govdocs_selected/DOC_127/696918.doc","696918.doc","Extension","Done",7936,"File","doc","2012-07-26T23:23:33","false","94a3ba789e2165821cac20c8c7c1e442",9,"x-fmt/2",,"Microsoft Word for Macintosh Document",6,"x-fmt/42",,"Wordperfect Secondary File",5,"x-fmt/43",,"Wordperfect Secondary File","5.1/5.2","x-fmt/129","application/msword","Microsoft Word for Macintosh Document","X","x-fmt/131",,"Stationery for Mac OS X",,"x-fmt/273","application/msword","Microsoft Word for MS-DOS Document",3,"x-fmt/329",,"Interleaf Document",,"fmt/609","application/msword","Microsoft Word (Generic)","6.0-2003","fmt/754","application/msword","Microsoft Word Document (Password Protected)","97-2003"
5720,5717,"file:/home/govdocs_selected/DOC_106/411909.doc","/home/govdocs_selected/DOC_106/411909.doc","411909.doc","Extension","Done",34560,"File","doc","2012-07-26T23:20:35","false","5b0997fda7c2f6b7debced003b441f3d",9,"x-fmt/2",,"Microsoft Word for Macintosh Document",6,"x-fmt/42",,"Wordperfect Secondary File",5,"x-fmt/43",,"Wordperfect Secondary File","5.1/5.2","x-fmt/129","application/msword","Microsoft Word for Macintosh Document","X","x-fmt/131",,"Stationery for Mac OS X",,"x-fmt/273","application/msword","Microsoft Word for MS-DOS Document",3,"x-fmt/329",,"Interleaf Document",,"fmt/609","application/msword","Microsoft Word (Generic)","6.0-2003","fmt/754","application/msword","Microsoft Word Document (Password Protected)","97-2003"
7451,7449,"file:/home/govdocs_selected/TEXT_95/042871.doc","/home/govdocs_selected/TEXT_95/042871.doc","042871.doc","Extension","Done",40229,"File","doc","2012-07-26T23:08:13","false","e8494b3b97dd3473f541208cb92381d8",9,"x-fmt/2",,"Microsoft Word for Macintosh Document",6,"x-fmt/42",,"Wordperfect Secondary File",5,"x-fmt/43",,"Wordperfect Secondary File","5.1/5.2","x-fmt/129","application/msword","Microsoft Word for Macintosh Document","X","x-fmt/131",,"Stationery for Mac OS X",,"x-fmt/273","application/msword","Microsoft Word for MS-DOS Document",3,"x-fmt/329",,"Interleaf Document",,"fmt/609","application/msword","Microsoft Word (Generic)","6.0-2003","fmt/754","application/msword","Microsoft Word Document (Password Protected)","97-2003"
7684,7681,"file:/home/govdocs_selected/HTML_143/558860.html","/home/govdocs_selected/HTML_143/558860.html","558860.html","Signature","Done",10701,"File","html","2012-07-26T23:22:11","true","6750b28fde934d7418c8908c55c9ef98",2,"fmt/99","text/html","Hypertext Markup Language",4,"x-fmt/394","application/vnd.wordperfect","WordPerfect for MS-DOS/Windows Document",5.1,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""


def test_sqlite_output_droid(database, tmp_path):
    """Ensure that the database outputs are correct for a DROID CSV."""
    basedb = database.baseline
    cursor = database.cursor

    dir_ = tmp_path
    droid_csv = dir_ / "droid_test.csv"
    droid_csv.write_text(DROID_CSV.strip())

    droid_loader = DROIDLoader(basedb, BOM=False)
    droid_loader.create_droid_database(str(droid_csv), cursor)

    res = cursor.execute("SELECT * from FILEDATA").fetchall()

    assert len(res) == 21

    res = cursor.execute("SELECT * FROM FILEDATA").fetchall()

    assert res[0] == (
        1,
        2,
        0,
        "file:////10.1.4.222/format-corpus/",
        "file",
        "\\10.1.4.222\\format-corpus",
        "",
        "format-corpus",
        "",
        "Folder",
        "",
        "2014-02-28T15:49:11",
        None,
        "",
        None,
    )

    assert res[7] == (
        8,
        9,
        4,
        "file:////10.1.4.222/format-corpus/video/Quicktime/apple-prores-422-proxy.mov",
        "file",
        "\\10.1.4.222\\format-corpus\\video\\Quicktime\\apple-prores-422-proxy.mov",
        "",
        "apple-prores-422-proxy.mov",
        242855,
        "File",
        "mov",
        "2014-02-18T16:58:16",
        None,
        "0e18911984ac1cd4721b4d3c9e0914cc98da3ab4",
        None,
    )

    assert res[11] == (
        12,
        13,
        4,
        u"file:////10.1.4.222/format-corpus/video/Quicktime/🖤dv-pal-progressive.mov",
        "file",
        u"\\10.1.4.222\\format-corpus\\video\\Quicktime\\🖤dv-pal-progressive.mov",
        "",
        u"🖤dv-pal-progressive.mov",
        3601749,
        "File",
        "mov",
        "2014-02-18T16:58:16",
        None,
        "7955c4e67b84f67bab77eff241a81ceba0177bf4",
        None,
    )

    res = cursor.execute("SELECT * FROM IDDATA").fetchall()
    assert len(res) == 61
    assert res[19] == (
        20,
        1,
        "Extension",
        "Done",
        "x-fmt/2",
        None,
        "",
        "Microsoft Word for Macintosh Document",
        "6",
        "False",
        None,
    )

    res = cursor.execute("SELECT * FROM IDRESULTS").fetchall()
    assert len(res) == 61

    multi_id_query = """
    SELECT FILEDATA.NAME, IDRESULTS.FILE_ID, IDDATA.METHOD
    FROM IDRESULTS
    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
    JOIN FILEDATA on FILEDATA.FILE_ID = IDRESULTS.FILE_ID
    WHERE FILEDATA.FILE_ID = 20
    """

    res = cursor.execute(multi_id_query).fetchall()
    assert len(res) == 9
    assert res == [
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
        (u"042871.doc", 20, u"Extension"),
    ]

    res = cursor.execute("SELECT * FROM NSDATA").fetchall()
    assert len(res) == 1
    assert res[0][0] == 1
    assert res[0][1] == "pronom"
    assert res[0][2] == str(droid_csv)


def test_sqlite_output_sf():
    assert True
