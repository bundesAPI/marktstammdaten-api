"""
    Marktdatenstammregister API

    Das MaStR führt die Stammdaten zu Strom- und Gaserzeugungsanlagen sowie Marktakteuren wie Anlagenbetreibern, Netzbetreibern und Energielieferanten.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.marktstammdaten.api.daten_api import DatenApi  # noqa: E501

from deutschland import marktstammdaten


class TestDatenApi(unittest.TestCase):
    """DatenApi unit test stubs"""

    def setUp(self):
        self.api = DatenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get(
        self,
    ):
        """Test case for einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get

        Erweiterte öffentliche Daten zur Stromerzeugung  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
