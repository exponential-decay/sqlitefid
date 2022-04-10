# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import sys

try:
    from sqlitefid.src.sqlitefid.libs.CSVHandlerClass import GenericCSVHandler
except ModuleNotFoundError:
    # Needed when imported as submodule via demystify.
    from src.demystify.sqlitefid.src.sqlitefid.libs.CSVHandlerClass import (
        GenericCSVHandler,
    )

FIDO_CSV = """"info.status","info.time","info.puid","info.formatname","info.signaturename","info.filesize","info.filename","info.mimetype","info.matchtype"
OK,203,fmt/729,"SQLite Database File Format","SQLite Database",249856,"data/🖤opf-test-corpus-droid-analysis.db","application/x-sqlite3","signature"
OK,15,x-fmt/18,"Comma Separated Values","External",167823,"data/opf-test-corpus-droid-analysis.csv","text/csv","extension"
OK,14,x-fmt/18,"Comma Separated Values","External",0,"data/fido.csv","text/csv","extension"
OK,12,fmt/818,"YAML","External",35868,"data/sf.yaml","None","extension"
OK,11,fmt/729,"SQLite Database File Format","SQLite Database",61440,"data/sf.db","application/x-sqlite3","signature"
KO,9,,,,5426,"diff",,"fail"
OK,14,fmt/938,"Python Script File","External",0,"__init__.py","None","extension"
OK,14,fido-fmt/python,"Python script file","External",0,"__init__.py","None","extension"
OK,9,fmt/939,"Python Compiled File","PYC 2.7",159,"__init__.pyc","None","signature"""

PY3 = bool(sys.version_info[0] == 3)


def test_fido_handler_no_BOM():
    """Ensure that the return for a non-identified CSV is accurate. This
    is determined in the constructor.
    """
    fidocsvhandler = GenericCSVHandler(BOM=False)
    csv_in = io.StringIO()
    csv_in.write(FIDO_CSV)
    res = fidocsvhandler._csv_to_list(csv_in)
    assert res == []
    assert len(res) == 0


def test_fido_handler_BOM():
    """Ensure that we get sensible values out of a valid CSV."""
    fidocsvhandler = GenericCSVHandler(BOM=True)
    csv_in = io.StringIO()
    csv_in.write(FIDO_CSV)
    res = fidocsvhandler._csv_to_list(csv_in)
    assert len(res) == 9

    STATUS = "info.status"
    TIME = "info.time"
    PUID = "info.puid"
    FORMAT = "info.formatname"
    SIGNATURE = "info.signaturename"
    FILE_SIZE = "info.filesize"
    FILE_NAME = "info.filename"
    MIME = "info.mimetype"
    MATCH = "info.matchtype"

    assert res[0][STATUS] == "OK"
    assert res[8][STATUS] == "OK"

    assert res[0][TIME] == "203"
    assert res[8][TIME] == "9"

    assert res[0][PUID] == "fmt/729"
    assert res[8][PUID] == "fmt/939"

    assert res[0][FORMAT] == "SQLite Database File Format"
    assert res[8][FORMAT] == "Python Compiled File"

    assert res[0][SIGNATURE] == "SQLite Database"
    assert res[8][SIGNATURE] == "PYC 2.7"

    assert res[0][FILE_SIZE] == "249856"
    assert res[8][FILE_SIZE] == "159"

    assert res[0][FILE_NAME] == u"data/🖤opf-test-corpus-droid-analysis.db"
    assert res[8][FILE_NAME] == "__init__.pyc"

    assert res[0][MIME] == "application/x-sqlite3"
    assert res[8][MIME] == "None"

    assert res[0][MATCH] == "signature"
    assert res[8][MATCH] == "signature"
