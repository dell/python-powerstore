"""Mock software_installed Api for Software Installed Unit Tests"""

# pylint: disable=no-member,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SoftwareResponse(Entity):
    """
    This class handles the response for software API.
    
    It inherits from the Entity class and provides methods for executing API calls and 
    retrieving software data.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes a SoftwareResponse object.
        
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
        Returns the name of the API call based on the method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/software_installed"):
                return self.get_softwares
            return self.get_software_details
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

    def get_softwares(self):
        """
        Returns a list of software.
        
        Returns:
            tuple: A tuple containing the status code and the list of software.
        """
        return self.status_code, self.data.software_list

    def get_software_details(self):
        """
        Returns the details of a software.
        
        Returns:
            tuple: A tuple containing the status code and the software details.
        """
        return self.status_code, self.data.software_details_1
