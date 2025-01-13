# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" Remote Support Contact operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<server_ip>",
                                      verify=False,
                                      timeout=180.0)

# Getting Remote Support Contact configurations
remote_support_contact_list = CONN.config_mgmt.get_remote_support_contact_list()
print(remote_support_contact_list)

# Getting Remote Support Contact instance details
remote_support_contact_details = CONN.config_mgmt.get_remote_support_contact_details(
    remote_support_contact_id=remote_support_contact_list[0]['id'])
print(remote_support_contact_details)

# Modifying the Remote Support Contact details
modify_dict = {
    "first_name": "abc",
    "last_name": "xyz",
    "email": "abc_xyz@dell.com",
    "phone": "111-222-333-444"
}

resp_modify = CONN.config_mgmt.modify_remote_support_contact_details(
    remote_support_contact_id=remote_support_contact_list[0]['id'], modify_parameters=modify_dict)
print(resp_modify)
