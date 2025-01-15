from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestNFSExport(TestBase):

    def test_get_nfsexports(self):
        nfs_list = self.provisioning.get_nfs_exports()
        self.assertListEqual(nfs_list, self.data.nfs_list)

    def test_get_nfsexport_with_filter(self):
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
        path = "/{0}".format(self.data.fs_name1)
        param = {"description": "My description"}
        nfs = self.provisioning.create_nfs_export(
            self.data.fs_id1, path, self.data.nfs_name1, param
        )
        self.assertEqual(nfs, self.data.create_nfs)

    def test_get_nfs_export_details(self):
        nfs_detail = self.provisioning.get_nfs_export_details(self.data.nfs_id1)
        self.assertEqual(nfs_detail, self.data.nfs_detail)

    def test_get_nfs_export_details_by_name(self):
        nfs_detail = self.provisioning.get_nfs_export_details_by_name(
            self.data.nfs_name1
        )
        self.assertEqual(nfs_detail, self.data.nfs_detail)

    def test_modify_nfs_export(self):
        param = {"min_security": "Kerberos"}
        resp = self.provisioning.modify_nfs_export(self.data.nfs_id1, param)
        self.assertIsNone(resp)

    def test_modify_nfs_export_with_invalid_param(self):
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.modify_nfs_export,
            self.data.nfs_id1,
            invalid_param,
        )

    def test_delete_nfs_export(self):
        resp = self.provisioning.delete_nfs_export(self.data.nfs_id1)
        self.assertIsNone(resp)

    def test_delete_invalid_nfs_export(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.delete_nfs_export,
            self.data.invalid_nfs,
        )
