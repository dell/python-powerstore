"""Unit tests for Chap Config"""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestChapConfig(TestBase):
    """
    Unit tests for Chap Config
    """

    def test_get_chap_configs(self):
        """
        Test getting chap configs

        Validates that chap config list is returned correctly
        """
        chap_config_list = self.configuration.get_chap_configs()
        self.assertListEqual(chap_config_list, self.data.chap_config_list)

    def test_get_chap_config_details(self):
        """
        Test getting chap config details

        Verifies that chap config details are returned correctly
        """
        chap_config_details = self.configuration.get_chap_config_details(
            self.data.chap_config_id_1,
        )
        self.assertEqual(chap_config_details, self.data.chap_config_details_1)

    def test_get_invalid_chap_config_details(self):
        """
        Test getting invalid chap config details

        Confirms that an exception is raised for invalid chap config id
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_chap_config_details,
            self.data.invalid_chap_config_id,
        )

    def test_modify_chap_config(self):
        """
        Test modifying chap config

        Verifies that chap config is modified correctly
        """
        chap_config_details_1 = self.configuration.modify_chap_config(
            self.data.chap_config_id_1, mode="Single",
        )
        self.assertEqual(chap_config_details_1, self.data.chap_config_details_1)
