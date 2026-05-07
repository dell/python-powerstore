"""Unit Tests for Volume"""

# pylint: disable=assignment-from-no-return,too-many-public-methods

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestVolume(TestBase):
    """
    Unit tests for Volume
    """

    def test_get_volumes(self):
        """
        Test Get Volumes

        Validates that the list of volumes matches the expected list.
        """
        vol_list = self.provisioning.get_volumes()
        self.assertListEqual(vol_list, self.data.volume_list)

    def test_get_volume_detail(self):
        """
        Test Get Volume Details

        Validates that the volume details match the expected volume details.
        """
        vol_details = self.provisioning.get_volume_details(self.data.vol_id1)
        self.assertEqual(vol_details, self.data.volume1)

    def test_create_volume(self):
        """
        Test Create Volume

        Validates that the response is None.
        """
        vol = self.provisioning.create_volume(self.data.vol_name1, self.data.size)
        self.assertIsNone(vol)

    def test_create_vol_with_app_type(self):
        """
        Test Create Volume with Application Type

        Validates that the response is None.
        """
        vol = self.provisioning.create_volume(
            self.data.vol_name1, self.data.size, app_type=self.data.app_type1,
        )
        self.assertIsNone(vol)

    def test_create_vol_with_app_type_and_with_app_type_other(self):
        """
        Test Create Volume with Application Type and Other

        Validates that the response is None.
        """
        vol = self.provisioning.create_volume(
            self.data.vol_name1,
            self.data.size,
            app_type=self.data.app_type2,
            app_type_other=self.data.app_type_other,
        )
        self.assertIsNone(vol)

    def test_create_vol_with_appliance_id(self):
        """
        Test Create Volume with Appliance ID

        Validates that the response is None.
        """
        vol = self.provisioning.create_volume(
            self.data.vol_name1, self.data.size, appliance_id=self.data.appliance_id,
        )
        self.assertIsNone(vol)

    def test_modify_volume(self):
        """
        Test Modify Volume

        Validates that the response is None.
        """
        vol = self.provisioning.modify_volume(self.data.vol_id1, self.data.vol_name1)
        self.assertIsNone(vol)

    def test_clone_volume(self):
        """
        Test Clone Volume

        Validates that the volume id matches the expected volume id.
        """
        vol_clone_id = self.provisioning.clone_volume(
            self.data.vol_id1,
            self.data.vol_name2,
            None,
            self.data.host_id1,
            self.data.hg_id1,
            1,
            self.data.pol_id,
            "default_low",
        )
        self.assertEqual(vol_clone_id, self.data.vol_id2)

    def test_refresh_volume(self):
        """
        Test Refresh Volume

        Validates that the snapshot id matches the expected snapshot id.
        """
        vol_snap_id = self.provisioning.refresh_volume(
            self.data.vol_id1,
            self.data.vol_id2,
            self.data.create_snapshot,
            self.data.backup_snapshot_profile["name"],
            self.data.backup_snapshot_profile["description"],
            self.data.backup_snapshot_profile["expiration_timestamp"],
            "default_low",
        )
        self.assertEqual(vol_snap_id, self.data.snapshot_id)

    def test_restore_volume(self):
        """
        Test Restore Volume

        Validates that the snapshot id matches the expected snapshot id.
        """
        vol_snap_id = self.provisioning.restore_volume(
            self.data.vol_id1,
            self.data.vol_snap_id,
            self.data.create_snapshot,
            self.data.backup_snapshot_profile["name"],
            self.data.backup_snapshot_profile["description"],
            self.data.backup_snapshot_profile["expiration_timestamp"],
            "default_low",
        )
        self.assertEqual(vol_snap_id, self.data.snapshot_id)

    def test_delete_volume(self):
        """
        Test Delete Volume

        Validates that the response is None.
        """
        vol = self.provisioning.delete_volume(self.data.vol_id1)
        self.assertIsNone(vol)

    def test_get_volumes_with_filter(self):
        """
        Test Get Volumes with Filter

        Validates that the request is called with the expected parameters.
        """
        querystring = {"name": "ilike.*test*"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_volumes(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_VOLUME_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_add_protection_policy_for_volume(self):
        """
        Test Add Protection Policy for Volume

        Validates that the response is None.
        """
        resp = self.provisioning.add_protection_policy_for_volume(
            self.data.vol_id1, self.data.pol_id,
        )
        self.assertIsNone(resp)

    def test_add_invalid_protection_policy_for_volume(self):
        """
        Test Add Invalid Protection Policy for Volume

        Validates that the exception is raised while adding invalid protection policy for volume.
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.add_protection_policy_for_volume,
            self.data.vol_id1,
            self.data.invalid_pol_id,
        )

    def test_remove_protection_policy_for_volume(self):
        """
        Test Remove Protection Policy for Volume

        Validates that the response is None.
        """
        resp = self.provisioning.remove_protection_policy_for_volume(self.data.vol_id1)
        self.assertIsNone(resp)

    def test_get_volume_by_name(self):
        """
        Test Get Volume by Name

        Validates that the volume details match the expected volume details.
        """
        vol_details = self.provisioning.get_volume_by_name(self.data.vol_name1)
        self.assertEqual(vol_details, [self.data.volume1])

    def test_map_volume_to_host(self):
        """
        Test Map Volume to Host

        Validates that the response is None.
        """
        resp = self.provisioning.map_volume_to_host(
            self.data.vol_id1, self.data.host_id1, self.data.lun,
        )
        self.assertIsNone(resp)

    def test_unmap_volume_from_host(self):
        """
        Test Unmap Volume from Host

        Validates that the response is None.
        """
        resp = self.provisioning.unmap_volume_from_host(
            self.data.vol_id1, self.data.host_id1,
        )
        self.assertIsNone(resp)

    def test_map_volume_to_hg(self):
        """
        Test Map Volume to Host Group

        Validates that the response is None.
        """
        resp = self.provisioning.map_volume_to_host_group(
            self.data.vol_id1, self.data.hg_id1, self.data.lun,
        )
        self.assertIsNone(resp)

    def test_unmap_volume_from_host_group(self):
        """
        Test Unmap Volume from Host Group

        Validates that the response is None.
        """
        resp = self.provisioning.unmap_volume_from_host_group(
            self.data.vol_id1, self.data.hg_id1,
        )
        self.assertIsNone(resp)

    def test_create_volume_snapshot(self):
        """
        Test Create Volume Snapshot

        Validates that the snapshot details match the expected snapshot details.
        """
        vol_snap_detail = self.protection.create_volume_snapshot(
            self.data.vol_id1, description="vol snap description",
        )
        self.assertEqual(vol_snap_detail, self.data.vol_snap_detail)

    def test_get_volume_snapshots(self):
        """
        Test Get Volume Snapshots

        Validates that the volume snapshot list matches the expected list.
        """
        snap = self.protection.get_volume_snapshots(self.data.vol_id1)
        self.assertListEqual(snap, self.data.volume_snap_list)

    def test_get_volume_snapshot_details(self):
        """
        Test Get Volume Snapshot Details

        Validates that the volume snapshot details match the expected details.
        """
        snap = self.protection.get_volume_snapshot_details(self.data.vol_snap_id)
        self.assertEqual(snap, self.data.vol_snap_detail)

    def test_modify_volume_snapshot(self):
        """
        Test Modify Volume Snapshot

        Validates that the volume snapshot details match the expected details.
        """
        snap = self.protection.modify_volume_snapshot(
            self.data.vol_snap_id, name="vol_snap",
        )
        self.assertEqual(snap, self.data.vol_snap_detail)

    def test_delete_volume_snapshot(self):
        """
        Test Delete Volume Snapshot

        Validates that the response is None.
        """
        resp = self.protection.delete_volume_snapshot(self.data.vol_snap_id)
        self.assertIsNone(resp)

    def test_config_metro_volume(self):
        """
        Test Configure Metro Volume

        Validates that the metro replication session id matches the expected id.
        """
        resp = self.provisioning.configure_metro_volume(
            self.data.vol_id1, self.data.remote_system_id,
        )
        self.assertEqual(resp, self.data.metro_replication_session_id)

    def test_end_metro_volume_config(self):
        """
        Test End Metro Volume Config

        Validates that the response is None.
        """
        resp = self.provisioning.end_volume_metro_config(self.data.vol_id1)
        self.assertIsNone(resp)
