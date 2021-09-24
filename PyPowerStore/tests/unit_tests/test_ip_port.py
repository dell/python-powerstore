from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestIPPort(TestBase):

    def test_ip_port_details(self):
        ip_port_details = self.configuration.get_ip_port_details(self.data.ip_port_id)
        self.assertEqual(ip_port_details, self.data.ip_port_details)