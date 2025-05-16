"""Mock ldap_account Api for Ldap Account Unit Tests"""

from PyPowerStore.tests.unit_tests.data.ldap_account_data import LdapAccountData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class LDAPAccountResponse(Entity):
    """
    This class is used to handle LDAP Account related responses.

    It provides methods to get LDAP account list, LDAP account details, create LDAP accounts, 
    modify LDAP account details, and delete LDAP accounts.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the LDAPAccountResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ldap_account_data = LdapAccountData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the API name based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/ldap_account"):
                return self.get_ldap_account_list
            return self.get_ldap_account_details
        if self.method == "POST":
            return self.create_ldap_account
        if self.method == "PATCH":
            return self.modify_ldap_account_details
        if self.method == "DELETE":
            return self.delete_ldap_account
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

    def get_ldap_account_list(self):
        """
        Returns the LDAP account list.

        Returns:
            tuple: A tuple containing the status code and the LDAP account list.
        """
        return self.status_code, self.ldap_account_data.ldap_account_list

    def get_ldap_account_details(self):
        """
        Returns the LDAP account details.

        Returns:
            tuple: A tuple containing the status code and the LDAP account details.
        """
        return self.status_code, self.ldap_account_data.ldap_account_details1

    def create_ldap_account(self):
        """
        Creates a new LDAP account.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return self.status_code, self.ldap_account_data.create_ldap_account_response

    def modify_ldap_account_details(self):
        """
        Modifies the LDAP account details.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_ldap_account(self):
        """
        Deletes the LDAP account.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
