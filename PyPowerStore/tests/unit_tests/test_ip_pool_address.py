from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestIPPoolAddress(TestBase):

    def test_ip_pool_address(self):
        filters = {'network_id': 'eq.' + 'NW6'}
        ip_pool_list = self.configuration.get_ip_pool_address(filter_dict=filters)
        self.assertListEqual(ip_pool_list, self.data.ip_pool_list)