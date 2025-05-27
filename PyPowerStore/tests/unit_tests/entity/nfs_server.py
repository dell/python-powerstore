"""Mock nfs_server Api for NFS Server Unit Tests"""

from PyPowerStore.tests.unit_tests.data.nfs_server_data import NFSServerData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class NFSServerResponse(Entity):
    """
    This class is used to handle NFS server related responses.
    
    It provides methods to get NFS servers, get NFS server details, 
    create NFS servers, modify NFS servers, and delete NFS servers.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the NFSServerResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.nfs_server_data = NFSServerData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/nfs_server"):
                return self.get_nfs_server_list
            return self.get_nfs_server_details
        if self.method == "PATCH":
            return self.modify_nfs_server
        if self.method == "POST":
            return self.create_nfs_server
        if self.method == "DELETE":
            return self.delete_nfs_server
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

    def get_nfs_server_list(self):
        """
        Returns a list of NFS servers.
        
        Returns:
            tuple: A tuple containing the status code and the list of NFS servers.
        """
        return self.status_code, self.nfs_server_data.nfs_server_list

    def get_nfs_server_details(self):
        """
        Returns the details of a NFS server.
        
        Returns:
            tuple: A tuple containing the status code and the NFS server details.
        """
        if self.url.endswith(
            f"/nfs_server/{self.nfs_server_data.nfs_server_id_not_exist}",
        ):
            return 404, self.nfs_server_data.nfs_server_error[404]
        return 200, self.nfs_server_data.nfs_server_detail

    def modify_nfs_server(self):
        """
        Modifies a NFS server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.nfs_server_data.nfs_server_valid_param_list):
            # invalid param given
            return 400, self.nfs_server_data.nfs_server_error[400]
        return 204, None

    def create_nfs_server(self):
        """
        Creates a new NFS server.
        
        Returns:
            tuple: A tuple containing the status code and the NFS server ID.
        """
        return 201, self.nfs_server_data.nfs_server_id

    def delete_nfs_server(self):
        """
        Deletes a NFS server.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
