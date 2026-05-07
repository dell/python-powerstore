"""Unit tests for Appliance."""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestAppliance(TestBase):
    """
    Unit tests for Appliance.
    """

    def test_get_appliances(self):
        """
        Test get appliances.
        
        Validates that the appliance list returned from the configuration 
        matches the expected appliance list.
        """
        appliance_list = self.configuration.get_appliances()
        self.assertListEqual(appliance_list, self.data.appliance_list)

    def test_get_appliance_details(self):
        """
        Test get appliance details.
        
        Verifies that the appliance details returned from the configuration 
        match the expected appliance details for a valid appliance ID.
        """
        appliance_details = self.configuration.get_appliance_details(
            self.data.appliance_id1,
        )
        self.assertEqual(appliance_details, self.data.appliance_details_1)

    def test_get_invalid_appliance_details(self):
        """
        Test get appliance details for an invalid appliance.
        
        Validates that a PowerStoreException is raised when attempting to 
        retrieve appliance details for a non-existent appliance ID.
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_appliance_details,
            self.data.appliance_does_not_exist,
        )

    def test_get_appliance_by_name(self):
        """
        Test get appliance by name.
        
        Confirms that the appliance details returned from the configuration 
        match the expected appliance details when retrieving by appliance name.
        """
        appliance_details_1 = self.configuration.get_appliance_by_name(
            self.data.appliance_name1,
        )
        self.assertListEqual(appliance_details_1, [self.data.appliance_details_1])
