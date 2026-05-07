"""Mock network Api for Network Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class NetworkResponse(Entity):
    """
    This class is used to handle Network related responses.

    It provides methods to get networks, network details, modify networks,
    add/remove ports to/from networks.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the NetworkResponse object.

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
            if self.url.endswith("/network"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_network_by_name
                return self.get_networks
            return self.get_network_details
        if self.method == "PATCH":
            return self.modify_network
        if self.method == "POST":
            return self.add_remove_ports
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

    def get_networks(self):
        """
        Returns a list of networks.

        Returns:
            tuple: A tuple containing the status code and the list of networks.
        """
        return self.status_code, self.data.network_list

    def get_network_details(self):
        """
        Returns the details of a network.

        Returns:
            tuple: A tuple containing the status code and the network details.
        """
        if self.url.endswith(f"/network/{self.data.network_does_not_exist}"):
            return 404, self.data.network_error[404]
        return self.status_code, self.data.network_details_1

    def get_network_by_name(self):
        """
        Returns a list of networks by name.

        Returns:
            tuple: A tuple containing the status code and the network details.
        """
        return self.status_code, [self.data.network_details_1]

    def modify_network(self):
        """
        Modifies a network.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.network_valid_param_list):
            # invalid param given
            return 400, self.data.network_error[400]
        return 204, None

    def add_remove_ports(self):
        """
        Adds or removes ports to/from a network.

        Returns:
            tuple: A tuple containing the status code and the network details.
        """
        return self.status_code, self.data.network_details_1
