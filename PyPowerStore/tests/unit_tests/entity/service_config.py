"""Mock service_config Api for Service Config Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ServiceConfigResponse(Entity):
    """
    This class is used to handle Service Config related responses.

    It provides methods to get service configs, service config details, 
    modify service config and execute Service Config APIs.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the ServiceConfigResponse object.

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
            if self.url.endswith("/service_config"):
                if self.kwargs.get("params", {}).get("appliance_id"):
                    return self.get_service_config_by_appliance_id
                return self.get_service_configs
            return self.get_service_config_details
        if self.method == "PATCH":
            return self.modify_service_config
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

    def get_service_configs(self):
        """
        Returns a list of service configs.

        Returns:
            tuple: A tuple containing the status code and the list of service configs.
        """
        return self.status_code, self.data.service_config_list

    def get_service_config_details(self):
        """
        Returns the details of a service config.

        Returns:
            tuple: A tuple containing the status code and the service config details.
        """
        if self.url.endswith(
            f"/service_config/{self.data.invalid_service_config_id}",
        ):
            return 404, self.data.service_config_error[404]
        return self.status_code, self.data.service_config_details_1

    def get_service_config_by_appliance_id(self):
        """
        Returns a list of service configs by appliance id.

        Returns:
            tuple: A tuple containing the status code and the list of service configs.
        """
        return self.status_code, [self.data.service_config_list]

    def modify_service_config(self):
        """
        Modifies a service config.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, self.data.service_config_details_1
