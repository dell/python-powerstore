"""Mock Ads Api for Ads Unit Tests"""

from PyPowerStore.tests.unit_tests.data.ads_data import AdsData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class AdsResponse(Entity):
    """
    This class is used to handle the response for ADS operations.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes an AdsResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ads_data = AdsData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the API name for the operation based on the HTTP method.

        Returns:
            function: The API name function.
        """
        if self.method == "GET":
            return self.get_file_ads
        return None

    def execute_api(self, api_name):
        """
        Executes the API operation.

        Args:
            api_name (function): The API name function.

        Returns:
            tuple: A tuple containing the HTTP status code and the response.
        """
        status_code, response = api_name()
        return status_code, response

    def get_file_ads(self):
        """
        Returns the list of ADS.

        Returns:
            tuple: A tuple containing the HTTP status code and the list of ADS.
        """
        return self.status_code, self.ads_data.ads_list
