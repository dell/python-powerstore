from PyPowerStore.tests.unit_tests.data.discovered_appliances import (
    DiscoveredApplianceData,
)
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class DiscoveredApplianceResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.discovered_appliance_data = DiscoveredApplianceData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            return self.get_discovered_appliances

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_discovered_appliances(self):
        return (
            self.status_code,
            self.discovered_appliance_data.discovered_appliance_list,
        )
