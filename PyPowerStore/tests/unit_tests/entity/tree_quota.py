from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.common_data import CommonData


class TreeQuotaResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/file_tree_quota'):
                return self.get_tree_quotas
            else:
                return self.get_tree_quota_detail
        elif self.method == 'POST':
            return self.create_tree_quota
        elif self.method == 'PATCH':
            return self.modify_tree_quota
        elif self.method == 'DELETE':
            return self.delete_tree_quota

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_tree_quotas(self):
        return self.status_code, self.data.tq_list

    def create_tree_quota(self):
        data = self.kwargs.get('data', {})
        if set(data.keys()) - set(self.data.tq_valid_param):
            return 400, self.data.tq_error[400]
        return 201, self.data.create_tree_quota

    def get_tree_quota_detail(self):
        return self.status_code, self.data.tq_detail

    def modify_tree_quota(self):
        return 204, None

    def delete_tree_quota(self):
        if self.url.endswith('/file_tree_quota/{0}'.format(
           self.data.invalid_tq_id)):
            return 404, self.data.tq_error[404]
        return 204, None
