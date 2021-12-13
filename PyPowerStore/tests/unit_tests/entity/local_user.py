from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class LocalUserResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/local_user'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_local_user_by_name
                else:
                    return self.get_local_users
            else:
                return self.get_local_user_details
        elif self.method == 'PATCH':
            return self.modify_local_user
        elif self.method == 'POST':
            return self.create_local_user
        elif self.method == 'DELETE':
            return self.delete_local_user

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_local_users(self):
        return self.status_code, self.data.local_user_list

    def get_local_user_details(self):
        if self.url.endswith('/local_user/{0}'.format(
           self.data.local_user_does_not_exist)):
            return 404, self.data.local_user_error[404]
        return self.status_code, self.data.local_user_details

    def get_local_user_by_name(self):
        return self.status_code, self.data.local_user_details

    def modify_local_user(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.data.local_user_valid_param_list):
            # invalid param given
            return 400, self.data.local_user_error[400]
        return 204, None

    def create_local_user(self):
        return 201, self.data.local_user_create_response

    def delete_local_user(self):
        return 204, None

