"""Unit tests for Certificate."""

# pylint: disable=assignment-from-no-return

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestCertificate(TestBase):
    """
    Unit tests for Certificate.
    """

    def test_get_certificates(self):
        """
        Test get certificates.

        Validates that the certificate list returned from the configuration 
        matches the expected certificate list.
        """
        certificates_list = self.configuration.get_certificates()
        self.assertEqual(certificates_list, self.certificate_data.certificate_list)

    def test_get_certificate_details(self):
        """
        Test get certificate details.

        Verifies that the certificate details returned from the configuration 
        match the expected certificate details for a valid certificate ID.
        """
        certificate_details = self.configuration.get_certificate_details(
            self.certificate_data.certificate_id1,
        )
        self.assertEqual(certificate_details, self.certificate_data.certificate_details)

    def test_get_invalid_certificate_details(self):
        """
        Test get invalid certificate details.

        Confirms that a PowerStoreException is raised when attempting to 
        retrieve certificate details for a non-existent certificate ID.
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_certificate_details,
            self.certificate_data.invalid_certificate_id,
        )

    def test_create_certificate(self):
        """
        Test create certificate.

        Validates that the create certificate response returned from the 
        configuration matches the expected create certificate response.
        """
        resp = self.configuration.create_certificate(
            self.certificate_data.certificate_create_params,
        )
        self.assertEqual(resp, self.certificate_data.certificate_create_response)

    def test_reset_certificates(self):
        """
        Test reset certificates.

        Verifies that the reset certificates response returned from the 
        configuration is None.
        """
        resp = self.configuration.reset_certificates(
            self.certificate_data.certificate_reset_params,
        )
        self.assertIsNone(resp)

    def test_exchange_certificates(self):
        """
        Test exchange certificates.

        Confirms that the exchange certificates response returned from the 
        configuration is None.
        """
        resp = self.configuration.exchange_certificate(
            self.certificate_data.certificate_exchange_params,
        )
        self.assertIsNone(resp)

    def test_modify_certificate(self):
        """
        Test modify certificate.

        Validates that the modify certificate response returned from the 
        configuration is None.
        """
        resp = self.configuration.modify_certificate(
            self.certificate_data.certificate_id2,
            self.certificate_data.certificate_modify_params,
        )
        self.assertIsNone(resp)

    def test_create_without_service(self):
        """
        Test create certificate without service.

        Verifies that a PowerStoreException is raised when attempting to 
        create a certificate without a service.
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.create_certificate,
            self.certificate_data.invalid_create_certificate,
        )

    def test_modify_certificate_without_is_current(self):
        """
        Test modify certificate without is current.

        Confirms that a PowerStoreException is raised when attempting to 
        modify a certificate without the is current parameter.
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 422, Unprocessable Entity",
            self.configuration.modify_certificate,
            self.certificate_data.certificate_id2,
            self.certificate_data.invalid_modify_certificate,
        )
