from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants, helpers
from PyPowerStore.utils.exception import PowerStoreException


class TestFileSystem(TestBase):

    def test_get_filesystems(self):
        fs_list = self.provisioning.get_file_systems()
        self.assertListEqual(fs_list, self.file_system_data.fs_list)

    def test_get_filesystem_with_filter(self):
        querystring = {"get_file_systems": "lt.10000"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_file_systems(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_FILE_SYSTEM_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_create_filesystem(self):
        param = {"is_smb_sync_writes_enabled": True, "config_type": "General"}
        fs = self.provisioning.create_filesystem(
            self.file_system_data.fs_name1,
            self.file_system_data.nas_id1,
            self.file_system_data.size,
            param,
        )
        self.assertEqual(fs, self.file_system_data.create_filesystem)

    def test_get_filesystem_details(self):
        fs = self.provisioning.get_filesystem_details(self.file_system_data.fs_id1)
        self.assertEqual(fs, self.file_system_data.fs_detail)

    def test_get_filesystem_by_name(self):
        fs = self.provisioning.get_filesystem_by_name(
            self.file_system_data.fs_name1, self.file_system_data.nas_id1,
        )
        self.assertEqual(fs, self.file_system_data.fs_detail)

    def test_create_filesystem_snapshot(self):
        fs_snap = self.protection.create_filesystem_snapshot(
            self.file_system_data.fs_id1, is_smb_sync_writes_enabled=True,
        )
        self.assertEqual(fs_snap, self.file_system_data.create_filesystem_snap)

    def test_get_filesystem_snapshot_details(self):
        fs_snap_detail = self.protection.get_filesystem_snapshot_details(
            self.file_system_data.fs_snap_id,
        )
        self.assertEqual(fs_snap_detail, self.file_system_data.fs_snap_detail)

    def test_get_filesystem_snapshot_details_by_name_and_nas(self):
        fs_snap_detail = self.protection.get_filesystem_snapshot_details_by_name(
            self.file_system_data.fs_snap_name,
            nas_server_id=self.file_system_data.nas_id1,
        )
        self.assertEqual(fs_snap_detail, self.file_system_data.fs_snap_detail)

    def test_get_filesystem_snapshot_details_by_name_and_fs(self):
        querystring = helpers.prepare_querystring(
            constants.SELECT_ALL_FILESYSTEM,
            name=constants.EQUALS + self.file_system_data.fs_snap_name,
            parent_id=constants.EQUALS + self.file_system_data.fs_id1,
        )
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            self.protection.get_filesystem_snapshot_details_by_name(
                self.file_system_data.fs_snap_name,
                filesystem_id=self.file_system_data.fs_id1,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_FILESYSTEM_DETAILS_BY_NAME_URL.format(
                    self.protection.server_ip,
                ),
                querystring=querystring,
            )

    def test_get_filesystem_snapshot_details_by_name_only(self):
        self.assertRaises(
            ValueError,
            self.protection.get_filesystem_snapshot_details_by_name,
            self.file_system_data.fs_snap_name,
        )

    def test_get_filesystem_snapshot_details_by_name_fs_nas(self):
        self.assertRaises(
            ValueError,
            self.protection.get_filesystem_snapshot_details_by_name,
            self.file_system_data.fs_snap_name,
            filesystem_id=self.file_system_data.fs_id1,
            nas_server_id=self.file_system_data.nas_id1,
        )

    def test_get_snapshots_filesystem(self):
        fs_snap_list = self.provisioning.get_snapshots_filesystem(
            self.file_system_data.fs_id1,
        )
        self.assertEqual(fs_snap_list, self.file_system_data.fs_snap_list)

    def test_modify_filesystem_snapshot(self):
        resp = self.protection.modify_filesystem_snapshot(
            self.file_system_data.fs_snap_id, description="My Desc",
        )
        self.assertIsNone(resp)

    def test_modify_filesystem_with_empty_params(self):
        self.assertRaises(
            ValueError,
            self.provisioning.modify_filesystem,
            self.file_system_data.fs_id1,
            {},
        )

    def test_modify_filesystem(self):
        param = {"folder_rename_policy": "All_Allowed"}
        resp = self.provisioning.modify_filesystem(self.file_system_data.fs_id1, param)
        self.assertIsNone(resp)

    def test_delete_filesystem_snapshot(self):
        resp = self.protection.delete_filesystem_snapshot(
            self.file_system_data.fs_snap_id,
        )
        self.assertIsNone(resp)

    def test_delete_filesystem(self):
        resp = self.provisioning.delete_filesystem(self.file_system_data.fs_id1)
        self.assertIsNone(resp)

    def test_clone_filesystem(self):
        resp = self.provisioning.clone_filesystem(
            self.file_system_data.fs_id1,
            advance_parameters={"name": self.file_system_data.fs_name2},
        )
        self.assertEqual(resp, self.file_system_data.create_filesystem)

    def test_restore_filesystem(self):
        resp = self.provisioning.restore_filesystem(self.file_system_data.fs_snap_id)
        self.assertIsNone(resp)

    def test_refresh_filesystem(self):
        resp = self.provisioning.refresh_filesystem(self.file_system_data.fs_snap_id)
        self.assertIsNone(resp)

    def test_delete_invalid_filesystem(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.delete_filesystem,
            self.file_system_data.invalid_fs_id,
        )

    def test_delete_filesystem_with_snap(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 422, Unprocessable Entity",
            self.provisioning.delete_filesystem,
            self.file_system_data.fs_id_with_snap,
        )
