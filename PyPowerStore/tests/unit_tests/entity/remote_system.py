"""Mock remote system Api for Remote System Unit Tests"""

# pylint: disable=too-many-return-statements

from PyPowerStore.tests.unit_tests.data.remote_system_data import RemoteSystemData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RemoteSystemResponse(Entity):
    """
    This class is used to handle Remote System related responses.

    It provides methods to get remote systems, remote system details, create remote systems, 
    modify remote systems and delete remote systems.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the RemoteSystemResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = RemoteSystemData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/remote_system"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_remote_system_by_name
                if self.kwargs.get("params", {}).get("management_address"):
                    return self.get_remote_system_by_mgmt_address
                return self.get_remote_systems
            return self.get_remote_system_details
        if self.method == "POST":
            if self.url.endswith("/query_appliances"):
                return self.get_remote_system_appliance_details
            return self.create_remote_system
        if self.method == "PATCH":
            return self.modify_remote_system
        if self.method == "DELETE":
            return self.delete_remote_system
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

    def get_remote_systems(self):
        """
        Returns a list of remote systems.
        
        Returns:
            tuple: A tuple containing the status code and the list of remote systems.
        """
        return self.status_code, self.data.remote_system_list

    def get_remote_system_details(self):
        """
        Returns the details of a remote system.
        
        Returns:
            tuple: A tuple containing the status code and the remote system details.
        """
        return self.status_code, self.data.remote_system_details_1

    def get_remote_system_by_name(self):
        """
        Returns the details of a remote system by name.
        
        Returns:
            tuple: A tuple containing the status code and the remote system details.
        """
        return self.status_code, [self.data.remote_system_details_1]

    def get_remote_system_by_mgmt_address(self):
        """
        Returns the details of a remote system by management address.
        
        Returns:
            tuple: A tuple containing the status code and the remote system details.
        """
        return self.status_code, [self.data.remote_system_details_1]

    def create_remote_system(self):
        """
        Creates a new remote system.
        
        Returns:
            tuple: A tuple containing the status code and the remote system details.
        """
        return 201, self.data.remote_system_details_1

    def modify_remote_system(self):
        """
        Modifies a remote system.
        
        Returns:
            tuple: A tuple containing the status code and the remote system details.
        """
        return 204, self.data.remote_system_details_1

    def delete_remote_system(self):
        """
        Deletes a remote system.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def get_remote_system_appliance_details(self):
        """
        Returns the appliance details of a remote system.
        
        Returns:
            tuple: A tuple containing the status code and the appliance details.
        """
        return self.status_code, self.data.remote_app_details
