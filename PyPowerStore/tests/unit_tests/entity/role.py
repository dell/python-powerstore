from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.common_data import CommonData


class RoleResponse(Entity):
    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/role'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_role_by_name
                else:
                    return self.get_roles
            else:
                return self.get_role_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_roles(self):
        return self.status_code, self.data.role_list

    def get_role_details(self):
        if self.url.endswith('/role/{0}'.format(
           self.data.role_does_not_exist)):
            return 404, self.data.role_error[404]
        return self.status_code, self.data.role_details_1

    def get_role_by_name(self):
        return self.status_code, [self.data.role_details_1]
