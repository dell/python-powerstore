"""Unit tests for Service User"""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestServiceUser(TestBase):
    """
    Unit tests for Service User
    """

    def test_get_service_users(self):
        """
        Test Get Service Users

        Validates that the service user list matches the expected list
        """
        service_user_list = self.configuration.get_service_users()
        self.assertListEqual(service_user_list, self.data.service_user_list)

    def test_get_service_user_details(self):
        """
        Test Get Service User Details

        Validates that the service user details match the expected details
        """
        service_user_details = self.configuration.get_service_user_details(
            self.data.service_user_id_1,
        )
        self.assertEqual(service_user_details, self.data.service_user_details_1)

    def test_get_invalid_service_user_details(self):
        """
        Test Get Invalid Service User Details

        Verifies that getting details of an invalid service user raises an exception
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_service_user_details,
            self.data.invalid_service_user_id,
        )

    def test_modify_service_user(self):
        """
        Test Modify Service User

        Validates that modifying a service user returns the expected details
        """
        service_user_details_1 = self.configuration.modify_service_user(
            self.data.service_user_id_1, password="Password123!",
        )
        self.assertEqual(service_user_details_1, self.data.service_user_details_1)

    def test_get_service_user_by_name(self):
        """
        Test Get Service User By Name

        Validates that getting a service user by name returns the expected list
        """
        service_user_list = self.configuration.get_service_user_by_name(
            self.data.service_user_name_1,
        )
        self.assertListEqual(service_user_list, self.data.service_user_list)
