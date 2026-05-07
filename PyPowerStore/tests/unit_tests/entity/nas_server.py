"""Mock nas_server Api for NAS Server Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class NASServerResponse(Entity):
    """
    This class is used to handle NAS server related responses.
    
    It provides methods to get NAS servers, get NAS server details, create NAS servers,
    modify NAS servers, and delete NAS servers.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the NASServerResponse object.
        
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
            if self.url.endswith("/nas_server"):
                sel = self.kwargs.get("params", {}).get("select", {})
                if sel and sel == constants.FHP_NAS_QUERYSTRING["select"]:
                    return self.get_nasserver_detail
                return self.get_nasservers
            return self.get_nasserver_detail
        if self.method == "PATCH":
            return self.modify_nas
        if self.method == "POST":
            return self.create_nasserver
        if self.method == "DELETE":
            return self.delete_nasserver
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

    def get_nasservers(self):
        """
        Returns a list of NAS servers.
        
        Returns:
            tuple: A tuple containing the status code and the list of NAS servers.
        """
        return self.status_code, self.data.nas_list

    def get_nasserver_detail(self):
        """
        Returns the details of a NAS server.
        
        Returns:
            tuple: A tuple containing the status code and the NAS server details.
        """
        if self.url.endswith(f"/nas_server/{self.data.nas_id_not_exist}"):
            return 404, self.data.nas_error[404]
        return 200, self.data.nas_detail

    def modify_nas(self):
        """
        Modifies a NAS server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.nas_valid_param_list):
            # invalid param given
            return 400, self.data.nas_error[400]
        if self.url.endswith(f"/nas_server/{self.data.nas_id_not_exist}"):
            return 404, self.data.nas_error[404]
        return 204, None

    def create_nasserver(self):
        """
        Creates a new NAS server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.nas_id1

    def delete_nasserver(self):
        """
        Deletes a NAS server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
