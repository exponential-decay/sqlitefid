# -*- coding: utf-8 -*-

# TODO: Come back to this...

from __future__ import absolute_import

import collections
import io
import sys

import pytest

from sqlitefid.libs import PyDateHandler, SFHandlerClass
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
filename : 'Q28205479.info'
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
filename : 'Q42332.pdf'
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
    warning : 'no match; possibilities based on extension are fmt/14, fmt/15, fmt/16, fmt/17, fmt/18, fmt/19, fmt/20, fmt/95, fmt/144, fmt/145, fmt/146, fmt/147, fmt/148, fmt/157, fmt/158, fmt/276, fmt/354, fmt/476, fmt/477, fmt/478, fmt/479, fmt/480, fmt/481, fmt/488, fmt/489, fmt/490, fmt/491, fmt/492, fmt/493, fmt/558, fmt/559, fmt/560, fmt/561, fmt/562, fmt/563, fmt/564, fmt/565, fmt/1129'
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
filename : 'Q42591.mp3'
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
    droid_csv = dir_ / "sf_test.yaml"
    droid_csv.write_text(SIEGFRIED_YAML.strip())

    sf = SFYAMLHandler()
    sf.readSFYAML(str(droid_csv))
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
    basedb.createDBMD(cursor)
    res = cursor.execute("select * from DBMD").fetchall()
    # assert res == [('timestamp_value', 'False', 'siegfried: 1.9.1')]


def test_sf_handler(database, tmp_path):
    """Ensure that SF data is written to sqlite as expected."""

    basedb = database.baseline
    cursor = database.cursor

    dir_ = tmp_path
    droid_csv = dir_ / "sf_test.yaml"
    droid_csv.write_text(SIEGFRIED_YAML.strip())

    sfloader = SFLoader(basedb)
    # sfloader.create_sf_database(str(droid_csv), cursor)

    # res = cursor.execute("select * from DBMD").fetchall()

    # print(res)

    # assert False
