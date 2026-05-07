"""Mock job Api for Job Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class JobResponse(Entity):
    """
    This class is used to handle Job related responses.
    
    It provides methods to get job details.
    """
    def __init__(self, method, url, **kwargs):
        """
        Initializes the JobResponse object.
        
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
        Returns the name of the API function based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            return self.get_job_details
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

    def get_job_details(self):
        """
        Returns the details of a job.
        
        Returns:
            tuple: A tuple containing the status code and the job details.
        """
        if self.url.endswith(f"/job/{self.data.job_does_not_exist}"):
            return 404, self.data.job_error[404]
        return self.status_code, self.data.job_details
