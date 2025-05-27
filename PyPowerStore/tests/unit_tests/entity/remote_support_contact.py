""""Mock remote_support_contact Api for Remote Support Contact Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.remote_support_contact_data import (
    RemoteSupportContactData,
)
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RemoteSupportContactResponse(Entity):
    """
    This class is used to handle Remote Support Contact related responses.

    It provides methods to get remote support contact configs, remote support contact details,
    and modify remote support contact details.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the RemoteSupportContactResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.remote_support_contact_data = RemoteSupportContactData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/remote_support_contact"):
                return self.get_remote_support_contact_configs
            return self.get_remote_support_contact_details
        if self.method == "PATCH":
            return self.modify_remote_support_contact_details
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

    def get_remote_support_contact_configs(self):
        """
        Returns a list of remote support contact configs.

        Returns:
            tuple: A tuple containing the status code and the list of remote support
            contact configs.
        """
        return (
            self.status_code,
            self.remote_support_contact_data.remote_support_contact_list,
        )

    def get_remote_support_contact_details(self):
        """
        Returns the details of a remote support contact.

        Returns:
            tuple: A tuple containing the status code and the remote support contact details.
        """
        return (
            self.status_code,
            self.remote_support_contact_data.remote_support_contact_details,
        )

    def modify_remote_support_contact_details(self):
        """
        Modifies the remote support contact details.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(
            self.remote_support_contact_data.remote_support_contact_valid_param_list,
        ):
            # invalid param given
            return (
                400,
                self.remote_support_contact_data.remote_support_contact_error[400],
            )
        return 204, None
