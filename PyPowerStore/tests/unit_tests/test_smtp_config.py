from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestSmtp_Config(TestBase):

    def test_get_smtp_configs(self):
        smtp_list = self.configuration.get_smtp_configs()
        print(smtp_list)
        self.assertListEqual(smtp_list, self.smtp_config_data.smtp_list)

    def test_get_smtp_config_details(self):
        resp = self.configuration.get_smtp_config_details(
            self.smtp_config_data.smtp_id)
        self.assertEqual(resp, self.smtp_config_data.smtp_details)

    def test_modify_smtp_config_details(self):
        resp = self.configuration.modify_smtp_config_details(
            self.smtp_config_data.smtp_id, self.smtp_config_data.modify_smtp_dict)
        self.assertIsNone(resp)

    def test_modify_smtp_config_details_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_smtp_config_details,
            self.smtp_config_data.smtp_id, invalid_param)

    def test_send_test_mail_smtp_config(self):
        resp = self.configuration.test_smtp_config(
            self.smtp_config_data.smtp_id, self.smtp_config_data.test_smtp_dict)
        self.assertIsNone(resp)
