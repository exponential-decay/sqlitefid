# -*- coding: utf-8 -*-

from __future__ import absolute_import

try:
    from sqlitefid.src.sqlitefid.libs.SFHandlerClass import IDResult, SFYAMLHandler
except ModuleNotFoundError:
    # Needed when imported as submodule via demystify.
    from src.demystify.sqlitefid.src.sqlitefid.libs.SFHandlerClass import (
        IDResult,
        SFYAMLHandler,
    )

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
filename : 'Q42591🖤.mp3'
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


def test_read_sf_yaml(tmp_path):
    """Ensure that the SF data above can be properly parsed and outputs
    sensible data.
    """

    dir_ = tmp_path
    sf_yaml = dir_ / "sf_test.yaml"
    sf_yaml.write_text(SIEGFRIED_YAML.strip(), encoding="UTF-8")

    sf = SFYAMLHandler()
    sf.read_sf_yaml(str(sf_yaml))

    assert sf.sectioncount == 5
    paths = ["{}".format(f["filename"]) for f in sf.files]

    res = list(set(paths))

    expected = ["Q10287816.gz", "Q28205479.info", "Q42332.pdf", "Q42591🖤.mp3"]

    res.sort()
    expected.sort()

    assert res == expected

    files = sf.sfdata["files"]

    assert len(sf.files) == 4
    assert len(files) == 4

    compare = files[0]
    assert compare.get("filename") == "Q10287816.gz"
    assert compare.get("filesize") == "3"
    assert compare.get("modified") == "2021-05-24T19:26:56+02:00"
    assert compare.get("errors") is None
    assert compare.get("md5") == "613ffd2ae0a8828aa573ce62bf2e30c3"
    assert compare.get("uri_scheme") == "file"

    compare_ids = compare.get("identification")

    ns = [item.ns for item in compare_ids]
    assert ns == ["pronom", "tika", "freedesktop.org", "loc"]

    id_ = [item.id for item in compare_ids]
    format_ = [item.format for item in compare_ids]
    mime = [item.mime for item in compare_ids]
    basis = [item.basis for item in compare_ids]
    warning = [item.warning for item in compare_ids]

    assert id_ == ["x-fmt/266", "application/gzip", "application/gzip", "UNKNOWN"]
    assert format_ == ["GZIP Format", "Gzip Compressed Archive", "Gzip archive", None]
    assert mime == ["application/gzip", "application/gzip", "application/gzip", None]
    assert basis == [
        "extension match gz; byte match at 0, 3",
        "extension match gz; byte match at 0, 2 (signature 1/2); byte match at 0, 2 (signature 2/2)",
        "extension match gz; byte match at 0, 2",
        None,
    ]
    assert warning == [None, None, None, "no match"]

    compare = files[2]
    assert compare.get("filename") == "Q42332.pdf"
    assert compare.get("filesize") == "4"
    assert compare.get("modified") == "2021-07-08T23:21:40+02:00"
    assert compare.get("errors") is None
    assert compare.get("md5") == "bfa4b10a76324b166cfdad5e02a63730"
    assert compare.get("uri_scheme") == "file"

    compare_ids = compare.get("identification")

    ns = [item.ns for item in compare_ids]
    assert ns == ["pronom", "tika", "freedesktop.org", "freedesktop.org", "loc"]

    id_ = [item.id for item in compare_ids]
    format_ = [item.format for item in compare_ids]
    mime = [item.mime for item in compare_ids]
    basis = [item.basis for item in compare_ids]
    warning = [item.warning for item in compare_ids]

    assert id_ == [
        "UNKNOWN",
        "application/pdf",
        "text/x-matlab",
        "text/x-tex",
        "fdd000030",
    ]
    assert format_ == [
        None,
        "Portable Document Format",
        "MATLAB file",
        "TeX document",
        "PDF (Portable Document Format) Family",
    ]
    assert mime == [
        None,
        "application/pdf",
        "text/x-matlab",
        "text/x-tex",
        "application/pdf",
    ]
    assert basis == [
        None,
        "extension match pdf",
        "byte match at 0, 1 (signature 1/3); text match ASCII",
        "byte match at 0, 1 (signature 1/2); text match ASCII",
        "extension match pdf; byte match at 0, 4",
    ]
    assert warning == [
        "no match; possibilities based on extension are fmt/14, fmt/15, fmt/16, fmt/17, fmt/18, fmt/19, fmt/20, fmt/95, fmt/144, fmt/145, fmt/146, fmt/147, fmt/148, fmt/157, fmt/158, fmt/276, fmt/354, fmt/476, fmt/477, fmt/478, fmt/479, fmt/480, fmt/481, fmt/488, fmt/489, fmt/490, fmt/491, fmt/492, fmt/493, fmt/558, fmt/559, fmt/560, fmt/561, fmt/562, fmt/563, fmt/564, fmt/565, fmt/1129",
        "match on filename only; byte/xml signatures for this format did not match",
        "filename mismatch",
        "filename mismatch",
        None,
    ]

    assert sf.sfdata["header"] == {
        "siegfried": "1.9.1",
        "scandate": "2021-07-17T22:11:59+02:00",
        "signature": "default.sig",
        "created": "2020-10-06T19:15:15+02:00",
        "id namespace 1": "pronom",
        "id details 1": "DROID_SignatureFile_V97.xml; container-signature-20201001.xml",
        "identifier count": 4,
        "id namespace 2": "tika",
        "id details 2": "tika-mimetypes.xml (1.24, 2020-04-17)",
        "id namespace 3": "freedesktop.org",
        "id details 3": "freedesktop.org.xml (2.0, 2020-06-05)",
        "id namespace 4": "loc",
        "id details 4": "fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)",
    }

    assert sf.hashtype == "md5"
    assert sf.identifiercount == 4
    assert sf.filecount == 4


SIEGFRIED_YAML_SKELETONS = """---
siegfried   : 1.9.1
scandate    : 2021-07-25T17:11:02+02:00
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
filename : 'fixtures/archive-types/container-example-four.tar.gz'
filesize : 726
modified : 2021-07-25T17:04:42+02:00
errors   :
md5      : c1a6723b6459b31642e2c84c670a90b4
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
    id      : 'fdd000286'
    format  : 'Spatial Data Transfer Standard'
    full    : 'Spatial Data Transfer Standard (SDTS) '
    mime    :
    basis   : 'glob match *.tar.gz'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar'
filesize : 20480
modified : 0001-01-01T00:00:00Z
errors   :
md5      : 2f63597327d2b33bf0121a57308bfdd2
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/265'
    format  : 'Tape Archive Format'
    version :
    mime    : 'application/x-tar'
    basis   : 'extension match tar; byte match at 0, 156'
    warning :
  - ns      : 'tika'
    id      : 'application/x-gtar'
    format  : 'GNU tar Compressed File Archive (GNU Tape Archive)'
    mime    : 'application/x-gtar'
    basis   : 'byte match at 257, 8 (signature 1/2)'
    warning : 'filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'application/x-tar'
    format  : 'Tar archive'
    mime    : 'application/x-tar'
    basis   : 'extension match tar; byte match at 257, 8 (signature 2/2)'
    warning :
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/cp437/año/cp437_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   : TEST-ONLY ERROR
md5      : a2530a3d32134654f0bef01cf252afd7
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/cp437/café/cp437_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : a2530a3d32134654f0bef01cf252afd7
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/big5/廣州/big5_encoded_dirs.txt'
filesize : 96
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 5d2cd701d4735045d108c762240002ec
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/emoji/chess-♕♖♗♘♙♚♛♜♝♞♟/utf-8_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 2e58bf86585ae31fcd7112f1beee358b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/emoji/hearts-❤💖💙💚💛💜💝/utf-8_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 2e58bf86585ae31fcd7112f1beee358b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/windows_1252/søster/cp1252_encoded_dirs.txt'
filesize : 98
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : b2d9653a8be9d9501789cdb55cf3c3f1
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/shift_jis/ぽっぷるメイル/shift-jis_encoded_dirs.txt'
filesize : 101
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 4071a2a321e8c429362483e98a80960b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/container-example-one.zip'
filesize : 3411
modified : 2021-07-25T17:02:27+02:00
errors   :
md5      : d70f5e3ee6c44c407abafbee446f1541
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/263'
    format  : 'ZIP Format'
    version :
    mime    : 'application/zip'
    basis   : 'extension match zip; container match with trigger and default extension'
    warning :
  - ns      : 'tika'
    id      : 'application/zip'
    format  : 'Compressed Archive File'
    mime    : 'application/zip'
    basis   : 'extension match zip; byte match at 0, 4 (signature 1/3)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/zip'
    format  : 'Zip archive'
    mime    : 'application/zip'
    basis   : 'extension match zip; byte match at 0, 4'
    warning :
  - ns      : 'loc'
    id      : 'fdd000354'
    format  : 'ZIP File Format (PKWARE)'
    full    : 'ZIP File Format (PKWARE)'
    mime    : 'application/zip'
    basis   : 'extension match zip; extension match zip; container match with trigger and default extension'
    warning : 'extension mismatch'
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/fmt-412-container-signature-id-1050.docx'
filesize : 49476
modified : 2020-11-30T03:21:34Z
errors   :
md5      : badba9781fbe694c1296dc642f70fd5d
matches  :
  - ns      : 'pronom'
    id      : 'fmt/412'
    format  : 'Microsoft Word for Windows'
    version : '2007 onwards'
    mime    : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    basis   : 'extension match docx; container name [Content_Types].xml with byte match at 16384, 188 (signature 3/3)'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    format  : 'Office Open XML Document'
    mime    : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    basis   : 'extension match docx; byte match at [[0 4] [30 19]] (signature 1/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    format  : 'Word 2007 document'
    mime    : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    basis   : 'extension match docx; byte match at 0, 4'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/fmt-631-container-signature-id-3080.potx'
filesize : 2276
modified : 2020-11-30T03:21:36Z
errors   :
md5      : fcd5800db9fcc15dbb2fb3f04e7627ac
matches  :
  - ns      : 'pronom'
    id      : 'fmt/631'
    format  : 'Microsoft PowerPoint Template'
    version : '2007'
    mime    : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    basis   : 'extension match potx; container name [Content_Types].xml with byte match at 2048, 92'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    format  : 'Office Open XML Presentation Template'
    mime    : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    basis   : 'extension match potx; byte match at [[0 4] [30 19]] (signature 1/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    format  : 'PowerPoint 2007 presentation template'
    mime    : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    basis   : 'extension match potx; byte match at 0, 4'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/fmt-999-container-signature-id-32010.kra'
filesize : 133
modified : 2020-11-30T03:21:36Z
errors   :
md5      : a1348398bc6ed5fda5c01034f0747e1a
matches  :
  - ns      : 'pronom'
    id      : 'fmt/999'
    format  : 'Krita Document Format'
    version :
    mime    : 'application/x-krita'
    basis   : 'extension match kra; container name mimetype with byte match at 0, 19'
    warning :
  - ns      : 'tika'
    id      : 'application/zip'
    format  : 'Compressed Archive File'
    mime    : 'application/zip'
    basis   : 'byte match at 0, 4 (signature 1/3)'
    warning : 'filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'application/x-krita'
    format  : 'Krita document'
    mime    : 'application/x-krita'
    basis   : 'extension match kra; byte match at [[0 4] [30 8] [38 19]] (signature 2/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/fmt-999-container-signature-id-32010.kra#mimetype'
filesize : 19
modified : 2020-11-29T21:21:36Z
errors   :
md5      : c1e1058caac602277d169573c7b13481
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; extension mismatch'
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; byte/xml signatures for this format did not match; filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; byte/xml signatures for this format did not match; filename mismatch'
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/fmt-443-container-signature-id-13020.vsd'
filesize : 2560
modified : 2020-11-30T03:21:36Z
errors   :
md5      : 318a3848eb0829c1f6e2e2ce0575fc33
matches  :
  - ns      : 'pronom'
    id      : 'fmt/443'
    format  : 'Microsoft Visio Drawing'
    version : '2003-2010'
    mime    : 'application/vnd.visio'
    basis   : 'extension match vsd; container name VisioDocument with byte match at 0, 27'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.visio'
    format  : 'Microsoft Visio Diagram'
    mime    : 'application/vnd.visio'
    basis   : 'extension match vsd; byte match at 0, 8'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.visio'
    format  : 'Microsoft Visio document'
    mime    : 'application/vnd.visio'
    basis   : 'extension match vsd; byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/fmt-853-container-signature-id-22520.dpp'
filesize : 4096
modified : 2020-11-30T03:21:36Z
errors   :
md5      : 1e729d44750c2ad9b59d069504edff22
matches  :
  - ns      : 'pronom'
    id      : 'fmt/853'
    format  : 'Serif DrawPlus Drawing'
    version : '5'
    mime    :
    basis   : 'extension match dpp; container name SummaryInformation with byte match at 512, 16'
    warning :
  - ns      : 'tika'
    id      : 'application/x-tika-msoffice'
    format  :
    mime    : 'application/x-tika-msoffice'
    basis   : 'byte match at 0, 8'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-ole-storage'
    format  : 'OLE2 compound document storage'
    mime    : 'application/x-ole-storage'
    basis   : 'byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/x-fmt-88-container-signature-id-3130.ppt'
filesize : 2560
modified : 2020-11-30T03:21:36Z
errors   :
md5      : 082ffda1984467ec4febe8dbe354e4ce
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/88'
    format  : 'Microsoft Powerpoint Presentation'
    version : '4.0'
    mime    : 'application/vnd.ms-powerpoint'
    basis   : 'extension match ppt; container name PP40 with name only'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.ms-powerpoint'
    format  : 'Microsoft Powerpoint Presentation'
    mime    : 'application/vnd.ms-powerpoint'
    basis   : 'extension match ppt; byte match at 0, 8 (signature 2/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-ole-storage'
    format  : 'OLE2 compound document storage'
    mime    : 'application/x-ole-storage'
    basis   : 'byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/archive-types/container-example-one.zip#container-objects/x-fmt-401-container-signature-id-23125.sda'
filesize : 2560
modified : 2020-11-30T03:21:36Z
errors   :
md5      : 254d1ed4e37720b38437661769339789
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/401'
    format  : 'StarOffice Draw'
    version : '5.x'
    mime    : 'application/vnd.stardivision.draw'
    basis   : 'extension match sda; container name CompObj with byte match at 64, 16 (signature 2/2)'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.stardivision.draw'
    format  :
    mime    : 'application/vnd.stardivision.draw'
    basis   : 'extension match sda; byte match at [[0 8] [2117 8]]'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-ole-storage'
    format  : 'OLE2 compound document storage'
    mime    : 'application/x-ole-storage'
    basis   : 'byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/archive-types/container-example-three.7z'
filesize : 1070
modified : 2021-07-25T17:02:52+02:00
errors   :
md5      : d9f27a9b0bf728ea90b5dce0f9650f7a
matches  :
  - ns      : 'pronom'
    id      : 'fmt/484'
    format  : '7Zip format'
    version :
    mime    :
    basis   : 'extension match 7z; byte match at 0, 6'
    warning :
  - ns      : 'tika'
    id      : 'application/x-7z-compressed'
    format  : '7-zip archive'
    mime    : 'application/x-7z-compressed'
    basis   : 'extension match 7z; byte match at [[0 2] [2 4]]'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-7z-compressed'
    format  : '7-zip archive'
    mime    : 'application/x-7z-compressed'
    basis   : 'extension match 7z; byte match at 0, 6'
    warning :
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/archive-types/container-example-two.tar.xz'
filesize : 348
modified : 2021-07-25T17:02:45+02:00
errors   :
md5      : 6f14b99d8bc93cd6dbb4e032018523ee
matches  :
  - ns      : 'pronom'
    id      : 'fmt/1098'
    format  : 'XZ File Format'
    version :
    mime    :
    basis   : 'extension match xz; byte match at [[0 6] [346 2]]'
    warning :
  - ns      : 'tika'
    id      : 'application/x-xz'
    format  :
    mime    : 'application/x-xz'
    basis   : 'extension match xz; byte match at 0, 6'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-xz'
    format  : 'XZ archive'
    mime    : 'application/x-xz'
    basis   : 'extension match xz; byte match at 0, 6'
    warning :
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/archive-types/fmt-1281-signature-id-1661.warc'
filesize : 280
modified : 2020-01-25T03:00:29+01:00
errors   :
md5      : 2102b96008741e77b4d2e31c7ea3fe70
matches  :
  - ns      : 'pronom'
    id      : 'fmt/1281'
    format  : 'WARC'
    version : '1.1'
    mime    : 'application/warc'
    basis   : 'extension match warc; byte match at 0, 280'
    warning :
  - ns      : 'tika'
    id      : 'application/warc'
    format  : 'WARC'
    mime    : 'application/warc'
    basis   : 'extension match warc; byte match at 0, 5'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'UNKNOWN'
    format  :
    mime    : 'UNKNOWN'
    basis   :
    warning : 'no match'
  - ns      : 'loc'
    id      : 'fdd000236'
    format  : 'WARC, Web ARChive file format'
    full    : 'WARC (Web ARChive) file format'
    mime    : 'application/warc'
    basis   : 'extension match warc; byte match at 0, 280'
    warning :
---
filename : 'fixtures/archive-types/fmt-1281-signature-id-1661.warc#'
filesize : 0
modified : 0001-01-01T00:00:00Z
errors   : 'error occurred during decompression: webarchive: error parsing WARC record'
matches  :
---
filename : 'fixtures/archive-types/fmt-289-signature-id-305.warc'
filesize : 832
modified : 2020-01-25T03:00:31+01:00
errors   :
md5      : 83becbc69c96130d249a82105b9f428a
matches  :
  - ns      : 'pronom'
    id      : 'fmt/289'
    format  : 'WARC'
    version :
    mime    : 'application/warc'
    basis   : 'extension match warc; byte match at 0, 19'
    warning :
  - ns      : 'tika'
    id      : 'application/warc'
    format  : 'WARC'
    mime    : 'application/warc'
    basis   : 'extension match warc; byte match at 0, 5'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'UNKNOWN'
    format  :
    mime    : 'UNKNOWN'
    basis   :
    warning : 'no match'
  - ns      : 'loc'
    id      : 'fdd000236'
    format  : 'WARC, Web ARChive file format'
    full    : 'WARC (Web ARChive) file format'
    mime    : 'application/warc'
    basis   : 'extension match warc; byte match at 0, 19'
    warning :
---
filename : 'fixtures/archive-types/fmt-289-signature-id-305.warc#'
filesize : 0
modified : 0001-01-01T00:00:00Z
errors   : 'error occurred during decompression: parsing time "" as "2006-01-02T15:04:05Z07:00": cannot parse "" as "2006"'
matches  :
---
filename : 'fixtures/archive-types/fmt-410-signature-id-580.arc'
filesize : 205
modified : 2020-11-30T03:25:18+01:00
errors   : 'failed to decompress, got: webarchive: invalid ARC version block'
md5      : 8e910e85838fd4cd7fc8e70159d198a0
matches  :
  - ns      : 'pronom'
    id      : 'fmt/410'
    format  : 'Internet Archive'
    version : '1.1'
    mime    :
    basis   : 'extension match arc; byte match at [[0 129] [149 56]]'
    warning :
  - ns      : 'tika'
    id      : 'application/x-internet-archive'
    format  : 'ARC'
    mime    : 'application/x-internet-archive'
    basis   : 'extension match arc; byte match at 0, 11'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'UNKNOWN'
    format  :
    mime    : 'UNKNOWN'
    basis   :
    warning : 'no match'
  - ns      : 'loc'
    id      : 'fdd000235'
    format  : 'ARC_IA, Internet Archive ARC file format'
    full    : 'ARC_IA, Internet Archive ARC file format.'
    mime    :
    basis   : 'extension match arc'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/x-fmt-219-signature-id-525.arc'
filesize : 205
modified : 2020-01-25T03:00:31+01:00
errors   : 'failed to decompress, got: webarchive: invalid ARC version block'
md5      : bb430b824544bc4250461f3c61de3be8
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/219'
    format  : 'Internet Archive'
    version : '1.0'
    mime    : 'application/x-internet-archive'
    basis   : 'extension match arc; byte match at [[0 129] [149 56]]'
    warning :
  - ns      : 'tika'
    id      : 'application/x-internet-archive'
    format  : 'ARC'
    mime    : 'application/x-internet-archive'
    basis   : 'extension match arc; byte match at 0, 11'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'UNKNOWN'
    format  :
    mime    : 'UNKNOWN'
    basis   :
    warning : 'no match'
  - ns      : 'loc'
    id      : 'fdd000235'
    format  : 'ARC_IA, Internet Archive ARC file format'
    full    : 'ARC_IA, Internet Archive ARC file format.'
    mime    :
    basis   : 'extension match arc'
    warning : 'match on extension only'
---
filename : 'fixtures/archive-types/x-fmt-263-signature-id-200.zip'
filesize : 65572
modified : 2020-11-30T03:25:20+01:00
errors   :
md5      : ae7688484c891d3c27e65367988ef270
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/263'
    format  : 'ZIP Format'
    version :
    mime    : 'application/zip'
    basis   : 'extension match zip; container match with trigger and default extension'
    warning :
  - ns      : 'tika'
    id      : 'application/zip'
    format  : 'Compressed Archive File'
    mime    : 'application/zip'
    basis   : 'extension match zip; byte match at 0, 4 (signature 1/3)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/zip'
    format  : 'Zip archive'
    mime    : 'application/zip'
    basis   : 'extension match zip; byte match at 0, 4'
    warning :
  - ns      : 'loc'
    id      : 'fdd000354'
    format  : 'ZIP File Format (PKWARE)'
    full    : 'ZIP File Format (PKWARE)'
    mime    : 'application/zip'
    basis   : 'extension match zip; extension match zip; container match with trigger and default extension'
    warning : 'extension mismatch'
---
filename : 'fixtures/archive-types/x-fmt-266-signature-id-201.gz'
filesize : 3
modified : 2020-11-30T03:25:20+01:00
errors   : 'failed to decompress, got: EOF'
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
filename : 'fixtures/container-objects/fmt-412-container-signature-id-1050.docx'
filesize : 49476
modified : 2020-11-30T03:21:35+01:00
errors   :
md5      : badba9781fbe694c1296dc642f70fd5d
matches  :
  - ns      : 'pronom'
    id      : 'fmt/412'
    format  : 'Microsoft Word for Windows'
    version : '2007 onwards'
    mime    : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    basis   : 'extension match docx; container name [Content_Types].xml with byte match at 16384, 188 (signature 3/3)'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    format  : 'Office Open XML Document'
    mime    : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    basis   : 'extension match docx; byte match at [[0 4] [30 19]] (signature 1/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    format  : 'Word 2007 document'
    mime    : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    basis   : 'extension match docx; byte match at 0, 4'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/container-objects/fmt-443-container-signature-id-13020.vsd'
filesize : 2560
modified : 2020-11-30T03:21:36+01:00
errors   :
md5      : 318a3848eb0829c1f6e2e2ce0575fc33
matches  :
  - ns      : 'pronom'
    id      : 'fmt/443'
    format  : 'Microsoft Visio Drawing'
    version : '2003-2010'
    mime    : 'application/vnd.visio'
    basis   : 'extension match vsd; container name VisioDocument with byte match at 0, 27'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.visio'
    format  : 'Microsoft Visio Diagram'
    mime    : 'application/vnd.visio'
    basis   : 'extension match vsd; byte match at 0, 8'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.visio'
    format  : 'Microsoft Visio document'
    mime    : 'application/vnd.visio'
    basis   : 'extension match vsd; byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/container-objects/fmt-631-container-signature-id-3080.potx'
filesize : 2276
modified : 2020-11-30T03:21:36+01:00
errors   :
md5      : fcd5800db9fcc15dbb2fb3f04e7627ac
matches  :
  - ns      : 'pronom'
    id      : 'fmt/631'
    format  : 'Microsoft PowerPoint Template'
    version : '2007'
    mime    : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    basis   : 'extension match potx; container name [Content_Types].xml with byte match at 2048, 92'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    format  : 'Office Open XML Presentation Template'
    mime    : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    basis   : 'extension match potx; byte match at [[0 4] [30 19]] (signature 1/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    format  : 'PowerPoint 2007 presentation template'
    mime    : 'application/vnd.openxmlformats-officedocument.presentationml.template'
    basis   : 'extension match potx; byte match at 0, 4'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/container-objects/fmt-853-container-signature-id-22520.dpp'
filesize : 4096
modified : 2020-11-30T03:21:37+01:00
errors   :
md5      : 1e729d44750c2ad9b59d069504edff22
matches  :
  - ns      : 'pronom'
    id      : 'fmt/853'
    format  : 'Serif DrawPlus Drawing'
    version : '5'
    mime    :
    basis   : 'extension match dpp; container name SummaryInformation with byte match at 512, 16'
    warning :
  - ns      : 'tika'
    id      : 'application/x-tika-msoffice'
    format  :
    mime    : 'application/x-tika-msoffice'
    basis   : 'byte match at 0, 8'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-ole-storage'
    format  : 'OLE2 compound document storage'
    mime    : 'application/x-ole-storage'
    basis   : 'byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/container-objects/fmt-999-container-signature-id-32010.kra'
filesize : 133
modified : 2020-11-30T03:21:37+01:00
errors   :
md5      : a1348398bc6ed5fda5c01034f0747e1a
matches  :
  - ns      : 'pronom'
    id      : 'fmt/999'
    format  : 'Krita Document Format'
    version :
    mime    : 'application/x-krita'
    basis   : 'extension match kra; container name mimetype with byte match at 0, 19'
    warning :
  - ns      : 'tika'
    id      : 'application/zip'
    format  : 'Compressed Archive File'
    mime    : 'application/zip'
    basis   : 'byte match at 0, 4 (signature 1/3)'
    warning : 'filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'application/x-krita'
    format  : 'Krita document'
    mime    : 'application/x-krita'
    basis   : 'extension match kra; byte match at [[0 4] [30 8] [38 19]] (signature 2/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/container-objects/fmt-999-container-signature-id-32010.kra#mimetype'
filesize : 19
modified : 2020-11-29T21:21:36Z
errors   :
md5      : c1e1058caac602277d169573c7b13481
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; extension mismatch'
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; byte/xml signatures for this format did not match; filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; byte/xml signatures for this format did not match; filename mismatch'
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/container-objects/x-fmt-401-container-signature-id-23125.sda'
filesize : 2560
modified : 2020-11-30T03:21:37+01:00
errors   :
md5      : 254d1ed4e37720b38437661769339789
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/401'
    format  : 'StarOffice Draw'
    version : '5.x'
    mime    : 'application/vnd.stardivision.draw'
    basis   : 'extension match sda; container name CompObj with byte match at 64, 16 (signature 2/2)'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.stardivision.draw'
    format  :
    mime    : 'application/vnd.stardivision.draw'
    basis   : 'extension match sda; byte match at [[0 8] [2117 8]]'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-ole-storage'
    format  : 'OLE2 compound document storage'
    mime    : 'application/x-ole-storage'
    basis   : 'byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/container-objects/x-fmt-88-container-signature-id-3130.ppt'
filesize : 2560
modified : 2020-11-30T03:21:36+01:00
errors   :
md5      : 082ffda1984467ec4febe8dbe354e4ce
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/88'
    format  : 'Microsoft Powerpoint Presentation'
    version : '4.0'
    mime    : 'application/vnd.ms-powerpoint'
    basis   : 'extension match ppt; container name PP40 with name only'
    warning :
  - ns      : 'tika'
    id      : 'application/vnd.ms-powerpoint'
    format  : 'Microsoft Powerpoint Presentation'
    mime    : 'application/vnd.ms-powerpoint'
    basis   : 'extension match ppt; byte match at 0, 8 (signature 2/2)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'application/x-ole-storage'
    format  : 'OLE2 compound document storage'
    mime    : 'application/x-ole-storage'
    basis   : 'byte match at 0, 4 (signature 2/2); byte match at 0, 8 (signature 1/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000380'
    format  : 'Microsoft Compound File Binary File Format, Version 3'
    full    : 'Microsoft Compound File Binary File Format, Version 3'
    mime    :
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'fixtures/dirs_with_various_encodings/big5/廣州/big5_encoded_dirs.txt'
filesize : 96
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 5d2cd701d4735045d108c762240002ec
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/dirs_with_various_encodings/cp437/año/cp437_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : a2530a3d32134654f0bef01cf252afd7
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/dirs_with_various_encodings/cp437/café/cp437_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : a2530a3d32134654f0bef01cf252afd7
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/dirs_with_various_encodings/emoji/chess-♕♖♗♘♙♚♛♜♝♞♟/utf-8_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 2e58bf86585ae31fcd7112f1beee358b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/dirs_with_various_encodings/emoji/hearts-❤💖💙💚💛💜💝/utf-8_encoded_dirs.txt'
filesize : 97
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 2e58bf86585ae31fcd7112f1beee358b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/dirs_with_various_encodings/shift_jis/ぽっぷるメイル/shift-jis_encoded_dirs.txt'
filesize : 101
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : 4071a2a321e8c429362483e98a80960b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/dirs_with_various_encodings/windows_1252/søster/cp1252_encoded_dirs.txt'
filesize : 98
modified : 2020-06-22T19:38:22+02:00
errors   :
md5      : b2d9653a8be9d9501789cdb55cf3c3f1
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/files_with_various_encodings/emoji/chess-♕♖♗♘♙♚♛♜♝♞♟.txt'
filesize : 54
modified : 2020-06-22T19:38:21+02:00
errors   :
md5      : 0653e4959fa11f1ffce974b092efdd00
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/files_with_various_encodings/emoji/hearts-❤💖💙💚💛💜💝.txt'
filesize : 54
modified : 2020-06-22T19:38:21+02:00
errors   :
md5      : 0653e4959fa11f1ffce974b092efdd00
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning :
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'extension match txt; text match ASCII'
    warning : 'match on filename and text only; byte/xml signatures for this format did not match'
  - ns      : 'loc'
    id      : 'fdd000284'
    format  : 'ESRI ArcInfo Coverage'
    full    : 'ESRI ArcInfo Coverage'
    mime    :
    basis   : 'extension match txt'
    warning : 'match on extension only'
---
filename : 'fixtures/files_with_various_encodings/windows_1252/søster'
filesize : 55
modified : 2020-06-22T19:38:21+02:00
errors   :
md5      : da53eb270f3ce333e91f0d742adb0e24
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/111'
    format  : 'Plain Text File'
    version :
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; extension mismatch'
  - ns      : 'tika'
    id      : 'text/plain'
    format  :
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; byte/xml signatures for this format did not match; filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'text/plain'
    format  : 'plain text document'
    mime    : 'text/plain'
    basis   : 'text match ASCII'
    warning : 'match on text only; byte/xml signatures for this format did not match; filename mismatch'
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/animation.mov'
filesize : 1020209
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 7c845af9f5aa44be9590067758760a8c
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/apple-intermediate-codec.mov'
filesize : 319539
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 627fba96fbcaaa50d02f0d33cc3fb361
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/apple-prores-422.mov'
filesize : 564775
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 44e2f4eee4b062179db7d7eb694fb453
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dv-dvchd-ntsc-interlaced.mov'
filesize : 3001365
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 38d98389ff914344fa1074fc023c4494
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dv-dvchd-ntsc-progressive.mov'
filesize : 3001365
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 7123e7a33c9026324b553a434efadff3
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dv-pal-interlaced.mov'
filesize : 3601749
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 042cc2c0db16b60eb6f7eddd3dc118ac
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-hd-1080i50.mov'
filesize : 14401365
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 23279d7284c946767602072fc2f48a94
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-hd-1080i60.mov'
filesize : 12001365
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 033dfe66d1fa70a827007bed284d703b
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-hd-1080p25.mov'
filesize : 14401365
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a461c14eaf56c34477d646b0c3dc27ad
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-hd-1080p30.mov'
filesize : 12001365
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 0812184da1c85eae2f27bf5763277f3f
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-hd-720p50.mov'
filesize : 7201357
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a02f51b2d4340d3a650822b980010e41
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-hd-720p60.mov'
filesize : 6001485
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 75aeb7ffd2f1bf156f3fc355e589dae5
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-pal-interlaced.mov'
filesize : 3601749
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a5a350848af8d4056426aecc0077827c
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro-pal-progressive.mov'
filesize : 3601749
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a005a1ccd6997d0fffce6e9b161c4324
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro50-pal-interlaced.mov'
filesize : 7203433
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a4f33762d95651446e84c32e181e19c2
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/dvcpro50-pal-progressive.mov'
filesize : 7203433
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 6e26144f9b0580f884114d4da7a43e74
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/jpeg2000.mov'
filesize : 383905
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : bfff74cd3b020f281512829cca291063
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/photo-jpeg.mov'
filesize : 575929
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 0a67f830ab31a6d0a7b213e2273593a6
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd-1080p25.mov'
filesize : 694863
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : ccf4aebd86a2d81ae9ad2544e90abe52
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd-1080p30.mov'
filesize : 583993
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a1ea1b20fca6e65e48454c7793f4be2a
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd422-1080i50.mov'
filesize : 6251203
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 5281f430744681ce4d5667aec30021df
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd422-1080i60.mov'
filesize : 5215055
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 7b8c215c05e46eaa68b1477cd0ca0082
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd422-720p30.mov'
filesize : 5215055
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : a9ef25f92febe9f2cd3b895fe38818af
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd422-720p50.mov'
filesize : 3125967
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : b4c6a638f5463139c80bdd63a5aedf53
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/opf-format-corpus/video/Quicktime/xdcam-hd422-720p60.mov'
filesize : 2607739
modified : 2019-01-30T11:48:01+01:00
errors   :
md5      : 2251ba9a965f591e34ca061d4d707ff4
matches  :
  - ns      : 'pronom'
    id      : 'x-fmt/384'
    format  : 'Quicktime'
    version :
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 8 (signature 4/8)'
    warning :
  - ns      : 'tika'
    id      : 'video/quicktime'
    format  : 'QuickTime Video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 4 (signature 6/7)'
    warning :
  - ns      : 'freedesktop.org'
    id      : 'video/quicktime'
    format  : 'QuickTime video'
    mime    : 'video/quicktime'
    basis   : 'extension match mov; byte match at 4, 6 (signature 4/4)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000254'
    format  : 'AMR, Adaptive Multi-Rate Speech Codec'
    full    : 'AMR, Adaptive Multi-Rate Speech Codec'
    mime    : 'audio/AMR'
    basis   : 'byte match at 0, 3 (signature 2/2)'
    warning : 'extension mismatch'
---
filename : 'fixtures/possible-multiples/fmt-140-signature-id-207.odb'
filesize : 105
modified : 2020-01-25T03:00:27+01:00
errors   : 'failed to decompress, got: zip: not a valid zip file'
md5      : 434240eb119cf0564eb3ab13b7b8cf3f
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match; possibilities based on extension are fmt/140, fmt/424, fmt/444'
  - ns      : 'tika'
    id      : 'application/zip'
    format  : 'Compressed Archive File'
    mime    : 'application/zip'
    basis   : 'byte match at 0, 4 (signature 1/3)'
    warning : 'filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'application/vnd.oasis.opendocument.database'
    format  : 'ODB database'
    mime    : 'application/vnd.oasis.opendocument.database'
    basis   : 'extension match odb; byte match at 0, 4 (signature 2/2)'
    warning :
  - ns      : 'loc'
    id      : 'fdd000514'
    format  : 'Microsoft XML Paper Specification, (XPS)'
    full    : 'Microsoft XML Paper Specification, (XPS)'
    mime    : 'application/vnd.ms-xpsdocument'
    basis   : 'byte match at 0, 4'
    warning : 'extension mismatch'
---
filename : 'fixtures/possible-multiples/fmt-641-signature-id-970.erf'
filesize : 348
modified : 2020-01-25T03:00:30+01:00
errors   :
md5      : 4425a5f4b078e9b716969a856c1015f6
matches  :
  - ns      : 'pronom'
    id      : 'fmt/641'
    format  : 'Epson Raw Image Format'
    version :
    mime    :
    basis   : 'extension match erf; byte match at 0, 348'
    warning :
  - ns      : 'tika'
    id      : 'image/tiff'
    format  : 'Tagged Image File Format'
    mime    : 'image/tiff'
    basis   : 'byte match at 0, 4 (signature 1/3)'
    warning : 'filename mismatch'
  - ns      : 'freedesktop.org'
    id      : 'image/tiff'
    format  : 'TIFF image'
    mime    : 'image/tiff'
    basis   : 'byte match at 0, 4 (signature 1/2)'
    warning : 'filename mismatch'
  - ns      : 'loc'
    id      : 'fdd000022'
    format  : 'TIFF, Revision 6.0'
    full    : 'TIFF (Tagged Image File Format), Revision 6.0'
    mime    : 'image/tiff'
    basis   : 'byte match at 0, 4 (signature 3/5)'
    warning : 'extension mismatch'
---
filename : 'fixtures/synthetically_unknown_formats/README.md'
filesize : 1257
modified : 2020-01-15T20:17:02+01:00
errors   :
md5      : cdde5e89dcb9b17e11780acd06bae840
matches  :
  - ns      : 'pronom'
    id      : 'fmt/1149'
    format  : 'Markdown'
    version :
    mime    : 'text/markdown'
    basis   : 'extension match md'
    warning : 'match on extension only'
  - ns      : 'tika'
    id      : 'text/x-web-markdown'
    format  : 'Markdown source code'
    mime    : 'text/x-web-markdown'
    basis   : 'extension match md; text match ASCII'
    warning : 'match on filename and text only'
  - ns      : 'freedesktop.org'
    id      : 'text/markdown'
    format  : 'Markdown document'
    mime    : 'text/markdown'
    basis   : 'extension match md; text match ASCII'
    warning : 'match on filename and text only'
  - ns      : 'loc'
    id      : 'UNKNOWN'
    format  :
    full    :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'fixtures/synthetically_unknown_formats/baseball.format'
filesize : 52
modified : 2020-01-15T20:17:02+01:00
errors   :
md5      : 1a6c6441a82f19ffcb604e02a57d0bf4
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match'
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
filename : 'fixtures/synthetically_unknown_formats/caboose.format'
filesize : 52
modified : 2020-01-15T20:17:02+01:00
errors   :
md5      : 8757e8a7cea74eab1510d84f89f78bed
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match'
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
filename : 'fixtures/synthetically_unknown_formats/cassette.format'
filesize : 52
modified : 2020-01-15T20:17:02+01:00
errors   :
md5      : d81cfa5d4fd884ee6f5631229bbf4a3e
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match'
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
filename : 'fixtures/synthetically_unknown_formats/debateable.format'
filesize : 52
modified : 2020-01-15T20:17:02+01:00
errors   :
md5      : 4c1a6c57613aaf221e4d5ea9b4920c6d
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match'
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
filename : 'fixtures/synthetically_unknown_formats/looseleaf.format'
filesize : 52
modified : 2020-01-15T20:17:02+01:00
errors   :
md5      : 34d8c18805e54a3cdffd6d4f018ee9d4
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match'
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
"""


def test_read_sf_yaml_skeletons(tmp_path):
    """Ensure that the SF data above can be properly parsed and outputs
    sensible data.

    From the DROID notes;

    In comparison to the SF output for the same dataset we have some
    divergence, in this set, we have:

       * container-example-four.tar where sf has: container-example-four.tar.gz#container-example-four.tar
         nb. DROID writes this as: container-example-four.tar.gz!/container-example-four.tar

       * sf is also able to scan: fmt-999-container-signature-id-32010.kra#mimetype where
         DROID cannot.

       SF can access two more: fmt-999-container-signature-id-32010.kra#mimetype and
       so its count is 77 vs. DROID's 75.
    """

    dir_ = tmp_path
    sf_yaml = dir_ / "sf_test.yaml"
    sf_yaml.write_text(SIEGFRIED_YAML_SKELETONS.strip(), encoding="UTF-8")

    sf = SFYAMLHandler()
    sf.read_sf_yaml(str(sf_yaml))

    # Access files in processed data to verify integrity.
    files = sf.sfdata["files"]

    # 77 files in the extract minus two with complete read errors.
    assert len(sf.files) == 77
    assert len(files) == 77

    "fixtures/archive-types/fmt-1281-signature-id-1661.warc#"
    "fixtures/archive-types/fmt-289-signature-id-305.warc#"

    for file_ in files:
        assert file_["filename"] != "fmt-1281-signature-id-1661.warc#"
        assert file_["filename"] != "fmt-289-signature-id-305.warc#"

    # 77 file sections + 2 errors + 1 header.
    assert sf.sectioncount == 80

    # 4 namespaces.
    assert sf.identifiercount == 4

    # List identifiers.
    assert sf.identifiers == ["pronom", "tika", "freedesktop.org", "loc"]

    # Check errors.
    errs = [err.get("errors") for err in sf.files if err.get("errors") is not None]

    assert errs == [
        "TEST-ONLY ERROR",
        "failed to decompress, got: webarchive: invalid ARC version block",
        "failed to decompress, got: webarchive: invalid ARC version block",
        "failed to decompress, got: EOF",
        "failed to decompress, got: zip: not a valid zip file",
    ]

    assert sf.hashtype == "md5"

    assert sf.sfdata["header"] == {
        "siegfried": "1.9.1",
        "scandate": "2021-07-25T17:11:02+02:00",
        "signature": "default.sig",
        "created": "2020-10-06T19:15:15+02:00",
        "id namespace 1": "pronom",
        "id details 1": "DROID_SignatureFile_V97.xml; container-signature-20201001.xml",
        "identifier count": 4,
        "id namespace 2": "tika",
        "id details 2": "tika-mimetypes.xml (1.24, 2020-04-17)",
        "id namespace 3": "freedesktop.org",
        "id details 3": "freedesktop.org.xml (2.0, 2020-06-05)",
        "id namespace 4": "loc",
        "id details 4": "fddXML.zip (2020-09-02, DROID_SignatureFile_V97.xml, container-signature-20201001.xml)",
    }

    assert (
        files[1].get("filename")
        == "fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar"
    )
    assert files[1].get("filesize") == "20480"
    assert files[1].get("modified") == "0001-01-01T00:00:00Z"
    assert files[1].get("errors") is None
    assert files[1].get("md5") == "2f63597327d2b33bf0121a57308bfdd2"
    assert files[1].get("type") == "Container"
    assert files[1].get("container_type") == "tar"
    assert files[1].get("uri_scheme") == "container"

    identification = files[1].get("identification")

    id_0 = IDResult()
    id_1 = IDResult()
    id_2 = IDResult()
    id_3 = IDResult()

    id_0.ns = "pronom"
    id_0.id = "x-fmt/265"
    id_0.format = "Tape Archive Format"
    id_0.version = None
    id_0.mime = "application/x-tar"
    id_0.method = "Signature"
    id_0.basis = "extension match tar; byte match at 0, 156"
    id_0.warning = None
    id_0.mismatch = False
    id_0.status = None

    id_1.ns = "tika"
    id_1.id = "application/x-gtar"
    id_1.format = "GNU tar Compressed File Archive (GNU Tape Archive)"
    id_1.version = None
    id_1.mime = "application/x-gtar"
    id_1.method = "Signature"
    id_1.basis = "byte match at 257, 8 (signature 1/2)"
    id_1.warning = "filename mismatch"
    id_1.mismatch = False
    id_1.status = None

    id_2.ns = "freedesktop.org"
    id_2.id = "application/x-tar"
    id_2.format = "Tar archive"
    id_2.version = None
    id_2.mime = "application/x-tar"
    id_2.method = "Signature"
    id_2.basis = "extension match tar; byte match at 257, 8 (signature 2/2)"
    id_2.warning = None
    id_2.mismatch = False
    id_2.status = None

    id_3.ns = "loc"
    id_3.id = "UNKNOWN"
    id_3.format = None
    id_3.version = None
    id_3.mime = None
    id_3.method = None
    id_3.basis = None
    id_3.warning = "no match"
    id_3.mismatch = False
    id_3.status = None

    assert id_0 == identification[0]
    assert id_1 == identification[1]
    assert id_2 == identification[2]
    assert id_3 == identification[3]

    assert (
        files[2].get("filename")
        == "fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/cp437/año/cp437_encoded_dirs.txt"
    )
    assert files[2].get("filesize") == "97"
    assert files[2].get("modified") == "2020-06-22T19:38:22+02:00"
    assert files[2].get("errors") == "TEST-ONLY ERROR", files[2].get("errors")
    assert files[2].get("md5") == "a2530a3d32134654f0bef01cf252afd7"
    assert files[2].get("type") == "File"
    assert files[2].get("container_type") is None
    assert files[2].get("uri_scheme") == "container"

    identification = files[2].get("identification")

    id_0.ns = "pronom"
    id_0.id = "x-fmt/111"
    id_0.format = "Plain Text File"
    id_0.version = None
    id_0.mime = "text/plain"
    id_0.method = "Text"
    id_0.basis = "extension match txt; text match ASCII"
    id_0.warning = None
    id_0.mismatch = False
    id_0.status = None

    id_1.ns = "tika"
    id_1.id = "text/plain"
    id_1.format = None
    id_1.version = None
    id_1.mime = "text/plain"
    id_1.method = "Text"
    id_1.basis = "extension match txt; text match ASCII"
    id_1.warning = "match on filename and text only; byte/xml signatures for this format did not match"
    id_1.mismatch = False
    id_1.status = None

    id_2.ns = "freedesktop.org"
    id_2.id = "text/plain"
    id_2.format = "plain text document"
    id_2.version = None
    id_2.mime = "application/x-tar"
    id_2.method = "Text"
    id_2.basis = "extension match txt; text match ASCII"
    id_2.warning = "match on filename and text only; byte/xml signatures for this format did not match"
    id_2.mismatch = False
    id_2.status = None

    id_3.ns = "loc"
    id_3.id = "fdd000284"
    id_3.format = "ESRI ArcInfo Coverage"
    id_3.version = None
    id_3.mime = None
    id_3.method = "Extension"
    id_3.basis = "extension match txt"
    id_3.warning = "match on extension only"
    id_3.mismatch = False
    id_3.status = None


BAD_YAML = """---
filename : 'Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon
'
filesize : 0
modified : 1996-11-14T13:29:32Z
errors   : 'empty source'
matches  :
  - ns      : 'pronom'
    id      : 'UNKNOWN'
    format  :
    version :
    mime    :
    basis   :
    warning : 'no match'
---
filename : 'Mac RF Test.zip#__MACOSX\\Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\._Icon
'
filesize : 2790
modified : 1996-11-14T13:29:32Z
errors   :
matches  :
  - ns      : 'pronom'
    id      : 'fmt/503'
    format  : 'AppleDouble Resource Fork'
    version : '2'
    mime    : 'multipart/appledouble'
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon
.as1'
filesize : 2829
modified : 2022-03-03T10:20:10Z
errors   :
matches  :
  - ns      : 'pronom'
    id      : 'fmt/968'
    format  : 'AppleSingle'
    version : '2'
    mime    : 'application/applefile'
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon
   .as2'
filesize : 2829
modified : 2022-03-03T10:20:10Z
errors   :
matches  :
  - ns      : 'pronom'
    id      : 'fmt/968'
    format  : 'AppleSingle'
    version : '2'
    mime    : 'application/applefile'
    basis   : 'byte match at 0, 8'
    warning :
---
filename : 'Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon
\t\t.as3'
filesize : 2829
modified : 2022-03-03T10:20:10Z
errors   :
matches  :
  - ns      : 'pronom'
    id      : 'fmt/968'
    format  : 'AppleSingle'
    version : '2'
    mime    : 'application/applefile'
    basis   : 'byte match at 0, 8'
    warning :
---
"""


def test_bad_yaml(tmp_path):
    """YAML may end up being output on multiple lines incorrectly. This
    output may be formatted with an indent, or not. Ensure that the
    output is predictable either way.
    """
    dir_ = tmp_path
    sf_yaml = dir_ / "sf_test.yaml"
    sf_yaml.write_text(BAD_YAML.strip(), encoding="UTF-8")

    sf = SFYAMLHandler()
    sf.read_sf_yaml(str(sf_yaml))

    # Access files in processed data to verify integrity.
    files = sf.sfdata["files"]

    assert len(files) == 4
    expected = [
        "Mac RF Test.zip#__MACOSX\\Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\._Icon",
        "Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon.as1",
        "Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon.as2",
        "Mac RF Test.zip#Mac RF Test\\ProTools AppleSingle\\Demo Session\\Audio Files\\Icon.as3",
    ]
    gathered = []
    for file in files:
        assert file.get("filename", False)
        gathered.append(file.get("filename", False))
    assert gathered == expected
