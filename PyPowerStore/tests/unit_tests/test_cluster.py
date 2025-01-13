from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestCluster(TestBase):

    def test_get_clusters(self):
        cluster_list = self.configuration.get_clusters()
        self.assertListEqual(cluster_list, self.data.cluster_list)

    def test_get_cluster_details(self):
        cluster_details = self.configuration.get_cluster_details(
            self.data.cluster_id_1)
        self.assertEqual(cluster_details, self.data.cluster_details_1)

    def test_get_invalid_cluster_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_cluster_details,
            self.data.invalid_cluster_id)

    def test_modify_cluster(self):
        cluster_details_1 = self.configuration.modify_cluster(
            self.data.cluster_id_1, physical_mtu=2000)
        self.assertEqual(cluster_details_1, self.data.cluster_details_1)

    def test_get_cluster_by_name(self):
        cluster_list = self.configuration.get_cluster_by_name(
            self.data.cluster_name_1)
        self.assertListEqual(cluster_list, self.data.cluster_list)

    def test_validate_cluster_create(self):
        resp = self.configuration. cluster_create_validate(
            cluster=self.data.cluster,
            appliances=self.data.appliances,
            dns_servers=self.data.dns_servers,
            ntp_servers=self.data.ntp_servers,
            networks=self.data.networks,
            is_http_redirect_enabled=self.data.is_http_redirect_enabled)
        self.assertIsNone(resp)

    def test_cluster_create(self):
        resp = self.configuration. cluster_create(
            cluster=self.data.cluster,
            appliances=self.data.appliances,
            dns_servers=self.data.dns_servers,
            ntp_servers=self.data.ntp_servers,
            networks=self.data.networks,
            is_http_redirect_enabled=self.data.is_http_redirect_enabled)
        self.assertEqual(resp, self.data.cluster_id_1)
