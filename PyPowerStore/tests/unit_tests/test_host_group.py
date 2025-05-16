"""Unit tests for Host Group"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestHostGroup(TestBase):
    """
    Unit tests for Host Group
    """

    def test_get_hostgroups(self):
        """
        Test Get Host Groups

        Validates the host group list returned from the server matches the expected list.
        """
        hg_list = self.provisioning.get_host_group_list()
        self.assertListEqual(hg_list, self.data.hg_list)

    def test_get_hostgroup_with_filter(self):
        """
        Test Get Host Group with Filter

        Confirms the request to get host groups with a filter is sent to the
        server with the correct parameters.
        """
        querystring = {"name": "neq.my_hg"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_host_group_list(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_HOST_GROUP_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_host_group_details(self):
        """
        Test Get Host Group Details

        Verifies the host group details returned from the server match the expected details.
        """
        hg = self.provisioning.get_host_group_details(self.data.hg_id1)
        self.assertEqual(hg, self.data.hg1)

    def test_get_host_group_by_name(self):
        """
        Test Get Host Group by Name

        Confirms the host group returned from the server by name matches the expected group.
        """
        hg = self.provisioning.get_host_group_by_name(self.data.hg_name1)
        self.assertEqual(hg, [self.data.hg1])

    def test_create_host_group(self):
        """
        Test Create Host Group

        Validates the host group created on the server matches the expected group.
        """
        hg = self.provisioning.create_host_group(
            self.data.hg_name1, host_ids=[self.data.host_id1],
        )
        self.assertEqual(hg, self.data.create_hg)

    def test_modify_host_group(self):
        """
        Test Modify Host Group

        Verifies the response is None.
        """
        hg = self.provisioning.modify_host_group(
            self.data.hg_id1, add_host_ids=[self.data.host_id2],
        )
        self.assertIsNone(hg)

    def test_invalid_rename_host_group(self):
        """
        Test Invalid Rename Host Group

        Confirms an exception is raised when renaming a host group to an existing name.
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.modify_host_group,
            self.data.hg_id1,
            name=self.data.existing_hg_name,
        )

    def test_add_invalid_host_to_host_group(self):
        """
        Test Add Invalid Host to Host Group

        Verifies an exception is raised when adding an invalid host to a host group.
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.add_hosts_to_host_group,
            self.data.hg_id1,
            add_host_ids=[self.data.invalid_host_id],
        )

    def test_delete_host_group(self):
        """
        Test Delete Host Group

        Confirms the response is None.
        """
        hg = self.provisioning.delete_host_group(self.data.hg_id1)
        self.assertIsNone(hg)
