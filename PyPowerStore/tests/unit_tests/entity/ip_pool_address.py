"""Mock ip_pool_address Api for IP Pool Address Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class IPPoolAddressResponse(Entity):
    """
    This class is used to handle IP Pool Address related responses.
    
    It provides methods to get IP pool address details.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the IPPoolAddressResponse object.
        
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
        Returns the name of the API based on the HTTP method.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            return self.get_ip_pool_address
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

    def get_ip_pool_address(self):
        """
        Returns the IP pool address details.
        
        Returns:
            tuple: A tuple containing the status code and the IP pool address details.
        """
        return self.status_code, self.data.ip_pool_list
