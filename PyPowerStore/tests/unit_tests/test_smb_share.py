"""Unit Tests for SMB Share"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestSMBShare(TestBase):
    """
    Unit tests for SMB Share
    """

    def test_get_smbshares(self):
        """
        Test Get SMB Shares
        
        Validates that the list of SMB shares matches the expected SMB details
        """
        smb_list = self.provisioning.get_smb_shares()
        self.assertEqual(smb_list, self.data.smb_detail)

    def test_get_smbshare_with_filter(self):
        """
        Test Get SMB Share with Filter
        
        Validates that the query string is correctly formatted and the request
        is made with the expected parameters
        """
        querystring = {"name": "eq.my_smb1"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_smb_shares(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_SMB_SHARE_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_create_smb_share(self):
        """
        Test Create SMB Share
        
        Validates that the created SMB share matches the expected SMB details
        """
        path = f"/{self.data.fs_name1}"
        smb = self.provisioning.create_smb_share(
            self.data.fs_id1,
            path,
            self.data.smb_name1,
            is_ABE_enabled=True,
            is_encryption_enabled=True,
        )
        self.assertEqual(smb, self.data.create_smb)

    def test_get_smb_share(self):
        """
        Test Get SMB Share
        
        Validates that the retrieved SMB share matches the expected SMB details
        """
        smb = self.provisioning.get_smb_share(self.data.smb_id1)
        self.assertEqual(smb, self.data.smb_detail)

    def test_get_smb_share_by_name(self):
        """
        Test Get SMB Share by Name
        
        Validates that the retrieved SMB share matches the expected SMB details
        """
        smb = self.provisioning.get_smb_share_by_name(self.data.smb_name1)
        self.assertEqual(smb, self.data.smb_detail)

    def test_update_smb_share(self):
        """
        Test Update SMB Share
        
        Validates that the response is None
        """
        resp = self.provisioning.update_smb_share(
            self.data.smb_id1, is_ABE_enabled=True,
        )
        self.assertIsNone(resp)

    def test_delete_smb_share(self):
        """
        Test Delete SMB Share
        
        Validates that the response is None
        """
        resp = self.provisioning.delete_smb_share(self.data.smb_id1)
        self.assertIsNone(resp)

    def test_delete_invalid_smb_share(self):
        """
        Test Delete Invalid SMB Share
        
        Validates that an error is raised when trying to delete an invalid SMB share
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.delete_smb_share,
            self.data.invalid_smb_id,
        )

    def test_get_acl(self):
        """
        Test Get ACL
        
        Validates that the request is made with the correct parameters
        """
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = self.data.acl_data
            response = self.provisioning.get_acl(self.data.smb_id1)
            self.assertEqual(response, self.data.acl_data)

            mock_request.assert_called_once_with(
                constants.POST,
                constants.GET_ACL_DETAILS.format(
                    self.provisioning.server_ip, self.data.smb_id1,
                ),
            )

    def test_set_acl(self):
        """
        Test Set ACL
        
        Validates that the request is made with the correct parameters
        """
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            mock_request.return_value = self.data.acl_data
            response = self.provisioning.set_acl(self.data.smb_id1, self.data.acl_data)
            self.assertEqual(response, self.data.acl_data)
            payload = {"add_aces": self.data.acl_data}
            mock_request.assert_called_once_with(
                constants.POST,
                constants.SET_ACL_DETAILS.format(
                    self.provisioning.server_ip, self.data.smb_id1,
                ),
                payload=payload,
            )
