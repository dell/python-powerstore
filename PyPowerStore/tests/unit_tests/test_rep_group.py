from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestStorageContainerDestination(TestBase):
    def test_get_replication_groups(self):
        replication_group_list = self.\
            protection.get_replication_groups()
        self.assertListEqual(
            replication_group_list,
            self.replication_group_data.replication_group_list)

    def test_get_replication_group_details(self):
        resp = self.protection.get_replication_group_details(
            self.replication_group_data.replication_group_id)
        self.assertEqual(resp, self.replication_group_data.replication_group_details)

    def test_get_replication_group_details_by_name(self):
        resp = self.protection.get_replication_group_details_by_name(
            self.replication_group_data.replication_group_name)
        self.assertEqual(resp[0],
                         self.replication_group_data.replication_group_details)
