"""Mock role Api for Role Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RoleResponse(Entity):
    """
    This class is used to handle Role related responses.

    It provides methods to get roles, role details, and execute Role APIs.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the RoleResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/role"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_role_by_name
                return self.get_roles
            return self.get_role_details
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

    def get_roles(self):
        """
        Returns a list of roles.

        Returns:
            tuple: A tuple containing the status code and the list of roles.
        """
        return self.status_code, self.data.role_list

    def get_role_details(self):
        """
        Returns the details of a role.

        Returns:
            tuple: A tuple containing the status code and the role details.
        """
        if self.url.endswith(f"/role/{self.data.role_does_not_exist}"):
            return 404, self.data.role_error[404]
        return self.status_code, self.data.role_details_1

    def get_role_by_name(self):
        """
        Returns the details of a role by name.

        Returns:
            tuple: A tuple containing the status code and the role details.
        """
        return self.status_code, [self.data.role_details_1]
