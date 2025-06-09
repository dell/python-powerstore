"""Mock vcenter Api for Vcenter Unit Tests"""

from PyPowerStore.tests.unit_tests.data.vcenter_data import VcenterData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class VcenterResponse(Entity):
    """
    This class is used to handle Vcenter related responses.

    It provides methods to get vcenters, vcenter details, add vcenters, 
    modify vcenters, and remove vcenters.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the VcenterResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.vcenter_data = VcenterData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/vcenter"):
                return self.get_vcenters
            return self.get_vcenter_details
        if self.method == "PATCH":
            return self.modify_vcenter
        if self.method == "POST":
            return self.add_vcenter
        if self.method == "DELETE":
            return self.remove_vcenter
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

    def get_vcenters(self):
        """
        Returns a list of vcenters.

        Returns:
            tuple: A tuple containing the status code and the list of vcenters.
        """
        return self.status_code, self.vcenter_data.vcenter_list

    def get_vcenter_details(self):
        """
        Returns the details of a vcenter.

        Returns:
            tuple: A tuple containing the status code and the vcenter details.
        """
        return self.status_code, self.vcenter_data.vcenter_details

    def modify_vcenter(self):
        """
        Modifies a vcenter.

        Returns:
            tuple: A tuple containing the status code and the vcenter details.
        """
        return self.status_code, self.vcenter_data.vcenter_details

    def add_vcenter(self):
        """
        Adds a new vcenter.

        Returns:
            tuple: A tuple containing the status code and the vcenter ID.
        """
        return 201, self.vcenter_data.vcenter_id

    def remove_vcenter(self):
        """
        Removes a vcenter.

        Returns:
            tuple: A tuple containing the status code and None.
        """
        return 204, None
