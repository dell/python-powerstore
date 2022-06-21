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

    def test_modify_volume(self):
        vol = self.provisioning.modify_volume(self.data.vol_id1,
                                              self.data.vol_name1)
        self.assertIsNone(vol)

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
