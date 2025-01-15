from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestVcenter(TestBase):

    def test_modify_vcenter(self):
        vcenter_details = self.configuration.modify_vcenter(
            self.vcenter_data.vcenter_id, self.vcenter_data.vasa_provider_credentials,
        )
        self.assertEqual(vcenter_details, self.vcenter_data.vcenter_details)

    def test_get_vcenters(self):
        vcenter_list = self.configuration.get_vcenters()
        self.assertListEqual(vcenter_list, self.vcenter_data.vcenter_list)

    def test_get_vcenter_details(self):
        vcenter_details = self.configuration.get_vcenter_details(
            self.vcenter_data.vcenter_id,
        )
        self.assertEqual(vcenter_details, self.vcenter_data.vcenter_details)

    def test_add_vcenter(self):
        vcenter_id = self.configuration.add_vcenter(
            self.vcenter_data.add_vcenter_params,
        )
        self.assertEqual(vcenter_id, self.vcenter_data.vcenter_id)

    def test_remove_vcenter(self):
        resp = self.configuration.remove_vcenter(
            self.vcenter_data.vcenter_id, self.vcenter_data.delete_vasa_provider,
        )
        self.assertIsNone(resp)
