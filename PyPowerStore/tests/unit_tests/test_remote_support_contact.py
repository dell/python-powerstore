"""Unit tests for Remote Support Contact"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestRemoteSupportContact(TestBase):
    """
    Unit tests for Remote Support Contact
    """

    def test_get_remote_support_contact_configs(self):
        """
        Test Get Remote Support Contact Configs

        Validates that the remote support contact list matches to the expected list
        """
        remote_support_contact_list = (
            self.configuration.get_remote_support_contact_list()
        )
        self.assertListEqual(
            remote_support_contact_list,
            self.remote_support_contact_data.remote_support_contact_list,
        )

    def test_get_remote_support_contact_details(self):
        """
        Test Get Remote Support Contact Details

        Validates that the remote support contact details matches to the expected details
        """
        resp = self.configuration.get_remote_support_contact_details(
            self.remote_support_contact_data.remote_support_contact_id,
        )
        self.assertEqual(
            resp, self.remote_support_contact_data.remote_support_contact_details,
        )

    def test_modify_remote_support_contact_details(self):
        """
        Test Modify Remote Support Contact Details

        Validates that modifying remote support contact details returns None
        """
        resp = self.configuration.modify_remote_support_contact_details(
            self.remote_support_contact_data.remote_support_contact_id,
            self.remote_support_contact_data.modify_remote_support_contact_dict,
        )
        self.assertIsNone(resp)

    def test_modify_remote_support_contact_details_with_invalid_param(self):
        """
        Test Modify Remote Support Contact Details With Invalid Param

        Confirms that modifying remote support contact details with
        invalid param raises PowerStoreException
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_remote_support_contact_details,
            self.remote_support_contact_data.remote_support_contact_id,
            invalid_param,
        )
