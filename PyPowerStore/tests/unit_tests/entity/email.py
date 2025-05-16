"""Mock email Api for Email Unit Tests"""

# pylint: disable=too-many-return-statements

from PyPowerStore.tests.unit_tests.data.email_data import EmailData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class EmailResponse(Entity):
    """
    This class is used to handle Email related responses.
    
    It provides methods to get emails, email details, create emails, 
    reset emails, exchange emails, and modify emails.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the EmailResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.email_data = EmailData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/email_notify_destination"):
                if self.kwargs.get("params", {}).get("email_address"):
                    return self.get_destination_email_by_address
                return self.get_destination_emails
            return self.get_destination_email_details
        if self.method == "POST":
            if self.url.endswith("/test"):
                return self.test_destination_email
            return self.create_destination_email
        if self.method == "PATCH":
            return self.modify_destination_email
        if self.method == "DELETE":
            return self.delete_destination_email
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

    def get_destination_emails(self):
        """
        Returns a list of emails.
        
        Returns:
            tuple: A tuple containing the status code and the list of emails.
        """
        return self.status_code, self.email_data.email_list

    def get_destination_email_details(self):
        """
        Returns the details of an email.
        
        Returns:
            tuple: A tuple containing the status code and the email details.
        """
        return self.status_code, self.email_data.email_details_1

    def get_destination_email_by_address(self):
        """
        Returns the details of an email by address.
        
        Returns:
            tuple: A tuple containing the status code and the email details.
        """
        return self.status_code, self.email_data.email_details_1

    def create_destination_email(self):
        """
        Creates a new email.
        
        Returns:
            tuple: A tuple containing the status code and the email details.
        """
        return 201, self.email_data.email_details_1

    def modify_destination_email(self):
        """
        Modifies an email.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.email_data.email_valid_param_list):
            # invalid param given
            return 400, self.email_data.email_error[400]
        return 204, None

    def delete_destination_email(self):
        """
        Deletes an email.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def test_destination_email(self):
        """
        Tests an email.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
