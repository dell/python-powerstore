from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestHostGroup(TestBase):

    def test_get_hostgroups(self):
        hg_list = self.provisioning.get_host_group_list()
        self.assertListEqual(hg_list, self.data.hg_list)

    def test_get_hostgroup_with_filter(self):
        querystring = {"name": "neq.my_hg"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_host_group_list(
                filter_dict=querystring, all_pages=True
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_HOST_GROUP_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_host_group_details(self):
        hg = self.provisioning.get_host_group_details(self.data.hg_id1)
        self.assertEqual(hg, self.data.hg1)

    def test_get_host_group_by_name(self):
        hg = self.provisioning.get_host_group_by_name(self.data.hg_name1)
        self.assertEqual(hg, [self.data.hg1])

    def test_create_host_group(self):
        hg = self.provisioning.create_host_group(
            self.data.hg_name1, host_ids=[self.data.host_id1]
        )
        self.assertEqual(hg, self.data.create_hg)

    def test_modify_host_group(self):
        hg = self.provisioning.modify_host_group(
            self.data.hg_id1, add_host_ids=[self.data.host_id2]
        )
        self.assertIsNone(hg)

    def test_invalid_rename_host_group(self):
        self.assertRaises(
            PowerStoreException,
            self.provisioning.modify_host_group,
            self.data.hg_id1,
            name=self.data.existing_hg_name,
        )

    def test_add_invalid_host_to_host_group(self):
        self.assertRaises(
            PowerStoreException,
            self.provisioning.add_hosts_to_host_group,
            self.data.hg_id1,
            add_host_ids=[self.data.invalid_host_id],
        )

    def test_delete_host_group(self):
        hg = self.provisioning.delete_host_group(self.data.hg_id1)
        self.assertIsNone(hg)
