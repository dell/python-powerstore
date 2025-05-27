"""Unit tests for Storage Container"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestStorageContainer(TestBase):
    """
    Unit tests for Storage Container
    """

    def test_get_storage_containers(self):
        """
        Test Get Storage Containers

        Validates that the storage container list matches the expected list
        """
        storage_container_list = self.configuration.get_storage_container_list()
        self.assertListEqual(
            storage_container_list, self.storage_container_data.storage_container_list,
        )

    def test_get_storage_container_details(self):
        """
        Test Get Storage Container Details

        Validates that the storage container details equal to the expected details
        """
        resp = self.configuration.get_storage_container_details(
            self.storage_container_data.storage_container_list[0]["id"],
        )
        self.assertEqual(resp, self.storage_container_data.storage_container_details)

    def test_get_storage_container_details_by_name(self):
        """
        Test Get Storage Container Details By Name

        Validates that the storage container details equal to the expected details
        """
        resp = self.configuration.get_storage_container_details_by_name(
            self.storage_container_data.storage_container_details["name"],
        )
        self.assertEqual(resp, self.storage_container_data.storage_container_details)

    def test_create_storage_container(self):
        """
        Test Create Storage Container

        Validates that the created storage container equals to the expected response
        """
        resp = self.configuration.create_storage_container(
            self.storage_container_data.create_storage_container_dict,
        )
        self.assertEqual(
            resp, self.storage_container_data.create_storage_container_response,
        )

    def test_modify_storage_container_details(self):
        """
        Test Modify Storage Container Details

        Validates that the response is None
        """
        resp = self.configuration.modify_storage_container_details(
            self.storage_container_data.storage_container_list[0]["id"],
            self.storage_container_data.modify_storage_container_dict,
        )
        self.assertIsNone(resp)

    def test_delete_storage_container(self):
        """
        Test Delete Storage Container

        Validates that the response is None
        """
        resp = self.configuration.delete_storage_container(
            self.storage_container_data.storage_container_list[0]["id"], False,
        )
        self.assertIsNone(resp)
