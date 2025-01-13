from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
from unittest import mock


class TestVolume(TestBase):

    def test_get_volumes(self):
        vol_list = self.provisioning.get_volumes()
        self.assertListEqual(vol_list, self.data.volume_list)

    def test_get_volume_detail(self):
        vol_details = self.provisioning.get_volume_details(self.data.vol_id1)
        self.assertEqual(vol_details, self.data.volume1)

    def test_create_volume(self):
        vol = self.provisioning.create_volume(self.data.vol_name1,
                                              self.data.size)
        self.assertIsNone(vol)

    def test_create_vol_with_app_type(self):
        vol = self.provisioning.create_volume(self.data.vol_name1,
                                              self.data.size,
                                              app_type=self.data.app_type1)
        self.assertIsNone(vol)

    def test_create_vol_with_app_type_and_with_app_type_other(self):
        vol = self.provisioning.create_volume(self.data.vol_name1,
                                              self.data.size,
                                              app_type=self.data.app_type2,
                                              app_type_other=self.data.
                                              app_type_other)
        self.assertIsNone(vol)

    def test_create_vol_with_appliance_id(self):
        vol = self.provisioning.create_volume(
            self.data.vol_name1,
            self.data.size,
            appliance_id=self.data.appliance_id)
        self.assertIsNone(vol)

    def test_modify_volume(self):
        vol = self.provisioning.modify_volume(self.data.vol_id1,
                                              self.data.vol_name1)
        self.assertIsNone(vol)

    def test_clone_volume(self):
        vol_clone_id = self.provisioning.clone_volume(
            self.data.vol_id1,
            self.data.vol_name2,
            None,
            self.data.host_id1,
            self.data.hg_id1,
            1,
            self.data.pol_id,
            'default_low')
        self.assertEqual(vol_clone_id, self.data.vol_id2)

    def test_refresh_volume(self):
        vol_snap_id = self.provisioning.refresh_volume(
            self.data.vol_id1,
            self.data.vol_id2,
            self.data.create_snapshot,
            self.data.backup_snapshot_profile['name'],
            self.data.backup_snapshot_profile['description'],
            self.data.backup_snapshot_profile['expiration_timestamp'],
            'default_low')
        self.assertEqual(vol_snap_id, self.data.snapshot_id)

    def test_restore_volume(self):
        vol_snap_id = self.provisioning.restore_volume(
            self.data.vol_id1,
            self.data.vol_snap_id,
            self.data.create_snapshot,
            self.data.backup_snapshot_profile['name'],
            self.data.backup_snapshot_profile['description'],
            self.data.backup_snapshot_profile['expiration_timestamp'],
            'default_low')
        self.assertEqual(vol_snap_id, self.data.snapshot_id)

    def test_delete_volume(self):
        vol = self.provisioning.delete_volume(self.data.vol_id1)
        self.assertIsNone(vol)

    def test_get_volumes_with_filter(self):
        querystring = {'name': 'ilike.*test*'}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client,
                               'request') as mock_request:
            self.provisioning.get_volumes(filter_dict=querystring,
                                          all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_VOLUME_LIST_URL.format(
                    self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_add_protection_policy_for_volume(self):
        resp = self.provisioning.add_protection_policy_for_volume(
            self.data.vol_id1, self.data.pol_id)
        self.assertIsNone(resp)

    def test_add_invalid_protection_policy_for_volume(self):
        self.assertRaises(PowerStoreException,
                          self.provisioning.add_protection_policy_for_volume,
                          self.data.vol_id1,
                          self.data.invalid_pol_id)

    def test_remove_protection_policy_for_volume(self):
        resp = self.provisioning.remove_protection_policy_for_volume(
            self.data.vol_id1)
        self.assertIsNone(resp)

    def test_get_volume_by_name(self):
        vol_details = self.provisioning.get_volume_by_name(
            self.data.vol_name1)
        self.assertEqual(vol_details, [self.data.volume1])

    def test_map_volume_to_host(self):
        resp = self.provisioning.map_volume_to_host(
            self.data.vol_id1, self.data.host_id1, self.data.lun)
        self.assertIsNone(resp)

    def test_unmap_volume_from_host(self):
        resp = self.provisioning.unmap_volume_from_host(
            self.data.vol_id1, self.data.host_id1)
        self.assertIsNone(resp)

    def test_map_volume_to_hg(self):
        resp = self.provisioning.map_volume_to_host_group(
            self.data.vol_id1, self.data.hg_id1, self.data.lun)
        self.assertIsNone(resp)

    def test_unmap_volume_from_host_group(self):
        resp = self.provisioning.unmap_volume_from_host_group(
            self.data.vol_id1, self.data.hg_id1)
        self.assertIsNone(resp)

    def test_create_volume_snapshot(self):
        vol_snap_detail = self.protection.create_volume_snapshot(
            self.data.vol_id1, description='vol snap description')
        self.assertEqual(vol_snap_detail, self.data.vol_snap_detail)

    def test_get_volume_snapshots(self):
        snap = self.protection.get_volume_snapshots(self.data.vol_id1)
        self.assertListEqual(snap, self.data.volume_snap_list)

    def test_get_volume_snapshot_details(self):
        snap = self.protection.get_volume_snapshot_details(
            self.data.vol_snap_id)
        self.assertEqual(snap, self.data.vol_snap_detail)

    def test_modify_volume_snapshot(self):
        snap = self.protection.modify_volume_snapshot(
            self.data.vol_snap_id, name='vol_snap')
        self.assertEqual(snap, self.data.vol_snap_detail)

    def test_delete_volume_snapshot(self):
        resp = self.protection.delete_volume_snapshot(self.data.vol_snap_id)
        self.assertIsNone(resp)

    def test_config_metro_volume(self):
        resp = self.provisioning.configure_metro_volume(
            self.data.vol_id1, self.data.remote_system_id)
        self.assertEqual(resp, self.data.metro_replication_session_id)

    def test_end_metro_volume_config(self):
        resp = self.provisioning.end_volume_metro_config(self.data.vol_id1)
        self.assertIsNone(resp)
