# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" NFS Server Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

MODIFY_PARAMS = {
    "host_name": "stringa",
    "is_nfsv3_enabled": False,
    "is_nfsv4_enabled": True,
    "is_secure_enabled": False,
    "is_skip_unjoin": True,
    "is_use_smb_config_enabled": True,
    "is_extended_credentials_enabled": True,
    "credentials_cache_TTL": 20
}

CREATE_PARAMS = {
    "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
    "host_name": "string",
    "is_nfsv3_enabled": True,
    "is_nfsv4_enabled": False,
    "is_secure_enabled": False,
    "is_use_smb_config_enabled": True,
    "is_extended_credentials_enabled": False,
    "credentials_cache_TTL": 15
}

# create NFS server
NFS_SERVER = CONN.nfs_server.create_nfs_server(CREATE_PARAMS)
print(NFS_SERVER)

# Get NFS servers list
NFS_SERVERS = CONN.nfs_server.get_nfs_server_list(all_pages=True)
print(NFS_SERVERS)

# get NFS server details by ID
NFS_SERVER = CONN.nfs_server.get_nfs_server_details(NFS_SERVER['id'])
print(NFS_SERVER)

# get NFS server details by NAS server
NFS_SERVER = CONN.nfs_server.get_nfs_server_by_nas_server_id(
    CREATE_PARAMS['nas_server_id'])
print(NFS_SERVER)

# modify NFS server
MODIFY_NFS_SERVER = CONN.nfs_server.modify_nfs_server(NFS_SERVER[0]['id'],
                                                      MODIFY_PARAMS)
print(MODIFY_NFS_SERVER)

# delete NFS server
DELETE_NFS_SERVER = CONN.nfs_server.delete_nfs_server(NFS_SERVER[0]['id'])
print(DELETE_NFS_SERVER)
