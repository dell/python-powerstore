from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.utils import constants


class NASServerResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/nas_server'):
                sel = self.kwargs.get('params', {}).get('select', {})
                if sel and sel == constants.SELECT_ALL_NAS_SERVER['select']:
                    return self.get_nasserver_detail
                else:
                    return self.get_nasservers
            else:
                return self.get_nasserver_detail
        elif self.method == 'PATCH':
            return self.modify_nas

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_nasservers(self):
        return self.status_code, self.data.nas_list

    def get_nasserver_detail(self):
        if self.url.endswith('/nas_server/{0}'.format(
           self.data.nas_id_not_exist)):
            return 404, self.data.nas_error[404]
        return 200, self.data.nas_detail

    def modify_nas(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.data.nas_valid_param_list):
            # invalid param given
            return 400, self.data.nas_error[400]
        elif self.url.endswith('/nas_server/{0}'.format(
             self.data.nas_id_not_exist)):
            return 404, self.data.nas_error[404]
        return 204, None
