"""Mock replication_group Api for Replication Group Unit Tests"""

from PyPowerStore.tests.unit_tests.data.replication_group_data import (
    ReplicationGroupData,
)
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ReplicationGroupResponse(Entity):
    """
    This class is used to handle Replication Group related responses.

    It provides methods to get replication group list, replication group details.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the ReplicationGroupResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.replication_group_data = ReplicationGroupData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the API name based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/replication_group"):
                return self.get_replication_group_list
            return self.get_replication_group_details
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

    def get_replication_group_list(self):
        """
        Returns the replication group list.

        Returns:
            tuple: A tuple containing the status code and the replication group list.
        """
        return self.status_code, self.replication_group_data.replication_group_list

    def get_replication_group_details(self):
        """
        Returns the replication group details.

        Returns:
            tuple: A tuple containing the status code and the replication group details.
        """
        return self.status_code, self.replication_group_data.replication_group_details
