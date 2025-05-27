"""Unit tests for LDAP Domain"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestLDAPDomain(TestBase):
    """
    Unit tests for LDAP Domain
    """

    def test_get_ldap_domains(self):
        """
        Test get LDAP domains

        Validates that the list of LDAP domains matches the expected list
        """
        ldap_domain_list = self.configuration.get_ldap_domain_configuration_list()
        self.assertListEqual(ldap_domain_list, self.ldap_data.ldap_domain_list)

    def test_get_ldap_domain_details(self):
        """
        Test get LDAP domain details

        Verifies that the details of the LDAP domain with the given ID match the expected details
        """
        resp = self.configuration.get_ldap_domain_configuration_details(
            self.ldap_data.ldap_domain_list[0]["id"],
        )
        self.assertEqual(resp, self.ldap_data.ldap_domain_details1)

    def test_get_ldap_domain_details_by_name(self):
        """
        Test get LDAP domain details by name

        Confirms that the details of the LDAP domain with the given name match the expected details
        """
        resp = self.configuration.get_ldap_domain_configuration_details(
            self.ldap_data.ldap_domain_details1["domain_name"],
        )
        self.assertEqual(resp, self.ldap_data.ldap_domain_details1)

    def test_create_ldap_domain_configuration(self):
        """
        Test create LDAP domain configuration

        Validates that the created LDAP domain configuration matches the expected response
        """
        resp = self.configuration.create_ldap_domain_configuration(
            self.ldap_data.create_ldap_domain_dict,
        )
        self.assertEqual(resp, self.ldap_data.create_ldap_domain_response)

    def test_modify_ldap_domain_configuration(self):
        """
        Test modify LDAP domain configuration

        Verifies that the response is None
        """
        resp = self.configuration.modify_ldap_domain_configuration(
            self.ldap_data.ldap_domain_list[0]["id"],
            self.ldap_data.modify_ldap_domain_dict,
        )
        self.assertIsNone(resp)

    def test_verify_ldap_domain_configuration(self):
        """
        Test verify LDAP domain configuration

        Confirms that the response is None
        """
        resp = self.configuration.verify_ldap_domain_configuration(
            self.ldap_data.ldap_domain_list[0]["id"],
        )
        self.assertIsNone(resp)

    def test_delete_ldap_domain_configuration(self):
        """
        Test delete LDAP domain configuration

        Verifies that the response is None
        """
        resp = self.configuration.delete_ldap_domain_configuration(
            self.ldap_data.ldap_domain_list[0]["id"],
        )
        self.assertIsNone(resp)
