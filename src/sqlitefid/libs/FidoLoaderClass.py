# -*- coding: utf-8 -*-

# Disable pylint warnings for CSVHandlerClass imports which are not
# straightforward as we try and handle PY2 and PY3.
#
# pylint: disable=E0611,E0401

"""FidoLoaderClass

Contains functions for handling fido exports for sqlitefid. The code
takes a fido export verbatim and converts it, adding a CSV header,
writing it into a temporary file before handing it over to the primary
code runner.
"""

from __future__ import absolute_import

import logging
import tempfile

from .CSVHandlerClass import GenericCSVHandler


class FidoLoader:
    """FidoLoader Class"""

    fido_header = '"info.status","info.time","info.puid","info.formatname","info.signaturename","info.filesize","info.filename","info.mimetype","info.matchtype"'
    basedb = ""

    delete = True
    BOM = False

    def __init__(self, basedb):
        """Initializes the FidoLoader class."""
        self.basedb = basedb

    def createtmpfile(self, fido_export):
        """Creates a temporary CSV file with fido headers for testing.

        :param fido_export: path to a fido export to convert to sqlite
            (string)

        :returns: named temporary file object with fido export and CSV
            header (temporary file object) or None (Nonetype)
        """
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=self.delete) as tmp_file:
            logging.info("Created tmp file: %s", tmp_file.name)
            with open(fido_export, "r") as csv_file:
                for i, row in enumerate(csv_file):
                    if i == 0:
                        tmp_file.write("{}\n".format(self.fido_header).encode())
                        tmp_file.write(row.encode())
                    else:
                        tmp_file.write(row.encode())
            return tmp_file

    def fido_db_setup(self, fido_export, _):
        """Sets the fido analysis database up.

        :param fido_export: path to a fido export to convert to sqlite
            (string)
        :param cursor: sqlite3 database cursor to work with
            (sqlite3 object)

        :returns: None (Nonetype)
        """
        logging.info(
            "Placeholder Code: Currently not handling FIDO exports (fido_export=%s)",
            fido_export,
        )
        if fido_export is False or fido_export == "":
            return
        tmpfile = self.createtmpfile(fido_export)
        fidocsvhandler = GenericCSVHandler(BOM=self.BOM)
        try:
            _ = fidocsvhandler.csvaslist(tmpfile.name)
            tmpfile.close()
        except AttributeError as err:
            logging.info("Cannot work with export: %s", err)
