"""Unit tests for Protection Policy"""

from unittest import mock

from PyPowerStore.protection import PROTECTION_POLICY_FILTER
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestPolicy(TestBase):
    """
    Unit tests for Policy
    """

    def test_get_policies(self):
        """
        Test get policies

        Validates that pol_list equals to self.data.pol_list
        """
        pol_list = self.protection.get_protection_policies()
        self.assertListEqual(pol_list, self.data.pol_list)

    def test_get_policies_with_filter(self):
        """
        Test get policies with filter

        Validates that mock_request is called with the correct arguments
        """
        querystring = {"name": "eq.my_pol"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        querystring.update(PROTECTION_POLICY_FILTER)
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            self.protection.get_protection_policies(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                constants.PROTECTION_POLICY_LIST_URL.format(
                    self.provisioning.server_ip,
                ),
                all_pages=True,
                querystring=querystring,
            )

    def test_get_protection_policy_details(self):
        """
        Test get protection policy details

        Validates that policy_details equals to self.data.protection_policy1
        """
        policy_details = self.protection.get_protection_policy_details(
            self.data.pol_id1,
        )
        self.assertEqual(policy_details, self.data.protection_policy1)

    def test_get_protection_policy_by_name(self):
        """
        Test get protection policy by name

        Validates that policy_details equals to [self.data.protection_policy1]
        """
        policy_details = self.protection.get_protection_policy_by_name(
            self.data.pol_name1,
        )
        self.assertEqual(policy_details, [self.data.protection_policy1])

    def test_create_protection_policy(self):
        """
        Test create protection policy

        Validates that policy_details equals to self.data.protection_policy1
        """
        policy_details = self.protection.create_protection_policy(
            self.data.pol_name1, snapshot_rule_ids=[self.data.pol_snap_rule_id],
        )
        self.assertEqual(policy_details, self.data.protection_policy1)

    def test_modify_protection_policy(self):
        """
        Test modify protection policy

        Validates that policy_details is not None
        """
        policy_details = self.protection.modify_protection_policy(
            policy_id=self.data.pol_id1, description=self.data.modify_description,
        )
        self.assertIsNotNone(policy_details)

    def test_add_invalid_snap_rule_to_policy(self):
        """
        Test add invalid snap rule to policy

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.protection.add_snapshot_rules_to_protection_policy,
            self.data.pol_id1,
            add_snapshot_rule_ids=[self.data.invalid_sr_id],
        )

    def test_remove_invalid_snap_rule_from_policy(self):
        """
        Test remove invalid snap rule from policy

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.protection.remove_snapshot_rules_from_protection_policy,
            self.data.pol_id1,
            remove_snapshot_rule_ids=[self.data.invalid_sr_id],
        )

    def test_delete_protection_policy(self):
        """
        Test delete protection policy

        Validates that policy_details is None
        """
        policy_details = self.protection.delete_protection_policy(self.data.pol_id1)
        self.assertIsNone(policy_details)
