"""Mock service_user Api for Service User Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ServiceUserResponse(Entity):
    """
    This class is used to handle Service User related responses.

    It provides methods to get service users, service user details, and execute Service User APIs.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the ServiceUserResponse object.

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
            if self.url.endswith("/service_user"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_service_user_by_name
                return self.get_service_users
            return self.get_service_user_details
        if self.method == "PATCH":
            return self.modify_service_user
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

    def get_service_users(self):
        """
        Returns a list of service users.

        Returns:
            tuple: A tuple containing the status code and the list of service users.
        """
        return self.status_code, self.data.service_user_list

    def get_service_user_details(self):
        """
        Returns the details of a service user.

        Returns:
            tuple: A tuple containing the status code and the service user details.
        """
        if self.url.endswith(
            f"/service_user/{self.data.invalid_service_user_id}",
        ):
            return 404, self.data.service_user_error[404]
        return self.status_code, self.data.service_user_details_1

    def get_service_user_by_name(self):
        """
        Returns the details of a service user by name.

        Returns:
            tuple: A tuple containing the status code and the service user details.
        """
        return self.status_code, [self.data.service_user_details_1]

    def modify_service_user(self):
        """
        Modifies a service user.

        Returns:
            tuple: A tuple containing the status code and the service user details.
        """
        return 204, self.data.service_user_details_1
