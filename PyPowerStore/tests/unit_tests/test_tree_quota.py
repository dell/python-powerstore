"""Unit Tests for Tree Quota"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants, helpers
from PyPowerStore.utils.exception import PowerStoreException


class TestTreeQuota(TestBase):
    """
    Unit tests for Tree Quota
    """

    def test_get_tree_quotas(self):
        """
        Test get tree quotas

        Validates that the tree quota list matches the expected list
        """
        tq_list = self.provisioning.get_file_tree_quotas()
        self.assertListEqual(tq_list, self.data.tq_list)

    def test_get_tree_quota_with_filter(self):
        """
        Test get tree quota with filter

        Validates that the get tree quota with filter request is called with the correct parameters
        """
        querystring = {"soft_limit": "lt.24117248"}
        querystring.update(constants.SELECT_ID_AND_PATH)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_file_tree_quotas(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_TREE_QUOTA_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_create_tree_quota(self):
        """
        Test create tree quota

        Validates that the created tree quota matches the expected quota
        """
        path = "/" + self.data.fs_name1
        param = {"is_user_quotas_enforced": True}
        quota = self.provisioning.create_tree_quota(self.data.fs_id1, path, param)
        self.assertEqual(quota, self.data.create_tree_quota)

    def test_create_tree_quota_with_invalid_param(self):
        """
        Test create tree quota with invalid param

        Validates that creating a tree quota with an invalid parameter raises a PowerStoreException
        """
        param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.create_tree_quota,
            self.data.fs_id1,
            "/" + self.data.fs_name1,
            param,
        )

    def test_get_tree_quota(self):
        """
        Test get tree quota

        Validates that the retrieved tree quota matches the expected quota
        """
        tq_detail = self.provisioning.get_tree_quota(self.data.tq_id1)
        self.assertEqual(tq_detail, self.data.tq_detail)

    def test_get_tree_quota_by_path_and_fs(self):
        """
        Test get tree quota by path and fs

        Validates that getting a tree quota by path and filesystem ID is
        called with the correct parameters
        """
        path = "/" + self.data.fs_name1
        querystring = helpers.prepare_querystring(
            constants.SELECT_ALL_TREE_QUOTA,
            path=constants.EQUALS + path,
            file_system_id=constants.EQUALS + self.data.fs_id1,
        )
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_tree_quota(
                tree_quota_id=None, path=path, file_system_id=self.data.fs_id1,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_TREE_QUOTA_LIST_URL.format(self.provisioning.server_ip),
                querystring=querystring,
            )

    def test_update_tree_quota(self):
        """
        Test update tree quota

        Validates that the response is None
        """
        param = {"description": "modify description", "is_user_quotas_enforced": False}
        resp = self.provisioning.update_tree_quota(self.data.tq_id1, param)
        self.assertIsNone(resp)

    def test_delete_tree_quota(self):
        """
        Test delete tree quota

        Validates that the response is None
        """
        resp = self.provisioning.delete_tree_quota(self.data.tq_id1)
        self.assertIsNone(resp)

    def test_delete_invalid_tree_quota(self):
        """
        Test delete invalid tree quota

        Validates that deleting an invalid tree quota raises a PowerStoreException
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.delete_tree_quota,
            self.data.invalid_tq_id,
        )
