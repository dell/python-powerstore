"""Mock rep_rule Api for Replication Rule Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RepRuleResponse(Entity):
    """
    This class is used to handle Replication Rule related responses.

    It provides methods to get replication rules, replication rule details, create
    replication rules, modify replication rules and delete replication rules.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the RepRuleResponse object.

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
            if self.url.endswith("/replication_rule"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_replication_rule_by_name
                return self.get_replication_rules
            return self.get_replication_rule_details
        if self.method == "POST":
            return self.create_replication_rule
        if self.method == "PATCH":
            return self.modify_replication_rule
        if self.method == "DELETE":
            return self.delete_replication_rule
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

    def get_replication_rules(self):
        """
        Returns a list of replication rules.

        Returns:
            tuple: A tuple containing the status code and the list of replication rules.
        """
        return self.status_code, self.data.rep_rule_list

    def get_replication_rule_details(self):
        """
        Returns the details of a replication rule.

        Returns:
            tuple: A tuple containing the status code and the replication rule details.
        """
        return self.status_code, self.data.rep_rule_details_1

    def get_replication_rule_by_name(self):
        """
        Returns a replication rule by name.

        Returns:
            tuple: A tuple containing the status code and the replication rule details.
        """
        return self.status_code, [self.data.rep_rule_details_1]

    def create_replication_rule(self):
        """
        Creates a new replication rule.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.snap_rule1

    def modify_replication_rule(self):
        """
        Modifies a replication rule.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "alert_threshold" in self.kwargs["data"]
            and self.kwargs["data"]["alert_threshold"]
            == self.data.invalid_alert_threshold
        ):
            return 400, self.data.rep_rule_error[400]
        return 204, self.data.rep_rule_details_1

    def delete_replication_rule(self):
        """
        Deletes a replication rule.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
