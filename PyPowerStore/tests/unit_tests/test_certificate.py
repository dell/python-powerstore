from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestCertificate(TestBase):
    def test_get_certificates(self):
        certificates_list = self.configuration.get_certificates()
        self.assertEqual(certificates_list,
                         self.certificate_data.certificate_list)

    def test_get_certificate_details(self):
        certificate_details = self.configuration.get_certificate_details(
            self.certificate_data.certificate_id1)
        self.assertEqual(certificate_details,
                         self.certificate_data.certificate_details)

    def test_get_invalid_certificate_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.configuration.get_certificate_details,
            self.certificate_data.invalid_certificate_id)

    def test_create_certificate(self):
        resp = self.configuration.create_certificate(
            self.certificate_data.certificate_create_params)
        self.assertEqual(
            resp, self.certificate_data.certificate_create_response)

    def test_reset_certificates(self):
        resp = self.configuration.reset_certificates(
            self.certificate_data.certificate_reset_params)
        self.assertIsNone(resp)

    def test_exchange_certificates(self):
        resp = self.configuration.exchange_certificate(
            self.certificate_data.certificate_exchange_params)
        self.assertIsNone(resp)

    def test_modify_certificate(self):
        resp = self.configuration.modify_certificate(
            self.certificate_data.certificate_id2, self.certificate_data.certificate_modify_params)
        self.assertIsNone(resp)

    def test_create_without_service(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 400, Bad Request",
            self.configuration.create_certificate,
            self.certificate_data.invalid_create_certificate)

    def test_modify_certificate_without_is_current(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 422, Unprocessable Entity",
            self.configuration.modify_certificate,
            self.certificate_data.certificate_id2,
            self.certificate_data.invalid_modify_certificate)
