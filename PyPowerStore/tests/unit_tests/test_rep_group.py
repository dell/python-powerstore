"""Unit tests for Replication Group"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestStorageContainerDestination(TestBase):
    """
    Unit tests for Storage Container Destination
    """

    def test_get_replication_groups(self):
        """
        Test get replication groups
        
        Validates that the list of replication groups matches the expected list
        """
        replication_group_list = self.protection.get_replication_groups()
        self.assertListEqual(
            replication_group_list, self.replication_group_data.replication_group_list,
        )

    def test_get_replication_group_details(self):
        """
        Test get replication group details
        
        Validates that the replication group details match the expected details
        """
        resp = self.protection.get_replication_group_details(
            self.replication_group_data.replication_group_id,
        )
        self.assertEqual(resp, self.replication_group_data.replication_group_details)

    def test_get_replication_group_details_by_name(self):
        """
        Test get replication group details by name
        
        Validates that the replication group details match the expected details
        """
        resp = self.protection.get_replication_group_details_by_name(
            self.replication_group_data.replication_group_name,
        )
        self.assertEqual(resp[0], self.replication_group_data.replication_group_details)
