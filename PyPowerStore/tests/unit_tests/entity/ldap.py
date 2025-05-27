"""Mock ldap Api for Ldap Unit Tests"""

from PyPowerStore.tests.unit_tests.data.ldap_data import LdapData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class LdapResponse(Entity):
    """
    This class is used to handle LDAP related responses.

    It provides methods to get LDAP list, LDAP details, and execute LDAP APIs.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the LdapResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ldap_data = LdapData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            return self.get_file_ldaps
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

    def get_file_ldaps(self):
        """
        Returns the LDAP list.

        Returns:
            tuple: A tuple containing the status code and the LDAP list.
        """
        return self.status_code, self.ldap_data.ldap_list
