from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class ClusterResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200
    
    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/cluster'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_cluster_by_name
                return self.get_clusters
            return self.get_cluster_details
        if self.method == 'PATCH':
            return self.modify_cluster
        if self.method == 'POST':
            if self.url.endswith('/validate_create'):
                return self.cluster_create_validate
            return self.cluster_create

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_clusters(self):
        return self.status_code, self.data.cluster_list

    def get_cluster_details(self):
        if self.url.endswith('/cluster/{0}'.format(
           self.data.invalid_cluster_id)):
            return 404, self.data.cluster_error[404]
        return self.status_code, self.data.cluster_details_1

    def get_cluster_by_name(self):
        return self.status_code, [self.data.cluster_details_1]

    def modify_cluster(self):
        return 204, self.data.cluster_details_1

    def cluster_create(self):
        return 201, self.data.cluster_id_1

    def cluster_create_validate(self):
        return 204, None

