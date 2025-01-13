from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.storage_container_destination_data import StorageContainerDestinationData


class StorageContainerDestinationResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.storage_container_destination_data = StorageContainerDestinationData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/storage_container_destination'):
                return self.get_storage_container_destination_list
            return self.get_storage_container_destination_details
        if self.method == 'POST':
            return self.create_storage_container_destination
        if self.method == "DELETE":
            return self.delete_storage_container_destination

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_storage_container_destination_list(self):
        return self.status_code, self.storage_container_destination_data.\
            storage_container_destination_list

    def get_storage_container_destination_details(self):
        return self.status_code, self.storage_container_destination_data.\
            storage_container_destination_details

    def create_storage_container_destination(self):
        return 201, self.storage_container_destination_data.\
            storage_container_destination_id

    def delete_storage_container_destination(self):
        return 204, None
