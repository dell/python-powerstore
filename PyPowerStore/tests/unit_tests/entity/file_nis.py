from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.file_nis_data import FileNISData
from PyPowerStore.utils import constants
from PyPowerStore.objects import file_nis

class FileNISResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.file_nis_data = FileNISData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/file_nis'):
                return self.get_file_nis_list
            else:
                return self.get_file_nis_details
        elif self.method == 'PATCH':
            return self.modify_file_nis
        elif self.method == 'POST':
            return self.create_file_nis
        elif self.method == 'DELETE':
            return self.delete_file_nis

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_file_nis_list(self):
        return self.status_code, self.file_nis_data.file_nis_list

    def get_file_nis_details(self):
        if self.url.endswith('/file_nis/{0}'.format(
           self.file_nis_data.file_nis_id_not_exist)):
            return 404, self.file_nis_data.file_nis_error[404]
        return 200, self.file_nis_data.file_nis_detail

    def modify_file_nis(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.file_nis_data.file_nis_valid_param_list):
            # invalid param given
            return 400, self.file_nis_data.file_nis_error[400]
        return 204, None

    def create_file_nis(self):
       return 201, self.file_nis_data.file_nis_id

    def delete_file_nis(self):
        return 204, None
