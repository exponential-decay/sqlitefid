# -*- coding: utf-8 -*-

from __future__ import absolute_import

import re


class IdentifyExport:

    DROIDTYPE = "droid"  # backward compatibility for now...

    # specific hashes
    DROIDMD5TYPE = "droid_md5"
    DROIDSHA1TYPE = "droid_md5"
    DROIDSHA256TYPE = "droid_md5"
    DROIDNOHASH = "droid_nohash"
    DROIDTYPEBOM = "droid_BOM"
    FIDOTYPE = "fido"
    UNKTYPE = "unknown"

    SFTYPE = "siegfried"
    SFCSVTYPE = "siegfried csv"

    droid_header = "{}{}{}{}".format(
        '"ID","PARENT_ID","URI","FILE_PATH","NAME","METHOD","STATUS"',
        ',"SIZE","TYPE","EXT","LAST_MODIFIED","EXTENSION_MISMATCH",',
        '"{}","FORMAT_COUNT","PUID","MIME_TYPE","FORMAT_NAME",',
        '"FORMAT_VERSION"',
    )

    droid_md5 = droid_header.format("MD5_HASH")
    droid_sha1 = droid_header.format("SHA1_HASH")
    droid_sha256 = droid_header.format("SHA256_HASH")
    droid_nohash = droid_header.format("HASH")

    fido_re = r"^(OK|KO),[0-9]+,(fmt|x-fmt)\/[0-9]{1,4},"
    sf_orig = r"---" + "\x0A" + "siegfried   :"
    sfcsv_re = r"^filename,filesize,modified,errors,md5,namespace,id,format,version,mime,basis,warning$"

    # UTF8 with BOM
    droid_utf8 = "\xEF\xBB\xBF"
    droid_utf8_md5 = droid_utf8 + droid_md5
    droid_utf8_sha1 = droid_utf8 + droid_sha1
    droid_utf8_sha256 = droid_utf8 + droid_sha256
    droid_utf8_nohash = droid_utf8 + droid_nohash

    def exportid(self, export):
        with open(export, "r") as f:
            droid_magic = f.readline()
            sf_magic = droid_magic + f.readline()
        if (
            droid_magic.strip() == self.droid_md5
            or droid_magic.strip() == self.droid_sha1
            or droid_magic.strip() == self.droid_sha256
            or droid_magic.strip() == self.droid_nohash
        ):
            return self.DROIDTYPE
        elif (
            droid_magic.strip() == self.droid_utf8_md5
            or droid_magic.strip() == self.droid_utf8_sha1
            or droid_magic.strip() == self.droid_utf8_sha256
            or droid_magic.strip() == self.droid_utf8_nohash
        ):
            return self.DROIDTYPEBOM
        elif self.sf_orig in sf_magic.strip():
            return self.SFTYPE
        elif re.search(re.compile(self.fido_re), droid_magic) is not None:
            return self.FIDOTYPE
        elif re.search(re.compile(self.sfcsv_re), droid_magic) is not None:
            return self.SFCSVTYPE
        else:
            return self.UNKTYPE
