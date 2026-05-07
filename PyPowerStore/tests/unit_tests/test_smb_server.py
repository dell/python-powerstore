"""Unit Tests for SMB Server"""

# pylint: disable=duplicate-code

from unittest import mock

from PyPowerStore.objects import smb_server
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestSMBServer(TestBase):
    """
    Unit tests for SMB Server
    """

    def test_get_smb_servers(self):
        """
        Test Get SMB Servers
        
        Validates that the list of SMB servers matches the expected list
        """
        smb_server_list = self.smb_server.get_smb_server_list()
        self.assertListEqual(smb_server_list, self.smb_server_data.smb_server_list)

    def test_get_smb_server_with_filter(self):
        """
        Test Get SMB Server with Filter
        
        Validates that the query string is correctly formatted and the request
        is made with the expected parameters
        """
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
        """
        Test Get SMB Server Details
        
        Validates that the SMB server details match the expected details
        """
        smb_server_detail = self.smb_server.get_smb_server_details(
            self.smb_server_data.smb_server_id,
        )
        self.assertEqual(smb_server_detail, self.smb_server_data.smb_server_detail)

    def test_get_invalid_smb_server_details(self):
        """
        Test Get Invalid SMB Server Details
        
        Verifies that a PowerStoreException is raised with the expected error
        message when trying to get non-existent SMB server details
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.smb_server.get_smb_server_details,
            self.smb_server_data.smb_server_id_not_exist,
        )

    def test_get_smb_server_by_nas(self):
        """
        Test Get SMB Server by NAS
        
        Validates that the list of SMB servers matches the expected list
        when retrieved by NAS server ID
        """
        smb_server_detail = self.smb_server.get_smb_server_by_nas_server_id(
            self.smb_server_data.nas_server_id,
        )
        self.assertEqual(smb_server_detail, self.smb_server_data.smb_server_list)

    def test_modify_smb_server(self):
        """
        Test Modify SMB Server
        
        Validates that the response is None
        """
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
        """
        Test Modify SMB Server with Invalid Parameter
        
        Verifies that a PowerStoreException is raised with the expected error
        message when trying to modify the SMB server with an invalid parameter
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.smb_server.modify_smb_server,
            self.smb_server_data.smb_server_id,
            invalid_param,
        )

    def test_modify_smb_server_with_empty_param(self):
        """
        Test Modify SMB Server with Empty Parameter
        
        Verifies that a ValueError is raised when trying to modify the
        SMB server with an empty parameter
        """
        self.assertRaises(
            ValueError,
            self.smb_server.modify_smb_server,
            self.smb_server_data.smb_server_id,
            {},
        )

    def test_create_smb_server(self):
        """
        Test Create SMB Server
        
        Validates that the the SMB server ID is returned
        """
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
        """
        Test Delete SMB Server
        
        Validates that the response is None
        """
        resp = self.smb_server.delete_smb_server(self.smb_server_data.smb_server_id)
        self.assertIsNone(resp)
