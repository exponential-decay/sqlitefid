# -*- coding: utf-8 -*-

# Disable pylint warnings for CSVHandlerClass imports which are not
# straightforward as we try and handle PY2 and PY3.
#
# pylint: disable=E0611,E0401

"""SFLoaderClass is responsible for placing much of the Siegfried data
into the sqlite db.
"""

from __future__ import absolute_import

# Required imports for main from root.
from .SFHandlerClass import SFYAMLHandler
from .ToolMappingClass import ToolMapping


class SFLoader:
    """SFLoader class contains functions needed to systematically
    walk through a parsed Siegfried export and load that information
    into a sqlite database.
    """

    basedb = ""
    identifiers = ""

    def __init__(self, basedb):
        self.basedb = basedb

    def insert_file_db_string(self, keys, values):
        ins = "INSERT INTO {} ({}) VALUES ({});".format(
            self.basedb.FILEDATATABLE, keys.strip(", "), values.strip(", ")
        )
        return ins

    def insert_id_db_string(self, keys, values):
        ins = "INSERT INTO {} ({}) VALUES ({});".format(
            self.basedb.IDTABLE, keys.strip(", "), values.strip(", ")
        )
        return ins

    def file_id_junction_insert(self, file, id_):
        ins = "INSERT INTO {} ({}, {}) VALUES ({}, {});".format(
            self.basedb.ID_JUNCTION, self.basedb.FILEID, self.basedb.IDID, file, id_
        )
        return ins

    def add_dirs_to_db(self, dirs, cursor):
        """Insert a directory entry from the Siegfried report into the
        database.
        """
        for dir_ in dirs:
            if "/" not in dir_:
                name = dir_.rsplit("\\", 1)
            else:
                name = dir_.rsplit("/", 1)
            try:
                name = name[1]
            except IndexError:
                name = dir_
            ins = u"INSERT INTO {0} (FILE_PATH, DIR_NAME, NAME,SIZE, TYPE) VALUES ('{1}', '{1}', '{2}', 0, 'Folder');".format(
                self.basedb.FILEDATATABLE, dir_, name
            )
            cursor.execute(ins)

    def generate_id_insert(self, id_records, namespace_dict):
        """Generate the information needed to become an insert statement
        for sqlite. The general form 'INSERT INTO {} () VALUES ();' is
        required by the caller, and so we generate two lists that can
        then be used to build that.

        :param id_records: List of identification records that all need
            adding to the IDDATA table in the database (list)
        :param namespace_dict: Lookup table of ID sources, e.g. LOC,
            PRONOM etc. and indices (dict)
        :return: header_list (list), value_list (list)
        """

        header_list = []
        value_list = []

        HEADERS = "ID, FORMAT_NAME, FORMAT_VERSION, MIME_TYPE, METHOD, BASIS, WARNING, EXTENSION_MISMATCH, STATUS, NS_ID"

        for id_ in id_records:
            header_list.append(HEADERS)
            value_list.append(id_.to_csv_list(namespace_dict.get(id_.ns)))

        return header_list, value_list

    def populate_namespace_table(self, sf, cursor, header):
        nsdict = {}
        count = header[sf.HEADCOUNT]
        nstext = sf.HEADNAMESPACE
        detailstext = sf.HEADDETAILS
        for idx in range(1, count + 1):
            ns = "{} {}".format(nstext, idx)
            details = "{} {}".format(detailstext, idx)
            ins = "INSERT INTO {} (NS_NAME, NS_DETAILS) VALUES ('{}', '{}');".format(
                self.basedb.NAMESPACETABLE, header[ns], header[details]
            )
            cursor.execute(ins)
            nsdict[str(header[ns])] = cursor.lastrowid
        return nsdict

    def handle_directories(self, dirs, sf, count=False):
        newlist = []
        dirset = set(dirs)
        for dir_ in dirset:
            newlist.append(sf.getDirName(dir_))
        newlist = set(newlist)
        dirset = list(dirset) + list(newlist)
        if count is False:
            return self.handle_directories(dirset, sf, len(dirset))
        if len(dirset) != count:
            return self.handle_directories(dirset, sf, len(dirset))
        return dirset

    def create_sf_database(self, sf_export, cursor):
        """Generate the insert commands and execute them on an sqlite
        instance to create the analysis database.
        """
        sf = SFYAMLHandler()
        sf.read_sf_yaml(sf_export)

        headers = sf.get_headers()
        self.basedb.tooltype = "siegfried: {}".format(headers["siegfried"])

        sfdata = sf.sfdata

        sf.add_file_name(sfdata)
        sf.add_dir_name(sfdata)
        sf.add_year(sfdata)
        sf.add_extension(sfdata)

        nsdict = self.populate_namespace_table(sf, cursor, headers)

        dirlist = []

        for file_entry in sf.get_files():
            filekeystring = ""
            filevaluestring = ""

            for key, value in file_entry.items():
                if key in ToolMapping.SF_FILE_MAP:
                    filekeystring = "{}{}, ".format(
                        filekeystring, ToolMapping.SF_FILE_MAP[key]
                    )
                    try:
                        if not isinstance(value, str):
                            val = value.encode("utf-8")
                        else:
                            val = value
                    except AttributeError:
                        val = value
                    filevaluestring = "{}'{}', ".format(filevaluestring, val)
                if key == sf.FIELD_DIR_NAME:
                    dirlist.append(value)
                    continue
                if key == sf.DICTID:
                    idkey, idvalue = self.generate_id_insert(
                        id_records=value, namespace_dict=nsdict
                    )

            fileid = None

            if filekeystring != "" and filevaluestring != "":
                ins = self.insert_file_db_string(filekeystring, filevaluestring)
                cursor.execute(ins)
                fileid = cursor.lastrowid

            insert = []
            for idx, value in enumerate(idkey):
                insert.append(
                    self.insert_id_db_string("".join(value), "".join(idvalue[idx]))
                )

            rowlist = []
            for i in insert:
                cursor.execute(i)
                rowlist.append(cursor.lastrowid)

            for rowid in rowlist:
                cursor.execute(self.file_id_junction_insert(fileid, rowid))

            if sf.hashtype is not False:
                self.basedb.hashtype = sf.hashtype

        # Finally, add directories to the file table.
        uniquedirs = set(dirlist)
        self.add_dirs_to_db(uniquedirs, cursor)
