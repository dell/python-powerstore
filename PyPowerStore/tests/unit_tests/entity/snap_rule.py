from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.data.common_data import CommonData


class SnapRuleResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/snapshot_rule'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_snapshot_rule_by_name
                else:
                    return self.get_snap_rules
            else:
                return self.get_snapshot_rule_details
        elif self.method == 'POST':
            return self.create_snapshot_rule
        elif self.method == "PATCH":
            return self.modify_snapshot_rule
        elif self.method == "DELETE":
            return self.delete_snapshot_rule

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_snap_rules(self):
        return self.status_code, self.data.snap_rule_list

    def get_snapshot_rule_details(self):
        return self.status_code, self.data.snap_rule1

    def get_snapshot_rule_by_name(self):
        return self.status_code, [self.data.snap_rule1]

    def create_snapshot_rule(self):
        return 201, self.data.snap_rule1

    def modify_snapshot_rule(self):
        if 'interval' in self.kwargs['data'] and \
                self.kwargs['data']['interval'] == self.data.invalid_interval:
            return 400, self.data.interval_error[400]
        return 204, self.data.snap_rule1_modified

    def delete_snapshot_rule(self):
        return 204, None
