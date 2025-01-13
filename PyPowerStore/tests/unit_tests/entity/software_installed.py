from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class SoftwareResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/software_installed'):
                return self.get_softwares
            return self.get_software_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_softwares(self):
        return self.status_code, self.data.software_list

    def get_software_details(self):
        return self.status_code, self.data.software_details_1