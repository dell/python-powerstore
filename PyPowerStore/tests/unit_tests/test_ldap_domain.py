from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestLDAPDomain(TestBase):
    def test_get_ldap_domains(self):
        ldap_domain_list = self.configuration.get_ldap_domain_configuration_list()
        self.assertListEqual(ldap_domain_list, self.ldap_data.ldap_domain_list)

    def test_get_ldap_domain_details(self):
        resp = self.configuration.get_ldap_domain_configuration_details(
            self.ldap_data.ldap_domain_list[0]["id"],
        )
        self.assertEqual(resp, self.ldap_data.ldap_domain_details1)

    def test_get_ldap_domain_details_by_name(self):
        resp = self.configuration.get_ldap_domain_configuration_details(
            self.ldap_data.ldap_domain_details1["domain_name"],
        )
        self.assertEqual(resp, self.ldap_data.ldap_domain_details1)

    def test_create_ldap_domain_configuration(self):
        resp = self.configuration.create_ldap_domain_configuration(
            self.ldap_data.create_ldap_domain_dict,
        )
        self.assertEqual(resp, self.ldap_data.create_ldap_domain_response)

    def test_modify_ldap_domain_configuration(self):
        resp = self.configuration.modify_ldap_domain_configuration(
            self.ldap_data.ldap_domain_list[0]["id"],
            self.ldap_data.modify_ldap_domain_dict,
        )
        self.assertIsNone(resp)

    def test_verify_ldap_domain_configuration(self):
        resp = self.configuration.verify_ldap_domain_configuration(
            self.ldap_data.ldap_domain_list[0]["id"],
        )
        self.assertIsNone(resp)

    def test_delete_ldap_domain_configuration(self):
        resp = self.configuration.delete_ldap_domain_configuration(
            self.ldap_data.ldap_domain_list[0]["id"],
        )
        self.assertIsNone(resp)
