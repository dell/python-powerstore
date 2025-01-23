from unittest import mock

from PyPowerStore.objects import smb_server
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestSMBServer(TestBase):

    def test_get_smb_servers(self):
        smb_server_list = self.smb_server.get_smb_server_list()
        self.assertListEqual(smb_server_list, self.smb_server_data.smb_server_list)

    def test_get_smb_server_with_filter(self):
        querystring = {"nas_server_id": "eq.6581683c-61a3-76ab-f107-62b767ad9845"}
        querystring.update(smb_server.SELECT_ALL_SMB_SERVER)
        with mock.patch.object(
            self.smb_server.smb_server_client, "request",
        ) as mock_request:
            self.smb_server.get_smb_server_list(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                smb_server.GET_SMB_SERVER_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_smb_server_details(self):
        smb_server_detail = self.smb_server.get_smb_server_details(
            self.smb_server_data.smb_server_id,
        )
        self.assertEqual(smb_server_detail, self.smb_server_data.smb_server_detail)

    def test_get_invalid_smb_server_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.smb_server.get_smb_server_details,
            self.smb_server_data.smb_server_id_not_exist,
        )

    def test_get_smb_server_by_nas(self):
        smb_server_detail = self.smb_server.get_smb_server_by_nas_server_id(
            self.smb_server_data.nas_server_id,
        )
        self.assertEqual(smb_server_detail, self.smb_server_data.smb_server_list)

    def test_modify_smb_server(self):
        param = {
            "is_standalone": False,
            "computer_name": "string",
            "domain": "string",
            "netbios_name": "string",
            "workgroup": "string",
            "description": "string",
            "local_admin_password": "string",
        }
        resp = self.smb_server.modify_smb_server(
            self.smb_server_data.smb_server_id, param,
        )
        self.assertIsNone(resp)

    def test_modify_smb_server_with_invalid_param(self):
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.smb_server.modify_smb_server,
            self.smb_server_data.smb_server_id,
            invalid_param,
        )

    def test_modify_smb_server_with_empty_param(self):
        self.assertRaises(
            ValueError,
            self.smb_server.modify_smb_server,
            self.smb_server_data.smb_server_id,
            {},
        )

    def test_create_smb_server(self):
        payload = {
            "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
            "is_standalone": False,
            "computer_name": "string",
            "domain": "string",
            "netbios_name": "string",
            "workgroup": "string",
            "description": "string",
            "local_admin_password": "string",
        }
        smb_server_id = self.smb_server.create_smb_server(payload)
        self.assertEqual(smb_server_id, self.smb_server_data.smb_server_id)

    def test_delete_smb_server(self):
        resp = self.smb_server.delete_smb_server(self.smb_server_data.smb_server_id)
        self.assertIsNone(resp)
