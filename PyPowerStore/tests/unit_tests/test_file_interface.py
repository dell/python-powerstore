"""Unit tests for File Interface"""

# pylint: disable=duplicate-code

from unittest import mock

from PyPowerStore.objects import file_interface
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestFileInterface(TestBase):
    """
    Unit tests for File Interface
    """

    def test_get_file_interfaces(self):
        """
        Test Get File Interfaces

        Validates the file interface list is equal to the expected list
        """
        file_interface_list = self.file_interface.get_file_interface_list()
        self.assertListEqual(
            file_interface_list, self.file_interface_data.file_interface_list,
        )

    def test_get_file_interface_with_filter(self):
        """
        Test Get File Interface With Filter

        Verifies the filter query is correctly applied to the file interface list
        """
        querystring = {"nas_server_id": "eq.6581683c-61a3-76ab-f107-62b767ad9845"}
        querystring.update(file_interface.SELECT_ALL_FILE_INTERFACE)
        with mock.patch.object(
            self.file_interface.file_interface_client, "request",
        ) as mock_request:
            self.file_interface.get_file_interface_list(
                filter_dict=querystring, all_pages=True,
            )
            mock_request.assert_called_with(
                constants.GET,
                file_interface.GET_FILE_INTERFACE_LIST_URL.format(
                    self.provisioning.server_ip,
                ),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_file_interface_details(self):
        """
        Test Get File Interface Details

        Confirms the file interface details match the expected details
        """
        file_interface_detail = self.file_interface.get_file_interface_details(
            self.file_interface_data.file_interface_id,
        )
        self.assertEqual(
            file_interface_detail, self.file_interface_data.file_interface_detail,
        )

    def test_get_invalid_file_interface_details(self):
        """
        Test Get Invalid File Interface Details

        Validates a PowerStoreException is raised for an invalid file interface ID
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.file_interface.get_file_interface_details,
            self.file_interface_data.file_interface_id_not_exist,
        )

    def test_get_file_interface_by_nas(self):
        """
        Test Get File Interface By NAS

        Verifies the file interface details match the expected details by NAS server ID
        """
        file_interface_detail = self.file_interface.get_file_interface_by_nas_server_id(
            self.file_interface_data.nas_server_id, self.file_interface_data.ip_address,
        )
        self.assertEqual(
            file_interface_detail, self.file_interface_data.file_interface_list,
        )

    def test_modify_file_interface(self):
        """
        Test Modify File Interface

        Confirms the response is None
        """
        param = {
            "ip_address": "10.10.10.10",
            "prefix_length": 21,
            "gateway": "10.10.10.1",
            "vlan_id": 0,
            "role": "Production",
            "is_disabled": False,
        }
        resp = self.file_interface.modify_file_interface(
            self.file_interface_data.file_interface_id, param,
        )
        self.assertIsNone(resp)

    def test_modify_file_interface_with_invalid_param(self):
        """
        Test Modify File Interface With Invalid Param

        Validates a PowerStoreException is raised for an invalid parameter
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.file_interface.modify_file_interface,
            self.file_interface_data.file_interface_id,
            invalid_param,
        )

    def test_modify_file_interface_with_empty_param(self):
        """
        Test Modify File Interface With Empty Param

        Validates a ValueError is raised for an empty parameter
        """
        self.assertRaises(
            ValueError,
            self.file_interface.modify_file_interface,
            self.file_interface_data.file_interface_id,
            {},
        )

    def test_create_file_interface(self):
        """
        Test Create File Interface

        Confirms a file interface can be created with the expected ID
        """
        payload = {
            "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
            "ip_address": "10.10.10.11",
            "prefix_length": 21,
            "gateway": "10.10.10.1",
            "vlan_id": 0,
            "role": "Production",
            "is_disabled": False,
        }
        file_interface_id = self.file_interface.create_file_interface(payload)
        self.assertEqual(file_interface_id, self.file_interface_data.file_interface_id)

    def test_delete_file_interface(self):
        """
        Test Delete File Interface

        Confirms the response is None
        """
        resp = self.file_interface.delete_file_interface(
            self.file_interface_data.file_interface_id,
        )
        self.assertIsNone(resp)
