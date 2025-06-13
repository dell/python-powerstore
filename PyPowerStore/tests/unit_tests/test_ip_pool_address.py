"""Unit tests for IP Pool Address"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestIPPoolAddress(TestBase):
    """
    Unit tests for IP Pool Address
    """

    def test_ip_pool_address(self):
        """
        Test IP Pool Address

        Validates that the IP pool address list retrieved from the
        configuration matches the expected IP pool address list.
        """

        filters = {"network_id": "eq." + "NW6"}
        ip_pool_list = self.configuration.get_ip_pool_address(filter_dict=filters)
        self.assertListEqual(ip_pool_list, self.data.ip_pool_list)
