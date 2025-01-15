from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ServiceConfigResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/service_config"):
                if self.kwargs.get("params", {}).get("appliance_id"):
                    return self.get_service_config_by_appliance_id
                return self.get_service_configs
            return self.get_service_config_details
        if self.method == "PATCH":
            return self.modify_service_config

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_service_configs(self):
        return self.status_code, self.data.service_config_list

    def get_service_config_details(self):
        if self.url.endswith(
            "/service_config/{0}".format(self.data.invalid_service_config_id)
        ):
            return 404, self.data.service_config_error[404]
        return self.status_code, self.data.service_config_details_1

    def get_service_config_by_appliance_id(self):
        return self.status_code, [self.data.service_config_list]

    def modify_service_config(self):
        return 204, self.data.service_config_details_1
