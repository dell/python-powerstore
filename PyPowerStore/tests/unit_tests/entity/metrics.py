"""Mock metrics Api for Metrics Unit Tests"""

from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class MetricsResponse(Entity):
    """
    This class is used to handle metrics related responses.

    It provides methods to get performance metrics.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the MetricsResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.status_code = 200

    def get_post_api_name(self):
        """
        Returns the API function name based on the POST request URL.

        Returns:
            function: The API function.
        """
        if self.url.endswith("/generate"):
            return self.get_performance_metrics
        return None

    def get_performance_metrics(self):
        """
        Mock performance metrics response.

        Returns:
            dict: Mock performance metrics data.
        """
        return {
            "metrics": [
                {
                    "timestamp": "2023-01-01T00:00:00Z",
                    "entity_id": "A1",
                    "entity_type": "appliance",
                    "values": {
                        "cpu_usage": 50.0,
                        "memory_usage": 60.0,
                        "disk_usage": 40.0
                    }
                }
            ]
        }

    def get_api_name(self):
        """
        Returns the API function name based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "POST":
            return self.get_post_api_name()
        return None

    def execute_api(self, api_name):
        """
        Executes the API function and returns the result.

        Args:
            api_name (function): The API function to execute.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if api_name:
            response = api_name()
            return self.status_code, response
        return 400, None
