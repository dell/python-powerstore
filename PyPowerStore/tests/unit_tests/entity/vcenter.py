from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.vcenter_data import VcenterData


class VcenterResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.vcenter_data = VcenterData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/vcenter'):
                return self.get_vcenters
            else:
                return self.get_vcenter_details
        elif self.method == 'PATCH':
            return self.modify_vcenter
        elif self.method == 'POST':
            return self.add_vcenter
        elif self.method == 'DELETE':
            return self.remove_vcenter

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_vcenters(self):
        return self.status_code, self.vcenter_data.vcenter_list

    def get_vcenter_details(self):
        return self.status_code, self.vcenter_data.vcenter_details

    def modify_vcenter(self):
        return self.status_code, self.vcenter_data.vcenter_details

    def add_vcenter(self):
        return 201, self.vcenter_data.vcenter_id

    def remove_vcenter(self):
        return 204, None
