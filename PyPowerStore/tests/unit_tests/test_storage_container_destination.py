from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestStorageContainerDestination(TestBase):
    def test_get_storage_container_destinations(self):
        storage_container_destination_list = self.\
            configuration.get_storage_container_destination_list()
        self.assertListEqual(
            storage_container_destination_list,
            self.storage_container_destination_data.storage_container_destination_list)

    def test_get_storage_container_destination_details(self):
        resp = self.configuration.get_storage_container_destination_details(
            self.storage_container_destination_data.storage_container_destination_details['id'])
        self.assertEqual(resp, self.storage_container_destination_data.storage_container_destination_details)

    def test_create_storage_container_destination(self):
        resp = self.configuration.create_storage_container_destination(self.storage_container_destination_data.create_storage_container_destination_dict)
        self.assertEqual(resp, self.storage_container_destination_data.storage_container_destination_id)

    def test_delete_storage_container_destination(self):
        resp = self.configuration.delete_storage_container_destination(self.storage_container_destination_data.storage_container_destination_id)
        self.assertIsNone(resp)
