"""Unit tests for DNS."""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestDns(TestBase):
    """
    Unit tests for DNS.
    """

    def test_get_dns_list(self):
        """
        Test get DNS list.
        
        Validates the DNS list retrieved from the configuration matches the expected DNS list.
        """
        dns_list = self.configuration.get_dns_list()
        self.assertListEqual(dns_list, self.dns_data.dns_list)

    def test_get_dns_details(self):
        """
        Test get DNS details.
        
        Verifies the DNS details retrieved from the configuration match the expected DNS details.
        """
        resp = self.configuration.get_dns_details(self.dns_data.dns_id)
        self.assertEqual(resp, self.dns_data.dns_details)

    def test_modify_dns_details(self):
        """
        Test modify DNS details.
        
        Confirms the DNS details can be modified successfully with valid parameters.
        """
        resp = self.configuration.modify_dns_details(
            self.dns_data.dns_id, self.dns_data.modify_dns_dict,
        )
        self.assertIsNone(resp)

    def test_modify_dns_details_with_invalid_param(self):
        """
        Test modify DNS details with invalid parameter.
        
        Verifies an exception is raised when modifying DNS details with an invalid parameter.
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_dns_details,
            self.dns_data.dns_id,
            invalid_param,
        )
