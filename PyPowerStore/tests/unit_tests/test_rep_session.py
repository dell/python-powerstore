from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestReplicationSession(TestBase):

    def test_get_replication_sessions(self):
        rep_session_list = self.protection.get_replication_sessions()
        self.assertListEqual(rep_session_list, self.data.rep_session_list)

    def test_get_replication_session_details(self):
        rep_session_detail = self.protection.get_replication_session_details(
            self.data.rep_session_id_1,
        )
        self.assertEqual(rep_session_detail, self.data.rep_session_details_1)

    def test_modify_replication_session(self):
        rep_session_detail = self.protection.modify_replication_session(
            self.data.rep_session_id_1, self.data.session_role,
        )
        self.assertIsNone(rep_session_detail)

    def test_reprotect_replication_session(self):
        rep_session_detail = self.protection.reprotect_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_failover_replication_session(self):
        rep_session_detail = self.protection.failover_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_invalid_param_failover_replication_session(self):
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.protection.failover_replication_session,
            self.data.rep_session_id_1,
            invalid_param,
        )

    def test_get_invalid_session_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.protection.get_replication_session_details,
            self.data.rep_session_id_not_exist,
        )

    def test_resume_replication_session(self):
        rep_session_detail = self.protection.resume_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_pause_replication_session(self):
        rep_session_detail = self.protection.pause_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_sync_replication_session(self):
        rep_session_detail = self.protection.sync_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)
