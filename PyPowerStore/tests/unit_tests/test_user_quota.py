"""Unit Tests for User Quota"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants, helpers
from PyPowerStore.utils.exception import PowerStoreException


class TestUserQuota(TestBase):
    """
    Unit tests for User Quota
    """

    def test_get_user_quotas(self):
        """
        Test get user quotas

        Validates that the returned user quota list matches the expected list.
        """
        uq_list = self.provisioning.get_file_user_quotas()
        self.assertListEqual(uq_list, self.data.uq_list)

    def test_get_user_quota_with_filter(self):
        """
        Test get user quota with filter

        Validates that the request to get user quota with filter is
        called with the expected parameters.
        """
        querystring = {"state": "eq.ok"}
        querystring.update(constants.SELECT_ID_AND_PATH)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_file_user_quotas(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_USER_QUOTA_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_create_user_quota(self):
        """
        Test create user quota

        Validates that the created user quota matches the expected quota.
        """
        param = {"soft_limit": 2097152, "hard_limit": 4194304}
        quota = self.provisioning.create_user_quota(self.data.fs_id1, param)
        self.assertEqual(quota, self.data.create_user_quota)

    def test_create_user_quota_with_invalid_param(self):
        """
        Test create user quota with invalid param

        Verifies that creating user quota with invalid param raises the expected exception.
        """
        param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.create_user_quota,
            self.data.fs_id1,
            param,
        )

    def test_get_user_quota(self):
        """
        Test get user quota

        Validates that the returned user quota matches the expected quota.
        """
        quota = self.provisioning.get_user_quota(self.data.uq_id1)
        self.assertEqual(quota, self.data.uq_detail)

    def test_get_user_quota_with_query_param(self):
        """
        Test get user quota with query param

        Validates that the request to get user quota with query param is
        called with the expected parameters.
        """
        param = {"uid": str(1), "tree_quota_id": self.data.tq_id1}
        my_param = {k: constants.EQUALS + v for k, v in param.items()}
        querystring = helpers.prepare_querystring(
            constants.SELECT_ALL_USER_QUOTA, my_param,
        )
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_user_quota(user_quota_id=None, query_params=param)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_USER_QUOTA_LIST_URL.format(self.provisioning.server_ip),
                querystring=querystring,
            )

    def test_update_user_quota(self):
        """
        Test update user quota

        Verifies that the response is None.
        """
        param = {"soft_limit": 2097152, "hard_limit": 4194304}
        resp = self.provisioning.update_user_quota(self.data.uq_id1, param)
        self.assertIsNone(resp)
