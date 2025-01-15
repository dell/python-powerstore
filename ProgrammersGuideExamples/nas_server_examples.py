# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" NAS Server Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
    timeout=180.0,
)
print(CONN)

MODIFY_PARAMS = {
    "description": "My Description",
    "current_unix_directory_service": "Local_Files",
    "protection_policy_id": "samplepolicyid",
}

CREATE_PARAMS = {
    "name": "test server",
    "current_unix_directory_service": "LDAP",
    "default_unix_user": "test-user",
    "is_username_translation_enabled": True,
    "is_auto_user_mapping_enabled": True,
}

# create nasserver
NAS_SERVER = CONN.provisioning.create_nasserver(CREATE_PARAMS)
print(NAS_SERVER)

# Get nasserver list
NAS_SERVERS = CONN.provisioning.get_nas_servers(all_pages=True)
print(NAS_SERVERS)

# get nasserver details by ID
NAS_SERVER = CONN.provisioning.get_nas_server_details(NAS_SERVERS[0]["id"])
print(NAS_SERVER)

# get nasserver details by NAME
NAS_SERVER = CONN.provisioning.get_nas_server_by_name(NAS_SERVERS[0]["name"])
print(NAS_SERVER)

# modify nasserver
MODIFY_NAS = CONN.provisioning.modify_nasserver(NAS_SERVER[0]["id"], MODIFY_PARAMS)
print(MODIFY_NAS)

# delete nasserver
DELETE_NAS = CONN.provisioning.delete_nasserver(NAS_SERVER[0]["id"])
print(DELETE_NAS)
