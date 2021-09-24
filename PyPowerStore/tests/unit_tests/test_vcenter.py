from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestVcenter(TestBase):

    def test_modify_vcenter(self):
        vcenter_details = self.configuration.modify_vcenter(
            self.data.vcenter_id1, self.data.vasa_provider_credentials)
        self.assertEqual(vcenter_details, self.data.vcenter_details)
        
    def test_get_vcenters(self):
        vcenter_list = self.configuration.get_vcenters()
        self.assertListEqual(vcenter_list, self.data.vcenter_list)

    def test_get_vcenter_details(self):
        vcenter_details = self.configuration.get_vcenter_details(self.data.vcenter_id1)
        self.assertEqual(vcenter_details, self.data.vcenter_details)
