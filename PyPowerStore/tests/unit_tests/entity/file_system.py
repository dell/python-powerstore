"""Mock FileSystem Api for File System Unit Tests"""

# pylint: disable=too-many-return-statements

from PyPowerStore.tests.unit_tests.data.file_system_data import FileSystemData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class FileSystemResponse(Entity):
    """
    This class is used to handle File System related responses.
    
    It provides methods to get file systems, create file systems, get file system details, 
    create file system snapshots, get snapshots of a file system, modify a file system, 
    restore a file system, refresh a file system, and delete a file system.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the FileSystemResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = FileSystemData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
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
        return None

    def execute_api(self, api_name):
        """
        Executes the API function and returns the result.
        
        Args:
            api_name (function): The API function to execute.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        status_code, response = api_name()
        return status_code, response

    def get_filesystems(self):
        """
        Returns a list of file systems.
        
        Returns:
            tuple: A tuple containing the status code and the list of file systems.
        """
        return self.status_code, self.data.fs_list

    def create_filesystem(self):
        """
        Creates a new file system.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.create_filesystem

    def get_filesystem_details(self):
        """
        Returns the details of a file system.
        
        Returns:
            tuple: A tuple containing the status code and the file system details.
        """
        return 200, self.data.fs_detail

    def create_filesystem_snapshot(self):
        """
        Creates a new file system snapshot.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 200, self.data.create_filesystem_snap

    def get_snapshots_filesystem(self):
        """
        Returns a list of snapshots of a file system.
        
        Returns:
            tuple: A tuple containing the status code and the list of snapshots.
        """
        return 200, self.data.fs_snap_list

    def modify_fs(self):
        """
        Modifies a file system.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def restore_filesystem(self):
        """
        Restores a file system.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def refresh_filesystem(self):
        """
        Refreshes a file system.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_fs(self):
        """
        Deletes a file system.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if self.url.endswith(f"/file_system/{self.data.invalid_fs_id}"):
            return 404, self.data.fs_error[404]
        if self.url.endswith(f"/file_system/{self.data.fs_id_with_snap}"):
            return 422, self.data.fs_error[422]
        return 204, None
