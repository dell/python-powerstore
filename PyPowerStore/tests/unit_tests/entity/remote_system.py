from PyPowerStore.tests.unit_tests.data.remote_system_data import RemoteSystemData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RemoteSystemResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = RemoteSystemData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/remote_system"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_remote_system_by_name
                if self.kwargs.get("params", {}).get("management_address"):
                    return self.get_remote_system_by_mgmt_address
                return self.get_remote_systems
            return self.get_remote_system_details
        if self.method == "POST":
            if self.url.endswith("/query_appliances"):
                return self.get_remote_system_appliance_details
            return self.create_remote_system
        if self.method == "PATCH":
            return self.modify_remote_system
        if self.method == "DELETE":
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

    def get_remote_system_appliance_details(self):
        return self.status_code, self.data.remote_app_details
