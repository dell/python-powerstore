"""Mock ip_port Api for IP Port Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class IPPortResponse(Entity):
    """
    This class is used to handle IP Port related responses.
    
    It provides methods to get IP Port details and execute API functions.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the IPPortResponse object.
        
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
            return self.get_ip_port_details
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

    def get_ip_port_details(self):
        """
        Returns the details of an IP Port.
        
        Returns:
            tuple: A tuple containing the status code and the IP Port details.
        """
        return self.status_code, self.data.ip_port_details
