"""Mock security_config Api for Security Config Unit Tests"""

from PyPowerStore.tests.unit_tests.data.security_config_data import SecurityConfigData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SecurityConfigResponse(Entity):
    """
    This class is used to handle Security Config related responses.

    It provides methods to get security configs, security config details, 
    modify security config, and execute API functions.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the SecurityConfigResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = SecurityConfigData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/security_config"):
                return self.get_security_configs
            return self.get_security_config_details
        if self.method == "PATCH":
            return self.modify_security_config
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

    def get_security_configs(self):
        """
        Returns a list of security configs.

        Returns:
            tuple: A tuple containing the status code and the list of security configs.
        """
        return self.status_code, self.data.security_config_list

    def get_security_config_details(self):
        """
        Returns the details of a security config.

        Returns:
            tuple: A tuple containing the status code and the security config details.
        """
        if self.url.endswith(
            f"/security_config/{self.data.invalid_security_config_id}",
        ):
            return 404, self.data.security_config_error[404]
        return self.status_code, self.data.security_config_details_1

    def modify_security_config(self):
        """
        Modifies a security config.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "protocol_mode" in self.kwargs["data"]
            and self.kwargs["data"]["protocol_mode"] == self.data.invalid_protocol_mode
        ):
            return 400, self.data.security_config_error[400]
        return 204, self.data.security_config_details_1
