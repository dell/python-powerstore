"""Unit Tests for NFS Export"""

# pylint: disable=duplicate-code

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestNFSExport(TestBase):
    """
    Unit tests for NFS Export
    """

    def test_get_nfsexports(self):
        """
        Test get NFS Exports
        
        Validates that the list of NFS exports matches the expected list
        """
        nfs_list = self.provisioning.get_nfs_exports()
        self.assertListEqual(nfs_list, self.data.nfs_list)

    def test_get_nfsexport_with_filter(self):
        """
        Test get NFS Export with filter
        
        Validates that the request to get NFS exports with filter
        is called with the expected querystring
        """
        querystring = {"default_access": "eq.Root"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_nfs_exports(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_NFS_EXPORT_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_create_nfsexport(self):
        """
        Test create NFS Export
        
        Validates that the created NFS export matches the expected export
        """
        path = f"/{self.data.fs_name1}"
        param = {"description": "My description"}
        nfs = self.provisioning.create_nfs_export(
            self.data.fs_id1, path, self.data.nfs_name1, param,
        )
        self.assertEqual(nfs, self.data.create_nfs)

    def test_get_nfs_export_details(self):
        """
        Test get NFS Export details
        
        Validates that the NFS export details match the expected details
        """
        nfs_detail = self.provisioning.get_nfs_export_details(self.data.nfs_id1)
        self.assertEqual(nfs_detail, self.data.nfs_detail)

    def test_get_nfs_export_details_by_name(self):
        """
        Test get NFS Export details by name
        
        Validates that the NFS export details match the expected details
        """
        nfs_detail = self.provisioning.get_nfs_export_details_by_name(
            self.data.nfs_name1,
        )
        self.assertEqual(nfs_detail, self.data.nfs_detail)

    def test_modify_nfs_export(self):
        """
        Test modify NFS Export
        
        Validates that the response is None
        """
        param = {"min_security": "Kerberos"}
        resp = self.provisioning.modify_nfs_export(self.data.nfs_id1, param)
        self.assertIsNone(resp)

    def test_modify_nfs_export_with_invalid_param(self):
        """
        Test modify NFS Export with invalid parameter
        
        Validates that modifying NFS export with invalid parameter raises an exception
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.modify_nfs_export,
            self.data.nfs_id1,
            invalid_param,
        )

    def test_delete_nfs_export(self):
        """
        Test delete NFS Export
        
        Validates that the response is None
        """
        resp = self.provisioning.delete_nfs_export(self.data.nfs_id1)
        self.assertIsNone(resp)

    def test_delete_invalid_nfs_export(self):
        """
        Test delete invalid NFS Export
        
        Validates that deleting an invalid NFS export raises an exception
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.delete_nfs_export,
            self.data.invalid_nfs,
        )
