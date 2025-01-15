from PyPowerStore.tests.unit_tests.data.security_config_data import SecurityConfigData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SecurityConfigResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = SecurityConfigData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/security_config"):
                return self.get_security_configs
            return self.get_security_config_details
        if self.method == "PATCH":
            return self.modify_security_config

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_security_configs(self):
        return self.status_code, self.data.security_config_list

    def get_security_config_details(self):
        if self.url.endswith(
            "/security_config/{0}".format(self.data.invalid_security_config_id)
        ):
            return 404, self.data.security_config_error[404]
        return self.status_code, self.data.security_config_details_1

    def modify_security_config(self):
        if (
            "protocol_mode" in self.kwargs["data"]
            and self.kwargs["data"]["protocol_mode"] == self.data.invalid_protocol_mode
        ):
            return 400, self.data.security_config_error[400]
        return 204, self.data.security_config_details_1
