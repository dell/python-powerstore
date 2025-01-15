from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class NetworkResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/network"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_network_by_name
                return self.get_networks
            return self.get_network_details
        if self.method == "PATCH":
            return self.modify_network
        if self.method == "POST":
            return self.add_remove_ports

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_networks(self):
        return self.status_code, self.data.network_list

    def get_network_details(self):
        if self.url.endswith("/network/{0}".format(self.data.network_does_not_exist)):
            return 404, self.data.network_error[404]
        return self.status_code, self.data.network_details_1

    def get_network_by_name(self):
        return self.status_code, [self.data.network_details_1]

    def modify_network(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.network_valid_param_list):
            # invalid param given
            return 400, self.data.network_error[400]
        return 204, None

    def add_remove_ports(self):
        return self.status_code, self.data.network_details_1
