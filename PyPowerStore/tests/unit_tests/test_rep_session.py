from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException

import copy
import mock


class TestReplicationSession(TestBase):

    def test_get_replication_sessions(self):
        rep_session_list = self.protection.get_replication_sessions()
        self.assertListEqual(rep_session_list, self.data.rep_session_list)

    def test_get_replication_session_details(self):
        rep_session_detail = self.protection.get_replication_session_details(
            self.data.rep_session_id_1)
        self.assertEqual(rep_session_detail, self.data.rep_session_details_1)