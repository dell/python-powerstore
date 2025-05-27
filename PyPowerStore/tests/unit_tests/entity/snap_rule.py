""""Mock snap_rule Api for Snap Rule Unit Tests"""

# pylint: disable=too-many-return-statements

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SnapRuleResponse(Entity):
    """
    This class is used to handle Snap Rule related responses.

    It provides methods to get snap rules, get snap rule details, 
    get snap rule by name, create snap rule, modify snap rule and delete snap rule.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the SnapRuleResponse object.

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
            if self.url.endswith("/snapshot_rule"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_snapshot_rule_by_name
                return self.get_snap_rules
            return self.get_snapshot_rule_details
        if self.method == "POST":
            return self.create_snapshot_rule
        if self.method == "PATCH":
            return self.modify_snapshot_rule
        if self.method == "DELETE":
            return self.delete_snapshot_rule
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

    def get_snap_rules(self):
        """
        Returns a list of snap rules.

        Returns:
            tuple: A tuple containing the status code and the list of snap rules.
        """
        return self.status_code, self.data.snap_rule_list

    def get_snapshot_rule_details(self):
        """
        Returns the details of a snap rule.

        Returns:
            tuple: A tuple containing the status code and the snap rule details.
        """
        return self.status_code, self.data.snap_rule1

    def get_snapshot_rule_by_name(self):
        """
        Returns a snap rule by name.

        Returns:
            tuple: A tuple containing the status code and the snap rule.
        """
        return self.status_code, [self.data.snap_rule1]

    def create_snapshot_rule(self):
        """
        Creates a new snap rule.

        Returns:
            tuple: A tuple containing the status code and the new snap rule.
        """
        return 201, self.data.snap_rule1

    def modify_snapshot_rule(self):
        """
        Modifies a snap rule.

        Returns:
            tuple: A tuple containing the status code and the modified snap rule.
        """
        if (
            "interval" in self.kwargs["data"]
            and self.kwargs["data"]["interval"] == self.data.invalid_interval
        ):
            return 400, self.data.interval_error[400]
        return 204, self.data.snap_rule1_modified

    def delete_snapshot_rule(self):
        """
        Deletes a snap rule.

        Returns:
            tuple: A tuple containing the status code and None.
        """
        return 204, None
