from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException

import mock


class TestSMBShare(TestBase):

    def test_get_smbshares(self):
        smb_list = self.provisioning.get_smb_shares()
        self.assertListEqual(smb_list, self.data.smb_list)

    def test_get_smbshare_with_filter(self):
        querystring = {'name': 'eq.my_smb1'}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client,
                               'request') as mock_request:
            self.provisioning.get_smb_shares(filter_dict=querystring,
                                             all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_SMB_SHARE_LIST_URL.format(
                    self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_create_smb_share(self):
        path = '/{0}'.format(self.data.fs_name1)
        smb = self.provisioning.create_smb_share(
            self.data.fs_id1, path, self.data.smb_name1,
            is_ABE_enabled=True, is_encryption_enabled=True)
        self.assertEqual(smb, self.data.create_smb)

    def test_get_smb_share(self):
        smb = self.provisioning.get_smb_share(self.data.smb_id1)
        self.assertEqual(smb, self.data.smb_detail)

    def test_get_smb_share_by_name(self):
        smb = self.provisioning.get_smb_share_by_name(self.data.smb_name1)
        self.assertEqual(smb, self.data.smb_detail)

    def test_update_smb_share(self):
        resp = self.provisioning.update_smb_share(
            self.data.smb_id1, is_ABE_enabled=True)
        self.assertIsNone(resp)

    def test_delete_smb_share(self):
        resp = self.provisioning.delete_smb_share(self.data.smb_id1)
        self.assertIsNone(resp)

    def test_delete_invalid_smb_share(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.delete_smb_share,
            self.data.invalid_smb_id)
