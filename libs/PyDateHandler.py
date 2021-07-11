# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import datetime
import re
import sys


class PyDateHandler:
    def getYear(self, datestring):
        if datestring != "":
            datestring = self.get_datestring_without_timezone(datestring)
        if datestring is False:
            datestring = None
        return datestring

    def get_datestring_without_timezone(self, datestring):
        """Return a simplified date string to the caller.

        :param datestring: full date string to simplify
        :returns: simplified date string without timezone, year if data
            isn't available, or None if a conversion cannot be made.

        # TODO: This whole function needs some work...
        #
        """
        newdate = False
        datestring = datestring.replace("Z", "")
        if len(datestring) == len("0000-00-00T00:00:00+00:00"):
            if "+" in datestring:
                # sf example: 2016-04-02T20:45:12+13:00
                datestring = datestring.rsplit("+", 1)[0]
            else:
                # sf example: 2016-04-02T20:45:12-04:00
                datestring = datestring.rsplit("-", 1)[0]
        try:
            newdate = int(
                datetime.datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S").year
            )
        except ValueError as err:
            print(
                "Problem in getYear function, likely due to timezone issues:",
                err,
                file=sys.stderr,
            )

        if newdate is not False:
            return newdate

        newdate = None
        testyear = datestring.split("-")[0]
        validyear = re.compile(r"^\d{4}$")
        if len(testyear) == 4 and re.search(validyear, testyear) is not None:
            newdate = int(testyear)
            print("Treating timestamp as a string and setting it to:", testyear)

        return newdate
