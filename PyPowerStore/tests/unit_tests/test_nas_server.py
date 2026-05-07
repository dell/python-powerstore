"""Unit Tests for NAS Server"""

import copy
from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestNASServer(TestBase):
    """
    Unit tests for NAS Server
    """

    def test_get_nasservers(self):
        """
        Test Get NAS Servers

        Validates that the list of NAS servers matches the expected list
        """
        nas_list = self.provisioning.get_nas_servers()
        self.assertListEqual(nas_list, self.data.nas_list)

    def test_get_nasserver_with_filter(self):
        """
        Test Get NAS Server with Filter

        Validates that the request to get NAS servers with a filter is
        called with the expected querystring
        """
        querystring = {"operational_status_l10n": "eq.started"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_nas_servers(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_NAS_SERVER_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_nas_server_details(self):
        """
        Test Get NAS Server Details

        Validates that the details of a NAS server match the expected details
        """
        nas_detail = self.provisioning.get_nas_server_details(self.data.nas_id1)
        self.assertEqual(nas_detail, self.data.nas_detail)

    def test_get_invalid_nas_server_details(self):
        """
        Test Get Invalid NAS Server Details

        Validates that getting the details of a non-existent NAS server raises an exception
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.get_nas_server_details,
            self.data.nas_id_not_exist,
        )

    def test_get_nas_server_by_name(self):
        """
        Test Get NAS Server by Name

        Validates that the details of a NAS server match the expected details when retrieved by name
        """
        nas_detail = self.provisioning.get_nas_server_by_name(self.data.nas_name1)
        self.assertEqual(nas_detail, self.data.nas_detail)

    def test_modify_nasserver(self):
        """
        Test Modify NAS Server

        Validates that the request to modify a NAS server is called with the expected payload
        """
        param = {
            "default_unix_user": "1",
            "default_windows_user": "10",
            "protection_policy_id": "samplepolicyid",
        }
        resp = self.provisioning.modify_nasserver(self.data.nas_id1, param)
        self.assertIsNone(resp)
        # name will be skipped and will not be passed to request()
        new_param = copy.copy(param)
        new_param["name"] = None
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.modify_nasserver(self.data.nas_id1, param)
            mock_request.assert_called_with(
                constants.PATCH,
                constants.MODIFY_NAS_SERVER_URL.format(
                    self.provisioning.server_ip, self.data.nas_id1,
                ),
                payload=param,
            )

    def test_modify_nasserver_with_invalid_param(self):
        """
        Test Modify NAS Server with Invalid Param

        Validates that modifying a NAS server with an invalid parameter raises an exception
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.modify_nasserver,
            self.data.nas_id1,
            invalid_param,
        )

    def test_modify_nasserver_which_does_not_exist(self):
        """
        Test Modify NAS Server Which Does Not Exist

        Validates that modifying a non-existent NAS server raises an exception
        """
        param = {"description": "My description"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.modify_nasserver,
            self.data.nas_id_not_exist,
            param,
        )

    def test_modify_nasserver_with_empty_param(self):
        """
        Test Modify NAS Server with Empty Param

        Validates that modifying a NAS server with an empty parameter raises a ValueError
        """
        self.assertRaises(
            ValueError, self.provisioning.modify_nasserver, self.data.nas_id1, {},
        )

    def test_create_nas_server(self):
        """
        Test Create NAS Server

        Validates that creating a NAS server returns the expected ID
        """
        payload = {
            "name": "nas1",
            "default_unix_user": "user1",
            "default_windows_user": "user2",
        }
        nas_id = self.provisioning.create_nasserver(payload)
        self.assertEqual(nas_id, self.data.nas_id1)

    def test_delete_nas_server(self):
        """
        Test Delete NAS Server

        Validates that response is None
        """
        resp = self.provisioning.delete_nasserver(self.data.nas_name1)
        self.assertIsNone(resp)
