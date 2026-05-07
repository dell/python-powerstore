"""Unit tests for Network"""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestNetwork(TestBase):
    """
    Unit tests for Network
    """

    def test_get_network_by_name(self):
        """
        Test get network by name

        Validates that the network list retrieved by name matches the expected network details
        """
        network_list = self.configuration.get_network_by_name(self.data.network_name1)
        self.assertListEqual(network_list, [self.data.network_details_1])

    def test_get_networks(self):
        """
        Test get networks

        Validates that the retrieved network list matches the expected network list
        """
        network_list = self.configuration.get_networks()
        self.assertListEqual(network_list, self.data.network_list)

    def test_get_network_details(self):
        """
        Test get network details

        Validates that the retrieved network details match the expected network details
        """
        network_details = self.configuration.get_network_details(self.data.network_id1)
        self.assertEqual(network_details, self.data.network_details_1)

    def test_get_invalid_network_details(self):
        """
        Test get invalid network details

        Confirms that an exception is raised when retrieving details of a non-existent network
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_network_details,
            self.data.network_does_not_exist,
        )

    def test_modify_network(self):
        """
        Test modify network

        Validates that the response is None
        """
        resp = self.configuration.modify_network(self.data.network_id1, {"mtu": 2000})
        self.assertIsNone(resp)

    def test_add_remove_ports(self):
        """
        Test add remove ports

        Validates that ports can be added and removed from a network successfully
        """
        network_details = self.configuration.add_remove_ports(
            self.data.network_id1, add_port_ids=self.data.add_ip_ports,
        )
        self.assertEqual(network_details, self.data.network_details_1)

    def test_modify_network_with_invalid_param(self):
        """
        Test modify network with invalid param

        Confirms that an exception is raised when modifying a network with an invalid parameter
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_network,
            self.data.network_id1,
            invalid_param,
        )
