from PyPowerStore.tests.unit_tests.data.file_dns_data import FileDNSData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class FileDNSResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.file_dns_data = FileDNSData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/file_dns"):
                return self.get_file_dns_list
            return self.get_file_dns_details
        if self.method == "PATCH":
            return self.modify_file_dns
        if self.method == "POST":
            return self.create_file_dns
        if self.method == "DELETE":
            return self.delete_file_dns

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_file_dns_list(self):
        return self.status_code, self.file_dns_data.file_dns_list

    def get_file_dns_details(self):
        if self.url.endswith(
            "/file_dns/{0}".format(self.file_dns_data.file_dns_id_not_exist)
        ):
            return 404, self.file_dns_data.file_dns_error[404]
        return 200, self.file_dns_data.file_dns_detail

    def modify_file_dns(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.file_dns_data.file_dns_valid_param_list):
            # invalid param given
            return 400, self.file_dns_data.file_dns_error[400]
        return 204, None

    def create_file_dns(self):
        return 201, self.file_dns_data.file_dns_id

    def delete_file_dns(self):
        return 204, None
