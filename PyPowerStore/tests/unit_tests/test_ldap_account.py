"""Unit tests for LDAP Account"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestLDAPAccount(TestBase):
    """
    Unit tests for LDAP Account
    """

    def test_get_ldap_accounts(self):
        """
        Test getting LDAP accounts

        Validates that the list of LDAP accounts matches the expected list
        """
        ldap_account_list = self.configuration.get_ldap_account_list()
        self.assertListEqual(
            ldap_account_list, self.ldap_account_data.ldap_account_list,
        )

    def test_get_ldap_account_details(self):
        """
        Test getting LDAP account details

        Verifies that the details of the LDAP account with the given ID match the expected details
        """
        resp = self.configuration.get_ldap_account_details(
            self.ldap_account_data.ldap_account_list[0]["id"],
        )
        self.assertEqual(resp, self.ldap_account_data.ldap_account_details1)

    def test_get_ldap_account_details_by_name(self):
        """
        Test getting LDAP account details by name

        Confirms that the details of the LDAP account with the given name match the expected details
        """
        resp = self.configuration.get_ldap_account_details_by_name(
            self.ldap_account_data.ldap_account_details1["name"],
        )
        self.assertEqual(resp, self.ldap_account_data.ldap_account_details1)

    def test_create_ldap_account(self):
        """
        Test creating an LDAP account

        Validates that the created LDAP account matches the expected response
        """
        resp = self.configuration.create_ldap_account(
            self.ldap_account_data.create_ldap_account_dict,
        )
        self.assertEqual(resp, self.ldap_account_data.create_ldap_account_response)

    def test_modify_ldap_account_details(self):
        """
        Test modifying LDAP account details

        Verifies that the response is None
        """
        resp = self.configuration.modify_ldap_account_details(
            self.ldap_account_data.ldap_account_list[0]["id"],
            self.ldap_account_data.modify_ldap_account_dict,
        )
        self.assertIsNone(resp)

    def test_delete_ldap_account(self):
        """
        Test deleting an LDAP account

        Confirms that the response is None
        """
        resp = self.configuration.delete_ldap_account(
            self.ldap_account_data.ldap_account_list[0]["id"],
        )
        self.assertIsNone(resp)
