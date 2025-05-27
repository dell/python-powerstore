"""Unit Tests for File DNS"""

from unittest import mock

from PyPowerStore.objects import file_dns
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestFileDNS(TestBase):
    """
    Unit tests for File DNS
    """

    def test_get_file_dnses(self):
        """
        Test Get File DNSes

        Validates that get_file_dns_list returns the correct list of file DNS
        """
        file_dns_list = self.file_dns.get_file_dns_list()
        self.assertListEqual(file_dns_list, self.file_dns_data.file_dns_list)

    def test_get_file_dns_with_filter(self):
        """
        Test Get File DNS With Filter

        Verifies that get_file_dns_list with filter is called correctly
        """
        querystring = {"nas_server_id": "eq.6581683c-61a3-76ab-f107-62b767ad9845"}
        querystring.update(file_dns.SELECT_ALL_FILE_DNS)
        with mock.patch.object(
            self.file_dns.file_dns_client, "request",
        ) as mock_request:
            self.file_dns.get_file_dns_list(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                file_dns.GET_FILE_DNS_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_file_dns_details(self):
        """
        Test Get File DNS Details

        Confirms that get_file_dns_details returns the correct details of a file DNS
        """
        file_dns_detail = self.file_dns.get_file_dns_details(
            self.file_dns_data.file_dns_id,
        )
        self.assertEqual(file_dns_detail, self.file_dns_data.file_dns_detail)

    def test_get_invalid_file_dns_details(self):
        """
        Test Get Invalid File DNS Details

        Validates that get_file_dns_details raises an exception for an invalid file DNS
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.file_dns.get_file_dns_details,
            self.file_dns_data.file_dns_id_not_exist,
        )

    def test_get_file_dns_by_nas(self):
        """
        Test Get File DNS By NAS

        Verifies that get_file_dns_by_nas_server_id returns the correct details of a file DNS
        """
        file_dns_detail = self.file_dns.get_file_dns_by_nas_server_id(
            self.file_dns_data.nas_server_id,
        )
        self.assertEqual(file_dns_detail, self.file_dns_data.file_dns_list)

    def test_modify_file_dns(self):
        """
        Test Modify File DNS

        Confirms that response of modify_file_dns is None
        """
        param = {
            "domain": "DNS_domain",
            "add_ip_addresses": ["10.10.10.11"],
            "remove_ip_addresses": ["10.10.10.10"],
            "transport": "UDP",
            "is_destination_override_enabled": False,
        }
        resp = self.file_dns.modify_file_dns(self.file_dns_data.file_dns_id, param)
        self.assertIsNone(resp)

    def test_modify_file_dns_with_invalid_param(self):
        """
        Test Modify File DNS With Invalid Param

        Validates that modify_file_dns raises an exception for an invalid parameter
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.file_dns.modify_file_dns,
            self.file_dns_data.file_dns_id,
            invalid_param,
        )

    def test_modify_file_dns_with_empty_param(self):
        """
        Test Modify File DNS With Empty Param

        Validates that modify_file_dns raises an exception for an empty parameter
        """
        self.assertRaises(
            ValueError,
            self.file_dns.modify_file_dns,
            self.file_dns_data.file_dns_id,
            {},
        )

    def test_create_file_dns(self):
        """
        Test Create File DNS

        Confirms that the file DNS is created correctly
        """
        payload = {
            "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
            "domain": "DNS_domain",
            "add_ip_addresses": ["10.10.10.10"],
            "transport": "UDP",
            "is_disabled": False,
        }
        file_dns_id = self.file_dns.create_file_dns(payload)
        self.assertEqual(file_dns_id, self.file_dns_data.file_dns_id)

    def test_delete_file_dns(self):
        """
        Test Delete File DNS

        Verifies that response of delete_file_dns is None
        """
        resp = self.file_dns.delete_file_dns(self.file_dns_data.file_dns_id)
        self.assertIsNone(resp)
