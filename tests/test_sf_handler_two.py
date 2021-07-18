# -*- coding: utf-8 -*-

# TODO RENAME

import sys

from sqlitefid.libs.SFHandlerClass import SFYAMLHandler

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

if sys.version_info[0] == 3:
    PY3 = True
else:
    PY3 = False


def test_read_sf_yaml(tmp_path):
    """Ensure that the SF data above can be properly parsed and outputs
    sensible data.
    """

    dir_ = tmp_path
    sf_yaml = dir_ / "sf_test.yaml"
    sf_yaml.write_text(SIEGFRIED_YAML.strip())

    sf = SFYAMLHandler()
    sf.readSFYAML(str(sf_yaml))

    assert sf.sectioncount == 5
    paths = [u"{}".format(f["filename"]) for f in sf.files]

    assert (
        list(set(paths)).sort()
        == ["Q10287816.gz", "Q42591🖤.mp3", "Q42332.pdf", "Q28205479.info"].sort()
    )

    files = sf.sfdata["files"]

    assert len(sf.files) == 4
    assert len(files) == 4

    assert files[0] == {
        "filename": "Q10287816.gz",
        "filesize": "3",
        "modified": "2021-05-24T19:26:56+02:00",
        "errors": "",
        "md5": "613ffd2ae0a8828aa573ce62bf2e30c3",
        "type": "Container",
        "containertype": "gz",
        "uri": "gz:file:///Q10287816.gz!",
        "uri scheme": "gz",
        "identification": {
            "pronom": {
                "id": "x-fmt/266",
                "format": "GZIP Format",
                "version": "",
                "mime": "application/gzip",
                "method": "Signature",
                "basis": "extension match gz; byte match at 0, 3",
                "warning": None,
            },
            "tika": {
                "id": "application/gzip",
                "format": "Gzip Compressed Archive",
                "mime": "application/gzip",
                "method": "Signature",
                "basis": "extension match gz; byte match at 0, 2 (signature 1/2); byte match at 0, 2 (signature 2/2)",
                "warning": None,
                "version": "",
            },
            "freedesktop.org": {
                "id": "application/gzip",
                "format": "Gzip archive",
                "mime": "application/gzip",
                "method": "Signature",
                "basis": "extension match gz; byte match at 0, 2",
                "warning": None,
                "version": "",
            },
            "loc": {
                "id": "UNKNOWN",
                "format": "",
                "mime": "none",
                "basis": None,
                "method": "None",
                "extension mismatch": False,
                "warning": "no match",
                "version": "",
            },
        },
    }

    assert files[3] == {
        "filename": u"Q42591🖤.mp3",
        "filesize": "3",
        "modified": "2021-07-08T23:21:40+02:00",
        "errors": "",
        "md5": "c0f44879dc0d4eae7b3f0b3e801e373c",
        "type": "File",
        "uri": "file:///Q42591🖤.mp3",
        "uri scheme": "file",
        "identification": {
            "pronom": {
                "id": "UNKNOWN",
                "format": "",
                "version": "",
                "mime": "none",
                "basis": None,
                "method": "None",
                "extension mismatch": False,
                "warning": "no match; possibilities based on extension are fmt/134",
            },
            "tika": {
                "id": "audio/mpeg",
                "format": "MPEG-1 Audio Layer 3",
                "mime": "audio/mpeg",
                "method": "Signature",
                "basis": "extension match mp3; byte match at 0, 3 (signature 12/12)",
                "warning": None,
                "version": "",
            },
            "freedesktop.org": {
                "id": "audio/mpeg",
                "format": "MP3 audio",
                "mime": "audio/mpeg",
                "method": "Signature",
                "basis": "extension match mp3; byte match at 0, 3 (signature 2/2)",
                "warning": None,
                "version": "",
            },
            "loc": {
                "id": "UNKNOWN",
                "format": "",
                "mime": "none",
                "basis": None,
                "method": "None",
                "extension mismatch": False,
                "warning": "no match; possibilities based on extension are fdd000052, fdd000053, fdd000105, fdd000111, fdd000256, fdd000275",
                "version": "",
            },
        },
    }

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
