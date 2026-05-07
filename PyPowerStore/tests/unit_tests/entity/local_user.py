"""Mock local_user Api for Local User Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class LocalUserResponse(Entity):
    """
    This class is used to handle Local User related responses.

    It provides methods to get local users, local user details, create local users,
    modify local users and delete local users.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the LocalUserResponse object.

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
            if self.url.endswith("/local_user"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_local_user_by_name
                return self.get_local_users
            return self.get_local_user_details
        if self.method == "PATCH":
            return self.modify_local_user
        if self.method == "POST":
            return self.create_local_user
        if self.method == "DELETE":
            return self.delete_local_user
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

    def get_local_users(self):
        """
        Returns a list of local users.

        Returns:
            tuple: A tuple containing the status code and the list of local users.
        """
        return self.status_code, self.data.local_user_list

    def get_local_user_details(self):
        """
        Returns the details of a local user.

        Returns:
            tuple: A tuple containing the status code and the local user details.
        """
        if self.url.endswith(
            f"/local_user/{self.data.local_user_does_not_exist}",
        ):
            return 404, self.data.local_user_error[404]
        return self.status_code, self.data.local_user_details

    def get_local_user_by_name(self):
        """
        Returns the details of a local user by name.

        Returns:
            tuple: A tuple containing the status code and the local user details.
        """
        return self.status_code, self.data.local_user_details

    def modify_local_user(self):
        """
        Modifies a local user.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.local_user_valid_param_list):
            # invalid param given
            return 400, self.data.local_user_error[400]
        return 204, None

    def create_local_user(self):
        """
        Creates a new local user.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.local_user_create_response

    def delete_local_user(self):
        """
        Deletes a local user.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
