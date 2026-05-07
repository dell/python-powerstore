"""Mock ldap_domain Api for Ldap Domain Unit Tests"""

# pylint: disable=too-many-return-statements

from PyPowerStore.tests.unit_tests.data.ldap_data import LdapData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class LDAPDomainResponse(Entity):
    """
    This class is used to handle LDAP Domain related responses.

    It provides methods to get LDAP Domain configurations, create, modify, verify, 
    and delete LDAP Domain configurations.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the LDAPDomainResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ldap_domain_data = LdapData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/ldap_domain"):
                return self.get_ldap_domain_configuration_list
            return self.get_ldap_domain_configuration_details
        if self.method == "POST":
            if self.url.endswith("/verify"):
                return self.verify_ldap_domain_configuration
            return self.create_ldap_domain_configuration
        if self.method == "PATCH":
            return self.modify_ldap_domain_configuration
        if self.method == "DELETE":
            return self.delete_ldap_domain_configuration
        return None

    def execute_api(self, api_name):
        """
        Executes the API function and returns the result.

        Args:
            api_name (function): The API function to execute.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        status_code, response = api_name()
        return status_code, response

    def get_ldap_domain_configuration_list(self):
        """
        Returns a list of LDAP Domain configurations.

        Returns:
            tuple: A tuple containing the status code and the list of LDAP Domain configurations.
        """
        return self.status_code, self.ldap_domain_data.ldap_domain_list

    def get_ldap_domain_configuration_details(self):
        """
        Returns the details of an LDAP Domain configuration.

        Returns:
            tuple: A tuple containing the status code and the LDAP Domain configuration details.
        """
        return self.status_code, self.ldap_domain_data.ldap_domain_details1

    def create_ldap_domain_configuration(self):
        """
        Creates a new LDAP Domain configuration.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return self.status_code, self.ldap_domain_data.create_ldap_domain_response

    def modify_ldap_domain_configuration(self):
        """
        Modifies an existing LDAP Domain configuration.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def verify_ldap_domain_configuration(self):
        """
        Verifies an LDAP Domain configuration.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_ldap_domain_configuration(self):
        """
        Deletes an LDAP Domain configuration.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
