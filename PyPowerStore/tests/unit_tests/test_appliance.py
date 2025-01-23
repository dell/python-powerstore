from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestAppliance(TestBase):

    def test_get_appliances(self):
        appliance_list = self.configuration.get_appliances()
        self.assertListEqual(appliance_list, self.data.appliance_list)

    def test_get_appliance_details(self):
        appliance_details = self.configuration.get_appliance_details(
            self.data.appliance_id1,
        )
        self.assertEqual(appliance_details, self.data.appliance_details_1)

    def test_get_invalid_appliance_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_appliance_details,
            self.data.appliance_does_not_exist,
        )

    def test_get_appliance_by_name(self):
        appliance_details_1 = self.configuration.get_appliance_by_name(
            self.data.appliance_name1,
        )
        self.assertListEqual(appliance_details_1, [self.data.appliance_details_1])
