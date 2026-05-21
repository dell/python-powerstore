"""Unit tests for QoS / File_Performance Policy"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestQosPolicy(TestBase):
    """
    Unit tests for QoS / File_Performance Policy SDK methods on protection.
    """

    def test_get_policy_details_qos(self):
        """
        Test get_policy_details for a QoS policy

        Validates that returned details equal self.data.qos_policy1
        """
        result = self.protection.get_policy_details(self.data.qos_policy_id1)
        self.assertEqual(result, self.data.qos_policy1)

    def test_get_policy_details_file_performance(self):
        """
        Test get_policy_details for a File_Performance policy

        Validates that returned details equal self.data.file_perf_policy1
        """
        result = self.protection.get_policy_details(self.data.qos_policy_id2)
        self.assertEqual(result, self.data.file_perf_policy1)

    def test_get_policy_by_name(self):
        """
        Test get_policy_by_name

        Validates that returned list equals [self.data.qos_policy1]
        """
        result = self.protection.get_policy_by_name(self.data.qos_policy_name1)
        self.assertEqual(result, [self.data.qos_policy1])

    def test_get_policy_by_name_uses_list_url(self):
        """
        Test get_policy_by_name uses PROTECTION_POLICY_LIST_URL

        Validates that mock_request is called with the list URL and name filter
        """
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = [self.data.qos_policy1]
            self.protection.get_policy_by_name(self.data.qos_policy_name1)
            args, _ = mock_request.call_args
            self.assertEqual(
                args[1],
                constants.PROTECTION_POLICY_LIST_URL.format(
                    self.provisioning.server_ip,
                ),
            )

    def test_get_policy_details_uses_qos_query(self):
        """
        Test get_policy_details uses QOS_POLICY_DETAILS_QUERY

        Validates the querystring contains the QoS select fields
        """
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = self.data.qos_policy1
            self.protection.get_policy_details(self.data.qos_policy_id1)
            _, kwargs = mock_request.call_args
            self.assertEqual(
                kwargs.get("querystring"), constants.QOS_POLICY_DETAILS_QUERY,
            )

    def test_get_policy_details_uses_object_url(self):
        """
        Test get_policy_details uses PROTECTION_POLICY_OBJECT_URL

        Validates that the URL contains the policy ID
        """
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = self.data.qos_policy1
            self.protection.get_policy_details(self.data.qos_policy_id1)
            args, _ = mock_request.call_args
            expected_url = constants.PROTECTION_POLICY_OBJECT_URL.format(
                self.provisioning.server_ip, self.data.qos_policy_id1,
            )
            self.assertEqual(args[1], expected_url)

    def test_create_policy_qos(self):
        """
        Test create_policy for QoS type

        Validates that returned dict contains the expected policy ID
        """
        payload = {
            "name": self.data.qos_policy_name1,
            "io_limit_rule_id": self.data.io_limit_rule_id1,
        }
        result = self.protection.create_policy(payload)
        self.assertEqual(result.get("id"), self.data.qos_policy_id1)

    def test_create_policy_file_performance(self):
        """
        Test create_policy for File_Performance type

        Validates that mock_request is called with POST and the list URL
        """
        payload = {
            "name": self.data.qos_policy_name2,
            "file_io_limit_rule_id": self.data.file_io_limit_rule_id1,
        }
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = {"id": self.data.qos_policy_id2}
            self.protection.create_policy(payload)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.POST)
            self.assertEqual(
                args[1],
                constants.PROTECTION_POLICY_LIST_URL.format(
                    self.provisioning.server_ip,
                ),
            )

    def test_create_policy_uses_post(self):
        """
        Test create_policy uses POST method

        Validates that mock_request is called with POST
        """
        payload = {"name": self.data.qos_policy_name1, "io_limit_rule_id": self.data.io_limit_rule_id1}
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = {"id": self.data.qos_policy_id1}
            self.protection.create_policy(payload)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.POST)

    def test_modify_policy(self):
        """
        Test modify_policy

        Validates that modify returns None (204 No Content)
        """
        payload = {"description": "Updated Gold QoS policy"}
        result = self.protection.modify_policy(self.data.qos_policy_id1, payload)
        self.assertIsNone(result)

    def test_modify_policy_invalid_id(self):
        """
        Test modify_policy with invalid ID

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.protection.modify_policy,
            self.data.invalid_qos_policy_id,
            {"description": "bad"},
        )

    def test_modify_policy_uses_patch(self):
        """
        Test modify_policy uses PATCH method

        Validates that mock_request is called with PATCH and the object URL
        """
        payload = {"io_limit_rule_id": self.data.io_limit_rule_id2}
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = None
            self.protection.modify_policy(self.data.qos_policy_id1, payload)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.PATCH)
            self.assertIn(self.data.qos_policy_id1, args[1])

    def test_modify_policy_uses_object_url(self):
        """
        Test modify_policy uses PROTECTION_POLICY_OBJECT_URL

        Validates that the URL contains the policy ID
        """
        payload = {"description": "test"}
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = None
            self.protection.modify_policy(self.data.qos_policy_id1, payload)
            args, _ = mock_request.call_args
            expected_url = constants.PROTECTION_POLICY_OBJECT_URL.format(
                self.provisioning.server_ip, self.data.qos_policy_id1,
            )
            self.assertEqual(args[1], expected_url)

    def test_delete_policy(self):
        """
        Test delete_policy

        Validates that delete returns None (204 No Content)
        """
        result = self.protection.delete_policy(self.data.qos_policy_id1)
        self.assertIsNone(result)

    def test_delete_policy_invalid_id(self):
        """
        Test delete_policy with invalid ID

        Validates that PowerStoreException is raised
        """
        self.assertRaises(
            PowerStoreException,
            self.protection.delete_policy,
            self.data.invalid_qos_policy_id,
        )

    def test_delete_policy_uses_delete(self):
        """
        Test delete_policy uses DELETE method

        Validates that mock_request is called with DELETE and the object URL
        """
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = None
            self.protection.delete_policy(self.data.qos_policy_id1)
            args, _ = mock_request.call_args
            self.assertEqual(args[0], constants.DELETE)
            self.assertIn(self.data.qos_policy_id1, args[1])

    def test_delete_policy_uses_object_url(self):
        """
        Test delete_policy uses PROTECTION_POLICY_OBJECT_URL

        Validates the URL contains the policy ID
        """
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = None
            self.protection.delete_policy(self.data.qos_policy_id1)
            args, _ = mock_request.call_args
            expected_url = constants.PROTECTION_POLICY_OBJECT_URL.format(
                self.provisioning.server_ip, self.data.qos_policy_id1,
            )
            self.assertEqual(args[1], expected_url)

    def test_get_policy_by_name_query_includes_io_limit_rule(self):
        """
        Test get_policy_by_name querystring includes io_limit_rule select

        Validates that the querystring select field contains 'io_limit_rule'
        """
        with mock.patch.object(self.protection.rest_client, "request") as mock_request:
            mock_request.return_value = [self.data.qos_policy1]
            self.protection.get_policy_by_name(self.data.qos_policy_name1)
            _, kwargs = mock_request.call_args
            qs = kwargs.get("querystring", {})
            self.assertIn("io_limit_rule", qs.get("select", ""))
