"""Mock remote_support Api for Remote Support Unit Tests"""

from PyPowerStore.tests.unit_tests.data.remote_support_data import RemoteSupportData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RemoteSupportResponse(Entity):
    """
    This class is used to handle Remote Support related responses.

    It provides methods to get remote support configs, remote support details,
    modify remote support details, verify remote support config, and send test
    remote support config.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the RemoteSupportResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.remote_support_data = RemoteSupportData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/remote_support"):
                return self.get_remote_support_configs
            return self.get_remote_support_details
        if self.method == "POST":
            if self.url.endswith("/verify"):
                return self.verify_remote_support_config
            return self.send_test_remote_support_config
        if self.method == "PATCH":
            return self.modify_remote_support_details
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

    def get_remote_support_configs(self):
        """
        Returns a list of remote support configs.

        Returns:
            tuple: A tuple containing the status code and the list of remote support configs.
        """
        return self.status_code, self.remote_support_data.remote_support_list

    def get_remote_support_details(self):
        """
        Returns the details of a remote support.

        Returns:
            tuple: A tuple containing the status code and the remote support details.
        """
        return self.status_code, self.remote_support_data.remote_support_details

    def modify_remote_support_details(self):
        """
        Modifies the remote support details.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.remote_support_data.remote_support_valid_param_list):
            # invalid param given
            return 400, self.remote_support_data.remote_support_error[400]
        return 204, None

    def verify_remote_support_config(self):
        """
        Verifies the remote support config.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def send_test_remote_support_config(self):
        """
        Sends a test remote support config.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
