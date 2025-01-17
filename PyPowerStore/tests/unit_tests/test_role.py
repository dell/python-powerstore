from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestRole(TestBase):

    def test_get_roles(self):
        role_list = self.configuration.get_roles()
        self.assertListEqual(role_list, self.data.role_list)

    def test_get_role_details(self):
        role_details = self.configuration.get_role_details(self.data.role_id1)
        self.assertEqual(role_details, self.data.role_details_1)

    def test_get_invalid_role_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_role_details,
            self.data.role_does_not_exist,
        )

    def test_get_role_by_name(self):
        role_details_1 = self.configuration.get_role_by_name(self.data.role_name1)
        self.assertListEqual([role_details_1], [self.data.role_details_1])
