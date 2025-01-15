from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.remote_support_data import RemoteSupportData


class RemoteSupportResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.remote_support_data = RemoteSupportData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/remote_support"):
                return self.get_remote_support_configs
            return self.get_remote_support_details
        if self.method == "POST":
            if self.url.endswith("/verify"):
                return self.verify_remote_support_config
            return self.send_test_remote_support_config
        if self.method == "PATCH":
            return self.modify_remote_support_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_remote_support_configs(self):
        return self.status_code, self.remote_support_data.remote_support_list

    def get_remote_support_details(self):
        return self.status_code, self.remote_support_data.remote_support_details

    def modify_remote_support_details(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.remote_support_data.remote_support_valid_param_list):
            # invalid param given
            return 400, self.remote_support_data.remote_support_error[400]
        return 204, None

    def verify_remote_support_config(self):
        return 204, None

    def send_test_remote_support_config(self):
        return 204, None
