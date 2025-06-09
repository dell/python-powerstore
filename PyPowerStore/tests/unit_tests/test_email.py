"""Unit tests for Email"""

# pylint: disable=duplicate-code

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestEmail(TestBase):
    """
    Unit tests for Email
    """

    def test_get_destination_emails(self):
        """
        Test get destination emails
        
        Validates that get destination emails returns the expected list of emails
        """
        emails_list = self.configuration.get_destination_emails()
        print(emails_list)
        self.assertListEqual(emails_list, self.email_data.email_list)

    def test_create_destination_email(self):
        """
        Test create destination email
        
        Verifies that create destination email creates an email with the expected details
        """
        resp = self.configuration.create_destination_email(
            self.email_data.create_email_dict,
        )
        self.assertEqual(resp, self.email_data.email_details_1)

    def test_get_destination_email_by_address(self):
        """
        Test get destination email by address
        
        Confirms that get destination email by address returns the expected email details
        """
        resp = self.configuration.get_destination_email_by_address(
            self.email_data.email_address_1,
        )
        self.assertEqual(resp, self.email_data.email_details_1)

    def test_get_destination_email_details(self):
        """
        Test get destination email details
        
        Validates that get destination email details returns the expected email details
        """
        resp = self.configuration.get_destination_email_details(
            self.email_data.email_id_1,
        )
        self.assertEqual(resp, self.email_data.email_details_1)

    def test_modify_destination_email(self):
        """
        Test modify destination email
        
        Verifies that the response is None
        """
        resp = self.configuration.modify_destination_email_details(
            self.email_data.email_id_1, self.email_data.modify_email_dict,
        )
        self.assertIsNone(resp)

    def test_modify_destination_email_with_invalid_param(self):
        """
        Test modify destination email with invalid param
        
        Confirms that modify destination email with invalid param raises a PowerStoreException
        """
        invalid_param = {"invalid_key": "invalid_value"}
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.modify_destination_email_details,
            self.email_data.email_id_1,
            invalid_param,
        )

    def test_delete_destination_email(self):
        """
        Test delete destination email
        
        Validates that delete destination email deletes the email successfully
        """
        resp = self.configuration.delete_destination_email(self.email_data.email_id_1)
        self.assertIsNone(resp)

    def test_send_test_mail_destination_email(self):
        """
        Test send test mail destination email
        
        Verifies that the response is None
        """
        resp = self.configuration.test_destination_email(self.email_data.email_id_1)
        self.assertIsNone(resp)
