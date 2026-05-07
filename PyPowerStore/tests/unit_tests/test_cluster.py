"""Unit tests for Cluster."""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestCluster(TestBase):
    """
    Unit tests for Cluster.
    """

    def test_get_clusters(self):
        """
        Test get clusters.

        Validates that the retrieved cluster list matches the expected list.
        """
        cluster_list = self.configuration.get_clusters()
        self.assertListEqual(cluster_list, self.data.cluster_list)

    def test_get_cluster_details(self):
        """
        Test get cluster details.

        Confirms that the retrieved cluster details match the expected details.
        """
        cluster_details = self.configuration.get_cluster_details(self.data.cluster_id_1)
        self.assertEqual(cluster_details, self.data.cluster_details_1)

    def test_get_invalid_cluster_details(self):
        """
        Test get invalid cluster details.

        Verifies that an exception is raised when retrieving details for an invalid cluster ID.
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_cluster_details,
            self.data.invalid_cluster_id,
        )

    def test_modify_cluster(self):
        """
        Test modify cluster.

        Validates that the modified cluster details match the expected details.
        """
        cluster_details_1 = self.configuration.modify_cluster(
            self.data.cluster_id_1, physical_mtu=2000,
        )
        self.assertEqual(cluster_details_1, self.data.cluster_details_1)

    def test_get_cluster_by_name(self):
        """
        Test get cluster by name.

        Confirms that the retrieved cluster list matches the expected list when filtered by name.
        """
        cluster_list = self.configuration.get_cluster_by_name(self.data.cluster_name_1)
        self.assertListEqual(cluster_list, self.data.cluster_list)

    def test_validate_cluster_create(self):
        """
        Test validate cluster create.

        Verifies that the cluster creation validation returns the expected response.
        """
        resp = self.configuration.cluster_create_validate(
            cluster=self.data.cluster,
            appliances=self.data.appliances,
            dns_servers=self.data.dns_servers,
            ntp_servers=self.data.ntp_servers,
            networks=self.data.networks,
            is_http_redirect_enabled=self.data.is_http_redirect_enabled,
        )
        self.assertIsNone(resp)

    def test_cluster_create(self):
        """
        Test cluster create.

        Validates that the created cluster ID matches the expected ID.
        """
        resp = self.configuration.cluster_create(
            cluster=self.data.cluster,
            appliances=self.data.appliances,
            dns_servers=self.data.dns_servers,
            ntp_servers=self.data.ntp_servers,
            networks=self.data.networks,
            is_http_redirect_enabled=self.data.is_http_redirect_enabled,
        )
        self.assertEqual(resp, self.data.cluster_id_1)
