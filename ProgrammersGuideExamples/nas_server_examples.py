# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dell Technologies

""" NAS Server Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

MODIFY_PARAMS = {
    'description': 'My Description',
    'current_unix_directory_service': 'Local_Files',
    'protection_policy_id': 'samplepolicyid'
}

# Get nasserver list
NAS_SERVERS = CONN.provisioning.get_nas_servers(all_pages=True)
print(NAS_SERVERS)

# get nasserver details by ID
NAS_SERVER = CONN.provisioning.get_nas_server_details(NAS_SERVERS[0]['id'])
print(NAS_SERVER)

# get nasserver details by NAME
NAS_SERVER = CONN.provisioning.get_nas_server_by_name(NAS_SERVERS[0]['name'])
print(NAS_SERVER)

# modify nasserver
MODIFY_NAS = CONN.provisioning.modify_nasserver(NAS_SERVER[0]['id'],
                                                MODIFY_PARAMS)
print(MODIFY_NAS)
