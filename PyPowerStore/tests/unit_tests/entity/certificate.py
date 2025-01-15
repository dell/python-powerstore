from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.certificate_data import CertificateData


class CertificateResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.certificate_data = CertificateData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/x509_certificate"):
                return self.get_certificates
            return self.get_certificate_details
        if self.method == "POST":
            if self.url.endswith("/exchange"):
                return self.exchange_certificates
            if self.url.endswith("/reset_certificates"):
                return self.reset_certificates
            if self.url.endswith("/x509_certificate"):
                return self.create_certificate
        elif self.method == "PATCH":
            return self.modify_certificate

    def get_certificates(self):
        return self.status_code, self.certificate_data.certificate_list

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_certificate_details(self):
        if self.url.endswith(
            "/x509_certificate/{0}".format(self.certificate_data.invalid_certificate_id)
        ):
            return 404, self.certificate_data.certificate_error[404]
        return self.status_code, self.certificate_data.certificate_details

    def create_certificate(self):
        if "service" not in self.kwargs["data"]:
            return 400, self.certificate_data.certificate_error[400]
        return 201, self.certificate_data.certificate_create_response

    def reset_certificates(self):
        return 204, None

    def exchange_certificates(self):
        return 204, None

    def modify_certificate(self):
        if "is_current" not in self.kwargs["data"]:
            return 422, self.certificate_data.certificate_error[422]
        return 204, self.certificate_data.certificate_details_2
