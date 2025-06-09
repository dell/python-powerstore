"""Mock file_dns Api for File DNS Unit Tests"""

from PyPowerStore.tests.unit_tests.data.file_dns_data import FileDNSData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class FileDNSResponse(Entity):
    """
    This class is used to handle File DNS related responses.
    
    It provides methods to get File DNS list, File DNS details, modify File DNS, 
    create File DNS, and delete File DNS.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the FileDNSResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.file_dns_data = FileDNSData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/file_dns"):
                return self.get_file_dns_list
            return self.get_file_dns_details
        if self.method == "PATCH":
            return self.modify_file_dns
        if self.method == "POST":
            return self.create_file_dns
        if self.method == "DELETE":
            return self.delete_file_dns
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

    def get_file_dns_list(self):
        """
        Returns the File DNS list.
        
        Returns:
            tuple: A tuple containing the status code and the File DNS list.
        """
        return self.status_code, self.file_dns_data.file_dns_list

    def get_file_dns_details(self):
        """
        Returns the File DNS details.
        
        Returns:
            tuple: A tuple containing the status code and the File DNS details.
        """
        if self.url.endswith(
            f"/file_dns/{self.file_dns_data.file_dns_id_not_exist}",
        ):
            return 404, self.file_dns_data.file_dns_error[404]
        return 200, self.file_dns_data.file_dns_detail

    def modify_file_dns(self):
        """
        Modifies the File DNS.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.file_dns_data.file_dns_valid_param_list):
            # invalid param given
            return 400, self.file_dns_data.file_dns_error[400]
        return 204, None

    def create_file_dns(self):
        """
        Creates a new File DNS.
        
        Returns:
            tuple: A tuple containing the status code and the File DNS ID.
        """
        return 201, self.file_dns_data.file_dns_id

    def delete_file_dns(self):
        """
        Deletes a File DNS.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
