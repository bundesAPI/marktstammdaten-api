"""
    Marktdatenstammregister API

    Das MaStR führt die Stammdaten zu Strom- und Gaserzeugungsanlagen sowie Marktakteuren wie Anlagenbetreibern, Netzbetreibern und Energielieferanten.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.marktstammdaten.model.filter_list_object_inner import (
    FilterListObjectInner,
)

from deutschland import marktstammdaten

globals()["FilterListObjectInner"] = FilterListObjectInner
from deutschland.marktstammdaten.model.filter import Filter


class TestFilter(unittest.TestCase):
    """Filter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFilter(self):
        """Test Filter"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Filter()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
