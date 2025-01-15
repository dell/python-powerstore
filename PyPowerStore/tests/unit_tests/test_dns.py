from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestDns(TestBase):

    def test_get_dns_list(self):
        dns_list = self.configuration.get_dns_list()
        self.assertListEqual(dns_list, self.dns_data.dns_list)

    def test_get_dns_details(self):
        resp = self.configuration.get_dns_details(self.dns_data.dns_id)
        self.assertEqual(resp, self.dns_data.dns_details)

    def test_modify_dns_details(self):
        resp = self.configuration.modify_dns_details(
            self.dns_data.dns_id, self.dns_data.modify_dns_dict,
        )
        self.assertIsNone(resp)

    def test_modify_dns_details_with_invalid_param(self):
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_dns_details,
            self.dns_data.dns_id,
            invalid_param,
        )
