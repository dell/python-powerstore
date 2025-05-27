"""Unit tests for LDAP"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestAds(TestBase):
    """Unit tests for Ads"""

    def test_get_ldap(self):
        """
        Test get LDAP

        Validates that LDAP list matches the expected data."""
        ldap_list = self.provisioning.get_file_ldaps()
        self.assertListEqual(ldap_list, self.ldap_data.ldap_list)
