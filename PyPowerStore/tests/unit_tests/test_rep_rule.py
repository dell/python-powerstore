"""Unit tests for Policy"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestPolicy(TestBase):
    """
    Unit tests for Policy
    """

    def test_get_replication_rules(self):
        """
        Test get replication rules

        Validates that get replication rules equals to rep rule list
        """
        rep_rule_list = self.protection.get_replication_rules()
        self.assertListEqual(rep_rule_list, self.data.rep_rule_list)

    def test_get_rep_rule_with_filter(self):
        """
        Test get replication rule with filter

        Validates that get replication rule with filter matches to expected request call
        """
        querystring = {"alert_threshold": "gt.10"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            self.protection.get_replication_rules(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.REPLICATION_RULE_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                querystring=querystring,
            )

    def test_get_replication_rule_details(self):
        """
        Test get replication rule details

        Validates that get replication rule details equals to rep rule details 1
        """
        rr_details = self.protection.get_replication_rule_details(
            self.data.rep_rule_id_1,
        )
        self.assertEqual(rr_details, self.data.rep_rule_details_1)

    def test_get_replication_rule_by_name(self):
        """
        Test get replication rule by name

        Validates that get replication rule by name equals to rep rule details 1
        """
        rr_details = self.protection.get_replication_rule_by_name(
            self.data.rep_rule_name_1,
        )
        self.assertEqual(rr_details, [self.data.rep_rule_details_1])

    def test_create_replication_rule(self):
        """
        Test create replication rule

        Validates that create replication rule equals to rep rule details 1
        """
        rep_rule = self.protection.create_replication_rule(
            name=self.data.rep_rule_name_1,
            alert_threshold=self.data.alert_threshold,
            remote_system_id=self.data.remote_system_id,
            rpo=self.data.rpo,
        )
        self.assertEqual(rep_rule, self.data.rep_rule_details_1)

    def test_modify_replication_rule(self):
        """
        Test modify replication rule

        Validates that modify replication rule response is not None
        """
        rep_rule = self.protection.modify_replication_rule(
            self.data.rep_rule_id_1, alert_threshold=self.data.new_alert_threshold,
        )
        self.assertIsNotNone(rep_rule)

    def test_modify_invalid_alert_threshold_replication_rule(self):
        """
        Test modify replication rule with invalid alert threshold

        Validates that modify replication rule with invalid alert
        threshold raises PowerStoreException
        """
        self.assertRaises(
            PowerStoreException,
            self.protection.modify_replication_rule,
            self.data.rep_rule_id_1,
            alert_threshold=self.data.invalid_alert_threshold,
        )

    def test_delete_replication_rule(self):
        """
        Test delete replication rule

        Validates that delete replication rule response equals to None
        """
        rep_rule = self.protection.delete_replication_rule(self.data.rep_rule_id_1)
        self.assertIsNone(rep_rule)
