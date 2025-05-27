"""Mock Storage Container Destination Api for Storage Container Destination Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.storage_container_destination_data import (
    StorageContainerDestinationData,
)
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class StorageContainerDestinationResponse(Entity):
    """
    This class handles the response for storage container destination API.

    It inherits from the Entity class and provides methods for executing API calls 
    and retrieving storage container destination data.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes a StorageContainerDestinationResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.storage_container_destination_data = StorageContainerDestinationData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API call based on the method and URL.

        Returns:
            function: The API function to execute.
        """
        if self.method == "GET":
            if self.url.endswith("/storage_container_destination"):
                return self.get_storage_container_destination_list
            return self.get_storage_container_destination_details
        if self.method == "POST":
            return self.create_storage_container_destination
        if self.method == "DELETE":
            return self.delete_storage_container_destination
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

    def get_storage_container_destination_list(self):
        """
        Returns a list of storage container destinations.

        Returns:
            tuple: A tuple containing the status code and the list of
            storage container destinations.
        """
        return (
            self.status_code,
            self.storage_container_destination_data.storage_container_destination_list,
        )

    def get_storage_container_destination_details(self):
        """
        Returns the details of a storage container destination.

        Returns:
            tuple: A tuple containing the status code and the details of
            the storage container destination.
        """
        return (
            self.status_code,
            self.storage_container_destination_data.storage_container_destination_details,
        )

    def create_storage_container_destination(self):
        """
        Creates a new storage container destination.

        Returns:
            tuple: A tuple containing the status code and the ID of the newly
            created storage container destination.
        """
        return (
            201,
            self.storage_container_destination_data.storage_container_destination_id,
        )

    def delete_storage_container_destination(self):
        """
        Deletes a storage container destination.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
