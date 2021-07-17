# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import sys

from sqlitefid.libs.CSVHandlerClass import GenericCSVHandler

DROID_CSV = """"ID","PARENT_ID","URI","FILE_PATH","NAME","METHOD","STATUS","SIZE","TYPE","EXT","LAST_MODIFIED","EXTENSION_MISMATCH","SHA1_HASH","FORMAT_COUNT","PUID","MIME_TYPE","FORMAT_NAME","FORMAT_VERSION"
"2","0","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus","🖤format-corpus",,"Done","","Folder",,"2014-02-28T15:49:11","false",,"",,"","",""
"3","2","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video","video",,"Done","","Folder",,"2014-02-28T15:48:47","false",,"",,"","",""
"4","3","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime","Quicktime",,"Done","","Folder",,"2014-02-28T15:48:59","false",,"",,"","",""
"5","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/apple-intermediate-codec.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\apple-intermediate-codec.mov","apple-intermediate-codec.mov","Signature","Done","319539","File","mov","2014-02-18T16:58:16","false","d097cf36467373f52b974542d48bec134279fa3f","1","x-fmt/384","video/quicktime","Quicktime",""
"6","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/animation.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\animation.mov","animation.mov","Signature","Done","1020209","File","mov","2014-02-18T16:58:16","false","edb5226b963f449ce58054809149cb812bdf8c0a","1","x-fmt/384","video/quicktime","Quicktime",""
"7","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/apple-prores-422-hq.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\apple-prores-422-hq.mov","apple-prores-422-hq.mov","Signature","Done","701111","File","mov","2014-02-18T16:58:16","false","484591affcae8ef5d896289db75503b603092ef8","1","x-fmt/384","video/quicktime","Quicktime",""
"8","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/apple-prores-422-lt.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\apple-prores-422-lt.mov","apple-prores-422-lt.mov","Signature","Done","476503","File","mov","2014-02-18T16:58:16","false","4dacced1685746d8e39bb6dc36d01bf2a60a17e2","1","x-fmt/384","video/quicktime","Quicktime",""
"9","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/apple-prores-422-proxy.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\apple-prores-422-proxy.mov","apple-prores-422-proxy.mov","Signature","Done","242855","File","mov","2014-02-18T16:58:16","false","0e18911984ac1cd4721b4d3c9e0914cc98da3ab4","1","x-fmt/384","video/quicktime","Quicktime",""
"10","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/apple-prores-422.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\apple-prores-422.mov","apple-prores-422.mov","Signature","Done","564775","File","mov","2014-02-18T16:58:16","false","faf81ab4a815cf0cd7c9b01d8ea950971d38dad1","1","x-fmt/384","video/quicktime","Quicktime",""
"11","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/dv-dvchd-ntsc-interlaced.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\\dv-dvchd-ntsc-interlaced.mov","dv-dvchd-ntsc-interlaced.mov","Signature","Done","3001365","File","mov","2014-02-18T16:58:16","false","b9d45fd2e79a83c69afe95d89a846b96bf1778b7","1","x-fmt/384","video/quicktime","Quicktime",""
"12","4","éfile:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/🖤dv-dvchd-ntsc-progressive.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\\dv-dvchd-ntsc-progressive.mov","🖤dv-dvchd-ntsc-progressive.mov","Signature","Done","3001365","File","mov","2014-02-18T16:58:16","false","a9caed081ab55ff1ea1b32d3eb30dab2841a9785","1","x-fmt/384","video/quicktime","Quicktime",""
"13","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/dv-pal-interlaced.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\\dv-pal-interlaced.mov","dv-pal-interlaced.mov","Signature","Done","3601749","File","mov","2014-02-18T16:58:16","false","2ab26184bc937de129640574e75d01ed420cc19f","1","x-fmt/384","video/quicktime","Quicktime",""
"14","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/dv-pal-progressive.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\\dv-pal-progressive.mov","dv-pal-progressive.mov","Signature","Done","3601749","File","mov","2014-02-18T16:58:16","false","7955c4e67b84f67bab77eff241a81ceba0177bf4","1","x-fmt/384","video/quicktime","Quicktime",""
"15","4","file:////10.1.4.222/gda/archives-sample-files/opf-format-corpus/format-corpus/video/Quicktime/dvcpro-hd-1080i60.mov","\\10.1.4.222\\gda\archives-sample-files\\opf-format-corpus\format-corpus\video\\Quicktime\\dvcpro-hd-1080i60.mov","dvcpro-hd-1080i60.mov","Signature","Done","12001365","File","mov","2014-02-18T16:58:17","false","d36ba66836ccc9a011e1517121648a1ba9b2f9e6","1","x-fmt/384","video/quicktime","Quicktime",""
"""

if sys.version_info[0] == 3:
    PY3 = True
else:
    PY3 = False


def _StringIO():
    if PY3 is True:
        return io.StringIO()
    return io.BytesIO()


def test_fido_handler_no_BOM():
    """Ensure that the return for a non-identified CSV is accurate. This
    is determined in the constructor.
    """
    droidcsvhandler = GenericCSVHandler(BOM=False)
    csv_in = _StringIO()
    csv_in.write(DROID_CSV)
    res = droidcsvhandler._csv_to_list(csv_in)
    assert res == []
    assert len(res) == 0


def test_fido_handler_BOM():
    """Ensure that we get sensible values out of a valid CSV."""
    droidcsvhandler = GenericCSVHandler(BOM=True)
    csv_in = _StringIO()
    csv_in.write(DROID_CSV)
    res = droidcsvhandler._csv_to_list(csv_in)
    assert len(res) == 14

    ID = "ID"
    NAME = "NAME"
    SIZE = "SIZE"
    MOD = "LAST_MODIFIED"
    SHA1 = "SHA1_HASH"
    PUID = "PUID"
    MIME = "MIME_TYPE"
    TYPE = "TYPE"

    assert res[0][ID] == "2"
    assert res[10][ID] == "12"

    if PY3 is True:
        assert res[0][NAME] == "🖤format-corpus"
        assert res[10][NAME] == "🖤dv-dvchd-ntsc-progressive.mov"
    else:
        assert res[0][NAME].encode("utf8") == "\xf0\x9f\x96\xa4format-corpus"
        assert (
            res[10][NAME].encode("utf8")
            == "\xf0\x9f\x96\xa4dv-dvchd-ntsc-progressive.mov"
        )

    assert res[0][SIZE] == ""
    assert res[10][SIZE] == "3001365"

    assert res[0][MOD] == "2014-02-28T15:49:11"
    assert res[10][MOD] == "2014-02-18T16:58:16"

    assert res[0][SHA1] == ""
    assert res[10][SHA1] == "a9caed081ab55ff1ea1b32d3eb30dab2841a9785"

    assert res[0][PUID] == ""
    assert res[10][PUID] == "x-fmt/384"

    assert res[0][MIME] == ""
    assert res[10][MIME] == "video/quicktime"

    assert res[0][TYPE] == "Folder"
    assert res[10][TYPE] == "File"
