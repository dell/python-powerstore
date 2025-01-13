from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class UserQuotaResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/file_user_quota'):
                return self.get_user_quotas
            return self.get_user_quota
        if self.method == 'POST':
            return self.create_user_quota
        if self.method == 'PATCH':
            return self.modify_user_quota

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_user_quotas(self):
        return self.status_code, self.data.uq_list

    def create_user_quota(self):
        data = self.kwargs.get('data', {})
        if set(data.keys()) - set(self.data.uq_valid_param):
            return 400, self.data.uq_error[400]
        return 201, self.data.create_user_quota

    def get_user_quota(self):
        return self.status_code, self.data.uq_detail

    def modify_user_quota(self):
        return 204, None
