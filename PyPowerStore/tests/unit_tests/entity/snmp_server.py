from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.snmp_server_data import SNMPServerData


class SNMPServerResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.snmp_server_data = SNMPServerData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/snmp_server"):
                return self.get_snmp_server_list
            return self.get_snmp_server_details
        if self.method == "PATCH":
            return self.modify_snmp_server
        if self.method == "POST":
            return self.create_snmp_server
        if self.method == "DELETE":
            return self.delete_snmp_server

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_snmp_server_list(self):
        return self.status_code, self.snmp_server_data.snmp_server_list

    def get_snmp_server_details(self):
        if self.url.endswith(
            "/snmp_server/{0}".format(self.snmp_server_data.snmp_server_id_not_exist)
        ):
            return 422, self.snmp_server_data.snmp_server_error[422]
        return 200, self.snmp_server_data.snmp_server_detail

    def modify_snmp_server(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.snmp_server_data.snmp_server_valid_param_list):
            # invalid param given
            return 400, self.snmp_server_data.snmp_server_error[400]
        return 204, None

    def create_snmp_server(self):
        return 201, self.snmp_server_data.snmp_server_id

    def delete_snmp_server(self):
        return 204, None
