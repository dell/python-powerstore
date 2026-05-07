"""Unit Tests for IP Port"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestIPPort(TestBase):
    """
    Unit tests for IP Port
    """

    def test_ip_port_details(self):
        """
        Test getting IP Port details
        
        Validates that the returned IP Port details match the expected details
        """

        ip_port_details = self.configuration.get_ip_port_details(self.data.ip_port_id)
        self.assertEqual(ip_port_details, self.data.ip_port_details)
