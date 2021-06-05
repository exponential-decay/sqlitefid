# -*- coding: utf-8 -*-

from __future__ import absolute_import

import collections
import io
import sys

import pytest

from sqlitefid.libs.GenerateBaselineDBClass import GenerateBaselineDB
from sqlitefid.libs.SFHandlerClass import SFYAMLHandler
from sqlitefid.libs.SFLoaderClass import SFLoader

SIEGFRIED_YAML = u"""---
siegfried   : 1.9.1
scandate    : 2021-07-17T22:11:59+02:00
signature   : default.sig
created     : 2020-10-06T19:15:15+02:00
identifiers :
  - name    : 'pronom'
    details : 'DROID_SignatureFile_V97.xml; container-signature-20201001.xml'
  - name    : 'tika'
    details : 'tika-mimetypes.xml (1.24, 2020-04-17)'
  - name    : 'freedesktop.org'
    details : 'freedesktop.org.xml (2.0, 2020-06-05)'
  - name    : 'loc'
    details : 'fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)'
---
filename : 'Q10287816.gz'
filesize : 3
modified : 2021-05-24T19:26:56+02:00
errors   :
md5      : 613ffd2ae0a8828aa573ce62bf2e30c3
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/266'
    format  : 'GZIP Format'
    version :
    mime    : 'application/gzip'
    basis   : 'extension match gz; byte match at 0, 3'
    warning :
  - ns      : 'tika'
    id      : 'application/gzip'
    format  : 'Gzip Compressed Archive'
    mime    : 'application/gzip'
    basis   : 'extension match gz; byte match at 0, 2 (signature 1/2); byte match at 0, 2 (signature 2/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/gzip'
    format  : 'Gzip archive'
    mime    : 'application/gzip'
    basis   : 'extension match gz; byte match at 0, 2'
    warning :
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'Q28205479🖤.info'
filesize : 8
modified : 2021-05-24T19:26:56+02:00
errors   :
md5      : bf40928c61f376064b110ff59d604160
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match; possibilities based on extension are fmt/1202'
  - ns      : 'tika'
    id      : 'UNKNOWN'
    format  :
    mime    : 'UNKNOWN'
    basis   :
    warning : 'no match'
  - ns      : 'freedesktop.org'
    id      : 'UNKNOWN'
    format  :
    mime    : 'UNKNOWN'
    basis   :
    warning : 'no match'
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'test_dir/Q42332.pdf'
filesize : 4
modified : 2021-07-08T23:21:40+02:00
errors   :
md5      : bfa4b10a76324b166cfdad5e02a63730
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'extension mismatch; possibilities based on extension are fmt/14, fmt/15, fmt/16, fmt/17, fmt/18, fmt/19, fmt/20, fmt/95, fmt/144, fmt/145, fmt/146, fmt/147, fmt/148, fmt/157, fmt/158, fmt/276, fmt/354, fmt/476, fmt/477, fmt/478, fmt/479, fmt/480, fmt/481, fmt/488, fmt/489, fmt/490, fmt/491, fmt/492, fmt/493, fmt/558, fmt/559, fmt/560, fmt/561, fmt/562, fmt/563, fmt/564, fmt/565, fmt/1129'
  - ns      : 'tika'
    id      : 'application/pdf'
    format  : 'Portable Document Format'
    mime    : 'application/pdf'
    basis   : 'extension match pdf'
    warning : 'match on filename only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/x-matlab'
    format  : 'MATLAB file'
    mime    : 'text/x-matlab'
    basis   : 'byte match at 0, 1 (signature 1/3); text match ASCII'
    warning : 'filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'text/x-tex'
    format  : 'TeX document'
    mime    : 'text/x-tex'
    basis   : 'byte match at 0, 1 (signature 1/2); text match ASCII'
    warning : 'filename mismatch'
  - ns      : 'loc'
    id      : 'fdd000030'
    format  : 'PDF (Portable Document Format) Family'
    full    : 'PDF (Portable Document Format) Family'
    mime    : 'application/pdf'
    basis   : 'extension match pdf; byte match at 0, 4'
    warning :
---
filename : 'test_dir/test_dir/Q42591.mp3'
filesize : 3
modified : 2021-07-08T23:21:40+02:00
errors   :
md5      : c0f44879dc0d4eae7b3f0b3e801e373c
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match; possibilities based on extension are fmt/134'
  - ns      : 'tika'
    id      : 'audio/mpeg'
    format  : 'MPEG-1 Audio Layer 3'
    mime    : 'audio/mpeg'
    basis   : 'extension match mp3; byte match at 0, 3 (signature 12/12)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'audio/mpeg'
    format  : 'MP3 audio'
    mime    : 'audio/mpeg'
    basis   : 'extension match mp3; byte match at 0, 3 (signature 2/2)'
    warning :
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match; possibilities based on extension are fdd000052, fdd000053, fdd000105, fdd000111, fdd000256, fdd000275'
"""

if sys.version_info[0] == 3:
    PY3 = True
else:
    PY3 = False


def _StringIO():
    if PY3 is True:
        return io.StringIO()
    return io.BytesIO()


FIDDatabase = collections.namedtuple("FIDDatabase", "baseline cursor")


@pytest.fixture(scope="function")
def database(tmp_path):
    """Create a baseline database for each of the tests below.

    :returns: Yielded named tuple containing a baseline db object
        (GenerateBaselineDB) and database cursor object (sqlite3.Cursor)
    """
    basedb = GenerateBaselineDB("sf_test.yaml")

    dir_ = tmp_path
    sf_yaml = dir_ / "sf_test.yaml"
    sf_yaml.write_text(SIEGFRIED_YAML.strip())

    sf = SFYAMLHandler()
    sf.readSFYAML(str(sf_yaml))
    headers = sf.getHeaders()

    basedb.tooltype = "siegfried: {}".format(headers["siegfried"])
    basedb.dbname = "file::memory:?cache=shared"

    connection = FIDDatabase(basedb, basedb.dbsetup())

    yield connection


def test_create_db_md(database, tmp_path):
    basedb = database.baseline
    cursor = database.cursor
    dir_ = tmp_path
    droid_csv = dir_ / "sf_test.yaml"
    droid_csv.write_text(SIEGFRIED_YAML.strip())
    basedb.timestamp = "timestamp_value"
    basedb.createDBMD()
    res = cursor.execute("select * from DBMD").fetchall()
    assert res == [("timestamp_value", "False", "siegfried: 1.9.1")]


def test_sf_handler(database, tmp_path):
    """Ensure that SF data is written to sqlite as expected."""

    basedb = database.baseline
    cursor = database.cursor

    dir_ = tmp_path
    droid_csv = dir_ / "sf_test.yaml"
    droid_csv.write_text(SIEGFRIED_YAML.strip())

    sfloader = SFLoader(basedb)

    sfloader.create_sf_database(str(droid_csv), cursor)

    res = cursor.execute(
        "SELECT URI, FILE_PATH, DIR_NAME, NAME, SIZE, TYPE from FILEDATA where TYPE = 'Folder'"
    ).fetchall()

    assert len(res) == 3
    assert (
        res.sort()
        == [
            (None, "", "", "", 0, "Folder"),
            (None, "test_dir/test_dir", "test_dir/test_dir", "test_dir", 0, "Folder"),
            (None, "test_dir", "test_dir", "test_dir", 0, "Folder"),
        ].sort()
    )

    res = cursor.execute(
        "SELECT URI, URI_SCHEME, FILE_PATH, DIR_NAME, NAME, SIZE, TYPE, EXT, LAST_MODIFIED, YEAR, HASH, ERROR from FILEDATA where TYPE != 'Folder'"
    ).fetchall()

    assert len(res) == 4

    assert (
        res.sort()
        == [
            (
                "gz:file:///Q10287816.gz!",
                "gz",
                "Q10287816.gz",
                "",
                "Q10287816.gz",
                3,
                "Container",
                "gz",
                "2021-05-24T19:26:56+02:00",
                2021,
                "613ffd2ae0a8828aa573ce62bf2e30c3",
                "",
            ),
            (
                "file:///Q28205479🖤.info",
                "file",
                "Q28205479🖤.info",
                "",
                "Q28205479🖤.info",
                8,
                "File",
                "info",
                "2021-05-24T19:26:56+02:00",
                2021,
                "bf40928c61f376064b110ff59d604160",
                "",
            ),
            (
                "file:///test_dir/Q42332.pdf",
                "file",
                "test_dir/Q42332.pdf",
                "test_dir",
                "Q42332.pdf",
                4,
                "File",
                "pdf",
                "2021-07-08T23:21:40+02:00",
                2021,
                "bfa4b10a76324b166cfdad5e02a63730",
                "",
            ),
            (
                "file:///test_dir/test_dir/Q42591.mp3",
                "file",
                "test_dir/test_dir/Q42591.mp3",
                "test_dir/test_dir",
                "Q42591.mp3",
                3,
                "File",
                "mp3",
                "2021-07-08T23:21:40+02:00",
                2021,
                "c0f44879dc0d4eae7b3f0b3e801e373c",
                "",
            ),
        ].sort()
    )

    res = cursor.execute("select * from iddata").fetchall()
    assert len(res) == 16

    ns_id_query_1 = """
    SELECT FILEDATA.NAME,
        IDRESULTS.FILE_ID,
        IDDATA.METHOD,
        IDDATA.STATUS,
        IDDATA.ID,
        IDDATA.BASIS,
        IDDATA.MIME_TYPE,
        IDDATA.FORMAT_NAME,
        IDDATA.FORMAT_VERSION,
        IDDATA.EXTENSION_MISMATCH,
        IDDATA.WARNING,
        NSDATA.NS_NAME,
        NSDATA.NS_DETAILS
    FROM IDRESULTS
    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
    JOIN FILEDATA on FILEDATA.FILE_ID = IDRESULTS.FILE_ID
    JOIN NSDATA on IDDATA.NS_ID == NSDATA.NS_ID
    WHERE NSDATA.NS_ID == 1
    """

    res = cursor.execute(ns_id_query_1).fetchall()
    assert len(res) == 4
    assert (
        res.sort()
        == [
            (
                "Q10287816.gz",
                1,
                "Signature",
                None,
                "x-fmt/266",
                "extension match gz; byte match at 0, 3",
                "application/gzip",
                "GZIP Format",
                "",
                None,
                "None",
                "pronom",
                "DROID_SignatureFile_V97.xml; container-signature-20201001.xml",
            ),
            (
                "Q28205479🖤.info",
                2,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match; possibilities based on extension are fmt/1202",
                "pronom",
                "DROID_SignatureFile_V97.xml; container-signature-20201001.xml",
            ),
            (
                "Q42332.pdf",
                3,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "True",
                "extension mismatch; possibilities based on extension are fmt/14, fmt/15, fmt/16, fmt/17, fmt/18, fmt/19, fmt/20, fmt/95, fmt/144, fmt/145, fmt/146, fmt/147, fmt/148, fmt/157, fmt/158, fmt/276, fmt/354, fmt/476, fmt/477, fmt/478, fmt/479, fmt/480, fmt/481, fmt/488, fmt/489, fmt/490, fmt/491, fmt/492, fmt/493, fmt/558, fmt/559, fmt/560, fmt/561, fmt/562, fmt/563, fmt/564, fmt/565, fmt/1129",
                "pronom",
                "DROID_SignatureFile_V97.xml; container-signature-20201001.xml",
            ),
            (
                "Q42591.mp3",
                4,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match; possibilities based on extension are fmt/134",
                "pronom",
                "DROID_SignatureFile_V97.xml; container-signature-20201001.xml",
            ),
        ].sort()
    )

    ns_id_query_2 = """
        SELECT FILEDATA.NAME,
        IDRESULTS.FILE_ID,
        IDDATA.METHOD,
        IDDATA.STATUS,
        IDDATA.ID,
        IDDATA.BASIS,
        IDDATA.MIME_TYPE,
        IDDATA.FORMAT_NAME,
        IDDATA.FORMAT_VERSION,
        IDDATA.EXTENSION_MISMATCH,
        IDDATA.WARNING,
        NSDATA.NS_NAME,
        NSDATA.NS_DETAILS
    FROM IDRESULTS
    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
    JOIN FILEDATA on FILEDATA.FILE_ID = IDRESULTS.FILE_ID
    JOIN NSDATA on IDDATA.NS_ID == NSDATA.NS_ID
    WHERE NSDATA.NS_ID == 2
    """

    res = cursor.execute(ns_id_query_2).fetchall()
    assert len(res) == 4

    assert (
        res.sort()
        == [
            (
                "Q10287816.gz",
                1,
                "Signature",
                None,
                "application/gzip",
                "extension match gz; byte match at 0, 2 (signature 1/2); byte match at 0, 2 (signature 2/2)",
                "application/gzip",
                "Gzip Compressed Archive",
                "",
                None,
                "None",
                "tika",
                "tika-mimetypes.xml (1.24, 2020-04-17)",
            ),
            (
                "Q28205479🖤.info",
                2,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match",
                "tika",
                "tika-mimetypes.xml (1.24, 2020-04-17)",
            ),
            (
                "Q42332.pdf",
                3,
                "Extension",
                None,
                "application/pdf",
                "extension match pdf",
                "application/pdf",
                "Portable Document Format",
                "",
                "False",
                "match on filename only; byte/xml signatures for this format did not match",
                "tika",
                "tika-mimetypes.xml (1.24, 2020-04-17)",
            ),
            (
                "Q42591.mp3",
                4,
                "Signature",
                None,
                "audio/mpeg",
                "extension match mp3; byte match at 0, 3 (signature 12/12)",
                "audio/mpeg",
                "MPEG-1 Audio Layer 3",
                "",
                None,
                "None",
                "tika",
                "tika-mimetypes.xml (1.24, 2020-04-17)",
            ),
        ].sort()
    )

    ns_id_query_3 = """
    SELECT FILEDATA.NAME,
        IDRESULTS.FILE_ID,
        IDDATA.METHOD,
        IDDATA.STATUS,
        IDDATA.ID,
        IDDATA.BASIS,
        IDDATA.MIME_TYPE,
        IDDATA.FORMAT_NAME,
        IDDATA.FORMAT_VERSION,
        IDDATA.EXTENSION_MISMATCH,
        IDDATA.WARNING,
        NSDATA.NS_NAME,
        NSDATA.NS_DETAILS
    FROM IDRESULTS
    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
    JOIN FILEDATA on FILEDATA.FILE_ID = IDRESULTS.FILE_ID
    JOIN NSDATA on IDDATA.NS_ID == NSDATA.NS_ID
    WHERE NSDATA.NS_ID == 3
    """

    res = cursor.execute(ns_id_query_3).fetchall()
    assert len(res) == 4
    assert (
        res.sort()
        == [
            (
                "Q10287816.gz",
                1,
                "Signature",
                None,
                "application/gzip",
                "extension match gz; byte match at 0, 2",
                "application/gzip",
                "Gzip archive",
                "",
                None,
                "None",
                "freedesktop.org",
                "freedesktop.org.xml (2.0, 2020-06-05)",
            ),
            (
                "Q28205479🖤.info",
                2,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match",
                "freedesktop.org",
                "freedesktop.org.xml (2.0, 2020-06-05)",
            ),
            (
                "Q42332.pdf",
                3,
                "Signature",
                None,
                "text/x-tex",
                "byte match at 0, 1 (signature 1/2); text match ASCII",
                "text/x-tex",
                "TeX document",
                "",
                "False",
                "filename mismatch",
                "freedesktop.org",
                "freedesktop.org.xml (2.0, 2020-06-05)",
            ),
            (
                "Q42591.mp3",
                4,
                "Signature",
                None,
                "audio/mpeg",
                "extension match mp3; byte match at 0, 3 (signature 2/2)",
                "audio/mpeg",
                "MP3 audio",
                "",
                None,
                "None",
                "freedesktop.org",
                "freedesktop.org.xml (2.0, 2020-06-05)",
            ),
        ].sort()
    )

    ns_id_query_4 = """
    SELECT FILEDATA.NAME,
        IDRESULTS.FILE_ID,
        IDDATA.METHOD,
        IDDATA.STATUS,
        IDDATA.ID,
        IDDATA.BASIS,
        IDDATA.MIME_TYPE,
        IDDATA.FORMAT_NAME,
        IDDATA.FORMAT_VERSION,
        IDDATA.EXTENSION_MISMATCH,
        IDDATA.WARNING,
        NSDATA.NS_NAME,
        NSDATA.NS_DETAILS
    FROM IDRESULTS
    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
    JOIN FILEDATA on FILEDATA.FILE_ID = IDRESULTS.FILE_ID
    JOIN NSDATA on IDDATA.NS_ID == NSDATA.NS_ID
    WHERE NSDATA.NS_ID == 4
    """

    res = cursor.execute(ns_id_query_4).fetchall()
    assert len(res) == 4
    assert (
        res.sort()
        == [
            (
                "Q10287816.gz",
                1,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match",
                "loc",
                "fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)",
            ),
            (
                "Q28205479🖤.info",
                2,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match",
                "loc",
                "fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)",
            ),
            (
                "Q42332.pdf",
                3,
                "Signature",
                None,
                "fdd000030",
                "extension match pdf; byte match at 0, 4",
                "application/pdf",
                "PDF (Portable Document Format) Family",
                "",
                None,
                "None",
                "loc",
                "fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)",
            ),
            (
                "Q42591.mp3",
                4,
                "None",
                None,
                "UNKNOWN",
                "None",
                "none",
                "",
                "",
                "False",
                "no match; possibilities based on extension are fdd000052, fdd000053, fdd000105, fdd000111, fdd000256, fdd000275",
                "loc",
                "fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)",
            ),
        ].sort()
    )
