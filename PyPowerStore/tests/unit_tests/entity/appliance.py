"""Mock appliance Api for Appliance Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ApplianceResponse(Entity):
    """
    This class handles the response for appliance API.
    
    It inherits from the Entity class and provides methods for executing API calls and 
    retrieving appliance data.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes an ApplianceResponse object.
        
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
            str: The name of the API call.
        """
        if self.method == "GET":
            if self.url.endswith("/appliance"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_appliance_by_name
                return self.get_appliances
            return self.get_appliance_details
        return None

    def execute_api(self, api_name):
        """
        Executes an API call and returns the response.
        
        Args:
            api_name (str): The name of the API call.
        
        Returns:
            tuple: A tuple containing the status code and response.
        """
        status_code, response = api_name()
        return status_code, response

    def get_appliances(self):
        """
        Returns a list of all appliances.
        
        Returns:
            tuple: A tuple containing the status code and a list of appliances.
        """
        return self.status_code, self.data.appliance_list

    def get_appliance_details(self):
        """
        Returns the details of a specific appliance.
        
        Returns:
            tuple: A tuple containing the status code and the appliance details.
        """
        if self.url.endswith(
            f"/appliance/{self.data.appliance_does_not_exist}",
        ):
            return 404, self.data.appliance_error[404]
        return self.status_code, self.data.appliance_details_1

    def get_appliance_by_name(self):
        """
        Returns the details of an appliance by name.
        
        Returns:
            tuple: A tuple containing the status code and a list of appliance details.
        """
        return self.status_code, [self.data.appliance_details_1]
