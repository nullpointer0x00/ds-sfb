import requests
from wunderground import WunderGroundApi
import datetime
import unittest


class TestParser(unittest.TestCase):
    def test_get_date_str(self):
        wg = WunderGroundApi()
        # self.assertEqual("", wg.get_date_str("not a date"))
        date = datetime.date(2002, 2, 21)
        self.assertEqual("20020221", wg.get_date_str(date))
        date = datetime.date(2002, 2, 3)
        self.assertEqual("20020203", wg.get_date_str(date))
