from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class VcenterResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/vcenter'):
                return self.get_vcenters
            else:
                return self.get_vcenter_details
        elif self.method == 'PATCH':
            return self.modify_vcenter

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_vcenters(self):
        return self.status_code, self.data.vcenter_list

    def get_vcenter_details(self):
        return self.status_code, self.data.vcenter_details

    def modify_vcenter(self):
        return self.status_code, self.data.vcenter_details