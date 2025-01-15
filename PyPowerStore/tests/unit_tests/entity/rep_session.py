from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class RepSessionResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            if self.url.endswith("/replication_session"):
                return self.get_replication_sessions
            return self.get_replication_session_details
        if self.method == "POST":
            if self.url.endswith("/sync"):
                return self.sync_replication_session
            if self.url.endswith("/pause"):
                return self.pause_replication_session
            if self.url.endswith("/resume"):
                return self.resume_replication_session
            if self.url.endswith("/failover"):
                return self.failover_replication_session
            if self.url.endswith("/reprotect"):
                return self.reprotect_replication_session
        elif self.method == "PATCH":
            return self.modify_replication_session

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_replication_sessions(self):
        return self.status_code, self.data.rep_session_list

    def get_replication_session_details(self):
        if self.url.endswith(
            "/replication_session/{0}".format(self.data.nas_id_not_exist)
        ):
            return 404, self.data.rep_session_error[404]
        return 200, self.data.rep_session_details_1

    def sync_replication_session(self):
        return 204, None

    def pause_replication_session(self):
        return 204, None

    def resume_replication_session(self):
        return 204, None

    def failover_replication_session(self):
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.rep_session_valid_param):
            # invalid param given
            return 400, self.data.rep_session_error[400]
        if self.url.endswith(
            "/replication_session/{0}".format(self.data.rep_session_id_not_exist)
        ):
            return 404, self.data.rep_session_error[404]
        return 204, None

    def reprotect_replication_session(self):
        return 204, None

    def modify_replication_session(self):
        return 204, None
