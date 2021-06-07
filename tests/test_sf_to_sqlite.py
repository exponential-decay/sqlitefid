# -*- coding: utf-8 -*-

import sys

import pytest

from libs import PyDateHandler
from libs import SFHandlerClass

@pytest.mark.parametrize(
    "date_string, year",
    [
        ("2016-01-01T20:45:12+13:00", 2016),
        ("2015-01-01T20:45:12-04:00", 2015),
        ("2015-01-01T20:45:12", 2015),
        ("nonsense-data", None),
        ("1999-01-01T20:45:12$04:00", 1999),
        ("2014-02-22T15:14:00", 2014),
    ]
)
def test_get_datestring_without_timezone(date_string, year):
    datehandler = PyDateHandler.PyDateHandler()
    res = datehandler.get_datestring_without_timezone(date_string)
    assert res == year


@pytest.mark.parametrize(
    "date_string, year",
    [
        ("2016-01-01T20:45:12+13:00", 2016),
        ("2015-01-01T20:45:12-04:00", 2015),
        ("2014-02-22T15:14:00", 2014),
        ("nonsense-data", None),
    ]
)
def test_getYear(date_string, year):
    sfhandler = SFHandlerClass.SFYAMLHandler()
    res = sfhandler.getYear(date_string)
    assert res == year
