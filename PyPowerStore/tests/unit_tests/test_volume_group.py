"""Unit Tests for Volume Group"""

# pylint: disable=assignment-from-no-return

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestVolumeGroup(TestBase):
    """
    Unit tests for Volume Group
    """

    def test_get_volumegroups(self):
        """
        Test Get Volume Groups
        
        Validates that volume group list equals to volumegroup_list
        """
        volgrp_list = self.provisioning.get_volume_group_list()
        self.assertListEqual(volgrp_list, self.data.volumegroup_list)

    def test_get_volumegroups_with_filter(self):
        """
        Test Get Volume Groups With Filter
        
        Validates that the request is called with the correct parameters
        """
        querystring = {"is_replication_destination": "eq.false"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_volume_group_list(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_VOLUME_GROUP_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_volume_group_details(self):
        """
        Test Get Volume Group Details
        
        Validates that volume group details equals to volume_group1
        """
        vg = self.provisioning.get_volume_group_details(self.data.vg_id1)
        self.assertEqual(vg, self.data.volume_group1)

    def test_get_volume_group_by_name(self):
        """
        Test Get Volume Group By Name
        
        Validates that volume group name equals to volume_group1
        """
        vg = self.provisioning.get_volume_group_by_name(self.data.vg_name1)
        self.assertEqual(vg, [self.data.volume_group1])

    def test_create_volume_group(self):
        """
        Test Create Volume Group
        
        Validates that created volume group id equals to vg_id1
        """
        vg = self.provisioning.create_volume_group(
            self.data.vg_name1, volume_ids=[self.data.vol_id1],
        )
        self.assertEqual(vg, self.data.vg_id1)

    def test_modify_volume_group(self):
        """
        Test Modify Volume Group
        
        Validates that the response is None
        """
        vg = self.provisioning.modify_volume_group(self.data.vg_id1, self.data.vg_name1)
        self.assertIsNone(vg)

    def test_add_invalid_protection_policy_for_volume_group(self):
        """
        Test Add Invalid Protection Policy For Volume Group
        
        Validates that adding invalid protection policy raises PowerStoreException
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.modify_volume_group,
            self.data.vg_id1,
            protection_policy_id=self.data.invalid_pol_id,
        )

    def test_add_invalid_volume_to_volume_group(self):
        """
        Test Add Invalid Volume To Volume Group
        
        Validates that adding invalid volume raises PowerStoreException
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.add_members_to_volume_group,
            self.data.vg_id1,
            volume_ids=[self.data.invalid_vol_id],
        )

    def test_delete_volume_group(self):
        """
        Test Delete Volume Group
        
        Validates that deleted volume group result is None
        """
        vg = self.provisioning.delete_volume_group(self.data.vg_id1)
        self.assertIsNone(vg)

    def test_clone_volume_group(self):
        """
        Test Clone Volume Group
        
        Validates that cloned volume group id equals to vg_id2
        """
        vg_clone_id = self.provisioning.clone_volume_group(
            self.data.vg_id1, self.data.vg_name2, None, self.data.pol_id,
        )
        self.assertEqual(vg_clone_id, self.data.vg_id2)

    def test_refresh_volume_group(self):
        """
        Test Refresh Volume Group
        
        Validates that refreshed volume group snapshot id equals to snapshot_id
        """
        snapshot_id = self.provisioning.refresh_volume_group(
            self.data.vg_id1,
            self.data.vg_name2,
            self.data.create_snapshot,
            self.data.backup_snapshot_profile,
        )
        self.assertEqual(snapshot_id, self.data.snapshot_id)

    def test_restore_volume_group(self):
        """
        Test Restore Volume Group
        
        Validates that restored volume group snapshot id equals to snapshot_id
        """
        snapshot_id = self.provisioning.restore_volume_group(
            self.data.vg_id1,
            self.data.vg_name2,
            self.data.create_snapshot,
            self.data.backup_snapshot_profile,
        )
        self.assertEqual(snapshot_id, self.data.snapshot_id)
