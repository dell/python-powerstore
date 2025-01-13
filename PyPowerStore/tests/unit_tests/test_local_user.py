from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestLocalUser(TestBase):

    def test_create_local_user(self):
        resp = self.configuration.create_local_user(
            self.data.local_user_create_params)
        self.assertEqual(resp, self.data.local_user_create_response)

    def test_get_local_user_by_name(self):
        local_user_details = self.configuration.get_local_user_by_name(
            self.data.local_user_name1)
        self.assertEqual(local_user_details, self.data.local_user_details)

    def test_get_local_users(self):
        local_user_list = self.configuration.get_local_users()
        self.assertListEqual(local_user_list, self.data.local_user_list)

    def test_get_local_user_details(self):
        local_user_details = self.configuration.get_local_user_details(
            self.data.local_user_id1)
        self.assertEqual(local_user_details, self.data.local_user_details)

    def test_get_invalid_local_user_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_local_user_details,
            self.data.local_user_does_not_exist)

    def test_modify_local_user(self):
        resp = self.configuration.modify_local_user(
            self.data.local_user_id1, {"role_id": "4"})
        self.assertIsNone(resp)

    def test_modify_local_user_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_local_user,
            self.data.local_user_id1, invalid_param)

    def test_delete_local_user(self):
        resp = self.configuration.delete_local_user(self.data.local_user_id1)
        self.assertIsNone(resp)
