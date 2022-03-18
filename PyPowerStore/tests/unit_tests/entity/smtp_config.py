from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.smtp_config_data import SmtpConfigData


class SmtpConfigResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.smtp_config_data = SmtpConfigData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/smtp_config'):
                return self.get_smtp_configs
            else:
                return self.get_smtp_config_details
        elif self.method == 'POST':
            return self.test_smtp_config
        elif self.method == "PATCH":
            return self.modify_smtp_config_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_smtp_configs(self):
        return self.status_code, self.smtp_config_data.smtp_list

    def get_smtp_config_details(self):
        return self.status_code, self.smtp_config_data.smtp_details

    def modify_smtp_config_details(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.smtp_config_data.smtp_valid_param_list):
            # invalid param given
            return 400, self.smtp_config_data.smtp_error[400]
        return 204, None

    def test_smtp_config(self):
        return 204, None
