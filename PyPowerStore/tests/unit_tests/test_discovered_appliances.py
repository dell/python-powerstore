"""Unit tests for Discovered Appliances."""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestDiscoveredAppliances(TestBase):
    """
    Unit tests for Discovered Appliances.
    """

    def test_get_discovered_appliances(self):
        """
        Test get discovered appliances.

        Validates that the discovered appliance list returned from the configuration 
        matches the expected discovered appliance list.
        """
        discovered_appliance_list = self.configuration.get_discovered_appliances()
        self.assertListEqual(
            discovered_appliance_list,
            self.discovered_appliance_data.discovered_appliance_list,
        )

    def test_get_discovered_appliances_all_pages(self):
        """
        Test get discovered appliances all pages.

        Verifies that the correct exception is raised when all_pages is set to True.
        """
        all_pages = True

        def callable_func():
            return self.configuration.get_discovered_appliances(None, all_pages)

        self.assertRaises(ValueError, callable_func)
