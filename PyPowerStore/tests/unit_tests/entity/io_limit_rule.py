"""Mock IO Limit Rule API for IO Limit Rule Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class IoLimitRuleResponse(Entity):
    """
    This class is used to handle IO Limit Rule related responses.

    It provides methods to get io_limit_rules, get io_limit_rule by name,
    get io_limit_rule details, create io_limit_rule, modify io_limit_rule,
    and delete io_limit_rule.
    """

    def __init__(self, method, url, **kwargs):
        """Initialize IoLimitRuleResponse.

        Args:
            method: HTTP method
            url: Request URL
            **kwargs: Additional request parameters
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        """Return the API method name based on HTTP method and URL.

        Returns:
            The corresponding API method
        """
        if self.method == "GET":
            if self.url.endswith("/io_limit_rule"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_io_limit_rule_by_name
                return self.get_io_limit_rules
            return self.get_io_limit_rule_details
        if self.method == "POST":
            return self.create_io_limit_rule
        if self.method == "PATCH":
            return self.modify_io_limit_rule
        if self.method == "DELETE":
            return self.delete_io_limit_rule
        return None

    def execute_api(self, api_name):
        """Execute the given API method.

        Args:
            api_name: The API method to execute

        Returns:
            Tuple of status code and response
        """
        status_code, response = api_name()
        return status_code, response

    def get_io_limit_rules(self):
        """Get all IO limit rules.

        Returns:
            Tuple of status code and rule list
        """
        return self.status_code, self.data.io_limit_rule_list

    def get_io_limit_rule_by_name(self):
        """Get IO limit rule by name.

        Returns:
            Tuple of status code and rule
        """
        return self.status_code, [self.data.io_limit_rule1]

    def get_io_limit_rule_details(self):
        """Get IO limit rule details by ID.

        Returns:
            Tuple of status code and rule details
        """
        if self.data.invalid_io_limit_rule_id in self.url:
            return 404, self.data.io_limit_rule_error[404]
        return self.status_code, self.data.io_limit_rule1

    def create_io_limit_rule(self):
        """Create a new IO limit rule.

        Returns:
            Tuple of status code and created rule ID
        """
        return 201, {"id": self.data.io_limit_rule_id1}

    def modify_io_limit_rule(self):
        """Modify an existing IO limit rule.

        Returns:
            Tuple of status code and response
        """
        if self.data.invalid_io_limit_rule_id in self.url:
            return 404, self.data.io_limit_rule_error[404]
        return 204, None

    def delete_io_limit_rule(self):
        """Delete an IO limit rule.

        Returns:
            Tuple of status code and response
        """
        if self.data.invalid_io_limit_rule_id in self.url:
            return 404, self.data.io_limit_rule_error[404]
        return 204, None
