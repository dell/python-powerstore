from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
from unittest import mock


class TestNtp(TestBase):

    def test_get_ntp_list(self):
        ntp_list = self.configuration.get_ntp_list()
        self.assertListEqual(ntp_list, self.ntp_data.ntp_list)

    def test_get_ntp_details(self):
        resp = self.configuration.get_ntp_details(
            self.ntp_data.ntp_id)
        self.assertEqual(resp, self.ntp_data.ntp_details)

    def test_modify_ntp_details(self):
        resp = self.configuration.modify_ntp_details(
            self.ntp_data.ntp_id, self.ntp_data.modify_ntp_dict)
        self.assertIsNone(resp)

    def test_modify_ntp_details_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_ntp_details,
            self.ntp_data.ntp_id, invalid_param)
