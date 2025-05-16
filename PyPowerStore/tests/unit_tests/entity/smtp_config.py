""""Mock smtp config Api for Smtp Config Unit Tests"""

from PyPowerStore.tests.unit_tests.data.smtp_config_data import SmtpConfigData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SmtpConfigResponse(Entity):
    """
    This class is used to handle SMTP config related responses.

    It provides methods to get SMTP configs, SMTP config details, 
    modify SMTP config details, and execute API functions.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the SmtpConfigResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.smtp_config_data = SmtpConfigData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/smtp_config"):
                return self.get_smtp_configs
            return self.get_smtp_config_details
        if self.method == "POST":
            return self.test_smtp_config
        if self.method == "PATCH":
            return self.modify_smtp_config_details
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

    def get_smtp_configs(self):
        """
        Returns a list of SMTP configs.
        
        Returns:
            tuple: A tuple containing the status code and the list of SMTP configs.
        """
        return self.status_code, self.smtp_config_data.smtp_list

    def get_smtp_config_details(self):
        """
        Returns the details of an SMTP config.
        
        Returns:
            tuple: A tuple containing the status code and the SMTP config details.
        """
        return self.status_code, self.smtp_config_data.smtp_details

    def modify_smtp_config_details(self):
        """
        Modifies the SMTP config details.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.smtp_config_data.smtp_valid_param_list):
            # invalid param given
            return 400, self.smtp_config_data.smtp_error[400]
        return 204, None

    def test_smtp_config(self):
        """
        Tests the SMTP config.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
