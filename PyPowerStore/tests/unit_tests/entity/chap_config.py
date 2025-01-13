from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class ChapConfigResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/chap_config'):
                return self.get_chap_configs
            return self.get_chap_config_details
        if self.method == 'PATCH':
            return self.modify_chap_config

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_chap_configs(self):
        return self.status_code, self.data.chap_config_list

    def get_chap_config_details(self):
        if self.url.endswith('/chap_config/{0}'.format(
           self.data.invalid_chap_config_id)):
            return 404, self.data.chap_config_error[404]
        return self.status_code, self.data.chap_config_details_1

    def modify_chap_config(self):
        return 204, self.data.chap_config_details_1
