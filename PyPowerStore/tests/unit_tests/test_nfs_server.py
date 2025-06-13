"""Unit tests for NFS Server"""

# pylint: disable=duplicate-code

from unittest import mock

from PyPowerStore.objects import nfs_server
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestNFSServer(TestBase):
    """
    Unit tests for NFS Server
    """

    def test_get_nfs_servers(self):
        """
        Test get NFS servers
        
        Validates that NFS server list equals to nfs_server_list
        """
        nfs_server_list = self.nfs_server.get_nfs_server_list()
        self.assertListEqual(nfs_server_list, self.nfs_server_data.nfs_server_list)

    def test_get_nfs_server_with_filter(self):
        """
        Test get NFS server with filter
        
        Verifies that the request to get_nfs_server_list with filter
        is called with the expected querystring
        """
        querystring = {"nas_server_id": "eq.6581683c-61a3-76ab-f107-62b767ad9845"}
        querystring.update(nfs_server.SELECT_ALL_NFS_SERVER)
        with mock.patch.object(
            self.nfs_server.nfs_server_client, "request",
        ) as mock_request:
            self.nfs_server.get_nfs_server_list(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                nfs_server.GET_NFS_SERVER_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_nfs_server_details(self):
        """
        Test get NFS server details
        
        Verifies that NFS server details equals to nfs_server_detail
        """
        nfs_server_detail = self.nfs_server.get_nfs_server_details(
            self.nfs_server_data.nfs_server_id,
        )
        self.assertEqual(nfs_server_detail, self.nfs_server_data.nfs_server_detail)

    def test_get_invalid_nfs_server_details(self):
        """
        Test get invalid NFS server details
        
        Confirms that get_nfs_server_details with invalid NFS server ID raises PowerStoreException
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.nfs_server.get_nfs_server_details,
            self.nfs_server_data.nfs_server_id_not_exist,
        )

    def test_get_nfs_server_by_nas(self):
        """
        Test get NFS server by NAS
        
        Verifies that NFS server details by NAS server ID equals to nfs_server_list
        """
        nfs_server_detail = self.nfs_server.get_nfs_server_by_nas_server_id(
            self.nfs_server_data.nas_server_id,
        )
        self.assertEqual(nfs_server_detail, self.nfs_server_data.nfs_server_list)

    def test_modify_nfs_server(self):
        """
        Test modify NFS server
        
        Validates that modify_nfs_server with valid parameters returns None
        """
        param = {
            "host_name": "stringa",
            "is_nfsv3_enabled": False,
            "is_nfsv4_enabled": True,
            "is_secure_enabled": False,
            "is_skip_unjoin": True,
            "is_use_smb_config_enabled": True,
            "is_extended_credentials_enabled": True,
            "credentials_cache_TTL": 20,
        }
        resp = self.nfs_server.modify_nfs_server(
            self.nfs_server_data.nfs_server_id, param,
        )
        self.assertIsNone(resp)

    def test_modify_nfs_server_with_invalid_param(self):
        """
        Test modify NFS server with invalid parameter
        
        Confirms that modify_nfs_server with invalid parameter raises PowerStoreException
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.nfs_server.modify_nfs_server,
            self.nfs_server_data.nfs_server_id,
            invalid_param,
        )

    def test_modify_nfs_server_with_empty_param(self):
        """
        Test modify NFS server with empty parameter
        
        Validates that modify_nfs_server with empty parameter raises ValueError
        """
        self.assertRaises(
            ValueError,
            self.nfs_server.modify_nfs_server,
            self.nfs_server_data.nfs_server_id,
            {},
        )

    def test_create_nfs_server(self):
        """
        Test create NFS server
        
        Verifies that create_nfs_server with valid payload returns nfs_server_id
        """
        payload = {
            "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
            "host_name": "string",
            "is_nfsv3_enabled": True,
            "is_nfsv4_enabled": False,
            "is_secure_enabled": False,
            "is_use_smb_config_enabled": True,
            "is_extended_credentials_enabled": False,
            "credentials_cache_TTL": 15,
        }
        nfs_server_id = self.nfs_server.create_nfs_server(payload)
        self.assertEqual(nfs_server_id, self.nfs_server_data.nfs_server_id)

    def test_delete_nfs_server(self):
        """
        Test delete NFS server
        
        Validates that delete_nfs_server returns None
        """
        resp = self.nfs_server.delete_nfs_server(self.nfs_server_data.nfs_server_id)
        self.assertIsNone(resp)
