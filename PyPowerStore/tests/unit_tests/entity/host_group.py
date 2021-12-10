from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class HostGroupResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/host_group'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_host_group_by_name
                else:
                    return self.get_hostgroups
            else:
                return self.get_host_group_details
        elif self.method == 'POST':
            return self.create_host_group
        elif self.method == 'PATCH':
            return self.modify_host_group
        elif self.method == 'DELETE':
            return self.delete_host_group

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_hostgroups(self):
        return self.status_code, self.data.hg_list

    def get_host_group_details(self):
        return self.status_code, self.data.hg1

    def get_host_group_by_name(self):
        return self.status_code, [self.data.hg1]

    def create_host_group(self):
        return 201, self.data.create_hg

    def modify_host_group(self):
        if 'name' in self.kwargs['data'] and \
                self.kwargs['data']['name'] == self.data.existing_hg_name:
            return 400, self.data.invalid_rename_error
        elif 'add_host_ids' in self.kwargs['data'] and \
                self.kwargs['data']['add_host_ids'][0] == \
                self.data.invalid_host_id:
            return 400, self.data.add_invalid_host_error
        return 204, None

    def delete_host_group(self):
        return 204, None
