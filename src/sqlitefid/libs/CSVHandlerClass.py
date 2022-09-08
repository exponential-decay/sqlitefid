# -*- coding: utf-8 -*-

# Disable pylint warnings for CSVHandlerClass imports which are not
# straightforward as we try and handle PY2 and PY3.
#
# pylint: disable=E0611,E0401

"""CSVHandlerClass

Handles the CSV inputs for demystify.
"""

from __future__ import absolute_import

import logging
import os.path
from urllib.parse import urlparse

from . import unicodecsv
from .PyDateHandler import PyDateHandler


class CSVExportException(Exception):
    """Exception when a CSV file cannot be parsed."""


class GenericCSVHandler:
    """GenericCSVHandler."""

    BOM = False
    BOMVAL = "\xEF\xBB\xBF"
    DICT_FORMATS = "FORMATS"

    def __init__(self, BOM=False):
        self.BOM = BOM

    @staticmethod
    def _getCSVheaders(header_row):
        """Retrieve CSV headers from first row."""
        header_list = []
        for header in header_row:
            header_list.append(header)
        return header_list

    def _csv_to_list(self, csvfile):
        """ConvertCSV to list.

        :param csv_file_stream: ...

        :returns: ...
        """
        columncount = 0
        csvlist = []
        if self.BOM is not True:
            logging.info(csvlist)
            return csvlist
        csvfile.seek(0)
        csvreader = unicodecsv.reader(csvfile)
        for row in csvreader:
            if csvreader.line_num == 1:  # not zero-based index
                header_list = self._getCSVheaders(row)
                columncount = len(header_list)
            else:
                csv_dict = {}
                # for each column in header
                # note: don't need ID data. Ignoring multiple ID.
                for i in range(columncount):
                    csv_dict[header_list[i]] = row[i]
                csvlist.append(csv_dict)
        logging.info(csvlist)
        return csvlist

    def csvaslist(self, csv_path):
        """Returns a list of dictionaries having parsed the input CSV.

        :param csv_path: Path to a CSV file to parse and convert to a
            list.

        :returns: parsed CSV list (list), CSVExportException if the CSV
            cannot be read.
        """
        if not os.path.isfile(csv_path):
            raise CSVExportException("CSV file '{}' does not exist".format(csv_path))
        logging.info("Creating CSV as Python list from input: '%s'", csv_path)
        with open(csv_path, "r") as csvfile:
            return self._csv_to_list(csvfile)

    def csvaslist_DROID(self, csv_file_name):
        """Return CSV as a list from a DROID report.

        :param csv_file_name: filename of the file to open (string)
        :returns: list containing the CSV contents (list)
        """
        MULTIPLE = False
        FORMAT_COUNT = 13  # index of FORMAT_COUNT
        multi_fields = ["ID", "MIME_TYPE", "FORMAT_NAME", "FORMAT_VERSION"]
        multilist = []

        columncount = 0
        csvlist = None
        if os.path.isfile(csv_file_name):
            csvlist = []
            with open(csv_file_name, "r", encoding="UTF-8") as csvfile:

                if self.BOM is True:
                    csvfile.seek(len(self.BOMVAL))

                # inspect line by reading it first.
                for lineno, line in enumerate(csvfile):

                    # check line for characters we can't parse...
                    line = self.checkline(line, lineno)

                    # create a dict to store row information
                    csv_dict = {}

                    # read each line into a unicode csv reader
                    csvreader = unicodecsv.reader(line.splitlines())

                    # first we need to retrieve the header information from the first line
                    if lineno == 0:
                        for row in csvreader:
                            header_list = self._getCSVheaders(row)
                            columncount = len(header_list)

                    for row in csvreader:

                        # for each column in header
                        # note: don't need ID data. Ignoring multiple ID.
                        for i in range(columncount):
                            if i == FORMAT_COUNT:
                                if row[i] != u"":
                                    count = int(row[i])
                                else:
                                    count = 0

                                csv_dict[header_list[i]] = count

                                # exception for multiple ids
                                if count > 1:
                                    MULTIPLE = True
                                    max_fields = len(multi_fields) * count

                                    # continue to put the remainder of the content into a dict
                                    format_list = row[FORMAT_COUNT + 1 :]
                                    format_list = format_list[:max_fields]

                                    while count > 0:
                                        mfields = multi_fields
                                        mdict = {}
                                        for idx, t in enumerate(mfields):
                                            mdict[t] = '"{}"'.format(format_list[idx])
                                        format_list = format_list[len(mfields) :]
                                        multilist.append(mdict)
                                        count -= 1

                                    # break for loop after cycling through remainder
                                    # for loop controls regular number of columns (count)
                                    # while loop takes us the into an exception mechanism negating that
                                    break
                            else:
                                try:
                                    csv_dict[header_list[i]] = row[i]
                                except IndexError:
                                    logging.error(
                                        "Row len too short. Cannot write row: %s", row
                                    )
                                    break

                        # continue with exception and add new dict to primary dict
                        if MULTIPLE is True:
                            csv_dict[self.DICT_FORMATS] = multilist
                            multilist = []

                        # add list and reset variables
                        csvlist.append(csv_dict)
                        MULTIPLE = False

        return csvlist

    @staticmethod
    def checkline(line, lineno):
        if "\x00" in line:
            logging.error(
                "CSV line %s contains null byte '\\x00'. Replacing with an empty string.\n",
                (lineno + 1),
            )
            line = line.replace("\x00", "")
        return line


class DroidCSVHandler:
    """DroidCSVHandler."""

    def __init__(self):
        # date handler class
        self.pydate = PyDateHandler()
        self.csv = None
        self.DICT_FORMATS = None

    def readDROIDCSV(self, droidcsvfname, BOM=False):
        csvhandler = GenericCSVHandler(BOM)
        self.DICT_FORMATS = csvhandler.DICT_FORMATS
        self.csv = csvhandler.csvaslist_DROID(droidcsvfname)
        return self.csv

    @staticmethod
    def getDirName(filepath):
        return os.path.dirname(filepath)

    def adddirname(self, droid_list):
        for row in droid_list:
            row["DIR_NAME"] = self.getDirName(row["FILE_PATH"])
        return droid_list

    def addurischeme(self, droid_list):
        for row in droid_list:
            row["URI_SCHEME"] = self.get_uri_scheme(row["URI"])
        return droid_list

    def getYear(self, datestring):
        return self.pydate.get_year(datestring)

    def addYear(self, droid_list):
        for row in droid_list:
            if row["LAST_MODIFIED"] != "":
                row["YEAR"] = self.getYear(row["LAST_MODIFIED"])
        return droid_list

    def removecontainercontents(self, droid_list):
        new_list = []  # naive remove causes loop to skip items
        for row in droid_list:
            if self.get_uri_scheme(row["URI"]) == "file":
                new_list.append(row)
        return new_list

    @staticmethod
    def removefolders(droid_list):
        """Remove folders from existing DROID list.

        :param droid_list: DROID export as CSV (list)
        :returns: list containing entries that aren't folders (list)
        """
        new_list = []  # naive remove causes loop to skip items
        for row in droid_list:
            if row["TYPE"] != "Folder":
                new_list.append(row)
        return new_list

    @staticmethod
    def retrievefolderlist(droid_list):
        """Return a list of folder file paths from a DROID list.

        :param droidlist: DROID export as CSV (list)
        :returns: list containing folder file paths (list)
        """
        new_list = []
        for row in droid_list:
            if row["TYPE"] == "Folder":
                new_list.append(row["FILE_PATH"])
        return new_list

    @staticmethod
    def retrievefoldernames(droid_list):
        """Return a list of folder names from a DROID list.

        :param droidlist: DROID export as CSV (list)
        :returns: list containing folder names from DROID export (list)
        """
        new_list = []
        for row in droid_list:
            if row["TYPE"] == "Folder":
                new_list.append(row["NAME"])
        return new_list

    @staticmethod
    def get_uri_scheme(url):
        """Return URI scheme from given URL.

        :param url: URL to return scheme for, e.g. HTTP:// FTP://
            (string)
        :returns: URL scheme (string)
        """
        return urlparse(url).scheme
