"""Unit tests for NTP"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestNtp(TestBase):
    """
    Unit tests for NTP
    """

    def test_get_ntp_list(self):
        """
        Test getting NTP list

        Validates that the retrieved NTP list equals to the expected NTP list
        """
        ntp_list = self.configuration.get_ntp_list()
        self.assertListEqual(ntp_list, self.ntp_data.ntp_list)

    def test_get_ntp_details(self):
        """
        Test getting NTP details

        Validates that the retrieved NTP details equals to the expected NTP details
        """
        resp = self.configuration.get_ntp_details(self.ntp_data.ntp_id)
        self.assertEqual(resp, self.ntp_data.ntp_details)

    def test_modify_ntp_details(self):
        """
        Test modifying NTP details

        Validates that the response is None
        """
        resp = self.configuration.modify_ntp_details(
            self.ntp_data.ntp_id, self.ntp_data.modify_ntp_dict,
        )
        self.assertIsNone(resp)

    def test_modify_ntp_details_with_invalid_param(self):
        """
        Test modifying NTP details with invalid parameter

        Validates that modifying NTP details with invalid parameter raises an exception
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_ntp_details,
            self.ntp_data.ntp_id,
            invalid_param,
        )
