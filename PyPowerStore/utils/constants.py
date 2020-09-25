# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Module for PowerStore constants"""

# HTTP constants
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
PATCH = 'PATCH'

# Default Connection Timeout in seconds
TIMEOUT = 120.0

# Pagination Constants
# offset is 0 and limit is 99 for first request
# offset for second request
OFFSET = 100
# max number of items limit in a response
MAX_LIMIT = 2000

# Query params

SELECT_ALL_VOLUME = {"select": "id,name,description,type,wwn,appliance_id,"
                               "state,size,creation_timestamp,"
                               "protection_policy_id,performance_policy_id,"
                               "protection_policy(name,id),"
                               "performance_policy(name,id),"
                               "is_replication_destination,"
                               "migration_session_id,"
                               "protection_data,location_history,type_l10n,"
                               "state_l10n,host_group(name,id),host(name,id),"
                               "volume_groups(name,id)"
                     }
SELECT_ALL_HOST = {"select": "id,name,description,os_type,"
                             "host_group_id,"
                             "host_initiators,os_type_l10n"
                   }

SELECT_ALL_HOST_GROUP = {"select": "name,id,description,hosts(id,name)"}

SELECT_ALL_VG = {"select": "id,name,description,creation_"
                           "timestamp, member_type,"
                           "is_protectable, protection_policy_id,"
                           "migration_session_id,"
                           "is_write_order_consistent,"
                           "placement_rule,type,"
                           "is_replication_destination,protection_data,"
                           "is_importing,location_history,"
                           "member_type_l10n,type_l10n,volumes"}

SELECT_ALL_VOL_GROUP = {"select": "id,name,description,creation_"
                                  "timestamp,"
                                  "is_protectable, protection_policy_id,"
                                  "protection_policy(name,id),"
                                  "migration_session_id,"
                                  "is_write_order_consistent,"
                                  "placement_rule,type,"
                                  "is_replication_destination,protection_data,"
                                  "is_importing,location_history,"
                                  "type_l10n,volumes(name,id)"}

SELECT_ID_AND_NAME = {"select": "id,name"}
SELECT_ID_AND_PATH = {"select": "id,path"}
SELECT_ALL_HOST_VOLUME_MAPPING = {"select": "id, host_id, host_group_id,"
                                            "logical_unit_number"}

SELECT_ALL_FILESYSTEM = {"select": "id,name, description,"
                         "parent_id, filesystem_type, size_total,size_used,"
                         "access_policy,locking_policy,"
                         "folder_rename_policy, is_smb_sync_writes_enabled,"
                         "is_smb_op_locks_enabled, is_smb_no_notify_enabled,"
                         "is_smb_notify_on_access_enabled,"
                         "is_smb_notify_on_write_enabled,"
                         "smb_notify_on_change_dir_depth,"
                         "is_async_MTime_enabled, is_quota_enabled,"
                         "grace_period, default_hard_limit,"
                         "default_soft_limit, creation_timestamp,"
                         "expiration_timestamp, last_refresh_timestamp,"
                         "last_writable_timestamp, is_modified,access_type,"
                         "creator_type, filesystem_type_l10n,"
                         "access_policy_l10n, locking_policy_l10n,"
                         "folder_rename_policy_l10n, access_type_l10n,"
                         "creator_type_l10n,nas_server(name,id),"
                         "protection_policy(name,id)"}

SELECT_ALL_NAS_SERVER = {"select": "id,name, description, operational_status,"
                         "current_node_id,preferred_node_id,"
                         "default_unix_user,default_windows_user,"
                         "current_unix_directory_service,"
                         "is_username_translation_enabled,"
                         "is_auto_user_mapping_enabled,"
                         "production_IPv4_interface_id,"
                         "production_IPv6_interface_id,"
                         "backup_IPv4_interface_id,"
                         "backup_IPv6_interface_id,"
                         "current_preferred_IPv4_interface_id,"
                         "current_preferred_IPv6_interface_id,"
                         "operational_status_l10n,"
                         "current_unix_directory_service_l10n,"
                         "file_interfaces(name,id,ip_address),"
                         "nfs_servers,smb_servers,"
                         "file_ldaps,file_nises,file_systems(id,name)"
                         }

SELECT_ALL_SMB_SHARE = {"select": "id,name,path,description,umask,"
                                  "is_continuous_availability_enabled,"
                                  "is_encryption_enabled,"
                                  "is_ABE_enabled,is_branch_cache_enabled,"
                                  "offline_availability,"
                                  "file_system(id,name,filesystem_type,"
                                  "nas_server(id,name))"}


# Select all tree quota

SELECT_ALL_TREE_QUOTA = {"select": "id,path,description,"
                                   "is_user_quotas_enforced,state,"
                                   "hard_limit,soft_limit,"
                                   "remaining_grace_period,size_used,"
                                   "file_system(id,name,filesystem_type,"
                                   "nas_server(id,name))"}
# Select all user quota
SELECT_ALL_USER_QUOTA = {"select": "id,tree_quota_id,uid,unix_name,"
                                   "windows_name,windows_sid,state,"
                                   "hard_limit,soft_limit,"
                                   "remaining_grace_period,size_used,"
                                   "state_l10n,file_system(id,name,"
                                   "filesystem_type,nas_server(id,name)),"
                                   "tree_quota(path,description,hard_limit,"
                                   "soft_limit,remaining_grace_period,"
                                   "size_used)"}

# Select All NFS Export
SELECT_ALL_NFS_EXPORT = {"select": "id, name, file_system(id, name, "
                                   "filesystem_type, nas_server(id, name)), "
                                   "path, description, default_access, "
                                   "min_security, nfs_owner_username, "
                                   "no_access_hosts, read_only_hosts, "
                                   "read_only_root_hosts, read_write_hosts, "
                                   "read_write_root_hosts, anonymous_UID, "
                                   "anonymous_GID, is_no_SUID, "
                                   "default_access_l10n, min_security_l10n"}

# Select all Snapshot

EQUALS = 'eq.'

# API endpoints

# Volume endpoints
VOLUME_CREATE_URL = 'https://{0}/api/rest/volume'
GET_VOLUME_LIST_URL = VOLUME_CREATE_URL
GET_VOLUME_DETAILS_URL = 'https://{0}/api/rest/volume/{1}'
MODIFY_VOLUME_URL = 'https://{0}/api/rest/volume/{1}'
DELETE_VOLUME_URL = MODIFY_VOLUME_URL
MAP_VOLUME_TO_HOST_URL = 'https://{0}/api/rest/volume/{1}/attach'
UNMAP_VOLUME_FROM_HOST_URL = 'https://{0}/api/rest/volume/{1}/detach'
RESTORE_VOLUME_FROM_SNAPSHOT_URL = 'https://{0}/api/rest/volume/{1}/restore'
GET_VOLUME_BY_NAME_URL = VOLUME_CREATE_URL
CREATE_VOLUME_SNAPSHOT_URL = 'https://{0}/api/rest/volume/{1}/snapshot'

# Host endpoints
GET_HOST_LIST_URL = 'https://{0}/api/rest/host'
GET_HOST_DETAILS_URL = 'https://{0}/api/rest/host/{1}'
CREATE_HOST_URL = GET_HOST_LIST_URL
MODIFY_HOST_URL = 'https://{0}/api/rest/host/{1}'
DELETE_HOST_URL = MODIFY_HOST_URL
ATTACH_HOST_URL = 'https://{0}/api/rest/host/{1}/attach'
DETACH_HOST_URL = 'https://{0}/api/rest/host/{1}/detach'
GET_HOST_BY_NAME_URL = GET_HOST_LIST_URL

# Hostgroup endpoints
GET_HOST_GROUP_LIST_URL = 'https://{0}/api/rest/host_group'
CREATE_HOST_GROUP_URL = GET_HOST_GROUP_LIST_URL
GET_HOST_GROUP_DETAILS_URL = 'https://{0}/api/rest/host_group/{1}'
MODIFY_HOST_GROUP_URL = GET_HOST_GROUP_DETAILS_URL
DELETE_HOST_GROUP_URL = GET_HOST_GROUP_DETAILS_URL
GET_HOST_GROUP_BY_NAME_URL = 'https://{0}/api/rest/host_group'
GET_HOSTS_BY_HOST_GROUP = GET_HOST_GROUP_LIST_URL

# Volume Group Endpoints

GET_VOLUME_GROUP_LIST_URL = 'https://{0}/api/rest/volume_group'
CREATE_VOLUME_GROUP_URL = GET_VOLUME_GROUP_LIST_URL
GET_VOLUME_GROUP_DETAILS_URL = 'https://{0}/api/rest/volume_group/{1}'
MODIFY_VOLUME_GROUP_URL = GET_VOLUME_GROUP_DETAILS_URL
DELETE_VOLUME_GROUP_URL = GET_VOLUME_GROUP_DETAILS_URL
ADD_MEMBERS_TO_VOLUME_GROUP_URL = \
    'https://{0}/api/rest/volume_group/{1}/add_members'
REMOVE_MEMBERS_FROM_VOLUME_GROUP_URL = \
    'https://{0}/api/rest/volume_group/{1}/remove_members'
GET_VOLUME_GROUP_BY_NAME_URL = GET_VOLUME_GROUP_LIST_URL
GET_VOLUMES_FROM_VOLUME_GROUP = GET_VOLUME_GROUP_LIST_URL
CREATE_VOLUME_GROUP_SNAPSHOT_URL = \
    'https://{0}/api/rest/volume_group/{1}/snapshot'

# Cluster endpoints
GET_CLUSTER = 'https://{0}/api/rest/cluster'

# Node endpoints
GET_NODE = 'https://{0}/api/rest/node'

# Snapshot Rule endpoints
SNAPSHOT_RULE_LIST_URL = 'https://{0}/api/rest/snapshot_rule'
SNAPSHOT_RULE_OBJECT_URL = 'https://{0}/api/rest/snapshot_rule/{1}'

# Protection Policy endpoint
PROTECTION_POLICY_LIST_URL = 'https://{0}/api/rest/policy'
PROTECTION_POLICY_OBJECT_URL = 'https://{0}/api/rest/policy/{1}'

# Host Volume Mapping enpoints
HOST_VOLUME_MAPPING_URL = 'https://{0}/api/rest/host_volume_mapping'

# NAS Server endpoints
GET_NAS_SERVER_LIST_URL = 'https://{0}/api/rest/nas_server'
GET_NAS_SERVER_DETAILS_URL = 'https://{0}/api/rest/nas_server/{1}'
GET_NAS_SERVER_DETAILS_BY_NAME_URL = GET_NAS_SERVER_LIST_URL
MODIFY_NAS_SERVER_URL = GET_NAS_SERVER_DETAILS_URL

# NFS Export endpoints
GET_NFS_EXPORT_LIST_URL = 'https://{0}/api/rest/nfs_export'
GET_NFS_EXPORT_DETAILS_URL = 'https://{0}/api/rest/nfs_export/{1}'
GET_NFS_EXPORT_DETAILS_BY_NAME_URL = GET_NFS_EXPORT_LIST_URL
CREATE_NFS_EXPORT_URL = GET_NFS_EXPORT_LIST_URL
MODIFY_NFS_EXPORT_URL = GET_NFS_EXPORT_DETAILS_URL
DELETE_NFS_EXPORT_URL = GET_NFS_EXPORT_DETAILS_URL

# SMB Share endpoints
GET_SMB_SHARE_LIST_URL = 'https://{0}/api/rest/smb_share'
CREATE_SMB_SHARE_URL = GET_SMB_SHARE_LIST_URL
GET_SMB_SHARE_DETAILS_URL = 'https://{0}/api/rest/smb_share/{1}'
MODIFY_SMB_SHARE_URL = GET_SMB_SHARE_DETAILS_URL
DELETE_SMB_SHARE_URL = GET_SMB_SHARE_DETAILS_URL

# File Tree Quota endpoints
GET_TREE_QUOTA_LIST_URL = 'https://{0}/api/rest/file_tree_quota'
CREATE_TREE_QUOTA_URL = GET_TREE_QUOTA_LIST_URL
GET_TREE_QUOTA_DETAILS_URL = 'https://{0}/api/rest/file_tree_quota/{1}'
MODIFY_TREE_QUOTA_URL = GET_TREE_QUOTA_DETAILS_URL
DELETE_TREE_QUOTA_URL = GET_TREE_QUOTA_DETAILS_URL

# File User Quota endpoints
GET_USER_QUOTA_LIST_URL = 'https://{0}/api/rest/file_user_quota'
CREATE_USER_QUOTA_URL = GET_USER_QUOTA_LIST_URL
GET_USER_QUOTA_DETAILS_URL = 'https://{0}/api/rest/file_user_quota/{1}'
MODIFY_USER_QUOTA_URL = GET_USER_QUOTA_DETAILS_URL

# File System endpoints
GET_FILE_SYSTEM_LIST_URL = 'https://{0}/api/rest/file_system'
GET_FILESYSTEM_DETAILS_URL = 'https://{0}/api/rest/file_system/{1}'
GET_FILESYSTEM_DETAILS_BY_NAME_URL = GET_FILE_SYSTEM_LIST_URL
CREATE_FILESYSTEM_URL = GET_FILESYSTEM_DETAILS_BY_NAME_URL
DELETE_FILESYSTEM_URL = GET_FILESYSTEM_DETAILS_URL

MODIFY_FILESYSTEM_URL = GET_FILESYSTEM_DETAILS_URL
CREATE_FILESYSTEM_SNAPSHOT_URL = 'https://{0}/api/rest/file_system/{1}/' \
                                 'snapshot'

GET_SNAPSHOTS_FILESYSTEM_URL = GET_FILE_SYSTEM_LIST_URL
