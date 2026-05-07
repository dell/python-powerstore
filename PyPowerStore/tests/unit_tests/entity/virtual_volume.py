"""Mock virtual volume Api for Virtual Volume Unit Tests"""

from PyPowerStore.tests.unit_tests.data.virtual_volume_data import VirtualVolumeData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class VirtualVolumeResponse(Entity):
    """
    This class is used to handle Virtual Volume related responses.

    It provides methods to get virtual volumes, execute Virtual Volume APIs, and more.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the VirtualVolumeResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.virtual_volume_data = VirtualVolumeData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/virtual_volume"):
                return self.get_virtual_volumes
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

    def get_virtual_volumes(self):
        """
        Returns a list of virtual volumes.

        Returns:
            tuple: A tuple containing the status code and the list of virtual volumes.
        """
        return self.status_code, self.virtual_volume_data.virtual_volume_list
