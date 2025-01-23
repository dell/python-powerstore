from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class IPPortResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            return self.get_ip_port_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_ip_port_details(self):
        return self.status_code, self.data.ip_port_details
