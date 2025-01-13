from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException

class TestRemoteSupport(TestBase):

    def test_get_remote_support_configs(self):
        remote_support_list = self.configuration.get_remote_support_list()
        print(remote_support_list)
        self.assertListEqual(remote_support_list, self.remote_support_data.remote_support_list)

    def test_get_remote_support_details(self):
        resp = self.configuration.get_remote_support_details(
            self.remote_support_data.remote_support_id)
        self.assertEqual(resp, self.remote_support_data.remote_support_details)

    def test_modify_remote_support_details(self):
        resp = self.configuration.modify_remote_support_details(
            self.remote_support_data.remote_support_id, self.remote_support_data.modify_remote_support_dict)
        self.assertIsNone(resp)

    def test_modify_remote_support_details_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_remote_support_details,
            self.remote_support_data.remote_support_id, invalid_param)

    def test_verify_remote_support_config(self):
        resp = self.configuration.verify_remote_support_config(
            self.remote_support_data.remote_support_id, self.remote_support_data.verify_remote_support_dict)
        self.assertIsNone(resp)

    def test_send_test_alert_remote_support(self):
        resp = self.configuration.test_remote_support_config(self.remote_support_data.remote_support_id)
        self.assertIsNone(resp)
