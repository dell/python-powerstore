"""Mock user_quota Api for User Quota Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class UserQuotaResponse(Entity):
    """
    This class is used to handle User Quota related responses.

    It provides methods to get user quotas, user quota details, create user quotas,
    and modify user quotas.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the UserQuotaResponse object.

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
            if self.url.endswith("/file_user_quota"):
                return self.get_user_quotas
            return self.get_user_quota
        if self.method == "POST":
            return self.create_user_quota
        if self.method == "PATCH":
            return self.modify_user_quota
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

    def get_user_quotas(self):
        """
        Returns a list of user quotas.

        Returns:
            tuple: A tuple containing the status code and the list of user quotas.
        """
        return self.status_code, self.data.uq_list

    def create_user_quota(self):
        """
        Creates a new user quota.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        if set(data.keys()) - set(self.data.uq_valid_param):
            return 400, self.data.uq_error[400]
        return 201, self.data.create_user_quota

    def get_user_quota(self):
        """
        Returns the details of a user quota.

        Returns:
            tuple: A tuple containing the status code and the user quota details.
        """
        return self.status_code, self.data.uq_detail

    def modify_user_quota(self):
        """
        Modifies a user quota.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
