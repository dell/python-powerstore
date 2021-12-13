from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.utils import constants


class VolumeResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'PATCH':
            return self.modify_volume
        elif self.method == 'POST':
            if self.url.endswith('/volume'):
                return self.create_volume
            elif self.url.endswith('/attach'):
                return self.map_volume
            elif self.url.endswith('/detach'):
                return self.unmap_volume
            elif self.url.endswith('/snapshot'):
                return self.create_snap
        elif self.method == 'GET':
            # its a GET request
            if self.url.endswith('/volume'):
                if self.kwargs.get('params', {}).get('select') == \
                   constants.SELECT_ALL_VOLUME.get('select'):
                    return self.get_volume_by_name
                else:
                    return self.get_volume_list
            else:
                return self.get_volume_details
        elif self.method == 'DELETE':
            return self.delete_volume

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_volume_list(self):
        return self.status_code, self.data.volume_list

    def create_volume(self):
        return 201, self.data.create_volume

    def get_volume_details(self):
        return self.status_code, self.data.volume1

    def get_volume_by_name(self):
        return self.status_code, [self.data.volume1]

    def modify_volume(self):
        if 'protection_policy_id' in self.kwargs['data'] and \
           self.kwargs['data']['protection_policy_id'] == \
               self.data.invalid_pol_id:
            return 404, self.data.policy_error[404]
        return 204, None

    def map_volume(self):
        return 204, None

    def unmap_volume(self):
        return 204, None

    def delete_volume(self):
        return 204, None

    def create_snap(self):
        return 200, self.data.create_vol_snap
