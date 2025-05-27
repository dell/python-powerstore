"""Unit Tests for Snapshot Rule"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestPolicy(TestBase):
    """
    Unit tests for policy
    """

    def test_get_snapshot_rules(self):
        """
        Test Get Snapshot Rules

        Validates that get_snapshot_rules returns the expected snapshot rule list
        """
        snap_rule_list = self.protection.get_snapshot_rules()
        self.assertListEqual(snap_rule_list, self.data.snap_rule_list)

    def test_get_snapshot_rule_with_filter(self):
        """
        Test Get Snapshot Rule With Filter

        Validates that request is called with the expected querystring
        """
        querystring = {"desired_retention": "gt.10"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            self.protection.get_snapshot_rules(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.SNAPSHOT_RULE_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                querystring=querystring,
            )

    def test_get_snapshot_rule_details(self):
        """
        Test Get Snapshot Rule Details

        Validates that get_snapshot_rule_details returns the expected snapshot rule details
        """
        sr_details = self.protection.get_snapshot_rule_details(self.data.snap_rule_id1)
        self.assertEqual(sr_details, self.data.snap_rule1)

    def test_get_snapshot_rule_by_name(self):
        """
        Test Get Snapshot Rule By Name

        Validates that get_snapshot_rule_by_name returns the expected snapshot rule details
        """
        sr_details = self.protection.get_snapshot_rule_by_name(
            self.data.snap_rule_name1,
        )
        self.assertEqual(sr_details, [self.data.snap_rule1])

    def test_create_snapshot_rule(self):
        """
        Test Create Snapshot Rule

        Validates that create_snapshot_rule_by_interval returns the expected snapshot rule
        """
        snap_rule = self.protection.create_snapshot_rule_by_interval(
            self.data.snap_rule_name1, self.data.desired_retention1, self.data.interval,
        )
        self.assertEqual(snap_rule, self.data.snap_rule1)

    def test_modify_snapshot_rule(self):
        """
        Test Modify Snapshot Rule

        Validates that modify_snapshot_rule returns the expected snapshot rule
        """
        snap_rule = self.protection.modify_snapshot_rule(
            self.data.snap_rule_id1, self.data.desired_retention2,
        )
        self.assertIsNotNone(snap_rule)

    def test_modify_invalid_interval_snapshot_rule(self):
        """
        Test Modify Invalid Interval Snapshot Rule

        Validates that modify_snapshot_rule raises an exception when interval is invalid
        """
        self.assertRaises(
            PowerStoreException,
            self.protection.modify_snapshot_rule,
            self.data.snap_rule_id1,
            interval=self.data.invalid_interval,
        )

    def test_delete_snapshot_rule(self):
        """
        Test Delete Snapshot Rule

        Validates that the response is None
        """
        snap_rule = self.protection.delete_snapshot_rule(self.data.snap_rule_id1)
        self.assertIsNone(snap_rule)
