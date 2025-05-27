"""Mock Discovered Appliance Api for Discovered Appliance Unit Tests"""

from PyPowerStore.tests.unit_tests.data.discovered_appliances import (
    DiscoveredApplianceData,
)
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class DiscoveredApplianceResponse(Entity):
    """
    This class is used to handle Discovered Appliance related responses.

    It provides methods to get discovered appliances and execute API calls.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the DiscoveredApplianceResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.discovered_appliance_data = DiscoveredApplianceData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API call based on the HTTP method.

        Returns:
            function: The API function to execute.
        """
        if self.method == "GET":
            return self.get_discovered_appliances
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

    def get_discovered_appliances(self):
        """
        Returns a list of discovered appliances.

        Returns:
            tuple: A tuple containing the status code and the list of discovered appliances.
        """
        return (
            self.status_code,
            self.discovered_appliance_data.discovered_appliance_list,
        )
