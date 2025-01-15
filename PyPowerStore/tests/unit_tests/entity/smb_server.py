from PyPowerStore.tests.unit_tests.data.smb_server_data import SMBServerData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class SMBServerResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.smb_server_data = SMBServerData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/smb_server"):
                return self.get_smb_server_list
            return self.get_smb_server_details
        if self.method == "PATCH":
            return self.modify_smb_server
        if self.method == "POST":
            return self.create_smb_server
        if self.method == "DELETE":
            return self.delete_smb_server

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_smb_server_list(self):
        return self.status_code, self.smb_server_data.smb_server_list

    def get_smb_server_details(self):
        if self.url.endswith(
            "/smb_server/{0}".format(self.smb_server_data.smb_server_id_not_exist)
        ):
            return 404, self.smb_server_data.smb_server_error[404]
        return 200, self.smb_server_data.smb_server_detail

    def modify_smb_server(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.smb_server_data.smb_server_valid_param_list):
            # invalid param given
            return 400, self.smb_server_data.smb_server_error[400]
        return 204, None

    def create_smb_server(self):
        return 201, self.smb_server_data.smb_server_id

    def delete_smb_server(self):
        return 204, None
