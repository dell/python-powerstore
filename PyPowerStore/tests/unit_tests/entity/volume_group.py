from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class VolumeGroupResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/volume_group'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_volume_group_by_name
                return self.get_volume_group_list
            return self.get_volume_group_details
        if self.method == 'POST':
            if self.url.endswith('/add_members'):
                return self.add_members_to_volume_group
            if self.url.endswith('/clone'):
                return self.clone_volume_group
            if self.url.endswith('/restore'):
                return self.restore_volume_group
            if self.url.endswith('/refresh'):
                return self.refresh_volume_group
            return self.create_volume_group
        if self.method == 'PATCH':
            return self.modify_volume_group
        if self.method == 'DELETE':
            return self.delete_volume_group

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_volume_group_list(self):
        return self.status_code, self.data.volumegroup_list

    def get_volume_group_details(self):
        return self.status_code, self.data.volume_group1

    def get_volume_group_by_name(self):
        return self.status_code, [self.data.volume_group1]

    def create_volume_group(self):
        return 201, self.data.vg_id1

    def add_members_to_volume_group(self):
        if 'volume_ids' in self.kwargs['data'] and \
                self.kwargs['data']['volume_ids'][0] == \
                self.data.invalid_vol_id:
            return 404, self.data.volume_error[404]
        return 201, None

    def modify_volume_group(self):
        if 'protection_policy_id' in self.kwargs['data'] and \
           self.kwargs['data']['protection_policy_id'] == \
                self.data.invalid_pol_id:
            return 404, self.data.policy_error[404]
        return 204, None

    def delete_volume_group(self):
        return 204, None

    def clone_volume_group(self):
        return self.status_code, self.data.vg_id2

    def refresh_volume_group(self):
        return self.status_code, self.data.snapshot_id

    def restore_volume_group(self):
        return self.status_code, self.data.snapshot_id
