from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
from PyPowerStore.objects import file_nis
from unittest import mock


class TestFileNIS(TestBase):

    def test_get_file_nises(self):
        file_nis_list = self.file_nis.get_file_nis_list()
        self.assertListEqual(file_nis_list, self.file_nis_data.file_nis_list)

    def test_get_file_nis_with_filter(self):
        querystring = {
            'nas_server_id': 'eq.6581683c-61a3-76ab-f107-62b767ad9845'}
        querystring.update(file_nis.SELECT_ALL_FILE_NIS)
        with mock.patch.object(self.file_nis.file_nis_client,
                               'request') as mock_request:
            self.file_nis.get_file_nis_list(filter_dict=querystring,
                                            all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                file_nis.GET_FILE_NIS_LIST_URL.format(
                    self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_get_file_nis_details(self):
        file_nis_detail = self.file_nis.get_file_nis_details(
            self.file_nis_data.file_nis_id)
        self.assertEqual(file_nis_detail, self.file_nis_data.file_nis_detail)

    def test_get_invalid_file_nis_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.file_nis.get_file_nis_details,
            self.file_nis_data.file_nis_id_not_exist)

    def test_get_file_nis_by_nas(self):
        file_nis_detail = self.file_nis.get_file_nis_by_nas_server_id(
            self.file_nis_data.nas_server_id)
        self.assertEqual(file_nis_detail, self.file_nis_data.file_nis_list)

    def test_modify_file_nis(self):
        param = {"domain": "stringa",
                 "add_ip_addresses": [
                     "10.10.10.11"
                 ],
                 "remove_ip_addresses": [
                     "10.10.10.10"
                 ]}
        resp = self.file_nis.modify_file_nis(
            self.file_nis_data.file_nis_id, param)
        self.assertIsNone(resp)

    def test_modify_file_nis_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.file_nis.modify_file_nis,
            self.file_nis_data.file_nis_id,
            invalid_param)

    def test_modify_file_nis_with_empty_param(self):
        self.assertRaises(
            ValueError, self.file_nis.modify_file_nis,
            self.file_nis_data.file_nis_id, {})

    def test_create_file_nis(self):
        payload = {"nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
                   "domain": "string",
                   "ip_addresses": [
                       "10.10.10.10"
                   ]}
        file_nis_id = self.file_nis.create_file_nis(payload)
        self.assertEqual(file_nis_id, self.file_nis_data.file_nis_id)

    def test_delete_file_nis(self):
        resp = self.file_nis.delete_file_nis(self.file_nis_data.file_nis_id)
        self.assertIsNone(resp)
