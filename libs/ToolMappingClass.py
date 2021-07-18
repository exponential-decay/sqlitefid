# -*- coding: utf-8 -*-

"""ToolMappingClass

Mapping of tool output fields to database fields.
"""

from __future__ import absolute_import


class ToolMapping:
    """ToolMapping."""

    DROID_FILE_MAP = {
        "ID": "INPUT_ID",
        "PARENT_ID": "PARENT_ID",
        "URI": "URI",
        "URI_SCHEME": "URI_SCHEME",
        "FILE_PATH": "FILE_PATH",
        "DIR_NAME": "DIR_NAME",
        "NAME": "NAME",
        "SIZE": "SIZE",
        "TYPE": "TYPE",
        "EXT": "EXT",
        "LAST_MODIFIED": "LAST_MODIFIED",
        "YEAR": "YEAR",
        "SHA1_HASH": "HASH",
        "SHA256_HASH": "HASH",
        "MD5_HASH": "HASH",
    }

    DROID_ID_MAP = {
        "METHOD": "METHOD",
        "STATUS": "STATUS",
        "PUID": "ID",
        "MIME_TYPE": "MIME_TYPE",
        "FORMAT_NAME": "FORMAT_NAME",
        "FORMAT_VERSION": "FORMAT_VERSION",
        "EXTENSION_MISMATCH": "EXTENSION_MISMATCH",
        "FORMAT_COUNT": "FORMAT_COUNT",
    }

    SF_FILE_MAP = {
        "uri": "URI",
        "uri_scheme": "URI_SCHEME",
        "filename": "FILE_PATH",
        "directory": "DIR_NAME",
        "name": "NAME",
        "filesize": "SIZE",
        "type": "TYPE",
        "ext": "EXT",
        "modified": "LAST_MODIFIED",
        "year": "YEAR",
        "md5": "HASH",
        "sha1": "HASH",
        "sha256": "HASH",
        "sha512": "HASH",
        "crc": "HASH",
        "errors": "ERROR",
    }

    SF_ID_MAP = {
        "basis": "BASIS",
        "method": "METHOD",
        "id": "ID",
        "mime": "MIME_TYPE",
        "format": "FORMAT_NAME",
        "version": "FORMAT_VERSION",  # no version in tika or freedesktop ids
        "extension_mismatch": "EXTENSION_MISMATCH",
        "warning": "WARNING",
    }
