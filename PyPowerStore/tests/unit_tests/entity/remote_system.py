from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.remote_system_data import RemoteSystemData


class RemoteSystemResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = RemoteSystemData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/remote_system'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_remote_system_by_name
                elif self.kwargs.get('params', {}).get('management_address'):
                    return self.get_remote_system_by_mgmt_address
                else:
                    return self.get_remote_systems
            else:
                return self.get_remote_system_details
        elif self.method == 'POST':
            return self.create_remote_system
        elif self.method == "PATCH":
            return self.modify_remote_system
        elif self.method == "DELETE":
            return self.delete_remote_system

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_remote_systems(self):
        return self.status_code, self.data.remote_system_list

    def get_remote_system_details(self):
        return self.status_code, self.data.remote_system_details_1

    def get_remote_system_by_name(self):
        return self.status_code, [self.data.remote_system_details_1]

    def get_remote_system_by_mgmt_address(self):
        return self.status_code, [self.data.remote_system_details_1]

    def create_remote_system(self):
        return 201, self.data.remote_system_details_1

    def modify_remote_system(self):
        return 204, self.data.remote_system_details_1

    def delete_remote_system(self):
        return 204, None
