from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestServiceConfig(TestBase):

    def test_get_service_configs(self):
        service_config_list = self.configuration.get_service_configs()
        self.assertListEqual(service_config_list, self.data.service_config_list)

    def test_get_service_config_details(self):
        service_config_details = self.configuration.get_service_config_details(
            self.data.service_config_id_1)
        self.assertEqual(service_config_details,
                         self.data.service_config_details_1)

    def test_get_invalid_service_config_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_service_config_details,
            self.data.invalid_service_config_id)

    def test_modify_service_config(self):
        service_config_details_1 = self.configuration.modify_service_config(
            self.data.service_config_id_1, is_ssh_enabled=True)
        self.assertEqual(service_config_details_1,
                         self.data.service_config_details_1)
