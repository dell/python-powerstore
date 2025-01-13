from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.ldap_data import LdapData


class LdapResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ldap_data = LdapData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            return self.get_file_ldaps

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_file_ldaps(self):
        return self.status_code, self.ldap_data.ldap_list
