from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.ldap_data import LdapData


class LDAPDomainResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ldap_domain_data = LdapData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/ldap_domain"):
                return self.get_ldap_domain_configuration_list
            return self.get_ldap_domain_configuration_details
        if self.method == "POST":
            if self.url.endswith("/verify"):
                return self.verify_ldap_domain_configuration
            return self.create_ldap_domain_configuration
        if self.method == "PATCH":
            return self.modify_ldap_domain_configuration
        if self.method == "DELETE":
            return self.delete_ldap_domain_configuration

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_ldap_domain_configuration_list(self):
        return self.status_code, self.ldap_domain_data.ldap_domain_list

    def get_ldap_domain_configuration_details(self):
        return self.status_code, self.ldap_domain_data.ldap_domain_details1

    def create_ldap_domain_configuration(self):
        return self.status_code, self.ldap_domain_data.create_ldap_domain_response

    def modify_ldap_domain_configuration(self):
        return 204, None

    def verify_ldap_domain_configuration(self):
        return 204, None

    def delete_ldap_domain_configuration(self):
        return 204, None
