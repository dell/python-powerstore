"""Mock policy Api for Policy Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class PolicyResponse(Entity):
    """
    This class is used to handle Policy related responses.
    
    It provides methods to get policies, get protection policy by name, get
    protection policy details, create protection policy, modify protection
    policy and delete protection policy.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the PolicyResponse object.
        
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
            if self.url.endswith("/policy"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_protection_policy_by_name
                return self.get_policies
            return self.get_protection_policy_details
        if self.method == "POST":
            return self.create_protection_policy
        if self.method == "PATCH":
            return self.modify_protection_policy
        if self.method == "DELETE":
            return self.delete_protection_policy
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

    def get_policies(self):
        """
        Returns a list of policies.
        
        Returns:
            tuple: A tuple containing the status code and the list of policies.
        """
        return self.status_code, self.data.pol_list

    def get_protection_policy_by_name(self):
        """
        Returns a protection policy by name.
        
        Returns:
            tuple: A tuple containing the status code and the protection policy.
        """
        return self.status_code, [self.data.protection_policy1]

    def get_protection_policy_details(self):
        """
        Returns the details of a protection policy.
        
        Returns:
            tuple: A tuple containing the status code and the protection policy details.
        """
        return self.status_code, self.data.protection_policy1

    def create_protection_policy(self):
        """
        Creates a new protection policy.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.protection_policy1

    def modify_protection_policy(self):
        """
        Modifies a protection policy.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "add_snapshot_rule_ids" in self.kwargs["data"]
            and self.kwargs["data"]["add_snapshot_rule_ids"][0]
            == self.data.invalid_sr_id
        ):
            return 404, self.data.add_invalid_sr_error[404]
        if (
            "remove_snapshot_rule_ids" in self.kwargs["data"]
            and self.kwargs["data"]["remove_snapshot_rule_ids"][0]
            == self.data.invalid_sr_id
        ):
            return 404, self.data.remove_invalid_sr_error[404]
        return 204, self.data.protection_policy1_modified

    def delete_protection_policy(self):
        """
        Deletes a protection policy.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
