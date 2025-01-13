from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestSecurityConfig(TestBase):

    def test_get_security_configs(self):
        security_config_list = self.configuration.get_security_configs()
        self.assertListEqual(security_config_list,
                             self.security_config_data.security_config_list)

    def test_get_security_config_details(self):
        security_config_details = self.configuration. \
            get_security_config_details(
                self.security_config_data.security_config_id_1)
        self.assertEqual(security_config_details,
                         self.security_config_data.security_config_details_1)

    def test_get_invalid_security_config_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_security_config_details,
            self.security_config_data.invalid_security_config_id)

    def test_modify_security_config(self):
        resp = self.configuration.modify_security_config(
            self.security_config_data.security_config_id_1, {
                "protocol_mode": "TLSv1_2"})
        self.assertIsNone(resp)

    def test_modify_security_config_with_invalid_param(self):
        self.assertRaises(PowerStoreException,
                          self.configuration.modify_security_config,
                          self.security_config_data.security_config_id_1,
                          self.security_config_data.invalid_protocol_mode)
