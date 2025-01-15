from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
from unittest import mock


class TestPolicy(TestBase):

    def test_get_replication_rules(self):
        rep_rule_list = self.protection.get_replication_rules()
        self.assertListEqual(rep_rule_list, self.data.rep_rule_list)

    def test_get_rep_rule_with_filter(self):
        querystring = {"alert_threshold": "gt.10"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            self.protection.get_replication_rules(
                filter_dict=querystring, all_pages=True
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.REPLICATION_RULE_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                querystring=querystring,
            )

    def test_get_replication_rule_details(self):
        rr_details = self.protection.get_replication_rule_details(
            self.data.rep_rule_id_1
        )
        self.assertEqual(rr_details, self.data.rep_rule_details_1)

    def test_get_replication_rule_by_name(self):
        rr_details = self.protection.get_replication_rule_by_name(
            self.data.rep_rule_name_1
        )
        self.assertEqual(rr_details, [self.data.rep_rule_details_1])

    def test_create_replication_rule(self):
        rep_rule = self.protection.create_replication_rule(
            name=self.data.rep_rule_name_1,
            alert_threshold=self.data.alert_threshold,
            remote_system_id=self.data.remote_system_id,
            rpo=self.data.rpo,
        )
        self.assertEqual(rep_rule, self.data.rep_rule_details_1)

    def test_modify_replication_rule(self):
        rep_rule = self.protection.modify_replication_rule(
            self.data.rep_rule_id_1, alert_threshold=self.data.new_alert_threshold
        )
        self.assertIsNotNone(rep_rule)

    def test_modify_invalid_alert_threshold_replication_rule(self):
        self.assertRaises(
            PowerStoreException,
            self.protection.modify_replication_rule,
            self.data.rep_rule_id_1,
            alert_threshold=self.data.invalid_alert_threshold,
        )

    def test_delete_replication_rule(self):
        rep_rule = self.protection.delete_replication_rule(self.data.rep_rule_id_1)
        self.assertIsNone(rep_rule)
