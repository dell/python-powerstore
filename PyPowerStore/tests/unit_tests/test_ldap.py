from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestAds(TestBase):

    def test_get_ldap(self):
        ldap_list = self.provisioning.get_file_ldaps()
        self.assertListEqual(ldap_list, self.ldap_data.ldap_list)
