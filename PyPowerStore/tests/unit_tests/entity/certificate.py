"""Mock Certificate Api for Certificate Unit Tests"""

# pylint: disable=too-many-return-statements

from PyPowerStore.tests.unit_tests.data.certificate_data import CertificateData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class CertificateResponse(Entity):
    """
    This class is used to handle Certificate related responses.
    
    It provides methods to get certificates, certificate details, create certificates,
    reset certificates, exchange certificates, and modify certificates.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the CertificateResponse object.
        
        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.certificate_data = CertificateData()
        self.status_code = 200

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.
        
        Returns:
            function: The API function.
        """
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
        return None

    def get_certificates(self):
        """
        Returns a list of certificates.
        
        Returns:
            tuple: A tuple containing the status code and the list of certificates.
        """
        return self.status_code, self.certificate_data.certificate_list

    def execute_api(self, api_name):
        """
        Executes the API function and returns the result.
        
        Args:
            api_name (function): The API function to execute.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        status_code, response = api_name()
        return status_code, response

    def get_certificate_details(self):
        """
        Returns the details of a certificate.
        
        Returns:
            tuple: A tuple containing the status code and the certificate details.
        """
        if self.url.endswith(
            f"/x509_certificate/{self.certificate_data.invalid_certificate_id}",
        ):
            return 404, self.certificate_data.certificate_error[404]
        return self.status_code, self.certificate_data.certificate_details

    def create_certificate(self):
        """
        Creates a new certificate.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if "service" not in self.kwargs["data"]:
            return 400, self.certificate_data.certificate_error[400]
        return 201, self.certificate_data.certificate_create_response

    def reset_certificates(self):
        """
        Resets the certificates.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def exchange_certificates(self):
        """
        Exchanges the certificates.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def modify_certificate(self):
        """
        Modifies a certificate.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if "is_current" not in self.kwargs["data"]:
            return 422, self.certificate_data.certificate_error[422]
        return 204, self.certificate_data.certificate_details_2
