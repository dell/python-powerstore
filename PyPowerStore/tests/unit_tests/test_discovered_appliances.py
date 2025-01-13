from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestDiscoveredAppliances(TestBase):
    def test_get_discovered_appliances(self):
        discovered_appliance_list = self.configuration.get_discovered_appliances()
        self.assertListEqual(discovered_appliance_list,
                             self.discovered_appliance_data.discovered_appliance_list)

    def test_get_discovered_appliances_all_pages(self):
        all_pages = True
        def callable_func(): return self.configuration.get_discovered_appliances(None, all_pages)
        # Check if the correct exception is raised
        self.assertRaises(ValueError, callable_func)
