"""Mock file_interface Api for File Interface Unit Tests"""

from PyPowerStore.tests.unit_tests.data.file_interface_data import FileInterfaceData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class FileInterfaceResponse(Entity):
    """
    This class is used to handle File Interface related responses.
    
    It provides methods to get file interface list, file interface details, 
    create file interface, modify file interface and delete file interface.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the FileInterfaceResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.file_interface_data = FileInterfaceData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/file_interface"):
                return self.get_file_interface_list
            return self.get_file_interface_details
        if self.method == "PATCH":
            return self.modify_file_interface
        if self.method == "POST":
            return self.create_file_interface
        if self.method == "DELETE":
            return self.delete_file_interface
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

    def get_file_interface_list(self):
        """
        Returns a list of file interfaces.
        
        Returns:
            tuple: A tuple containing the status code and the list of file interfaces.
        """
        return self.status_code, self.file_interface_data.file_interface_list

    def get_file_interface_details(self):
        """
        Returns the details of a file interface.
        
        Returns:
            tuple: A tuple containing the status code and the file interface details.
        """
        if self.url.endswith(
            f"/file_interface/{self.file_interface_data.file_interface_id_not_exist}",
        ):
            return 404, self.file_interface_data.file_interface_error[404]
        return 200, self.file_interface_data.file_interface_detail

    def modify_file_interface(self):
        """
        Modifies a file interface.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.file_interface_data.file_interface_valid_param_list):
            # invalid param given
            return 400, self.file_interface_data.file_interface_error[400]
        return 204, None

    def create_file_interface(self):
        """
        Creates a new file interface.
        
        Returns:
            tuple: A tuple containing the status code and the file interface ID.
        """
        return 201, self.file_interface_data.file_interface_id

    def delete_file_interface(self):
        """
        Deletes a file interface.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
