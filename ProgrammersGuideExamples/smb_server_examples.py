# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" SMB Server Operations"""
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
    "is_standalone": False,
    "computer_name": "string",
    "domain": "string",
    "netbios_name": "string",
    "workgroup": "string",
    "description": "string",
    "local_admin_password": "string",
}

CREATE_PARAMS = {
    "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
    "is_standalone": False,
    "computer_name": "string",
    "domain": "string",
    "netbios_name": "string",
    "workgroup": "string",
    "description": "string",
    "local_admin_password": "string",
}

# create SMB server
SMB_SERVER = CONN.smb_server.create_smb_server(CREATE_PARAMS)
print(SMB_SERVER)

# Get SMB servers list
SMB_SERVERS = CONN.smb_server.get_smb_server_list(all_pages=True)
print(SMB_SERVERS)

# get SMB server details by ID
SMB_SERVER = CONN.smb_server.get_smb_server_details(SMB_SERVER["id"])
print(SMB_SERVER)

# get SMB server details by NAS server
SMB_SERVER = CONN.smb_server.get_smb_server_by_nas_server_id(
    CREATE_PARAMS["nas_server_id"]
)
print(SMB_SERVER)

# modify SMB server
MODIFY_SMB_SERVER = CONN.smb_server.modify_smb_server(
    SMB_SERVER[0]["id"], MODIFY_PARAMS
)
print(MODIFY_SMB_SERVER)

# delete SMB server
DELETE_SMB_SERVER = CONN.smb_server.delete_smb_server(SMB_SERVER[0]["id"])
print(DELETE_SMB_SERVER)
