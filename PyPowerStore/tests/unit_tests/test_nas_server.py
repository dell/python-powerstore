from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException

import copy
import mock


class TestNASServer(TestBase):

    def test_get_nasservers(self):
        nas_list = self.provisioning.get_nas_servers()
        self.assertListEqual(nas_list, self.data.nas_list)

    def test_get_nasserver_with_filter(self):
        querystring = {'operational_status_l10n': 'eq.started'}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client,
                               'request') as mock_request:
            self.provisioning.get_nas_servers(filter_dict=querystring,
                                              all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_NAS_SERVER_LIST_URL.format(
                    self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_get_nas_server_details(self):
        nas_detail = self.provisioning.get_nas_server_details(
            self.data.nas_id1)
        self.assertEqual(nas_detail, self.data.nas_detail)

    def test_get_invalid_nas_server_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.get_nas_server_details,
            self.data.nas_id_not_exist)

    def test_get_nas_server_by_name(self):
        nas_detail = self.provisioning.get_nas_server_by_name(
            self.data.nas_name1)
        self.assertEqual(nas_detail, self.data.nas_detail)

    def test_modify_nasserver(self):
        param = {'default_unix_user': '1', 'default_windows_user': '10', 'protection_policy_id': 'samplepolicyid'}
        resp = self.provisioning.modify_nasserver(self.data.nas_id1, param)
        self.assertIsNone(resp)
        # name will be skipped and will not be passed to request()
        new_param = copy.copy(param)
        new_param['name'] = None
        with mock.patch.object(self.provisioning.client,
                               'request') as mock_request:
            self.provisioning.modify_nasserver(self.data.nas_id1, param)
            mock_request.assert_called_with(
                constants.PATCH,
                constants.MODIFY_NAS_SERVER_URL.format(
                    self.provisioning.server_ip, self.data.nas_id1),
                payload=param)

    def test_modify_nasserver_with_invalid_param(self):
        invalid_param = {'invalid_key': 'invalid_value'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.provisioning.modify_nasserver,
            self.data.nas_id1,
            invalid_param)

    def test_modify_nasserver_which_does_not_exist(self):
        param = {'description': 'My description'}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.modify_nasserver,
            self.data.nas_id_not_exist,
            param)

    def test_modify_nasserver_with_empty_param(self):
        self.assertRaises(
            ValueError, self.provisioning.modify_nasserver,
            self.data.nas_id1, {})
