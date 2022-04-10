# -*- coding: utf-8 -*-

# Disable pylint warnings for CSVHandlerClass imports which are not
# straightforward as we try and handle PY2 and PY3.
#
# pylint: disable=E0611,E0401

"""sqlitefid is the primary entry point for the sqlitefid application.
The application takes a format identification report, e.g. DROID or
Siegfried and maps it to a sqlite database for higher performance
analysis of format identification results.
"""

from __future__ import absolute_import

import argparse
import logging
import os
import sys
import time

from .libs.DROIDLoaderClass import DROIDLoader
from .libs.FidoLoaderClass import FidoLoader
from .libs.GenerateBaselineDBClass import GenerateBaselineDB
from .libs.IdentifyExportClass import IdentifyExport
from .libs.SFLoaderClass import SFLoader
from .libs.Version import SqliteFIDVersion

LOGFORMAT = "%(asctime)-15s %(levelname)s: %(message)s"
DATEFORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(format=LOGFORMAT, datefmt=DATEFORMAT, level="INFO")

args = None


def identify_and_process_input(report_path):
    """Identify an input from a given path and process the results if
    there is support.

    :param report_path: path to a format identification report (String)
    :return: path to the processed sqlite3 database (String)
    """
    export = report_path
    id_ = IdentifyExport()
    type_ = id_.exportid(export)
    if type_ == id_.DROIDTYPE:
        return handleDROIDCSV(export)
    if type_ == id_.DROIDTYPEBOM:
        return handleDROIDCSV(export, True)
    if type_ == id_.SFTYPE:
        return handleSFYAML(export)
    if type_ == id_.FIDOTYPE:
        return handleFIDOCSV(export)
    if type_ == id_.SFCSVTYPE:
        logging.info("Siegfried CSV. Not currently handled")
        return None
    if type_ == id_.UNKTYPE:
        logging.info("Unknown export type")
        return None


def handleDROIDCSV(droidcsv, BOM=False):
    debug = False
    try:
        debug = args.debug
    except AttributeError:
        pass
    basedb = GenerateBaselineDB(droidcsv, debug)

    loader = DROIDLoader(basedb, BOM, debug=debug)
    loader.create_droid_database(droidcsv, basedb.getcursor())
    basedb.closedb()
    return basedb.dbname


def handleSFYAML(sfexport):
    debug = False
    try:
        debug = args.debug
    except AttributeError:
        pass
    basedb = GenerateBaselineDB(sfexport, debug)
    loader = SFLoader(basedb)
    loader.create_sf_database(sfexport, basedb.getcursor())
    basedb.closedb()
    return basedb.dbname


def handleFIDOCSV(fidoexport):
    basedb = None
    loader = FidoLoader(basedb)
    loader.fido_db_setup(fidoexport, None)


def outputtime(start_time):
    logging.info("Process took: %s seconds", (time.time() - start_time))


def main():
    """Primary entry point for sqlitefid."""

    # 	Usage: 	--csv [droid report]
    # 	Handle command line arguments for the script
    parser = argparse.ArgumentParser(
        description="Place DROID profiles into a SQLite DB"
    )
    parser.add_argument(
        "--export", "--droid", "--sf", help="Optional: Single tool export to read."
    )
    parser.add_argument(
        "--debug", help="Optional: Log SQL queries", action="store_true"
    )
    parser.add_argument(
        "--version", help="Optional: Output version number.", action="store_true"
    )

    start_time = time.time()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    global args
    args = parser.parse_args()

    if args.version:
        v = SqliteFIDVersion()
        print(v.getVersion())
        sys.exit(1)

    if not args.export:
        sys.exit(0)

    if not os.path.isfile(args.export):
        logging.error("Not a file: %s", args.export)
        sys.exit(1)

    identify_and_process_input(args.export)
    outputtime(start_time)


if __name__ == "__main__":
    main()
