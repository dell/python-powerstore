# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell Technologies

""" Local User Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)

print(CONN)

# Get users list
local_users_list = CONN.config_mgmt.get_local_users()
print(local_users_list)

# Get local user details by name
local_user_details_by_name = CONN.config_mgmt.get_local_user_by_name(name=local_users_list[0]['name'])
print(local_user_details_by_name)

# Get local user details by ID
local_user_details = CONN.config_mgmt.get_local_user_details(user_id=local_users_list[0]['id'])
print(local_user_details)

# Create a local user
create_params = {
    "name": "<<local user name>>",
    "password":"<<local user passoword>>",
    "role_id":"3"
}
local_user = CONN.config_mgmt.create_local_user(create_params=create_params)
print(local_user)

# Modify a local user
modify_parameters = {
    'role_id': "4",
    'is_locked': False,
    'current_password': "<<local user passoword>>",
    'password': "<<New local user passoword>>"
}
updated_local_user = CONN.config_mgmt.modify_local_user(local_user_id=local_user['id'], modify_parameters=modify_parameters)
print(updated_local_user)

# Delete local user
deleted_local_user_resp = CONN.config_mgmt.delete_local_user(user_id=local_user['id'])
print(deleted_local_user_resp)
