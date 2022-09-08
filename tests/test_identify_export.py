# -*- coding: utf-8 -*-

try:
    from sqlitefid.src.sqlitefid.libs.IdentifyExportClass import IdentifyExport
except ModuleNotFoundError:
    # Needed when imported as submodule via demystify.
    from src.demystify.sqlitefid.src.sqlitefid.libs.IdentifyExportClass import (
        IdentifyExport,
    )

DROID_CSV = """"ID","PARENT_ID","URI","FILE_PATH","NAME","METHOD","STATUS","SIZE","TYPE","EXT","LAST_MODIFIED","EXTENSION_MISMATCH","SHA1_HASH","FORMAT_COUNT","PUID","MIME_TYPE","FORMAT_NAME","FORMAT_VERSION"
"2","0","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus","🖤format-corpus",,"Done","","Folder",,"2014-02-28T15:49:11","false",,"",,"","",""
"3","2","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video","video",,"Done","","Folder",,"2014-02-28T15:48:47","false",,"",,"","",""
"""

DROID_CSV_BOM = """\xEF\xBB\xBF"ID","PARENT_ID","URI","FILE_PATH","NAME","METHOD","STATUS","SIZE","TYPE","EXT","LAST_MODIFIED","EXTENSION_MISMATCH","SHA1_HASH","FORMAT_COUNT","PUID","MIME_TYPE","FORMAT_NAME","FORMAT_VERSION"
"2","0","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus","🖤format-corpus",,"Done","","Folder",,"2014-02-28T15:49:11","false",,"",,"","",""
"3","2","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video","video",,"Done","","Folder",,"2014-02-28T15:48:47","false",,"",,"","",""
"""

SIEGFRIED_YAML = """---
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
"""

SIEGFRIED_CSV = """filename,filesize,modified,errors,namespace,id,format,version,mime,basis,warning,namespace,id,format,mime,basis,warning,namespace,id,format,mime,basis,warning,namespace,id,format,full,mime,basis,warning
data/dr.db,40960,2021-07-17T19:23:55+02:00,,pronom,fmt/729,SQLite Database File Format,3,application/x-sqlite3,"extension match db; byte match at 0, 16",,tika,application/x-sqlite3,,application/x-sqlite3,"byte match at 0, 16",,freedesktop.org,application/vnd.sqlite3,SQLite3 database,application/vnd.sqlite3,"byte match at 0, 15",filename mismatch,loc,fdd000461,"SQLite, Version 3","SQLite, Version 3",,"extension match db; byte match at 0, 16",
data/dr.py,4130,2021-07-17T19:19:09+02:00,,pronom,fmt/938,Python Script File,,,extension match py,match on extension only,tika,text/x-python,Python script,text/x-python,extension match py; text match ASCII,match on filename and text only; byte/xml signatures for this format did not match,freedesktop.org,text/x-python,Python script,text/x-python,extension match py,match on filename only; byte/xml signatures for this format did not match,loc,UNKNOWN,,,,,no match
"""

FIDO_CSV = """OK,155,fmt/729,"SQLite Database File Format","SQLite Database",249856,"data/opf-test-corpus-droid-analysis.db","application/x-sqlite3","signature"
OK,9,x-fmt/18,"Comma Separated Values","External",167823,"data/opf-test-corpus-droid-analysis.csv","text/csv","extension"
OK,6,fmt/729,"SQLite Database File Format","SQLite Database",40960,"data/dr.db","application/x-sqlite3","signature"
OK,6,x-fmt/18,"Comma Separated Values","External",10547,"data/fido.csv","text/csv","extension"
OK,6,fmt/818,"YAML","External",4677,"data/sf.yaml","None","extension"
OK,6,fmt/938,"Python Script File","External",4130,"data/dr.py","None","extension"
OK,6,fido-fmt/python,"Python script file","External",4130,"data/dr.py","None","extension"
OK,7,fmt/729,"SQLite Database File Format","SQLite Database",40960,"data/sf.db","application/x-sqlite3","signature"
KO,7,,,,5426,"diff",,"fail"
"""


def test_identify_export_sf(tmp_path):
    dir_ = tmp_path
    input_file = dir_ / "sf_test.yaml"
    input_file.write_text(SIEGFRIED_YAML.strip(), encoding="UTF-8")
    res = IdentifyExport().exportid(str(input_file))
    assert res == IdentifyExport().SFTYPE


def test_identify_export_sf_csv(tmp_path):
    dir_ = tmp_path
    input_file = dir_ / "sf_test.yaml"
    input_file.write_text(SIEGFRIED_CSV.strip(), encoding="UTF-8")
    res = IdentifyExport().exportid(str(input_file))
    assert res == IdentifyExport().SFCSVTYPE


def test_identify_export_droid(tmp_path):
    dir_ = tmp_path
    input_file = dir_ / "sf_test.yaml"
    input_file.write_text(DROID_CSV.strip(), encoding="UTF-8")
    res = IdentifyExport().exportid(str(input_file))
    assert res == IdentifyExport().DROIDTYPE


def test_identify_export_droid_bom(tmp_path):
    dir_ = tmp_path
    input_file = dir_ / "sf_test.yaml"
    input_file.write_text(DROID_CSV_BOM, encoding="utf8")
    res = IdentifyExport().exportid(str(input_file))
    assert res == IdentifyExport().DROIDTYPEBOM


def test_identify_export_fido(tmp_path):
    dir_ = tmp_path
    input_file = dir_ / "sf_test.yaml"
    input_file.write_text(FIDO_CSV.strip(), encoding="UTF-8")
    res = IdentifyExport().exportid(str(input_file))
    assert res == IdentifyExport().FIDOTYPE


def test_identify_export_unk(tmp_path):
    dir_ = tmp_path
    input_file = dir_ / "sf_test.yaml"
    input_file.write_text("ba5eba11,badf00d".strip(), encoding="UTF-8")
    res = IdentifyExport().exportid(str(input_file))
    assert res == IdentifyExport().UNKTYPE
