#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import argparse
import os
import sys
import time

if __name__ == "__main__":
    from libs.DROIDLoaderClass import DROIDLoader
    from libs.FidoLoaderClass import FidoLoader
    from libs.GenerateBaselineDBClass import GenerateBaselineDB
    from libs.IdentifyExportClass import IdentifyExport
    from libs.SFLoaderClass import SFLoader
    from libs.Version import SqliteFIDVersion
else:
    from sqlitefid.libs.DROIDLoaderClass import DROIDLoader
    from sqlitefid.libs.FidoLoaderClass import FidoLoader
    from sqlitefid.libs.GenerateBaselineDBClass import GenerateBaselineDB
    from sqlitefid.libs.IdentifyExportClass import IdentifyExport
    from sqlitefid.libs.SFLoaderClass import SFLoader
    from sqlitefid.libs.Version import SqliteFIDVersion


def identifyinput(export):
    id_ = IdentifyExport()
    type_ = id_.exportid(export)
    if type_ == id_.DROIDTYPE:
        return handleDROIDCSV(export)
    elif type_ == id_.DROIDTYPEBOM:
        return handleDROIDCSV(export, True)
    elif type_ == id_.SFTYPE:
        return handleSFYAML(export)
    elif type_ == id_.FIDOTYPE:
        return handleFIDOCSV(export)
    elif type_ == id_.SFCSVTYPE:
        sys.stderr.write("Siegfried CSV. Not currently handled.")
    elif type_ == id_.UNKTYPE:
        sys.stderr.write("Unknown export type.")
        return None


def handleDROIDCSV(droidcsv, BOM=False):
    global basedb
    basedb = GenerateBaselineDB(droidcsv)
    loader = DROIDLoader(basedb, BOM)
    loader.droidDBSetup(droidcsv, basedb.getcursor())
    basedb.closedb()
    return basedb.dbname


def handleSFYAML(sfexport):
    global basedb
    basedb = GenerateBaselineDB(sfexport)
    loader = SFLoader(basedb)
    loader.sfDBSetup(sfexport, basedb.getcursor())
    basedb.closedb()
    return basedb.dbname


def handleFIDOCSV(fidoexport):
    # global basedb
    # basedb = GenerateBaselineDB(fidoexport)
    basedb = None
    loader = FidoLoader(basedb)
    loader.fidoDBSetup(fidoexport, None)
    # loader.fidoDBSetup(fidoexport, basedb.getcursor())
    # basedb.closedb()
    # return basedb.dbname


def outputtime(start_time):
    sys.stderr.write("\n" + "--- %s seconds ---" % (time.time() - start_time) + "\n")


def main():

    # 	Usage: 	--csv [droid report]
    # 	Handle command line arguments for the script
    parser = argparse.ArgumentParser(
        description="Place DROID profiles into a SQLite DB"
    )
    parser.add_argument(
        "--export", "--droid", "--sf", help="Optional: Single tool export to read."
    )
    parser.add_argument(
        "--version", help="Optional: Output version number.", action="store_true"
    )

    start_time = time.time()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # 	Parse arguments into namespace object to reference later in the script
    global args
    args = parser.parse_args()

    if args.version:
        v = SqliteFIDVersion()
        sys.stdout.write(v.getVersion() + "\n")
        sys.exit(1)

    if args.export:
        if os.path.isfile(args.export):
            identifyinput(args.export)
            outputtime(start_time)
        else:
            sys.exit("Exiting: Not a file.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
