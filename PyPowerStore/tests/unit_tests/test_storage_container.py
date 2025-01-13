from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestStorageContainer(TestBase):
    def test_get_storage_containers(self):
        storage_container_list = self.configuration.get_storage_container_list()
        self.assertListEqual(storage_container_list, self.storage_container_data.storage_container_list)

    def test_get_storage_container_details(self):
        resp = self.configuration.get_storage_container_details(
            self.storage_container_data.storage_container_list[0]['id'])
        self.assertEqual(resp, self.storage_container_data.storage_container_details)

    def test_get_storage_container_details_by_name(self):
        resp = self.configuration.get_storage_container_details_by_name(
            self.storage_container_data.storage_container_details['name'])
        self.assertEqual(resp, self.storage_container_data.storage_container_details)

    def test_create_storage_container(self):
        resp = self.configuration.create_storage_container(self.storage_container_data.create_storage_container_dict)
        self.assertEqual(resp, self.storage_container_data.create_storage_container_response)

    def test_modify_storage_container_details(self):
        resp = self.configuration.modify_storage_container_details(
            self.storage_container_data.storage_container_list[0]['id'], self.storage_container_data.modify_storage_container_dict)
        self.assertIsNone(resp)

    def test_delete_storage_container(self):
        resp = self.configuration.delete_storage_container(self.storage_container_data.storage_container_list[0]['id'], False)
        self.assertIsNone(resp)

