"""Unit tests for Role"""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestRole(TestBase):
    """
    Unit tests for Role
    """

    def test_get_roles(self):
        """
        Test get roles

        Validates that the list of roles matches the expected role list
        """
        role_list = self.configuration.get_roles()
        self.assertListEqual(role_list, self.data.role_list)

    def test_get_role_details(self):
        """
        Test get role details

        Validates that the role details match the expected role details
        """
        role_details = self.configuration.get_role_details(self.data.role_id1)
        self.assertEqual(role_details, self.data.role_details_1)

    def test_get_invalid_role_details(self):
        """
        Test get invalid role details

        Verifies that an exception is raised when getting details of a non-existent role
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_role_details,
            self.data.role_does_not_exist,
        )

    def test_get_role_by_name(self):
        """
        Test get role by name

        Validates that the role details match the expected role details when retrieved by name
        """
        role_details_1 = self.configuration.get_role_by_name(self.data.role_name1)
        self.assertListEqual([role_details_1], [self.data.role_details_1])
