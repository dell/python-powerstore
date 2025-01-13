from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData

class RepRuleResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/replication_rule'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_replication_rule_by_name
                return self.get_replication_rules
            return self.get_replication_rule_details
        if self.method == 'POST':
            return self.create_replication_rule
        if self.method == "PATCH":
            return self.modify_replication_rule
        if self.method == "DELETE":
            return self.delete_replication_rule

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_replication_rules(self):
        return self.status_code, self.data.rep_rule_list

    def get_replication_rule_details(self):
        return self.status_code, self.data.rep_rule_details_1

    def get_replication_rule_by_name(self):
        return self.status_code, [self.data.rep_rule_details_1]

    def create_replication_rule(self):
        return 201, self.data.snap_rule1

    def modify_replication_rule(self):
        if 'alert_threshold' in self.kwargs['data'] and \
                self.kwargs['data']['alert_threshold'] ==\
                self.data.invalid_alert_threshold:
            return 400, self.data.rep_rule_error[400]
        return 204, self.data.rep_rule_details_1

    def delete_replication_rule(self):
        return 204, None
