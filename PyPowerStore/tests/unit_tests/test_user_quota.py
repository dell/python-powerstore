from PyPowerStore.utils import constants, helpers
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException

from unittest import mock


class TestUserQuota(TestBase):

    def test_get_user_quotas(self):
        uq_list = self.provisioning.get_file_user_quotas()
        self.assertListEqual(uq_list, self.data.uq_list)

    def test_get_user_quota_with_filter(self):
        querystring = {"state": "eq.ok"}
        querystring.update(constants.SELECT_ID_AND_PATH)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_file_user_quotas(
                filter_dict=querystring, all_pages=True
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_USER_QUOTA_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_create_user_quota(self):
        param = {"soft_limit": 2097152, "hard_limit": 4194304}
        quota = self.provisioning.create_user_quota(self.data.fs_id1, param)
        self.assertEqual(quota, self.data.create_user_quota)

    def test_create_user_quota_with_invalid_param(self):
        param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.create_user_quota,
            self.data.fs_id1,
            param,
        )

    def test_get_user_quota(self):
        quota = self.provisioning.get_user_quota(self.data.uq_id1)
        self.assertEqual(quota, self.data.uq_detail)

    def test_get_user_quota_with_query_param(self):
        param = {"uid": str(1), "tree_quota_id": self.data.tq_id1}
        my_param = {k: constants.EQUALS + v for k, v in param.items()}
        querystring = helpers.prepare_querystring(
            constants.SELECT_ALL_USER_QUOTA, my_param
        )
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_user_quota(user_quota_id=None, query_params=param)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_USER_QUOTA_LIST_URL.format(self.provisioning.server_ip),
                querystring=querystring,
            )

    def test_update_user_quota(self):
        param = {"soft_limit": 2097152, "hard_limit": 4194304}
        resp = self.provisioning.update_user_quota(self.data.uq_id1, param)
        self.assertIsNone(resp)
