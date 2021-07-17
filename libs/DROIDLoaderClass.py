# -*- coding: utf-8 -*-

from __future__ import absolute_import

if __name__.startswith("sqlitefid"):
    from sqlitefid.libs.CSVHandlerClass import DroidCSVHandler
    from sqlitefid.libs.ToolMappingClass import ToolMapping
else:
    from libs.CSVHandlerClass import DroidCSVHandler
    from libs.ToolMappingClass import ToolMapping


class DROIDLoader:

    basedb = ""
    BOM = False
    NS_NAME = "pronom"
    NS_ID = 0
    NS_DETAILS = "droid"  # to be overwritten by filename

    def __init__(self, basedb, BOM=False):
        self.basedb = basedb
        self.BOM = BOM
        self.basedb.tooltype = "droid"

    def insertfiledbstring(self, keys, values):
        insert = "INSERT INTO " + self.basedb.FILEDATATABLE
        return (
            insert + "(" + keys.strip(", ") + ") VALUES (" + values.strip(", ") + ");"
        )

    def insertiddbstring(self, keys, values):
        insert = "INSERT INTO " + self.basedb.IDTABLE
        return (
            insert + "(" + keys.strip(", ") + ") VALUES (" + values.strip(", ") + ");"
        )

    def file_id_junction_insert(self, file, id):

        # ins = "INSERT INTO {} ({}, {}) VALUES ({}, {});".format(self.basedb.ID_JUNCTION, self.basedb.FILEID, self.basedb.IDID, str(file), str(id))
        return (
            "INSERT INTO "
            + self.basedb.ID_JUNCTION
            + "("
            + self.basedb.FILEID
            + ","
            + self.basedb.IDID
            + ") VALUES ("
            + str(file)
            + ","
            + str(id)
            + ");"
        )

    def populateIDTable(self, formats, method, status, mismatch):
        add_fields = ["METHOD", "STATUS", "NS_ID", "EXTENSION_MISMATCH"]
        add_values = [
            '"' + method + '"',
            '"' + status + '"',
            '"' + str(self.NS_ID) + '"',
            '"' + str(mismatch) + '"',
        ]
        idvaluelist = []
        idkeylist = []
        idkeystring = ""
        idvaluestring = ""
        for format in formats:
            idkeystring = ", ".join(format.keys()).split(",") + add_fields
            idvaluestring = ", ".join(format.values()).split(",") + add_values
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

    def droidDBSetup(self, droidcsv, cursor):
        """Reads a DROID CSV file and adds its data to an sqlite DB.

        :param droidcsv: path to DROID csv file (string)
        :param cursor: sqlite database cursor to work with
            (sqlite3.Cursor)

        :returns: None (Nonetype)
        """

        self.NS_ID = self.setupNamespaceConstants(cursor, droidcsv)

        if droidcsv is not False:
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

            # FIELDS FOR MULTIPLE ID FIELDS
            METHOD = file["METHOD"]
            if METHOD == "":
                METHOD = "None"
            STATUS = file["STATUS"]
            MISMATCH = file["EXTENSION_MISMATCH"]
            if MISMATCH == "true":
                MISMATCH = "True"
            else:
                MISMATCH = "False"

            MULTIPLE = False
            if int(file["FORMAT_COUNT"]) > 1:
                MULTIPLE = True
            MULTIPLE_DONE = False

            for key, value in file.items():
                if key != "FORMAT_COUNT":
                    if key == "MIME_TYPE" or key == "METHOD":
                        if value == "":
                            value = "None"
                    if self.basedb.hashtype is False:
                        if "_HASH" in key:
                            self.basedb.hashtype = key.split("_", 1)[0]
                        elif key == "HASH":
                            # no hash used in export
                            self.basedb.hashtype = "None"
                    if key in ToolMapping.DROID_FILE_MAP:
                        filekeystring = (
                            filekeystring + ToolMapping.DROID_FILE_MAP[key] + ", "
                        )
                        filevaluestring = filevaluestring + '"' + value + '", '
                    if MULTIPLE is False:
                        if key in ToolMapping.DROID_ID_MAP:
                            if key == "EXTENSION_MISMATCH":
                                if value == "true":
                                    value = "True"
                                elif value == "false":
                                    value = "False"
                            idkeystring = (
                                idkeystring + ToolMapping.DROID_ID_MAP[key] + ", "
                            )
                            idvaluestring = idvaluestring + '"' + value + '", '
                    else:
                        if MULTIPLE_DONE is False:
                            (
                                MULTIPLE_KEY_LIST,
                                MULTIPLE_VALUE_LIST,
                            ) = self.populateIDTable(
                                file[droidcsvhandler.DICT_FORMATS],
                                METHOD,
                                STATUS,
                                MISMATCH,
                            )
                            MULTIPLE_DONE = (
                                True  # don't loop around this more than is needed
                            )

            id = None
            fileidx = None

            if filekeystring != "" and filevaluestring != "":
                cursor.execute(self.insertfiledbstring(filekeystring, filevaluestring))
                fileidx = cursor.lastrowid

            if not folder:
                if MULTIPLE is not True:
                    if idkeystring != "" and idvaluestring != "":
                        idkeystring = idkeystring + "NS_ID"
                        idvaluestring = idvaluestring + '"' + str(self.NS_ID) + '"'
                        cursor.execute(
                            self.insertiddbstring(idkeystring, idvaluestring)
                        )
                        id = cursor.lastrowid

                    if id is not None and file is not None:
                        cursor.execute(self.file_id_junction_insert(fileidx, id))
                else:
                    for i, v in enumerate(MULTIPLE_KEY_LIST):
                        insert = self.insertiddbstring(
                            ", ".join(v), ", ".join(MULTIPLE_VALUE_LIST[i])
                        )
                        cursor.execute(insert)
                        id = cursor.lastrowid
                        if fileidx is not None:
                            cursor.execute(self.file_id_junction_insert(fileidx, id))
