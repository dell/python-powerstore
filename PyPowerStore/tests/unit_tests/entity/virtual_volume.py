from PyPowerStore.tests.unit_tests.data.virtual_volume_data import VirtualVolumeData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class VirtualVolumeResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.virtual_volume_data = VirtualVolumeData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/virtual_volume"):
                return self.get_virtual_volumes

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_virtual_volumes(self):
        return self.status_code, self.virtual_volume_data.virtual_volume_list
