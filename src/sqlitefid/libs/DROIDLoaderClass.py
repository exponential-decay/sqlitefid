# -*- coding: utf-8 -*-

# Disable pylint warnings for CSVHandlerClass imports which are not
# straightforward as we try and handle PY2 and PY3.
#
# pylint: disable=E0611,E0401

"""DROIDLoaderClass is responsible for inputting the majority of the
DROID data into the sqlite db.
"""

from __future__ import absolute_import, print_function

import logging
from sqlite3 import OperationalError

from .CSVHandlerClass import DroidCSVHandler
from .ToolMappingClass import ToolMapping


class DROIDLoader:
    """DROIDLoader."""

    BOM = False
    NS_NAME = "pronom"
    NS_ID = 0
    NS_DETAILS = "droid"  # to be overwritten by filename

    def __init__(self, basedb, BOM=False, debug=False):
        self.debug = debug
        self.basedb = basedb
        self.BOM = BOM
        self.basedb.tooltype = "droid"

    def insertfiledbstring(self, keys, values):
        ins = u"INSERT INTO {} ({}) VALUES ({});".format(
            self.basedb.FILEDATATABLE, keys.strip(", "), values.strip(", ")
        )
        return ins

    def insertiddbstring(self, keys, values):
        insert = "INSERT INTO " + self.basedb.IDTABLE
        return (
            insert + "(" + keys.strip(", ") + ") VALUES (" + values.strip(", ") + ");"
        )

    def file_id_junction_insert(self, file, id_):
        ins = "INSERT INTO {} ({}, {}) VALUES ({}, {});".format(
            self.basedb.ID_JUNCTION, self.basedb.FILEID, self.basedb.IDID, file, id_
        )
        return ins

    def populateIDTable(self, formats, method, status, mismatch):
        add_fields = ["METHOD", "STATUS", "NS_ID", "EXTENSION_MISMATCH"]
        add_values = [
            '"{}"'.format(method),
            '"{}"'.format(status),
            '"{}"'.format(self.NS_ID),
            '"{}"'.format(mismatch),
        ]
        idvaluelist = []
        idkeylist = []
        idkeystring = ""
        idvaluestring = ""
        for format_ in formats:
            idkeystring = ", ".join(format_.keys()).split(",") + add_fields
            idvaluestring = ", ".join(format_.values()).split(",") + add_values
            idvaluelist.append(idvaluestring)
            idkeylist.append(idkeystring)
        return idkeylist, idvaluelist

    def setupNamespaceConstants(self, cursor, filename):
        self.NS_DETAILS = filename
        ins = 'INSERT INTO {} (NS_NAME, NS_DETAILS) VALUES ("{}", "{}");'.format(
            self.basedb.NAMESPACETABLE, self.NS_NAME, self.NS_DETAILS
        )
        cursor.execute(ins)
        return cursor.lastrowid

    def create_droid_database(self, droidcsv, cursor):
        """Reads a DROID CSV file and adds its data to an sqlite DB.

        :param droidcsv: path to DROID csv file (string)
        :param cursor: sqlite database cursor to work with
            (sqlite3.Cursor)

        :returns: None (Nonetype)
        """

        self.NS_ID = self.setupNamespaceConstants(cursor, droidcsv)

        if droidcsv is False:
            return

        droidcsvhandler = DroidCSVHandler()
        droidlist = droidcsvhandler.readDROIDCSV(droidcsv, self.BOM)
        droidlist = droidcsvhandler.addurischeme(droidlist)
        droidlist = droidcsvhandler.addYear(droidlist)
        droidlist = droidcsvhandler.adddirname(droidlist)

        for file in droidlist:

            folder = False
            if file["TYPE"].lower() == "folder":
                folder = True

            filekeystring = ""
            filevaluestring = ""
            idkeystring = ""
            idvaluestring = ""

            # Multiple identification fields.
            METHOD = file["METHOD"]
            if METHOD == "":
                METHOD = None
            STATUS = file["STATUS"]
            MISMATCH = file["EXTENSION_MISMATCH"]
            if MISMATCH == "true":
                MISMATCH = True
            else:
                MISMATCH = False
            MULTIPLE = False
            MULTIPLE_DONE = False
            try:
                if int(file["FORMAT_COUNT"]) > 1:
                    MULTIPLE = True
            except ValueError:
                # We anticipate an integer or empty cell here, e.g. for
                # a directory entry.
                pass

            for key, value in file.items():

                try:
                    # Convert the value to Unicode to work with.
                    value = u"{}".format(value)
                except AttributeError:
                    pass

                if key == "FORMAT_COUNT":
                    continue
                if key in ("MIME_TYPE", "METHOD"):
                    if value == "":
                        value = None
                if self.basedb.hashtype is None:
                    if "_HASH" in key:
                        self.basedb.hashtype = key.split("_", 1)[0]
                if key in ToolMapping.DROID_FILE_MAP:
                    filekeystring = u"{}{}, ".format(
                        filekeystring, ToolMapping.DROID_FILE_MAP[key]
                    )
                    filevaluestring = u'{}"{}", '.format(filevaluestring, value)

                if MULTIPLE is False:
                    if key in ToolMapping.DROID_ID_MAP:
                        if key == "EXTENSION_MISMATCH":
                            if value == "true":
                                value = True
                            else:
                                value = False
                        idkeystring = u"{}{}, ".format(
                            idkeystring, ToolMapping.DROID_ID_MAP[key]
                        )
                        idvaluestring = u'{} "{}", '.format(idvaluestring, value)
                else:
                    if MULTIPLE_DONE is False:
                        (MULTIPLE_KEY_LIST, MULTIPLE_VALUE_LIST) = self.populateIDTable(
                            file[droidcsvhandler.DICT_FORMATS], METHOD, STATUS, MISMATCH
                        )
                        MULTIPLE_DONE = True

            id_ = None
            fileidx = None

            if filekeystring != "" and filevaluestring != "":
                ins = self.insertfiledbstring(filekeystring, filevaluestring)
                try:
                    cursor.execute(ins)
                except OperationalError as err:
                    # Output some logging to help users determine which rows
                    # are affected by this issue. It is likely the input report
                    # is not escaped properly, or we need to handle it better
                    # when converting it.
                    logging.error("Insert failed: %s insert: '%s'", err, ins[131:160])
                    continue
                fileidx = cursor.lastrowid

            if folder:
                continue

            if MULTIPLE:
                for i, v in enumerate(MULTIPLE_KEY_LIST):
                    insert = self.insertiddbstring(
                        ", ".join(v), ", ".join(MULTIPLE_VALUE_LIST[i])
                    )
                    cursor.execute(insert)
                    id_ = cursor.lastrowid
                    if fileidx is not None:
                        cursor.execute(self.file_id_junction_insert(fileidx, id_))
                continue

            if idkeystring != "" and idvaluestring != "":
                idkeystring = idkeystring + "NS_ID"
                idvaluestring = idvaluestring + '"' + str(self.NS_ID) + '"'
                cursor.execute(self.insertiddbstring(idkeystring, idvaluestring))
                id_ = cursor.lastrowid

            if id_ is not None and file is not None:
                cursor.execute(self.file_id_junction_insert(fileidx, id_))
