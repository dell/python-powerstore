from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.ntp_data import NtpData


class NtpResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.ntp_data = NtpData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/ntp'):
                return self.get_ntp_list
            return self.get_ntp_details
        if self.method == "PATCH":
            return self.modify_ntp_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_ntp_list(self):
        return self.status_code, self.ntp_data.ntp_list

    def get_ntp_details(self):
        return self.status_code, self.ntp_data.ntp_details

    def modify_ntp_details(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.ntp_data.ntp_valid_param_list):
            # invalid param given
            return 400, self.ntp_data.ntp_error[400]
        return 204, None
