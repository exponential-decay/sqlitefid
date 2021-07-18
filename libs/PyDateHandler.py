# -*- coding: utf-8 -*-

"""PYDateHandler helps to normalize the dates from the different ID
tools. While the code works, it could do with some further work to
bring it up to scratch.
"""

from __future__ import absolute_import, print_function

import datetime
import logging
import re


class PyDateHandler:
    """PyDateHandler."""

    def get_year(self, datestring):
        """Return year from given datestring."""
        if datestring != "":
            datestring = self.get_datestring_without_timezone(datestring)
        if datestring is False:
            datestring = None
        return datestring

    @staticmethod
    def get_datestring_without_timezone(date_value):
        """Return a simplified date string to the caller.

        :param datestring: full date string to simplify
        :returns: simplified date string without timezone, year if data
            isn't available, or None if a conversion cannot be made.
        """
        # If an error occurred during scanning we will get odd values.
        # This seems to be the default for when that happens.
        if date_value.startswith("0001-01-01T00:00:00"):
            return None
        newdate = None
        datestring = date_value.replace("Z", "")
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
            logging.error(
                "Problem in getYear function, likely due to timezone issues: %s", err
            )
        if newdate:
            return newdate
        testyear = datestring.split("-")[0]
        validyear = re.compile(r"^\d{4}$")
        if len(testyear) == 4 and re.search(validyear, testyear) is not None:
            newdate = int(testyear)
            logging.info(
                "Treating timestamp as a string and setting it to: %s", testyear
            )

        return newdate
