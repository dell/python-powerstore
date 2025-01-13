from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.dns_data import DnsData


class DnsResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.dns_data = DnsData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/dns'):
                return self.get_dns_list
            return self.get_dns_details
        if self.method == "PATCH":
            return self.modify_dns_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_dns_list(self):
        return self.status_code, self.dns_data.dns_list

    def get_dns_details(self):
        return self.status_code, self.dns_data.dns_details

    def modify_dns_details(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.dns_data.dns_valid_param_list):
            # invalid param given
            return 400, self.dns_data.dns_error[400]
        return 204, None
