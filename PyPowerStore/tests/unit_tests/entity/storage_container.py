"""Mock storage container Api for Storage Container Unit Tests"""

from PyPowerStore.tests.unit_tests.data.storage_container_data import (
    StorageContainerData,
)
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class StorageContainerResponse(Entity):
    """
    This class is used to handle Storage Container related responses.

    It provides methods to get storage container list, storage container details, 
    create storage containers, modify storage container details and delete storage containers.
    """
    def __init__(self, method, url, **kwargs):
        """
        Initializes the StorageContainerResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.storage_container_data = StorageContainerData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/storage_container"):
                return self.get_storage_container_list
            return self.get_storage_container_details
        if self.method == "POST":
            return self.create_storage_container
        if self.method == "PATCH":
            return self.modify_storage_container_details
        if self.method == "DELETE":
            return self.delete_storage_container
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

    def get_storage_container_list(self):
        """
        Returns a list of storage containers.

        Returns:
            tuple: A tuple containing the status code and the list of storage containers.
        """
        return self.status_code, self.storage_container_data.storage_container_list

    def get_storage_container_details(self):
        """
        Returns the details of a storage container.

        Returns:
            tuple: A tuple containing the status code and the storage container details.
        """
        return self.status_code, self.storage_container_data.storage_container_details

    def create_storage_container(self):
        """
        Creates a new storage container.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return (
            self.status_code,
            self.storage_container_data.create_storage_container_response,
        )

    def modify_storage_container_details(self):
        """
        Modifies a storage container.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_storage_container(self):
        """
        Deletes a storage container.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
