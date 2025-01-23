from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class JobResponse(Entity):
    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == "GET":
            return self.get_job_details

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_job_details(self):
        if self.url.endswith(f"/job/{self.data.job_does_not_exist}"):
            return 404, self.data.job_error[404]
        return self.status_code, self.data.job_details
