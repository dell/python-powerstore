from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class ServiceUserResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/service_user'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_service_user_by_name
                return self.get_service_users
            return self.get_service_user_details
        if self.method == 'PATCH':
            return self.modify_service_user

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_service_users(self):
        return self.status_code, self.data.service_user_list

    def get_service_user_details(self):
        if self.url.endswith('/service_user/{0}'.format(
           self.data.invalid_service_user_id)):
            return 404, self.data.service_user_error[404]
        return self.status_code, self.data.service_user_details_1

    def get_service_user_by_name(self):
        return self.status_code, [self.data.service_user_details_1]

    def modify_service_user(self):
        return 204, self.data.service_user_details_1
