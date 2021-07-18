# -*- coding: utf-8 -*-

# Disable pylint warnings for CSVHandlerClass imports which are not
# straightforward as we try and handle PY2 and PY3.
#
# pylint: disable=E0611,E0401

"""SFLoaderClass is responsible for placing much of the Siegfried data
into the sqlite db.
"""

from __future__ import absolute_import

import logging

if __name__.startswith("sqlitefid"):
    from sqlitefid.libs.SFHandlerClass import SFYAMLHandler
    from sqlitefid.libs.ToolMappingClass import ToolMapping
else:
    from libs.SFHandlerClass import SFYAMLHandler
    from libs.ToolMappingClass import ToolMapping


class SFLoader:
    """SFLoader."""

    basedb = ""
    identifiers = ""

    def __init__(self, basedb):
        self.basedb = basedb

    def insertfiledbstring(self, keys, values):
        ins = "INSERT INTO {} ({}) VALUES ({});".format(
            self.basedb.FILEDATATABLE, keys.strip(", "), values.strip(", ")
        )
        return ins

    def insertiddbstring(self, keys, values):
        ins = "INSERT INTO {} ({}) VALUES ({});".format(
            self.basedb.IDTABLE, keys.strip(", "), values.strip(", ")
        )
        return ins

    def file_id_junction_insert(self, file, id_):
        ins = "INSERT INTO {} ({}, {}) VALUES ({}, {});".format(
            self.basedb.ID_JUNCTION, self.basedb.FILEID, self.basedb.IDID, file, id_
        )
        return ins

    def addDirsToDB(self, dirs, cursor):
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
            ins = "INSERT INTO {} (FILE_PATH, DIR_NAME, NAME,SIZE, TYPE) VALUES ('{}', '{}', '{}', 0, 'Folder');".format(
                self.basedb.FILEDATATABLE, dir_, dir_, name
            )
            cursor.execute(ins)

    def handleID(self, idsection, idkeystring, idvaluestring, nsdict):
        idk = []
        idv = []
        for x in self.identifiers:
            for key, value in idsection[x].items():
                if key in ToolMapping.SF_ID_MAP:
                    idkeystring = idkeystring + ToolMapping.SF_ID_MAP[key] + ", "
                    idvaluestring = "{}'{}', ".format(idvaluestring, value)
                # unmapped: Basis and Warning
            if x in nsdict:
                idkeystring = idkeystring + self.basedb.NSID
                idvaluestring = "{}{}".format(idvaluestring, nsdict[x])
            else:
                logging.error(
                    "Issue with namespace dictionary table, can't find: %s", x
                )
            idk.append(idkeystring.strip(", "))
            idv.append(idvaluestring.strip(", "))
            idkeystring = ""
            idvaluestring = ""
        return idk, idv

    def populateNStable(self, sf, cursor, header):
        nsdict = {}
        # N.B. Not handling: sig.sig name
        # N.B. Not handling: scandate
        # N.B. Not handling: siegfried version
        count = header[sf.HEADCOUNT]
        nstext = sf.HEADNAMESPACE
        detailstext = sf.HEADDETAILS
        for h in range(count):
            no = h + 1
            ns = "{}{}".format(nstext, no)
            details = "{}{}".format(detailstext, no)
            ins = "INSERT INTO {} (NS_NAME, NS_DETAILS) VALUES ('{}', '{}');".format(
                self.basedb.NAMESPACETABLE, header[ns], header[details]
            )
            cursor.execute(ins)
            nsdict[str(header[ns])] = cursor.lastrowid
        return nsdict

    def handledirectories(self, dirs, sf, count=False):
        newlist = []
        dirset = set(dirs)
        for d in dirset:
            newlist.append(sf.getDirName(d))
        newlist = set(newlist)
        dirset = list(dirset) + list(newlist)
        if count is False:
            return self.handledirectories(dirset, sf, len(dirset))
        if len(dirset) != count:
            return self.handledirectories(dirset, sf, len(dirset))
        return dirset

    def create_sf_database(self, sfexport, cursor):
        sf = SFYAMLHandler()
        sf.readSFYAML(sfexport)

        headers = sf.getHeaders()
        self.basedb.tooltype = "siegfried: {}".format(headers["siegfried"])

        sfdata = sf.sfdata

        sf.addfilename(sfdata)
        sf.adddirname(sfdata)
        sf.addYear(sfdata)
        sf.addExt(sfdata)

        self.identifiers = sf.getIdentifiersList()
        nsdict = self.populateNStable(sf, cursor, headers)

        dirlist = []

        # Awkward structures to navigate----------#
        # sf.sfdata['header']                     #
        # sf.sfdata['files']                      #
        # sf.sfdata['files'][0]['identification'] #
        # ----------------------------------------#
        for f in sf.getFiles():
            filekeystring = ""
            filevaluestring = ""
            idkeystring = ""
            idvaluestring = ""
            for key, value in f.items():
                if key in ToolMapping.SF_FILE_MAP:
                    filekeystring = filekeystring + ToolMapping.SF_FILE_MAP[key] + ", "
                    if not isinstance(value, int):
                        if not isinstance(value, str):
                            tmp = value.encode("utf-8")
                        else:
                            tmp = value
                    else:
                        tmp = value
                    filevaluestring = "{}'{}', ".format(filevaluestring, tmp)
                if key == sf.FIELDDIRNAME:
                    dirlist.append(value)
                else:
                    if key == sf.DICTID:
                        idkey, idvalue = self.handleID(
                            value, idkeystring, idvaluestring, nsdict
                        )

            fileid = None

            if filekeystring != "" and filevaluestring != "":
                cursor.execute(self.insertfiledbstring(filekeystring, filevaluestring))
                fileid = cursor.lastrowid

            insert = []
            for idx, value in enumerate(idkey):
                insert.append(
                    self.insertiddbstring("".join(value), "".join(idvalue[idx]))
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
        self.addDirsToDB(uniquedirs, cursor)
