from PyPowerStore.tests.unit_tests.data.file_interface_data import FileInterfaceData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class FileInterfaceResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.file_interface_data = FileInterfaceData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/file_interface"):
                return self.get_file_interface_list
            return self.get_file_interface_details
        if self.method == "PATCH":
            return self.modify_file_interface
        if self.method == "POST":
            return self.create_file_interface
        if self.method == "DELETE":
            return self.delete_file_interface

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_file_interface_list(self):
        return self.status_code, self.file_interface_data.file_interface_list

    def get_file_interface_details(self):
        if self.url.endswith(
            f"/file_interface/{self.file_interface_data.file_interface_id_not_exist}",
        ):
            return 404, self.file_interface_data.file_interface_error[404]
        return 200, self.file_interface_data.file_interface_detail

    def modify_file_interface(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.file_interface_data.file_interface_valid_param_list):
            # invalid param given
            return 400, self.file_interface_data.file_interface_error[400]
        return 204, None

    def create_file_interface(self):
        return 201, self.file_interface_data.file_interface_id

    def delete_file_interface(self):
        return 204, None
