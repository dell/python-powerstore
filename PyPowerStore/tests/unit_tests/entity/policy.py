from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.tests.unit_tests.common_data import CommonData


class PolicyResponse(Entity):

    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_api_name(self):
        if self.method == 'GET':
            if self.url.endswith('/policy'):
                if self.kwargs.get('params', {}).get('name'):
                    return self.get_protection_policy_by_name
                else:
                    return self.get_policies
            else:
                return self.get_protection_policy_details
        elif self.method == "POST":
            return self.create_protection_policy
        elif self.method == "PATCH":
            return self.modify_protection_policy
        elif self.method == "DELETE":
            return self.delete_protection_policy

    def execute_api(self, api_name):
        status_code, response = api_name()
        return status_code, response

    def get_policies(self):
        return self.status_code, self.data.pol_list

    def get_protection_policy_by_name(self):
        return self.status_code, [self.data.protection_policy1]

    def get_protection_policy_details(self):
        return self.status_code, self.data.protection_policy1

    def create_protection_policy(self):
        return 201, self.data.protection_policy1

    def modify_protection_policy(self):
        if 'add_snapshot_rule_ids' in self.kwargs['data'] and\
                self.kwargs['data']['add_snapshot_rule_ids'][0] == \
                self.data.invalid_sr_id:
            return 404, self.data.add_invalid_sr_error[404]
        elif 'remove_snapshot_rule_ids' in self.kwargs['data'] and\
                self.kwargs['data']['remove_snapshot_rule_ids'][0] == \
                self.data.invalid_sr_id:
            return 404, self.data.remove_invalid_sr_error[404]
        return 204, self.data.protection_policy1_modified

    def delete_protection_policy(self):
        return 204, None
