from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.common_data import CommonData


class HostResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/host_volume_mapping'):
                return self.get_host_volume_mapping
            elif self.url.endswith('/host'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_host_by_name
                return self.get_hosts
            else:
                return self.get_host_details
        elif self.method == 'POST':
            return self.create_host
        elif self.method == 'PATCH':
            return self.modify_host
        elif self.method == 'DELETE':
            return self.delete_host

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_host_volume_mapping(self):
        return self.status_code, self.data.hlu_details

    def get_hosts(self):
        return self.status_code, self.data.host_list

    def get_host_by_name(self):
        return self.status_code, [self.data.host1]

    def get_host_details(self):
        return self.status_code, self.data.host1

    def create_host(self):
        return 201, self.data.create_host

    def modify_host(self):
        if 'add_initiators' in self.kwargs['data'] and\
                self.kwargs['data']['add_initiators']['name'] == \
                self.data.invalid_initiator['name']:
            return 400, self.data.add_invalid_initiator_error[400]
        elif 'remove_initiators' in self.kwargs['data'] and\
                self.kwargs['data']['remove_initiators'][0] == \
                self.data.invalid_initiator['name']:
            return 400, self.data.remove_invalid_initiator_error[400]
        return 204, None

    def delete_host(self):
        return 204, None
