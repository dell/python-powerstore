from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
import mock


class TestVolumeGroup(TestBase):

    def test_get_volumegroups(self):
        volgrp_list = self.provisioning.get_volume_group_list()
        self.assertListEqual(volgrp_list, self.data.volumegroup_list)

    def test_get_volumegroups_with_filter(self):
        querystring = {'is_replication_destination': 'eq.false'}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client,
                               'request') as mock_request:
            volgrp_list = self.provisioning.get_volume_group_list(
                filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_VOLUME_GROUP_LIST_URL.format(
                   self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_get_volume_group_details(self):
        vg = self.provisioning.get_volume_group_details(self.data.vg_id1)
        self.assertEqual(vg, self.data.volume_group1)

    def test_get_volume_group_by_name(self):
        vg = self.provisioning.get_volume_group_by_name(self.data.vg_name1)
        self.assertEqual(vg, [self.data.volume_group1])

    def test_create_volume_group(self):
        vg = self.provisioning.create_volume_group(
            self.data.vg_name1, volume_ids=[self.data.vol_id1])
        self.assertEqual(vg, self.data.vg_id1)

    def test_modify_volume_group(self):
        vg = self.provisioning.modify_volume_group(self.data.vg_id1,
                                                   self.data.vg_name1)
        self.assertIsNone(vg)

    def test_add_invalid_protection_policy_for_volume_group(self):
        self.assertRaises(PowerStoreException,
                          self.provisioning.modify_volume_group,
                          self.data.vg_id1,
                          protection_policy_id=self.data.invalid_pol_id)

    def test_add_invalid_volume_to_volume_group(self):
        self.assertRaises(PowerStoreException,
                          self.provisioning.add_members_to_volume_group,
                          self.data.vg_id1,
                          volume_ids=[self.data.invalid_vol_id])

    def test_delete_volume_group(self):
        vg = self.provisioning.delete_volume_group(self.data.vg_id1)
        self.assertIsNone(vg)
