"""Mock smb_share Api for SMB Share Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class SMBShareResponse(Entity):
    """
    This class is used to handle SMB share related responses.
    
    It provides methods to get SMB shares, create SMB shares, modify SMB
    shares, and delete SMB shares.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the SMBShareResponse object.
        
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
            if self.url.endswith("/smb_share"):
                if self.kwargs.get("params", {}).get(
                    "select",
                ) == constants.SELECT_ALL_SMB_SHARE.get("select"):
                    return self.get_smb_detail
                return self.get_smbshares
            return self.get_smb_detail
        if self.method == "POST":
            return self.create_smb
        if self.method == "PATCH":
            return self.modify_smb
        if self.method == "DELETE":
            return self.delete_smb
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

    def get_smbshares(self):
        """
        Returns a list of SMB shares.
        
        Returns:
            tuple: A tuple containing the status code and the list of SMB shares.
        """
        return self.status_code, self.data.smb_list

    def create_smb(self):
        """
        Creates a new SMB share.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.create_smb

    def get_smb_detail(self):
        """
        Returns the details of an SMB share.
        
        Returns:
            tuple: A tuple containing the status code and the SMB share details.
        """
        return 200, self.data.smb_detail

    def modify_smb(self):
        """
        Modifies an existing SMB share.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_smb(self):
        """
        Deletes an existing SMB share.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if self.url.endswith(f"/smb_share/{self.data.invalid_smb_id}"):
            return 404, self.data.smb_error[404]
        return 204, None
