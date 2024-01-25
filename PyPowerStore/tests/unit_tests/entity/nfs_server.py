from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.nfs_server_data import NFSServerData
from PyPowerStore.utils import constants
from PyPowerStore.objects import nfs_server

class NFSServerResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.nfs_server_data = NFSServerData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/nfs_server'):
                return self.get_nfs_server_list
            else:
                return self.get_nfs_server_details
        elif self.method == 'PATCH':
            return self.modify_nfs_server
        elif self.method == 'POST':
            return self.create_nfs_server
        elif self.method == 'DELETE':
            return self.delete_nfs_server

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_nfs_server_list(self):
        return self.status_code, self.nfs_server_data.nfs_server_list

    def get_nfs_server_details(self):
        if self.url.endswith('/nfs_server/{0}'.format(
           self.nfs_server_data.nfs_server_id_not_exist)):
            return 404, self.nfs_server_data.nfs_server_error[404]
        return 200, self.nfs_server_data.nfs_server_detail

    def modify_nfs_server(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.nfs_server_data.nfs_server_valid_param_list):
            # invalid param given
            return 400, self.nfs_server_data.nfs_server_error[400]
        return 204, None

    def create_nfs_server(self):
       return 201, self.nfs_server_data.nfs_server_id

    def delete_nfs_server(self):
        return 204, None
