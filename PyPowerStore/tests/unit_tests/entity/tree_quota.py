"""Mock tree_quota Api for Tree Quota Unit Tests"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class TreeQuotaResponse(Entity):
    """
    This class is used to handle Tree Quota related responses.

    It provides methods to get tree quotas, tree quota details, create tree quotas, 
    modify tree quotas and delete tree quotas.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the TreeQuotaResponse object.
        
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
            if self.url.endswith("/file_tree_quota"):
                return self.get_tree_quotas
            return self.get_tree_quota_detail
        if self.method == "POST":
            return self.create_tree_quota
        if self.method == "PATCH":
            return self.modify_tree_quota
        if self.method == "DELETE":
            return self.delete_tree_quota
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

    def get_tree_quotas(self):
        """
        Returns a list of tree quotas.
        
        Returns:
            tuple: A tuple containing the status code and the list of tree quotas.
        """
        return self.status_code, self.data.tq_list

    def create_tree_quota(self):
        """
        Creates a new tree quota.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        if set(data.keys()) - set(self.data.tq_valid_param):
            return 400, self.data.tq_error[400]
        return 201, self.data.create_tree_quota

    def get_tree_quota_detail(self):
        """
        Returns the details of a tree quota.
        
        Returns:
            tuple: A tuple containing the status code and the tree quota details.
        """
        return self.status_code, self.data.tq_detail

    def modify_tree_quota(self):
        """
        Modifies a tree quota.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_tree_quota(self):
        """
        Deletes a tree quota.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if self.url.endswith(f"/file_tree_quota/{self.data.invalid_tq_id}"):
            return 404, self.data.tq_error[404]
        return 204, None
