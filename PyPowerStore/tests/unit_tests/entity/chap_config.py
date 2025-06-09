"""Mock chap_config Api for Chaps Config Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ChapConfigResponse(Entity):
    """
    This class is used to handle ChapConfig related responses.
    
    It provides methods to get chap configs, chap config details, modify chap configs.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the ChapConfigResponse object.
        
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
            if self.url.endswith("/chap_config"):
                return self.get_chap_configs
            return self.get_chap_config_details
        if self.method == "PATCH":
            return self.modify_chap_config
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

    def get_chap_configs(self):
        """
        Returns a list of chap configs.
        
        Returns:
            tuple: A tuple containing the status code and the list of chap configs.
        """
        return self.status_code, self.data.chap_config_list

    def get_chap_config_details(self):
        """
        Returns the details of a chap config.
        
        Returns:
            tuple: A tuple containing the status code and the chap config details.
        """
        if self.url.endswith(
            f"/chap_config/{self.data.invalid_chap_config_id}",
        ):
            return 404, self.data.chap_config_error[404]
        return self.status_code, self.data.chap_config_details_1

    def modify_chap_config(self):
        """
        Modifies a chap config.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, self.data.chap_config_details_1
