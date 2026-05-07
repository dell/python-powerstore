"""Unit tests for SMTP Config"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestSmtpConfig(TestBase):
    """
    Unit tests for SMTP Config
    """

    def test_get_smtp_configs(self):
        """
        Test Get SMTP Configs
        
        Validates that the list of SMTP configs matches the expected list
        """
        smtp_list = self.configuration.get_smtp_configs()
        print(smtp_list)
        self.assertListEqual(smtp_list, self.smtp_config_data.smtp_list)

    def test_get_smtp_config_details(self):
        """
        Test Get SMTP Config Details
        
        Validates that the SMTP config details match the expected details
        """
        resp = self.configuration.get_smtp_config_details(self.smtp_config_data.smtp_id)
        self.assertEqual(resp, self.smtp_config_data.smtp_details)

    def test_modify_smtp_config_details(self):
        """
        Test Modify SMTP Config Details
        
        Validates that the response is None
        """
        resp = self.configuration.modify_smtp_config_details(
            self.smtp_config_data.smtp_id, self.smtp_config_data.modify_smtp_dict,
        )
        self.assertIsNone(resp)

    def test_modify_smtp_config_details_with_invalid_param(self):
        """
        Test Modify SMTP Config Details with Invalid Param
        
        Verifies that modifying SMTP config details with an invalid parameter raises an exception
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_smtp_config_details,
            self.smtp_config_data.smtp_id,
            invalid_param,
        )

    def test_send_test_mail_smtp_config(self):
        """
        Test Send Test Mail SMTP Config
        
        Confirms that response is None
        """
        resp = self.configuration.test_smtp_config(
            self.smtp_config_data.smtp_id, self.smtp_config_data.test_smtp_dict,
        )
        self.assertIsNone(resp)
