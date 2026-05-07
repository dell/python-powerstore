"""Mock cluster Api for Cluster Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class ClusterResponse(Entity):
    """
    This class is used to handle Cluster related responses.

    It provides methods to get clusters, cluster details, create clusters, 
    validate create cluster, modify clusters.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the ClusterResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/cluster"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_cluster_by_name
                return self.get_clusters
            return self.get_cluster_details
        if self.method == "PATCH":
            return self.modify_cluster
        if self.method == "POST":
            if self.url.endswith("/validate_create"):
                return self.cluster_create_validate
            return self.cluster_create
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

    def get_clusters(self):
        """
        Returns a list of clusters.

        Returns:
            tuple: A tuple containing the status code and the list of clusters.
        """
        return self.status_code, self.data.cluster_list

    def get_cluster_details(self):
        """
        Returns the details of a cluster.

        Returns:
            tuple: A tuple containing the status code and the cluster details.
        """
        if self.url.endswith(f"/cluster/{self.data.invalid_cluster_id}"):
            return 404, self.data.cluster_error[404]
        return self.status_code, self.data.cluster_details_1

    def get_cluster_by_name(self):
        """
        Returns the details of a cluster by name.

        Returns:
            tuple: A tuple containing the status code and the cluster details.
        """
        return self.status_code, [self.data.cluster_details_1]

    def modify_cluster(self):
        """
        Modifies a cluster.

        Returns:
            tuple: A tuple containing the status code and the cluster details.
        """
        return 204, self.data.cluster_details_1

    def cluster_create(self):
        """
        Creates a new cluster.

        Returns:
            tuple: A tuple containing the status code and the cluster id.
        """
        return 201, self.data.cluster_id_1

    def cluster_create_validate(self):
        """
        Validates the create cluster operation.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
