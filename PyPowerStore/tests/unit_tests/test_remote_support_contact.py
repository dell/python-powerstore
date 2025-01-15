from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestRemoteSupportContact(TestBase):

    def test_get_remote_support_contact_configs(self):
        remote_support_contact_list = (
            self.configuration.get_remote_support_contact_list()
        )
        self.assertListEqual(
            remote_support_contact_list,
            self.remote_support_contact_data.remote_support_contact_list,
        )

    def test_get_remote_support_contact_details(self):
        resp = self.configuration.get_remote_support_contact_details(
            self.remote_support_contact_data.remote_support_contact_id
        )
        self.assertEqual(
            resp, self.remote_support_contact_data.remote_support_contact_details
        )

    def test_modify_remote_support_contact_details(self):
        resp = self.configuration.modify_remote_support_contact_details(
            self.remote_support_contact_data.remote_support_contact_id,
            self.remote_support_contact_data.modify_remote_support_contact_dict,
        )
        self.assertIsNone(resp)

    def test_modify_remote_support_contact_details_with_invalid_param(self):
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_remote_support_contact_details,
            self.remote_support_contact_data.remote_support_contact_id,
            invalid_param,
        )
