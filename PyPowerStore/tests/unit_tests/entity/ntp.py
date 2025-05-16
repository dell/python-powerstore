"""Mock ntp Api for Ntp Unit Tests"""

from PyPowerStore.tests.unit_tests.data.ntp_data import NtpData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class NtpResponse(Entity):
    """
    This class is used to handle NTP related responses.
    
    It provides methods to get NTP list, NTP details, and modify NTP details.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the NtpResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ntp_data = NtpData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/ntp"):
                return self.get_ntp_list
            return self.get_ntp_details
        if self.method == "PATCH":
            return self.modify_ntp_details
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

    def get_ntp_list(self):
        """
        Returns a list of NTP instances.
        
        Returns:
            tuple: A tuple containing the status code and the list of NTP instances.
        """
        return self.status_code, self.ntp_data.ntp_list

    def get_ntp_details(self):
        """
        Returns the details of an NTP instance.
        
        Returns:
            tuple: A tuple containing the status code and the NTP instance details.
        """
        return self.status_code, self.ntp_data.ntp_details

    def modify_ntp_details(self):
        """
        Modifies the details of an NTP instance.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.ntp_data.ntp_valid_param_list):
            # invalid param given
            return 400, self.ntp_data.ntp_error[400]
        return 204, None
