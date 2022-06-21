# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dell Technologies

""" File System Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

FS_NAME = "sample_fs"
NAS_ID = "5f4a3017-0bad-899e-e1eb-c6f547282e76"
SIZE = 3221225472
ADV_PARAM = {}

# Create filesystem
FS = CONN.provisioning.create_filesystem(FS_NAME, NAS_ID, SIZE, ADV_PARAM)
print(FS)

# Get filesystem list
filter_dict = {'name': 'eq.{0}'.format(FS_NAME)}
FS_LIST = CONN.provisioning.get_file_systems(filter_dict=filter_dict)
print(FS_LIST)

# Get filesystem details by ID
FS_DETAIL = CONN.provisioning.get_filesystem_details(FS_LIST[0]['id'])
print(FS_DETAIL)

# Get filesystem details by name
FS_DETAIL = CONN.provisioning.get_filesystem_by_name(
    FS_LIST[0]['name'], NAS_ID)
print(FS_DETAIL)

# Modify filesystem
MODIFY_FS_PARAM = {
    "description": "My Description",
    # Grace period of soft limits (seconds)
    "grace_period": 1209600,
    # hard limit of quotas (bytes)
    "default_hard_limit": 2147483648,
    # Lowest directory level to which the enabled notifications apply, if any
    "smb_notify_on_change_dir_depth": 3,
    # hard limit of quotas (bytes)
    "default_soft_limit": 1073741824
}
MODIFY_FS = CONN.provisioning.modify_filesystem(FS['id'], MODIFY_FS_PARAM)
print(MODIFY_FS)

# Create filesystem snapshot
FS_SNAP = CONN.protection.create_filesystem_snapshot(FS["id"])
print(FS_SNAP)

# Get snapshots of a filesystem
FS_SNAPS = CONN.provisioning.get_snapshots_filesystem(FS['id'])
print(FS_SNAPS)

# Get filesystem snapshot details by ID
FS_SNAP_DETAIL = CONN.protection.get_filesystem_snapshot_details(FS_SNAP['id'])
print(FS_SNAP_DETAIL)

# Get filesystem snapshot details by name
FS_SNAP_DETAIL = CONN.protection.get_filesystem_snapshot_details_by_name(
    FS_SNAP_DETAIL['name'], nas_server_id=NAS_ID)
print(FS_SNAP_DETAIL)

# Modify filesystem snapshot
MODIFY_FS_SNAP = CONN.protection.modify_filesystem_snapshot(
    FS_SNAP['id'], description="My Description")
print(MODIFY_FS_SNAP)

# Delete filesystem snapshot
DELETE_FS_SNAP = CONN.protection.delete_filesystem_snapshot(FS_SNAP['id'])
print(DELETE_FS_SNAP)

# Delete filesystem
DELETE_FS_SNAP = CONN.provisioning.delete_filesystem(FS['id'])
print(DELETE_FS_SNAP)
