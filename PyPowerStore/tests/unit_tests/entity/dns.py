"""Mock dns Api for Dns Unit Tests"""

from PyPowerStore.tests.unit_tests.data.dns_data import DnsData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class DnsResponse(Entity):
    """
    This class is used to handle DNS related responses.
    
    It provides methods to get DNS list, DNS details, and modify DNS details.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the DnsResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.dns_data = DnsData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/dns"):
                return self.get_dns_list
            return self.get_dns_details
        if self.method == "PATCH":
            return self.modify_dns_details
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

    def get_dns_list(self):
        """
        Returns the DNS list.
        
        Returns:
            tuple: A tuple containing the status code and the DNS list.
        """
        return self.status_code, self.dns_data.dns_list

    def get_dns_details(self):
        """
        Returns the DNS details.
        
        Returns:
            tuple: A tuple containing the status code and the DNS details.
        """
        return self.status_code, self.dns_data.dns_details

    def modify_dns_details(self):
        """
        Modifies the DNS details.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.dns_data.dns_valid_param_list):
            # invalid param given
            return 400, self.dns_data.dns_error[400]
        return 204, None
