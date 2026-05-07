"""Mock file_nis Api for File NIS Unit Tests"""

from PyPowerStore.tests.unit_tests.data.file_nis_data import FileNISData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class FileNISResponse(Entity):
    """
    This class holds the required data for File NIS unit tests.

    It provides methods to get file NIS list, file NIS details, 
    modify file NIS, create file NIS and delete file NIS.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the FileNISResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.file_nis_data = FileNISData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/file_nis"):
                return self.get_file_nis_list
            return self.get_file_nis_details
        if self.method == "PATCH":
            return self.modify_file_nis
        if self.method == "POST":
            return self.create_file_nis
        if self.method == "DELETE":
            return self.delete_file_nis
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

    def get_file_nis_list(self):
        """
        Returns a list of file NIS.

        Returns:
            tuple: A tuple containing the status code and the list of file NIS.
        """
        return self.status_code, self.file_nis_data.file_nis_list

    def get_file_nis_details(self):
        """
        Returns the details of a file NIS.

        Returns:
            tuple: A tuple containing the status code and the file NIS details.
        """
        if self.url.endswith(
            f"/file_nis/{self.file_nis_data.file_nis_id_not_exist}",
        ):
            return 404, self.file_nis_data.file_nis_error[404]
        return 200, self.file_nis_data.file_nis_detail

    def modify_file_nis(self):
        """
        Modifies a file NIS.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.file_nis_data.file_nis_valid_param_list):
            # invalid param given
            return 400, self.file_nis_data.file_nis_error[400]
        return 204, None

    def create_file_nis(self):
        """
        Creates a new file NIS.

        Returns:
            tuple: A tuple containing the status code and the file NIS ID.
        """
        return 201, self.file_nis_data.file_nis_id

    def delete_file_nis(self):
        """
        Deletes a file NIS.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
