from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.ldap_account_data import LdapAccountData


class LDAPAccountResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ldap_account_data = LdapAccountData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/ldap_account"):
                return self.get_ldap_account_list
            return self.get_ldap_account_details
        if self.method == "POST":
            return self.create_ldap_account
        if self.method == "PATCH":
            return self.modify_ldap_account_details
        if self.method == "DELETE":
            return self.delete_ldap_account

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_ldap_account_list(self):
        return self.status_code, self.ldap_account_data.ldap_account_list

    def get_ldap_account_details(self):
        return self.status_code, self.ldap_account_data.ldap_account_details1

    def create_ldap_account(self):
        return self.status_code, self.ldap_account_data.create_ldap_account_response

    def modify_ldap_account_details(self):
        return 204, None

    def delete_ldap_account(self):
        return 204, None
