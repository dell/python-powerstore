"""Mock nfs_export Api for NFS Export Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class NFSExportResponse(Entity):
    """
    This class is used to handle NFS Export related responses.
    
    It provides methods to get NFS exports, create NFS exports, get NFS export details, 
    modify NFS exports, and delete NFS exports.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the NFSExportResponse object.
        
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
            if self.url.endswith("/nfs_export"):
                sel = self.kwargs.get("params", {}).get("select")
                if sel == constants.SELECT_ALL_NFS_EXPORT["select"]:
                    return self.get_nfs_detail
                return self.get_nfsexports
            return self.get_nfs_detail
        if self.method == "POST":
            return self.create_nfs
        if self.method == "PATCH":
            return self.modify_nfs
        if self.method == "DELETE":
            return self.delete_nfs
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

    def get_nfsexports(self):
        """
        Returns a list of NFS exports.
        
        Returns:
            tuple: A tuple containing the status code and the list of NFS exports.
        """
        return self.status_code, self.data.nfs_list

    def create_nfs(self):
        """
        Creates a new NFS export.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.create_nfs

    def get_nfs_detail(self):
        """
        Returns the details of an NFS export.
        
        Returns:
            tuple: A tuple containing the status code and the NFS export details.
        """
        return self.status_code, self.data.nfs_detail

    def modify_nfs(self):
        """
        Modifies an NFS export.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.nfs_valid_param):
            # invalid param given
            return 400, self.data.nfs_error[400]
        return 204, None

    def delete_nfs(self):
        """
        Deletes an NFS export.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if self.url.endswith(f"/nfs_export/{self.data.invalid_nfs}"):
            return 404, self.data.nfs_error[404]
        return 204, None
