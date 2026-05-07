"""Unit tests for Local User"""

# pylint: disable=assignment-from-none,duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestLocalUser(TestBase):
    """
    Unit tests for Local User
    """

    def test_create_local_user(self):
        """
        Test Create Local User

        Validates that the created local user matches the expected response
        """
        resp = self.configuration.create_local_user(self.data.local_user_create_params)
        self.assertEqual(resp, self.data.local_user_create_response)

    def test_get_local_user_by_name(self):
        """
        Test Get Local User By Name

        Validates that the retrieved local user details match the expected details
        """
        local_user_details = self.configuration.get_local_user_by_name(
            self.data.local_user_name1,
        )
        self.assertEqual(local_user_details, self.data.local_user_details)

    def test_get_local_users(self):
        """
        Test Get Local Users

        Validates that the retrieved local user list matches the expected list
        """
        local_user_list = self.configuration.get_local_users()
        self.assertListEqual(local_user_list, self.data.local_user_list)

    def test_get_local_user_details(self):
        """
        Test Get Local User Details

        Validates that the retrieved local user details match the expected details
        """
        local_user_details = self.configuration.get_local_user_details(
            self.data.local_user_id1,
        )
        self.assertEqual(local_user_details, self.data.local_user_details)

    def test_get_invalid_local_user_details(self):
        """
        Test Get Invalid Local User Details

        Validates that trying to retrieve details for a non-existent
        local user raises the expected error
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_local_user_details,
            self.data.local_user_does_not_exist,
        )

    def test_modify_local_user(self):
        """
        Test Modify Local User

        Validates that modifying the local user with valid parameters does not raise any errors
        """
        resp = self.configuration.modify_local_user(
            self.data.local_user_id1, {"role_id": "4"},
        )
        self.assertIsNone(resp)

    def test_modify_local_user_with_invalid_param(self):
        """
        Test Modify Local User With Invalid Param

        Validates that modifying the local user with invalid parameters raises the expected error
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_local_user,
            self.data.local_user_id1,
            invalid_param,
        )

    def test_delete_local_user(self):
        """
        Test Delete Local User

        Validates that the response is None
        """
        resp = self.configuration.delete_local_user(self.data.local_user_id1)
        self.assertIsNone(resp)
