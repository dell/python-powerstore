"""Mock host_group Api for Host Group Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class HostGroupResponse(Entity):
    """
    This class is used to handle Host Group related responses.

    It provides methods to get host groups, host group details, create host groups, 
    modify host groups and delete host groups.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the HostGroupResponse object.

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
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/host_group"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_host_group_by_name
                return self.get_hostgroups
            return self.get_host_group_details
        if self.method == "POST":
            return self.create_host_group
        if self.method == "PATCH":
            return self.modify_host_group
        if self.method == "DELETE":
            return self.delete_host_group
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

    def get_hostgroups(self):
        """
        Returns a list of host groups.

        Returns:
            tuple: A tuple containing the status code and the list of host groups.
        """
        return self.status_code, self.data.hg_list

    def get_host_group_details(self):
        """
        Returns the details of a host group.

        Returns:
            tuple: A tuple containing the status code and the host group details.
        """
        return self.status_code, self.data.hg1

    def get_host_group_by_name(self):
        """
        Returns a host group by name.

        Returns:
            tuple: A tuple containing the status code and the host group.
        """
        return self.status_code, [self.data.hg1]

    def create_host_group(self):
        """
        Creates a new host group.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.create_hg

    def modify_host_group(self):
        """
        Modifies a host group.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "name" in self.kwargs["data"]
            and self.kwargs["data"]["name"] == self.data.existing_hg_name
        ):
            return 400, self.data.invalid_rename_error
        if (
            "add_host_ids" in self.kwargs["data"]
            and self.kwargs["data"]["add_host_ids"][0] == self.data.invalid_host_id
        ):
            return 400, self.data.add_invalid_host_error
        return 204, None

    def delete_host_group(self):
        """
        Deletes a host group.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
