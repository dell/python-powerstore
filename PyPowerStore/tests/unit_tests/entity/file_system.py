from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.file_system_data import FileSystemData


class FileSystemResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = FileSystemData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/file_system"):
                params = self.kwargs.get("params", {})
                select = params.get("select", {})
                const_sel = constants.SELECT_ID_AND_NAME["select"]
                if params.get("name") and params.get("nas_server_id"):
                    return self.get_filesystem_details
                if params.get("parent_id") and select == const_sel:
                    return self.get_snapshots_filesystem
                return self.get_filesystems
            return self.get_filesystem_details
        if self.method == "POST":
            if self.url.endswith("/snapshot"):
                return self.create_filesystem_snapshot
            if self.url.endswith("/refresh"):
                return self.refresh_filesystem
            if self.url.endswith("/restore"):
                return self.restore_filesystem
            return self.create_filesystem
        if self.method == "PATCH":
            return self.modify_fs
        if self.method == "DELETE":
            return self.delete_fs

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_filesystems(self):
        return self.status_code, self.data.fs_list

    def create_filesystem(self):
        return 201, self.data.create_filesystem

    def get_filesystem_details(self):
        return 200, self.data.fs_detail

    def create_filesystem_snapshot(self):
        return 200, self.data.create_filesystem_snap

    def get_snapshots_filesystem(self):
        return 200, self.data.fs_snap_list

    def modify_fs(self):
        return 204, None

    def restore_filesystem(self):
        return 204, None

    def refresh_filesystem(self):
        return 204, None

    def delete_fs(self):
        if self.url.endswith("/file_system/{0}".format(self.data.invalid_fs_id)):
            return 404, self.data.fs_error[404]
        if self.url.endswith("/file_system/{0}".format(self.data.fs_id_with_snap)):
            return 422, self.data.fs_error[422]
        return 204, None
