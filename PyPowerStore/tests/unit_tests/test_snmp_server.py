from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
from PyPowerStore.objects import snmp_server
import copy
from unittest import mock


class TestSNMPServer(TestBase):

    def test_get_snmp_servers(self):
        snmp_server_list = self.snmp_server.get_snmp_server_list()
        self.assertListEqual(snmp_server_list, self.snmp_server_data.snmp_server_list)

    def test_get_snmp_server_with_filter(self):
        querystring = {"version": "V2c"}
        querystring.update(snmp_server.SELECT_ALL_SNMP)
        with mock.patch.object(self.snmp_server.snmp_server_client,
                               'request') as mock_request:
            self.snmp_server.get_snmp_server_list(filter_dict=querystring,
                                                      all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                snmp_server.GET_SNMP_LIST_URL.format(
                    self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_get_snmp_server_details(self):
        snmp_server_detail = self.snmp_server.get_snmp_server_details(
            self.snmp_server_data.snmp_server_id)
        self.assertEqual(snmp_server_detail, self.snmp_server_data.snmp_server_detail)

    def test_get_invalid_snmp_server_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "Server Record Not Found",
            self.snmp_server.get_snmp_server_details,
            self.snmp_server_data.snmp_server_id_not_exist)

    def test_modify_snmp_server(self):
        param = {
                    "ip_address": "127.0.0.8",
                    "port": 162,
                    "version": "V2c",
                    "alert_severity": "Info",
                    "trap_community": "public"
                    }
        resp = self.snmp_server.modify_snmp_server(self.snmp_server_data.snmp_server_id, param)
        self.assertIsNone(resp)

    def test_modify_snmp_server_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.snmp_server.modify_snmp_server,
            self.snmp_server_data.snmp_server_id,
            invalid_param)

    def test_modify_snmp_server_with_empty_param(self):
        self.assertRaises(
            ValueError, self.snmp_server.modify_snmp_server,
            self.snmp_server_data.snmp_server_id, {})

    def test_create_snmp_server(self):
        payload = {
                    "ip_address": "127.0.0.8",
                    "port": 162,
                    "version": "V2c",
                    "alert_severity": "Info",
                    "trap_community": "public"
                    }
        snmp_server_id = self.snmp_server.create_snmp_server(payload)
        self.assertEqual(snmp_server_id, self.snmp_server_data.snmp_server_id)

    def test_delete_snmp_server(self):
        resp = self.snmp_server.delete_snmp_server(self.snmp_server_data.snmp_server_id)
        self.assertIsNone(resp)