"""Mock smb_server Api for SMB Server Unit Tests"""

from PyPowerStore.tests.unit_tests.data.smb_server_data import SMBServerData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SMBServerResponse(Entity):
    """
    This class is used to handle SMB server related responses.
    
    It provides methods to get SMB server list, details, create, modify, and delete.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the SMBServerResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.smb_server_data = SMBServerData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/smb_server"):
                return self.get_smb_server_list
            return self.get_smb_server_details
        if self.method == "PATCH":
            return self.modify_smb_server
        if self.method == "POST":
            return self.create_smb_server
        if self.method == "DELETE":
            return self.delete_smb_server
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

    def get_smb_server_list(self):
        """
        Returns a list of SMB servers.
        
        Returns:
            tuple: A tuple containing the status code and the list of SMB servers.
        """
        return self.status_code, self.smb_server_data.smb_server_list

    def get_smb_server_details(self):
        """
        Returns the details of a SMB server.
        
        Returns:
            tuple: A tuple containing the status code and the SMB server details.
        """
        if self.url.endswith(
            f"/smb_server/{self.smb_server_data.smb_server_id_not_exist}",
        ):
            return 404, self.smb_server_data.smb_server_error[404]
        return 200, self.smb_server_data.smb_server_detail

    def modify_smb_server(self):
        """
        Modifies a SMB server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.smb_server_data.smb_server_valid_param_list):
            # invalid param given
            return 400, self.smb_server_data.smb_server_error[400]
        return 204, None

    def create_smb_server(self):
        """
        Creates a new SMB server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.smb_server_data.smb_server_id

    def delete_smb_server(self):
        """
        Deletes a SMB server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
