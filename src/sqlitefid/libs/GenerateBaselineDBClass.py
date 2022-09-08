# -*- coding: utf-8 -*-

"""GenerateBaselineDBClass is responsible for setting up the baseline
sqlite DB we will analyze all identification results with.
"""

from __future__ import absolute_import

import logging
import sqlite3
import time


class GenerateBaselineDB:
    """GenerateBaselineDB."""

    IDTABLE = "IDDATA"
    METADATATABLE = "DBMD"
    FILEDATATABLE = "FILEDATA"
    NAMESPACETABLE = "NSDATA"
    ID_JUNCTION = "IDRESULTS"

    # file_id_junction
    FILEID = "FILE_ID"
    IDID = "ID_ID"
    NSID = "NS_ID"

    # How to create an ID in SQLITE: http://stackoverflow.com/a/9342301
    # FILE ID is a new ID for the purpose of this database
    # INPUT_FILE_ID is the ID from the input analysis
    # PARENT ID is the ID of the parent of the file, will be a folder
    FILEDATA_TABLE = [
        FILEID,
        "INPUT_ID",
        "PARENT_ID",
        "URI",
        "URI_SCHEME",
        "FILE_PATH",
        "DIR_NAME",
        "NAME",
        "SIZE",
        "TYPE",
        "EXT",
        "LAST_MODIFIED",
        "YEAR",
        "HASH",
        "ERROR",
    ]

    # N.B. FORMAT_COUNT removed to reside in multiple NS rows
    IDTABLE_TABLE = [
        IDID,
        NSID,
        "METHOD",
        "STATUS",
        "ID",
        "BASIS",
        "MIME_TYPE",
        "FORMAT_NAME",
        "FORMAT_VERSION",
        "EXTENSION_MISMATCH",
        "WARNING",
    ]

    # NAMESPACE_TABLE
    NS_TABLE = [NSID, "NS_NAME", "NS_DETAILS"]

    def __init__(self, export, debug=False, in_memory=False):
        self.timestamp = None
        self.cursor = None
        self.hashtype = None
        self.tooltype = None
        self.log = debug
        if in_memory:
            self.dbname = ":memory:"
        else:
            # For compatibility non-memory databases require this.
            self.dbname = self.getDBFilename(export)
            self.dbsetup()

    def dbsetup(self):
        self.timestamp = self.gettimestamp()
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.droptables(self.cursor)

        # create a table to hold information about the file only
        self.createfiledatatable()
        self.createidtable()
        self.createjunctiontable(self.ID_JUNCTION, self.FILEID, self.IDID)
        self.createNStable()
        self.create_indices()
        return self.cursor

    def getcursor(self):
        return self.cursor

    def closedb(self):
        # write MD
        self.createDBMD()

        # Save (commit) the changes
        self.conn.commit()

        # We can also close the connection if we are done with it.
        # TO be sure any changes have been committed or they will be lost.
        self.conn.close()

    @staticmethod
    def getDBFilename(export):
        return "{}{}".format(export.split(".", 1)[0], ".db")

    def sethashtype(self, hash_):
        self.hashtype = hash_

    @staticmethod
    def gettimestamp():
        return time.strftime("%Y-%m-%dT%H:%M:%S")

    def droptables(self, cursor):
        self.dropDBMDTable(cursor)
        self.dropFILEDATATable(cursor)
        self.dropIDTable(cursor)
        self.dropIDJunction(cursor)
        self.dropNSTable(cursor)

    def dropTable(self, cursor, tablename):
        # check we have a table to drop
        self.execute_create(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(
                tablename
            )
        )
        # can't drop something that doesn't exist
        if cursor.fetchone() is not None:
            self.execute_create("DROP table " + tablename + "")  # DROP just in case

    def dropDBMDTable(self, cursor):
        self.dropTable(cursor, self.METADATATABLE)

    def dropFILEDATATable(self, cursor):
        self.dropTable(cursor, self.FILEDATATABLE)

    def dropIDTable(self, cursor):
        self.dropTable(cursor, self.IDTABLE)

    def dropIDJunction(self, cursor):
        self.dropTable(cursor, self.ID_JUNCTION)

    def dropNSTable(self, cursor):
        self.dropTable(cursor, self.NAMESPACETABLE)

    def createDBMD(self):
        create = "CREATE TABLE {} (TIMESTAMP TIMESTAMP, HASH_TYPE, TOOL_TYPE)".format(
            self.METADATATABLE
        )
        self.execute_create(create)
        ins = 'INSERT INTO {} VALUES ("{}", "{}", "{}")'.format(
            self.METADATATABLE, self.timestamp, self.hashtype, self.tooltype
        )
        self.execute_create(ins)

    @staticmethod
    def createfield(table, column, type_=False):
        if type_ is not False:
            table = "{}{} {}, ".format(table, column, type_)
        else:
            table = "{}{}, ".format(table, column)
        return table

    def createfiledatatable(self):
        table = "CREATE TABLE " + self.FILEDATATABLE + " ("
        for column in self.FILEDATA_TABLE:
            if column == "LAST_MODIFIED":
                table = self.createfield(table, column, "TIMESTAMP")
            elif column == "YEAR":
                table = self.createfield(table, column, "INTEGER")
            elif column == "FILE_ID":
                table = self.createfield(table, column, "INTEGER primary key")
            elif column in ("PARENT_ID", "INPUT_ID", "SIZE"):
                table = self.createfield(table, column, "INTEGER")
            else:
                table = self.createfield(table, column)
        table = "{} FOREIGN KEY(FILE_ID) REFERENCES IDRESULTS(FILE_ID), ".format(table)
        table = table.rstrip(", ") + ")"
        self.execute_create(table)

    def createidtable(self):
        table = "CREATE TABLE " + self.IDTABLE + " ("
        for column in self.IDTABLE_TABLE:
            if column == self.IDID:
                table = self.createfield(table, column, "INTEGER PRIMARY KEY")
            elif column == self.NSID:
                table = self.createfield(table, column, "INTEGER")
            elif column == "EXTENSION_MISMATCH":
                table = self.createfield(table, column, "BOOLEAN")
            else:
                table = self.createfield(table, column)
        table = "{} FOREIGN KEY(ID_ID) REFERENCES IDRESULTS(ID_ID), ".format(table)
        table = "{} FOREIGN KEY(NS_ID) REFERENCES NSDATA(NS_ID), ".format(table)
        table = table.rstrip(", ") + ")"
        self.execute_create(table)

    def createjunctiontable(self, name, pkey1, pkey2):
        # CREATE TABLE IDRESULTS(FILE_ID INTEGER, ID_ID INTEGER, PRIMARY KEY (FILE_ID,ID_ID)) ???
        table = "CREATE TABLE " + name + "("
        table = table + pkey1 + " INTEGER, "
        table = table + pkey2 + " INTEGER, "
        table = (
            table + "PRIMARY KEY (" + pkey1 + ", " + pkey2 + ")"
        )  # composite primary key? (correct?)
        table = table.rstrip(",") + ")"
        self.execute_create(table)

    def createNStable(self):
        table = "CREATE TABLE " + self.NAMESPACETABLE + " ("
        for column in self.NS_TABLE:
            if column == self.NSID:
                table = "{}{} INTEGER PRIMARY KEY, ".format(table, column)
            else:
                table = "{}{}, ".format(table, column)
        table = "{})".format(table.rstrip(", "))
        self.execute_create(table)

    def create_indices(self):
        self.execute_create("CREATE INDEX HASH ON {} (HASH)".format(self.FILEDATATABLE))
        self.execute_create("CREATE INDEX NAME ON {} (NAME)".format(self.FILEDATATABLE))
        self.execute_create("CREATE INDEX PUID ON {} (ID)".format(self.IDTABLE))

    def execute_create(self, query):
        if self.log is not False:
            logging.info(query)
        return self.cursor.execute(query)
