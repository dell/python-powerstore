from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestNetwork(TestBase):

    def test_get_network_by_name(self):
        network_list = self.configuration.get_network_by_name(
            self.data.network_name1)
        self.assertListEqual(network_list, [self.data.network_details_1])

    def test_get_networks(self):
        network_list = self.configuration.get_networks()
        self.assertListEqual(network_list, self.data.network_list)

    def test_get_network_details(self):
        network_details = self.configuration.get_network_details(
            self.data.network_id1)
        self.assertEqual(network_details, self.data.network_details_1)

    def test_get_invalid_network_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_network_details,
            self.data.network_does_not_exist)

    def test_modify_network(self):
        resp = self.configuration.modify_network(
            self.data.network_id1, {"mtu": 2000})
        self.assertIsNone(resp)

    def test_add_remove_ports(self):
        network_details = self.configuration.add_remove_ports(
            self.data.network_id1, add_port_ids=self.data.add_ip_ports)
        self.assertEqual(network_details, self.data.network_details_1)

    def test_modify_network_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_network,
            self.data.network_id1, invalid_param)
