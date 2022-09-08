# -*- coding: utf-8 -*-

"""IdentifyExportClass is responsible for identifying the type of export
provided to sqlitefid. It largely does this using magic numbers.
"""

from __future__ import absolute_import

import logging
import re


class IdentifyExport:
    """IdentifyExport."""

    DROIDTYPE = "droid"  # backward compatibility for now...
    SFTYPE = "siegfried"
    SFCSVTYPE = "siegfried csv"
    FIDOTYPE = "fido"
    UNKTYPE = "unknown"

    # specific hashes
    DROIDMD5TYPE = "droid_md5"
    DROIDSHA1TYPE = "droid_md5"
    DROIDSHA256TYPE = "droid_md5"
    DROIDNOHASH = "droid_nohash"
    DROIDTYPEBOM = "droid_BOM"

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
    sfcsv_re = r"^filename,filesize,modified,errors,namespace,id,format,version,mime,basis,warning"
    sfcsv_re_md5 = r"^filename,filesize,modified,errors,md5,namespace,id,format,version,mime,basis,warning"
    sfcsv_re_sha1 = r"^filename,filesize,modified,errors,sha1,namespace,id,format,version,mime,basis,warning"
    sfcsv_re_sha256 = r"^filename,filesize,modified,errors,sha256,namespace,id,format,version,mime,basis,warning"
    sfcsv_re_sha512 = r"^filename,filesize,modified,errors,sha512,namespace,id,format,version,mime,basis,warning"
    sfcsv_re_crc = r"^filename,filesize,modified,errors,crc,namespace,id,format,version,mime,basis,warning"

    # UTF8 with BOM
    droid_utf8 = "\xEF\xBB\xBF"
    droid_utf8_md5 = droid_utf8 + droid_md5
    droid_utf8_sha1 = droid_utf8 + droid_sha1
    droid_utf8_sha256 = droid_utf8 + droid_sha256
    droid_utf8_nohash = droid_utf8 + droid_nohash

    droid_utf16 = "\xC3\xAF\xC2\xBB\xC2\xBF"
    droid_utf16_md5 = droid_utf16 + droid_md5
    droid_utf16_sha1 = droid_utf16 + droid_sha1
    droid_utf16_sha256 = droid_utf16 + droid_sha256
    droid_utf16_nohash = droid_utf16 + droid_nohash

    def exportid(self, export):
        """Opens an identification report export and attempts to
        identify the creating tool based on identifying characteristics.
        """
        sf_magic = ""
        droid_magic = ""

        try:
            with open(export, "r", encoding="UTF-8") as f:
                droid_magic = f.readline()
                sf_magic = droid_magic + f.readline()
        except IOError as err:
            logging.error("Cannot identify export: %s", err)

        if (
            droid_magic.strip() == self.droid_md5
            or droid_magic.strip() == self.droid_sha1
            or droid_magic.strip() == self.droid_sha256
            or droid_magic.strip() == self.droid_nohash
        ):
            return self.DROIDTYPE

        if (
            droid_magic.strip() == self.droid_utf8_md5
            or droid_magic.strip() == self.droid_utf8_sha1
            or droid_magic.strip() == self.droid_utf8_sha256
            or droid_magic.strip() == self.droid_utf8_nohash
        ):
            return self.DROIDTYPEBOM

        if (
            droid_magic.strip() == self.droid_utf16_md5
            or droid_magic.strip() == self.droid_utf16_sha1
            or droid_magic.strip() == self.droid_utf16_sha256
            or droid_magic.strip() == self.droid_utf16_nohash
        ):
            return self.DROIDTYPEBOM

        if self.sf_orig in sf_magic.strip():
            return self.SFTYPE
        if (
            re.search(re.compile(self.sfcsv_re), droid_magic) is not None
            or re.search(re.compile(self.sfcsv_re_md5), droid_magic) is not None
            or re.search(re.compile(self.sfcsv_re_sha1), droid_magic) is not None
            or re.search(re.compile(self.sfcsv_re_sha256), droid_magic) is not None
            or re.search(re.compile(self.sfcsv_re_sha512), droid_magic) is not None
            or re.search(re.compile(self.sfcsv_re_crc), droid_magic) is not None
        ):
            return self.SFCSVTYPE

        if re.search(re.compile(self.fido_re), droid_magic) is not None:
            return self.FIDOTYPE

        return self.UNKTYPE
