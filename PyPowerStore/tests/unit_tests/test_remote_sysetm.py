from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestRemoteSystem(TestBase):

    def test_get_remote_systems(self):
        remote_system_list = self.protection.get_remote_systems()
        self.assertListEqual(remote_system_list,
                             self.remote_system_data.remote_system_list)

    def test_get_remote_system(self):
        remote_system_details_1 = self.protection.get_remote_system_details(
            self.remote_system_data.remote_system_id_1)
        self.assertEqual(remote_system_details_1,
                         self.remote_system_data.remote_system_details_1)

    def test_get_remote_system_by_name(self):
        remote_system_details_1 = self.protection.get_remote_system_by_name(
            self.remote_system_data.remote_system_name_1, self.remote_system_data.mgmt_ip_1)
        self.assertEqual(remote_system_details_1, [
                         self.remote_system_data.remote_system_details_1])

    def test_get_remote_system_by_mgmt_address(self):
        remote_system_details_1 = self.protection.get_remote_system_by_mgmt_address(
            self.remote_system_data.mgmt_ip_1)
        self.assertEqual(remote_system_details_1, [
                         self.remote_system_data.remote_system_details_1])

    def test_create_remote_system(self):
        remote_system_details_1 = self.protection.create_remote_system(
            self.remote_system_data.create_remote_sys_dict)
        self.assertEqual(remote_system_details_1,
                         self.remote_system_data.remote_system_details_1)

    def test_modify_remote_system(self):
        modify_remote_system_resp = self.protection.modify_remote_system(
            self.remote_system_data.remote_system_id_1,
            self.remote_system_data.modify_remote_system_dict,
            is_async=False)
        self.assertIsNone(modify_remote_system_resp)

    def test_delete_remote_system(self):
        remote_system = self.protection.delete_remote_system(
            self.remote_system_data.remote_system_id_1)
        self.assertIsNone(remote_system)

    def test_get_remote_appliance_details(self):
        remote_app_details_1 = self.protection.get_remote_system_appliance_details(
            self.remote_system_data.remote_system_id_1)
        self.assertEqual(remote_app_details_1,
                         self.remote_system_data.remote_app_details)
