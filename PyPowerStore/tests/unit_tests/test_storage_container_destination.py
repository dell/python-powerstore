"""Unit tests for Storage Container Destination"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestStorageContainerDestination(TestBase):
    """
    Unit tests for Storage Container Destination
    """

    def test_get_storage_container_destinations(self):
        """
        Test get storage container destinations.

        Validates that the retrieved storage container destination list matches the expected list.
        """
        storage_container_destination_list = (
            self.configuration.get_storage_container_destination_list()
        )
        self.assertListEqual(
            storage_container_destination_list,
            self.storage_container_destination_data.storage_container_destination_list,
        )

    def test_get_storage_container_destination_details(self):
        """
        Test get storage container destination details.

        Verifies that the retrieved storage container destination details
        match the expected details.
        """
        resp = self.configuration.get_storage_container_destination_details(
            self.storage_container_destination_data.storage_container_destination_details[
                "id"
            ],
        )
        self.assertEqual(
            resp,
            self.storage_container_destination_data.storage_container_destination_details,
        )

    def test_create_storage_container_destination(self):
        """
        Test create storage container destination.

        Confirms that the created storage container destination ID equals to the expected ID.
        """
        resp = self.configuration.create_storage_container_destination(
            self.storage_container_destination_data.create_storage_container_destination_dict,
        )
        self.assertEqual(
            resp,
            self.storage_container_destination_data.storage_container_destination_id,
        )

    def test_delete_storage_container_destination(self):
        """
        Test delete storage container destination.

        Validates that the response is None.
        """
        resp = self.configuration.delete_storage_container_destination(
            self.storage_container_destination_data.storage_container_destination_id,
        )
        self.assertIsNone(resp)
