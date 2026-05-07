"""Unit tests for Security Config"""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestSecurityConfig(TestBase):
    """
    Unit tests for Security Config
    """

    def test_get_security_configs(self):
        """
        Test Get Security Configs
        
        Validates that security config list matches expected list
        """
        security_config_list = self.configuration.get_security_configs()
        self.assertListEqual(
            security_config_list, self.security_config_data.security_config_list,
        )

    def test_get_security_config_details(self):
        """
        Test Get Security Config Details
        
        Validates that security config details match expected details
        """
        security_config_details = self.configuration.get_security_config_details(
            self.security_config_data.security_config_id_1,
        )
        self.assertEqual(
            security_config_details, self.security_config_data.security_config_details_1,
        )

    def test_get_invalid_security_config_details(self):
        """
        Test Get Invalid Security Config Details
        
        Verifies that an exception is raised when getting invalid security config details
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_security_config_details,
            self.security_config_data.invalid_security_config_id,
        )

    def test_modify_security_config(self):
        """
        Test Modify Security Config
        
        Confirms that modifying security config returns None
        """
        resp = self.configuration.modify_security_config(
            self.security_config_data.security_config_id_1, {"protocol_mode": "TLSv1_2"},
        )
        self.assertIsNone(resp)

    def test_modify_security_config_with_invalid_param(self):
        """
        Test Modify Security Config with Invalid Param
        
        Verifies that an exception is raised when modifying security config with invalid param
        """
        self.assertRaises(
            PowerStoreException,
            self.configuration.modify_security_config,
            self.security_config_data.security_config_id_1,
            self.security_config_data.invalid_protocol_mode,
        )
