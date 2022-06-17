# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dell Technologies

""" NFS Export Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

NFS_NAME = "sample_nfs"
FS_ID = "5f4e57d3-2f6e-5fb4-3ac9-c6f547282e76"
PATH = "/sample_fs"
OTHER_PARAM = {'description': 'Description'}

# Create nfsexport
NFS = CONN.provisioning.create_nfs_export(FS_ID, PATH, NFS_NAME, OTHER_PARAM)
print(NFS)

# Get nfsexport list
filter_dict = {'name': 'eq.{0}'.format(NFS_NAME)}
NFS_LIST = CONN.provisioning.get_nfs_exports(filter_dict=filter_dict)
print(NFS_LIST)

# Get nfsexport details by ID
NFS_DETAIL = CONN.provisioning.get_nfs_export_details(NFS['id'])
print(NFS_DETAIL)

# Get nfsexport details by name
NFS_DETAIL = CONN.provisioning.get_nfs_export_details_by_name(NFS_NAME)
print(NFS_DETAIL)

# modify nfsexport
MODIFY_PARAM = {"description": "My Description", "default_access": "Root"}
MODIFY_NFS = CONN.provisioning.modify_nfs_export(NFS['id'], MODIFY_PARAM)
print(MODIFY_NFS)

DELETE_NFS = CONN.provisioning.delete_nfs_export(NFS['id'])
print(DELETE_NFS)
