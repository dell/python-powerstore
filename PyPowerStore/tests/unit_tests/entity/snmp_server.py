"""Mock snmp_server Api for SNMP Server Unit Tests"""

from PyPowerStore.tests.unit_tests.data.snmp_server_data import SNMPServerData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SNMPServerResponse(Entity):
    """
    This class is used to handle SNMP server related responses.

    It provides methods to get SNMP servers, get SNMP server details, 
    create SNMP servers, modify SNMP servers, and delete SNMP servers.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the SNMPServerResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.snmp_server_data = SNMPServerData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/snmp_server"):
                return self.get_snmp_server_list
            return self.get_snmp_server_details
        if self.method == "PATCH":
            return self.modify_snmp_server
        if self.method == "POST":
            return self.create_snmp_server
        if self.method == "DELETE":
            return self.delete_snmp_server
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

    def get_snmp_server_list(self):
        """
        Returns a list of SNMP servers.

        Returns:
            tuple: A tuple containing the status code and the list of SNMP servers.
        """
        return self.status_code, self.snmp_server_data.snmp_server_list

    def get_snmp_server_details(self):
        """
        Returns the details of a SNMP server.

        Returns:
            tuple: A tuple containing the status code and the SNMP server details.
        """
        if self.url.endswith(
            f"/snmp_server/{self.snmp_server_data.snmp_server_id_not_exist}",
        ):
            return 422, self.snmp_server_data.snmp_server_error[422]
        return 200, self.snmp_server_data.snmp_server_detail

    def modify_snmp_server(self):
        """
        Modifies a SNMP server.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.snmp_server_data.snmp_server_valid_param_list):
            # invalid param given
            return 400, self.snmp_server_data.snmp_server_error[400]
        return 204, None

    def create_snmp_server(self):
        """
        Creates a new SNMP server.

        Returns:
            tuple: A tuple containing the status code and the snmp server id.
        """
        return 201, self.snmp_server_data.snmp_server_id

    def delete_snmp_server(self):
        """
        Deletes a SNMP server.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
