# -*- coding: utf-8 -*-

# Disables deprecated urllib function warning where we use urllib in
# addFileURI below.
#
# Also disables import warnings as we try and import for PY2 and PY3
# together.
#
# pylint: disable=W1658,E1101,E0611,E0401

"""SFHandlerClass provides the functions needed to understand a
Siegfried YAML file so that it can be parsed into an sqlite DB.
"""

from __future__ import absolute_import

import io
import logging
import ntpath
import os.path

from .PyDateHandler import PyDateHandler


class SFYAMLHandler:
    """SFYAMLHandler."""

    YAMLSECTION = "---"
    YAMLNAMESPACE = "name"
    YAMLDETAILS = "details"

    IDENTIFIERS = "identifiers"

    HEADDETAILS = "id details"
    HEADNAMESPACE = "id namespace"
    HEADCOUNT = "identifier count"

    FILERECORDLEN = 6

    hashes = ["md5", "sha1", "sha256", "sha512", "crc"]
    file_dict_headers = [
        "filename",
        "filesize",
        "modified",
        "errors",
        "md5",
        "sha1",
        "sha256",
        "sha512",
        "crc",
    ]

    id_data_headers = ["ns", "id", "format", "version", "mime", "basis", "warning"]

    containers = {
        "zip": "x-fmt/263",
        "gz": "x-fmt/266",
        "tar": "x-fmt/265",
        "warc": "fmt/289",
        "arc": "x-fmt/219",
        "arc_1": "fmt/410",
    }
    path_indicators = [".zip#", ".gz#", ".tar#", ".warc#", ".arc#"]

    PROCESSING_ERROR = -1

    DICTHEADER = "header"
    DICTFILES = "files"
    DICTID = "identification"

    TYPE_CONTAINER = "Container"
    TYPE_FILE = "File"

    URI_SCHEME_FILE = "file"
    URI_SCHEME_CONTAINER = "container"

    # Additional fields given to SF output
    FIELD_FILE_NAME = "filename"
    FIELD_ERRORS = "errors"
    FIELD_URI_SCHEME = "uri_scheme"
    FIELD_DIR_NAME = "directory"
    FIELD_YEAR = "year"
    FIELD_CONTAINER_TYPE = "container_type"
    FIELD_TYPE = "type"
    FIELD_EXT = "ext"

    def __init__(self):
        """Constructor for SF Handler Class."""
        self.pydate = PyDateHandler()
        self.sectioncount = 0
        self.identifiercount = 0
        self.hashtype = None
        self.sfdata = {}
        self.header = {}
        self.files = []

    @property
    def filecount(self):
        """Return a count of all the files processed form a Siegfried
        report.
        """
        return len(self.files)

    @property
    def identifiers(self):
        namespaces = []
        ids = self.sfdata[self.DICTHEADER][self.HEADCOUNT]
        for idx in range(ids):
            ns = "{} {}".format(self.HEADNAMESPACE, (idx + 1))
            namespaces.append(self.sfdata[self.DICTHEADER][ns])
        return namespaces

    def get_headers(self):
        return self.sfdata[self.DICTHEADER]

    def get_files(self):
        return self.sfdata[self.DICTFILES]

    @staticmethod
    def _stripkey(line):
        line = line.strip()
        line = line.replace("- ", "")
        return line

    def _stripvalue(self, line):
        line = line.strip()
        line = line.lstrip("'").rstrip("'")
        return self._escape_value(line)

    @staticmethod
    def _escape_value(line):
        """Escape values with single quotes in them.

        Alternative for future reference:

           * http://stackoverflow.com/a/12066822)

        :params line: A line of YAML from Siegfried (string)
        :returns: Escaped version of the input line (string)
        """
        return line.replace("'", "''")

    def _handle_entry(self, line):
        """Return a processed line from a YAML entry.

        :param line: YAML entry such as "key: value" to process (string)
        :returns: Processed line (string)
        """
        line = line.split(":", 1)
        line[0] = self._stripkey(line[0])
        value = self._stripvalue(line[1])
        if value == "":
            line[1] = None
        else:
            line[1] = value
        return line

    def process_header(self, line):
        """Processes the header section of a Siegfried report.

        :param line: Line of the header section to process (string)
        :returns: None (Nonetype)
        """
        if line == self.YAMLSECTION:
            return
        line = self._handle_entry(line)
        if line[0] == self.YAMLNAMESPACE:
            self.identifiercount += 1
            ns = "{} {}".format(self.HEADNAMESPACE, self.identifiercount)
            self.header[ns] = line[1]
        elif line[0] == self.YAMLDETAILS:
            details = "{} {}".format(self.HEADDETAILS, self.identifiercount)
            self.header[details] = line[1]
            self.header[self.HEADCOUNT] = self.identifiercount
        elif line[0] != self.IDENTIFIERS:
            self.header[line[0]] = line[1]

    def process_file_section(self, sf_record):
        """Returns some information about the SF report.

        :param sf_record: A list of non-parsed records from Siegfried
            to be converted. (list[(string)])
        :returns: A file dictionary to be appended to the global file
            list. If an error was given by SF during processing the
            return is an empty dictionary for the caller to check
            against (dict)
        """

        KEY_ID = "id"
        KEY_MATCHES = "matches"
        KEY_FULL = "full"
        KEY_WARNING = "warning"

        filedict = {}
        idlist = []

        for section in sf_record:
            section = self._handle_entry(section)
            key = section[0].strip()
            try:
                value = section[1].strip()
            except AttributeError:
                # Likely a Nonetype value from the list.
                value = section[1]
            if key in self.file_dict_headers:
                filedict[key] = value
                if key in self.hashes and self.hashtype is None:
                    self.hashtype = key
            else:
                if key == KEY_ID:
                    self.add_file_type_to_file_dict(value, filedict)
                try:
                    try:
                        id_record.add_field(key, value)  # NOQA
                    except (UnboundLocalError, AttributeError):
                        # Object doesn't exist this iteration or has been
                        # reset to None so needs to be reinitialized.
                        id_record = IDResult()
                        id_record.add_field(key, value)
                except IDError as err:
                    # Field doesn't exist in the class and that might be just
                    # fine.
                    if key != KEY_MATCHES and key != KEY_FULL:
                        raise err
                if key == KEY_WARNING:
                    # Results all added to an entry... warning should be the
                    # last field. If there is any problem with that, then an
                    # ordered dictionary might be needed, or an alternative
                    # tabulation method.
                    id_record.add_field(key, value)
                    idlist.append(id_record)
                    id_record = None

        self._add_file_uri(filedict)

        # Add complete identification data to filedata, return
        filedict[self.DICTID] = idlist

        # Finally, some errors in the Siegfried report create spurious
        # file entries. Remove those here.
        if (
            filedict.get(self.FIELD_FILE_NAME, "").endswith("#")
            and filedict.get(self.FIELD_ERRORS) is not None
        ):
            logging.info(
                "SF encountered an error on: %s", filedict.get(self.FIELD_FILE_NAME, "")
            )
            filedict = {}

        return filedict

    def _process_sf(self, sf_report, filedata, processed):
        """Process a Siegfried file and return the results."""
        for line in sf_report:
            line = line.strip()
            # Guard for incorrectly formatted filenames/YAML.
            if not line.endswith("'") and line.startswith("filename"):
                line = f"{line}{next(sf_report).strip()}"
            if line == self.YAMLSECTION:
                self.sectioncount += 1
                processed = False
            if self.sectioncount == 1:
                self.process_header(line)
            elif self.sectioncount > 1:
                if processed is False and len(filedata) > 0:
                    filesec = self.process_file_section(filedata)
                    if filesec:
                        self.files.append(filesec)
                    filedata = []
                else:
                    processed = True
                    if line != self.YAMLSECTION:
                        filedata.append(line)
        return filedata

    def read_sf_yaml(self, sf_report):
        """Opens a Siegfried YAML report and processes it section by
        section.

        :param sf_report: path to a sf report on disk (string)
        :returns: a count of all the sections processed in the report
            (int)
        """
        processed = False
        filedata = []

        # Warn users if there might be a problem reading the file.
        try:
            with io.open(sf_report, "r", encoding="UTF8") as sf:
                pass
        except UnicodeDecodeError as err:
            logging.error("Unicode err: '%s', io.open errors set to 'ignore'", err)
            pass

        with io.open(sf_report, "r", encoding="UTF8", errors="ignore") as sf:
            filedata = self._process_sf(sf, filedata, processed)

        # Add final section of data to list.
        if len(filedata) > 0:
            self.files.append(self.process_file_section(filedata))

        # Add header and file details.
        self.sfdata[self.DICTHEADER] = self.header
        self.sfdata[self.DICTFILES] = self.files

        return self.sectioncount

    @staticmethod
    def get_dir_name(filepath):
        return os.path.dirname(filepath)

    @staticmethod
    def get_file_name(filepath):
        fname = os.path.basename(filepath)
        if len(fname) == len(filepath):
            # Retrieving filename probably didn't work... maybe windows
            # path.
            fname = ntpath.basename(filepath)
        return os.path.basename(fname)

    def add_dir_name(self, sfdata):
        for row in sfdata[self.DICTFILES]:
            fname = row[self.FIELD_FILE_NAME]
            row[self.FIELD_DIR_NAME] = self.get_dir_name(fname)
        return sfdata

    def add_file_name(self, sfdata):
        for row in sfdata[self.DICTFILES]:
            fname = row[self.FIELD_FILE_NAME]
            row["name"] = self.get_file_name(fname)
        return sfdata

    def add_year(self, sfdata):
        for row in sfdata[self.DICTFILES]:
            year = row["modified"]
            row[self.FIELD_YEAR] = self.get_year(year)
        return sfdata

    def get_year(self, datestring):
        return self.pydate.get_year(datestring)

    def add_extension(self, sfdata):
        for row in sfdata[self.DICTFILES]:
            name = row["name"].rsplit(".", 1)
            if len(name) == 2:
                row[self.FIELD_EXT] = name[1]
            else:
                row[self.FIELD_EXT] = ""  # no extension...
        return sfdata

    def add_file_type_to_file_dict(self, id_, filedict):
        # only set as File if and only if it isn't a Container
        # container overrides all...
        if id_ in self.containers.values():
            filedict[self.FIELD_TYPE] = self.TYPE_CONTAINER
            # get container type: http://stackoverflow.com/a/13149770
            filedict[self.FIELD_CONTAINER_TYPE] = list(self.containers.keys())[
                list(self.containers.values()).index(id_)
            ]
        else:
            if self.FIELD_TYPE in filedict:
                if filedict[self.FIELD_TYPE] != self.TYPE_CONTAINER:
                    filedict[self.FIELD_TYPE] = self.TYPE_FILE
            else:
                filedict[self.FIELD_TYPE] = self.TYPE_FILE

    def _add_file_uri(self, filedict):
        """Add file URI will eventually construct a URI out of absolute
        paths from Siegfried if they are provided, e.g. if enabled in
        SF or if a user has scanned an absolute path.

        :param filedict: filedict structure containing information
            about our file.
        :returns: None (nonetype)
        """
        file_name = filedict[self.FIELD_FILE_NAME]
        if os.path.abspath(file_name):
            logging.debug(
                "Absolute path '%s', a URI can be created from this", file_name
            )
        filedict[self.FIELD_URI_SCHEME] = self.URI_SCHEME_FILE
        if self._id_object_in_container(file_name):
            filedict[self.FIELD_URI_SCHEME] = self.URI_SCHEME_CONTAINER

    def _id_object_in_container(self, file_path):
        """Identify objects in containers using the best heuristic we
        have.

        :param file_path: Path to a file we're looking at (string)
        :returns: True or False if the path is within a container (bool)
        """
        for indicator in self.path_indicators:
            if (
                indicator in file_path
                and not file_path.startswith(indicator)
                and not file_path.endswith(indicator)
            ):
                return True
        return False


class IDError(Exception):
    """Error to raise when something has gone wrong with the IDResult
    Class.
    """


class IDResult(object):
    """Class to hold the results of an identification from Siegfried,
    whatever the namespace used.
    """

    ns = None
    id = None
    format = None
    version = None
    mime = None
    method = None
    basis = None
    warning = None
    mismatch = None
    status = None

    mismatch_warning = "extension mismatch"
    filename_only = "match on filename only"
    extension_only_one = "match on extension only"
    extension_only_two = "extension match"

    text_basis = "text match"
    byte_basis = "byte match"
    container_basis_one = "container match"
    container_basis_two = "container name"
    xml_basis = "xml match"

    def __init__(self):
        """Initialize class with specific information."""
        self.mismatch = False

    def add_field(self, field, value):
        """Add value to the class if the field exists within the class."""
        FIELD_BASIS = "basis"
        FIELD_WARNING = "warning"
        FIELD_MIME = "mime"
        FIELD_STATUS = "status"

        VALUE_UNK = "UNKNOWN"

        if not hasattr(self, field):
            raise IDError("Field '%s' doesn't exist" % field)
        if field == FIELD_STATUS:
            raise IDError("Field '%s' ('%s') shouldn't exist" % field, value)
        if field == FIELD_BASIS:
            self.method = self._get_method_for_id_record(value)
        if field == FIELD_WARNING:
            self.method = self._get_method_for_id_record(value, True)
        if field == FIELD_MIME and value == VALUE_UNK:
            value = None
        try:
            if field == FIELD_WARNING and self.mismatch_warning in value:
                self.mismatch = True
        except TypeError:
            # Value is None, ignore.
            pass
        setattr(self, field, value)

    def _get_method_for_id_record(self, basis, warning=False):
        """Return method of identification from the export.

        :param basis: Usually the basis or warning field from the sf
            export. (string)
        :param: Warning field to identify if we're looking at the warning
            field. (bool)
        :return: identification method (string)
        """
        METHOD_SIG = "Signature"
        METHOD_CONT = "Container"
        METHOD_XML = "XML"
        METHOD_TEXT = "Text"
        METHOD_FILENAME = "Filename"
        METHOD_EXT = "Extension"

        if self.method is not None:
            return self.method
        if warning is False and basis is not None:
            if self.container_basis_one in basis or self.container_basis_two in basis:
                return METHOD_CONT
            elif self.byte_basis in basis:
                return METHOD_SIG
            elif self.xml_basis in basis:
                return METHOD_XML
            elif self.text_basis in basis:
                return METHOD_TEXT
            elif self.extension_only_two in basis:
                return METHOD_EXT
        elif warning is True and basis is not None:
            if self.filename_only in basis:
                return METHOD_FILENAME
            elif self.extension_only_one in basis:
                return METHOD_EXT
        else:
            return None

    def to_csv_list(self, ns_id=1):
        """Convert data to a CSV list suitable for placing in the sqlite
        database.

        The insert requires a string, for the headers:

            'ID, FORMAT_NAME, FORMAT_VERSION, MIME_TYPE,
             METHOD, BASIS, WARNING, NS_ID'
        """
        return "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(
            self.id,
            self.format,
            self.version,
            self.mime,
            self.method,
            self.basis,
            self.warning,
            self.mismatch,
            self.status,
            ns_id,
        )

    def __eq__(self, other):
        """Equality comparison for IDRecord class."""
        if self.ns != other.ns:
            return False
        if self.id != other.id:
            return False
        if self.format != other.format:
            return False
        if self.version != other.version:
            return False
        if self.mime != other.mime:
            return False
        if self.method != other.method:
            return False
        if self.basis != other.basis:
            return False
        if self.warning != other.warning:
            return False
        if self.mismatch != other.mismatch:
            return False
        if self.status != other.status:
            return False
        return True
