from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestLDAPAccount(TestBase):
    def test_get_ldap_accounts(self):
        ldap_account_list = self.configuration.get_ldap_account_list()
        self.assertListEqual(
            ldap_account_list, self.ldap_account_data.ldap_account_list
        )

    def test_get_ldap_account_details(self):
        resp = self.configuration.get_ldap_account_details(
            self.ldap_account_data.ldap_account_list[0]["id"]
        )
        self.assertEqual(resp, self.ldap_account_data.ldap_account_details1)

    def test_get_ldap_account_details_by_name(self):
        resp = self.configuration.get_ldap_account_details_by_name(
            self.ldap_account_data.ldap_account_details1["name"]
        )
        self.assertEqual(resp, self.ldap_account_data.ldap_account_details1)

    def test_create_ldap_account(self):
        resp = self.configuration.create_ldap_account(
            self.ldap_account_data.create_ldap_account_dict
        )
        self.assertEqual(resp, self.ldap_account_data.create_ldap_account_response)

    def test_modify_ldap_account_details(self):
        resp = self.configuration.modify_ldap_account_details(
            self.ldap_account_data.ldap_account_list[0]["id"],
            self.ldap_account_data.modify_ldap_account_dict,
        )
        self.assertIsNone(resp)

    def test_delete_ldap_account(self):
        resp = self.configuration.delete_ldap_account(
            self.ldap_account_data.ldap_account_list[0]["id"]
        )
        self.assertIsNone(resp)
