from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class ApplianceResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/appliance"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_appliance_by_name
                return self.get_appliances
            return self.get_appliance_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_appliances(self):
        return self.status_code, self.data.appliance_list

    def get_appliance_details(self):
        if self.url.endswith(
            "/appliance/{0}".format(self.data.appliance_does_not_exist)
        ):
            return 404, self.data.appliance_error[404]
        return self.status_code, self.data.appliance_details_1

    def get_appliance_by_name(self):
        return self.status_code, [self.data.appliance_details_1]
