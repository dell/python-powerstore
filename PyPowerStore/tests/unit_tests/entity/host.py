"""Mock host Api for Host Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class HostResponse(Entity):
    """
    This class handles the response for host API.

    It provides methods to execute API calls and retrieve host data.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes a HostResponse object.

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
            if self.url.endswith("/host_volume_mapping"):
                return self.get_host_volume_mapping
            if self.url.endswith("/host"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_host_by_name
                return self.get_hosts
            return self.get_host_details
        if self.method == "POST":
            return self.create_host
        if self.method == "PATCH":
            return self.modify_host
        if self.method == "DELETE":
            return self.delete_host
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

    def get_host_volume_mapping(self):
        """
        Returns the host volume mapping.

        Returns:
            tuple: A tuple containing the status code and the host volume mapping.
        """
        return self.status_code, self.data.hlu_details

    def get_hosts(self):
        """
        Returns a list of hosts.

        Returns:
            tuple: A tuple containing the status code and the list of hosts.
        """
        return self.status_code, self.data.host_list

    def get_host_by_name(self):
        """
        Returns a host by name.

        Returns:
            tuple: A tuple containing the status code and the host.
        """
        return self.status_code, [self.data.host1]

    def get_host_details(self):
        """
        Returns the details of a host.

        Returns:
            tuple: A tuple containing the status code and the host details.
        """
        return self.status_code, self.data.host1

    def create_host(self):
        """
        Creates a new host.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.create_host

    def modify_host(self):
        """
        Modifies a host.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "add_initiators" in self.kwargs["data"]
            and self.kwargs["data"]["add_initiators"]["name"]
            == self.data.invalid_initiator["name"]
        ):
            return 400, self.data.add_invalid_initiator_error[400]
        if (
            "remove_initiators" in self.kwargs["data"]
            and self.kwargs["data"]["remove_initiators"][0]
            == self.data.invalid_initiator["name"]
        ):
            return 400, self.data.remove_invalid_initiator_error[400]
        return 204, None

    def delete_host(self):
        """
        Deletes a host.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
