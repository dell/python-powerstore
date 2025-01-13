from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.email_data import EmailData


class EmailResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.email_data = EmailData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/email_notify_destination'):
                if self.kwargs.get('params', {}).get('email_address'):
                    return self.get_destination_email_by_address
                return self.get_destination_emails
            return self.get_destination_email_details
        if self.method == 'POST':
            if self.url.endswith('/test'):
                return self.test_destination_email
            return self.create_destination_email
        if self.method == "PATCH":
            return self.modify_destination_email
        if self.method == "DELETE":
            return self.delete_destination_email

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_destination_emails(self):
        return self.status_code, self.email_data.email_list

    def get_destination_email_details(self):
        return self.status_code, self.email_data.email_details_1

    def get_destination_email_by_address(self):
        return self.status_code, self.email_data.email_details_1

    def create_destination_email(self):
        return 201, self.email_data.email_details_1

    def modify_destination_email(self):
        data = self.kwargs.get('data', {})
        param = list(data.keys())
        if set(param) - set(self.email_data.email_valid_param_list):
            # invalid param given
            return 400, self.email_data.email_error[400]
        return 204, None

    def delete_destination_email(self):
        return 204, None

    def test_destination_email(self):
        return 204, None
