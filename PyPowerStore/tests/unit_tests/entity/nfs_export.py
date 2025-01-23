from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class NFSExportResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/nfs_export"):
                sel = self.kwargs.get("params", {}).get("select")
                if sel == constants.SELECT_ALL_NFS_EXPORT["select"]:
                    return self.get_nfs_detail
                return self.get_nfsexports
            return self.get_nfs_detail
        if self.method == "POST":
            return self.create_nfs
        if self.method == "PATCH":
            return self.modify_nfs
        if self.method == "DELETE":
            return self.delete_nfs

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_nfsexports(self):
        return self.status_code, self.data.nfs_list

    def create_nfs(self):
        return 201, self.data.create_nfs

    def get_nfs_detail(self):
        return self.status_code, self.data.nfs_detail

    def modify_nfs(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.nfs_valid_param):
            # invalid param given
            return 400, self.data.nfs_error[400]
        return 204, None

    def delete_nfs(self):
        if self.url.endswith(f"/nfs_export/{self.data.invalid_nfs}"):
            return 404, self.data.nfs_error[404]
        return 204, None
