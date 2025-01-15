from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.storage_container_data import (
    StorageContainerData,
)


class StorageContainerResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.storage_container_data = StorageContainerData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/storage_container"):
                return self.get_storage_container_list
            return self.get_storage_container_details
        if self.method == "POST":
            return self.create_storage_container
        if self.method == "PATCH":
            return self.modify_storage_container_details
        if self.method == "DELETE":
            return self.delete_storage_container

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_storage_container_list(self):
        return self.status_code, self.storage_container_data.storage_container_list

    def get_storage_container_details(self):
        return self.status_code, self.storage_container_data.storage_container_details

    def create_storage_container(self):
        return (
            self.status_code,
            self.storage_container_data.create_storage_container_response,
        )

    def modify_storage_container_details(self):
        return 204, None

    def delete_storage_container(self):
        return 204, None
