from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class SMBShareResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/smb_share"):
                if self.kwargs.get("params", {}).get(
                    "select"
                ) == constants.SELECT_ALL_SMB_SHARE.get("select"):
                    return self.get_smb_detail
                return self.get_smbshares
            return self.get_smb_detail
        if self.method == "POST":
            return self.create_smb
        if self.method == "PATCH":
            return self.modify_smb
        if self.method == "DELETE":
            return self.delete_smb

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_smbshares(self):
        return self.status_code, self.data.smb_list

    def create_smb(self):
        return 201, self.data.create_smb

    def get_smb_detail(self):
        return 200, self.data.smb_detail

    def modify_smb(self):
        return 204, None

    def delete_smb(self):
        if self.url.endswith("/smb_share/{0}".format(self.data.invalid_smb_id)):
            return 404, self.data.smb_error[404]
        return 204, None
