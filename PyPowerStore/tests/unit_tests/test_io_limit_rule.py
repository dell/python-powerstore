"""Unit tests for IO Limit Rule"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestIoLimitRule(TestBase):
    """
    Unit tests for IO Limit Rule SDK methods on provisioning.
    """

    def test_get_io_limit_rules(self):
        """
        Test get io_limit_rules

        Validates that the returned list equals self.data.io_limit_rule_list
        """
        result = self.provisioning.get_io_limit_rules()
        self.assertListEqual(result, self.data.io_limit_rule_list)

    def test_get_io_limit_rules_with_filter(self):
        """
        Test get io_limit_rules with filter and all_pages

        Validates that mock_request is called with the correct arguments
        """
        filter_dict = {"name": constants.EQUALS + self.data.io_limit_rule_name1}
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_io_limit_rules(
                filter_dict=filter_dict, all_pages=True,
            )
            mock_request.assert_called_once()

    def test_get_io_limit_rule_details(self):
        """
        Test get io_limit_rule details by ID

        Validates that rule details equals self.data.io_limit_rule1
        """
        result = self.provisioning.get_io_limit_rule_details(
            self.data.io_limit_rule_id1,
        )
        self.assertEqual(result, self.data.io_limit_rule1)

    def test_get_io_limit_rule_details_invalid_id(self):
        """
        Test get io_limit_rule details with invalid ID

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.get_io_limit_rule_details,
            self.data.invalid_io_limit_rule_id,
        )

    def test_get_io_limit_rule_by_name(self):
        """
        Test get io_limit_rule by name

        Validates that rule details list equals [self.data.io_limit_rule1]
        """
        result = self.provisioning.get_io_limit_rule_by_name(
            self.data.io_limit_rule_name1,
        )
        self.assertEqual(result, [self.data.io_limit_rule1])

    def test_get_io_limit_rule_by_name_uses_correct_url(self):
        """
        Test get io_limit_rule by name uses IO_LIMIT_RULE_LIST_URL

        Validates that mock_request is called with the list URL and name filter
        """
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = [self.data.io_limit_rule1]
            self.provisioning.get_io_limit_rule_by_name(self.data.io_limit_rule_name1)
            args, kwargs = mock_request.call_args
            self.assertIn(
                constants.IO_LIMIT_RULE_LIST_URL.format(self.provisioning.server_ip),
                args,
            )

    def test_create_io_limit_rule(self):
        """
        Test create io_limit_rule

        Validates that the returned dict contains the expected rule ID
        """
        payload = {
            "name": self.data.io_limit_rule_name1,
            "type": "Absolute",
            "max_iops": 5000,
            "max_bw": 102400,
        }
        result = self.provisioning.create_io_limit_rule(payload)
        self.assertEqual(result.get("id"), self.data.io_limit_rule_id1)

    def test_create_io_limit_rule_uses_post(self):
        """
        Test create io_limit_rule uses POST method

        Validates that mock_request is called with POST
        """
        payload = {"name": self.data.io_limit_rule_name1, "type": "Absolute", "max_iops": 1}
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = {"id": self.data.io_limit_rule_id1}
            self.provisioning.create_io_limit_rule(payload)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.POST)

    def test_modify_io_limit_rule(self):
        """
        Test modify io_limit_rule

        Validates that modify returns None (204 No Content)
        """
        payload = {"max_iops": 10000}
        result = self.provisioning.modify_io_limit_rule(
            self.data.io_limit_rule_id1, payload,
        )
        self.assertIsNone(result)

    def test_modify_io_limit_rule_invalid_id(self):
        """
        Test modify io_limit_rule with invalid ID

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.modify_io_limit_rule,
            self.data.invalid_io_limit_rule_id,
            {"max_iops": 10000},
        )

    def test_modify_io_limit_rule_uses_patch(self):
        """
        Test modify io_limit_rule uses PATCH method

        Validates that mock_request is called with PATCH and the rule object URL
        """
        payload = {"max_bw": 204800}
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = None
            self.provisioning.modify_io_limit_rule(self.data.io_limit_rule_id1, payload)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.PATCH)
            self.assertIn(self.data.io_limit_rule_id1, args[1])

    def test_delete_io_limit_rule(self):
        """
        Test delete io_limit_rule

        Validates that delete returns None (204 No Content)
        """
        result = self.provisioning.delete_io_limit_rule(self.data.io_limit_rule_id1)
        self.assertIsNone(result)

    def test_delete_io_limit_rule_invalid_id(self):
        """
        Test delete io_limit_rule with invalid ID

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.delete_io_limit_rule,
            self.data.invalid_io_limit_rule_id,
        )

    def test_delete_io_limit_rule_uses_delete(self):
        """
        Test delete io_limit_rule uses DELETE method

        Validates that mock_request is called with DELETE and the rule object URL
        """
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = None
            self.provisioning.delete_io_limit_rule(self.data.io_limit_rule_id1)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.DELETE)
            self.assertIn(self.data.io_limit_rule_id1, args[1])

    def test_get_io_limit_rule_details_query_select(self):
        """
        Test get io_limit_rule details uses IO_LIMIT_RULE_DETAILS_QUERY

        Validates that the querystring includes the correct select fields
        """
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = self.data.io_limit_rule1
            self.provisioning.get_io_limit_rule_details(self.data.io_limit_rule_id1)
            _, kwargs = mock_request.call_args
            self.assertEqual(
                kwargs.get("querystring"), constants.IO_LIMIT_RULE_DETAILS_QUERY,
            )

    def test_get_io_limit_rule_details_object_url(self):
        """
        Test get io_limit_rule details uses IO_LIMIT_RULE_OBJECT_URL

        Validates that the URL contains the rule ID
        """
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = self.data.io_limit_rule1
            self.provisioning.get_io_limit_rule_details(self.data.io_limit_rule_id1)
            args, _ = mock_request.call_args
            expected_url = constants.IO_LIMIT_RULE_OBJECT_URL.format(
                self.provisioning.server_ip, self.data.io_limit_rule_id1,
            )
            self.assertEqual(args[1], expected_url)
