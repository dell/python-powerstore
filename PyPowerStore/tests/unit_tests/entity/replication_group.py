from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.replication_group_data import ReplicationGroupData


class ReplicationGroupResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.replication_group_data = ReplicationGroupData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/replication_group'):
                return self.get_replication_group_list
            return self.get_replication_group_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_replication_group_list(self):
        return self.status_code, self.replication_group_data.\
            replication_group_list

    def get_replication_group_details(self):
        return self.status_code, self.replication_group_data.\
            replication_group_details
