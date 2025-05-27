"""Unit tests for Remote Support"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestRemoteSupport(TestBase):
    """
    Unit tests for Remote Support
    """

    def test_get_remote_support_configs(self):
        """
        Test Get Remote Support Configs
        
        Validates that the remote support list matches the expected remote support list.
        """
        remote_support_list = self.configuration.get_remote_support_list()
        print(remote_support_list)
        self.assertListEqual(
            remote_support_list, self.remote_support_data.remote_support_list,
        )

    def test_get_remote_support_details(self):
        """
        Test Get Remote Support Details
        
        Validates that the remote support details match the expected remote support details.
        """
        resp = self.configuration.get_remote_support_details(
            self.remote_support_data.remote_support_id,
        )
        self.assertEqual(resp, self.remote_support_data.remote_support_details)

    def test_modify_remote_support_details(self):
        """
        Test Modify Remote Support Details
        
        Verifies that modifying the remote support details returns None.
        """
        resp = self.configuration.modify_remote_support_details(
            self.remote_support_data.remote_support_id,
            self.remote_support_data.modify_remote_support_dict,
        )
        self.assertIsNone(resp)

    def test_modify_remote_support_details_with_invalid_param(self):
        """
        Test Modify Remote Support Details with Invalid Param
        
        Confirms that modifying the remote support details with an
        invalid parameter raises a PowerStoreException.
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_remote_support_details,
            self.remote_support_data.remote_support_id,
            invalid_param,
        )

    def test_verify_remote_support_config(self):
        """
        Test Verify Remote Support Config
        
        Validates that verifying the remote support config with valid parameters returns None.
        """
        resp = self.configuration.verify_remote_support_config(
            self.remote_support_data.remote_support_id,
            self.remote_support_data.verify_remote_support_dict,
        )
        self.assertIsNone(resp)

    def test_send_test_alert_remote_support(self):
        """
        Test Send Test Alert Remote Support
        
        Verifies that sending a test alert for remote support returns None.
        """
        resp = self.configuration.test_remote_support_config(
            self.remote_support_data.remote_support_id,
        )
        self.assertIsNone(resp)
