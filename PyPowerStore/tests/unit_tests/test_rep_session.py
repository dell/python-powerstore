"""Unit tests for Replication Session"""

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestReplicationSession(TestBase):
    """
    Unit tests for ReplicationSession
    """

    def test_get_replication_sessions(self):
        """
        Test get replication sessions.

        Validates that the list of replication sessions matches the expected list.
        """
        rep_session_list = self.protection.get_replication_sessions()
        self.assertListEqual(rep_session_list, self.data.rep_session_list)

    def test_get_replication_session_details(self):
        """
        Test get replication session details.

        Verifies that the replication session details equal the expected details.
        """
        rep_session_detail = self.protection.get_replication_session_details(
            self.data.rep_session_id_1,
        )
        self.assertEqual(rep_session_detail, self.data.rep_session_details_1)

    def test_modify_replication_session(self):
        """
        Test modify replication session.

        Confirms that the response is None.
        """
        rep_session_detail = self.protection.modify_replication_session(
            self.data.rep_session_id_1, self.data.session_role,
        )
        self.assertIsNone(rep_session_detail)

    def test_reprotect_replication_session(self):
        """
        Test reprotect replication session.

        Validates that the response is None.
        """
        rep_session_detail = self.protection.reprotect_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_failover_replication_session(self):
        """
        Test failover replication session.

        Verifies that the response is None.
        """
        rep_session_detail = self.protection.failover_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_invalid_param_failover_replication_session(self):
        """
        Test failover replication session with invalid parameter.

        Confirms that the failover replication session with invalid
        parameter raises a PowerStoreException.
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.protection.failover_replication_session,
            self.data.rep_session_id_1,
            invalid_param,
        )

    def test_get_invalid_session_details(self):
        """
        Test get invalid session details.

        Verifies that the get invalid session details raises a PowerStoreException.
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.protection.get_replication_session_details,
            self.data.rep_session_id_not_exist,
        )

    def test_resume_replication_session(self):
        """
        Test resume replication session.

        Validates that the response is None.
        """
        rep_session_detail = self.protection.resume_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_pause_replication_session(self):
        """
        Test pause replication session.

        Confirms that the response is None.
        """
        rep_session_detail = self.protection.pause_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)

    def test_sync_replication_session(self):
        """
        Test sync replication session.

        Verifies that the response is None.
        """
        rep_session_detail = self.protection.sync_replication_session(
            self.data.rep_session_id_1,
        )
        self.assertIsNone(rep_session_detail)
