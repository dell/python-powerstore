# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell Technologies

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

# Volume Query
SELECT_ALL_VOLUME = {"select": "id,name,description,type,wwn,appliance_id,"
                               "state,size,creation_timestamp,"
                               "protection_policy_id,performance_policy_id,"
                               "protection_policy(name,id),"
                               "performance_policy(name,id),"
                               "is_replication_destination,"
                               "migration_session_id,"
                               "protection_data,location_history,type_l10n,"
                               "state_l10n,host_group(name,id),host(name,id),"
                               "volume_groups(name,id),"
                               "mapped_volumes(id,logical_unit_number)"
                     }
FHC_VOLUME_DETAILS_QUERY = {
    "select": "id,name,description,type,wwn,appliance_id,state,size,"
              "creation_timestamp,protection_policy_id,performance_policy_id,"
              "protection_policy(name,id),performance_policy(name,id),"
              "is_replication_destination,migration_session_id,"
              "protection_data,location_history,type_l10n,state_l10n,"
              "host_group(name,id),host(name,id),volume_groups(name,id),"
              "mapped_volumes(id,logical_unit_number),nsid,nguid,"
              "node_affinity,node_affinity_l10n"
}

FHP_VOLUME_DETAILS_QUERY = {
    "select": "id,name,description,type,wwn,appliance_id,state,size,"
              "creation_timestamp,protection_policy_id,performance_policy_id,"
              "protection_policy(name,id),performance_policy(name,id),"
              "is_replication_destination,logical_used,"
              "protection_data,location_history,type_l10n,state_l10n,"
              "host_group(name,id),volume_groups(name,id),"
              "mapped_volumes(id,logical_unit_number),nsid,nguid,"
              "node_affinity,node_affinity_l10n,metro_replication_session_id,"
              "is_host_access_available,app_type,app_type_other,app_type_l10n,"
              "migration_session_id"
}

# Host Query
SELECT_ALL_HOST = {"select": "id,name,description,os_type,"
                             "host_group_id,"
                             "host_initiators,os_type_l10n,"
                             "mapped_hosts(id,logical_unit_number,"
                             "host_group(id,name),volume(id,name))"
                   }
FHC_HOST_DETAILS_QUERY = {
    "select": "id,name,description,os_type,host_group_id,host_initiators,"
              "os_type_l10n,mapped_hosts(id,logical_unit_number,"
              "host_group(id,name),volume(id,name)),type,type_l10n"
}
FHP_HOST_DETAILS_QUERY = {
    "select": "id,name,description,type,os_type,host_group_id,"
              "host_connectivity,os_type_l10n,"
              "mapped_hosts(id,logical_unit_number,host_group(id,name),"
              "volume(id,name)),type_l10n,host_connectivity_l10n,"
              "initiators(id,port_name,port_type,chap_single_username,"
              "chap_mutual_username,active_sessions),host_initiators"
}

SELECT_ALL_HOST_GROUP = {"select": "name,id,description,hosts(id,name)"}
FHP_HOST_GROUP_QUERY = {"select": "name,id,description,hosts(id,name),"
                                  "host_connectivity,host_connectivity_l10n,"
                                  "mapped_host_groups(id,volume_id,"
                                  "logical_unit_number)"}

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
# For getting the list of appliances (mentioned in configuration.py)
SELECT_ID_NAME_AND_MODEL = {"select": "id,name,model"}
SELECT_ID = {"select": "id"}
SELECT_ID_AND_ADDRESS = {"select": "id,email_address"}
SELECT_VERSION = {"select": "release_version"}
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


FHP_NAS_QUERYSTRING = {"select": "id,name, description, operational_status,"
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
                       "protection_policy_id,"
                       "operational_status_l10n,"
                       "current_unix_directory_service_l10n,"
                       "file_interfaces(name,id,ip_address),"
                       "nfs_servers,smb_servers,"
                       "file_ldaps,file_nises,file_systems(id,name)"
                       "file_events_publishing_mode,"
                       "is_replication_destination,"
                       "is_production_mode_enabled,"
                       "current_unix_directory_service_l10n,"
                       "file_events_publishing_mode_l10n"}
                       
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

# SELECT JOB DETAILS
JOB_DETAILS_QUERY = {
    'select': 'id,resource_action,resource_type,resource_id,resource_name,'
              'description_l10n,state,start_time,phase,end_time,'
              'estimated_completion_time,progress_percentage,parent_id,'
              'root_id,user,response_body,step_order,'
              'resource_action_l10n,resource_type_l10n,state_l10n,phase_l10n'
}
FHC_JOB_DETAILS_QUERY = {
    'select': 'id,resource_action,resource_type,resource_id,resource_name,'
              'description_l10n,state,start_time,phase,end_time,'
              'estimated_completion_time,progress_percentage,parent_id,'
              'root_id,user,response_body,response_status,step_order,'
              'resource_action_l10n,resource_type_l10n,state_l10n,phase_l10n,'
              'response_status_l10n'
}

# Select cluster details
CLUSTER_DETAILS_QUERY = {
    'select': 'id,global_id,name,management_address,'
              'storage_discovery_address,master_appliance_id,'
              'appliance_count,physical_mtu,is_encryption_enabled,'
              'compatibility_level,state,state_l10n'
}

# Network details
NETWORK_DETAILS_QUERY = {
    'select': 'id,type,ip_version,vlan_id,prefix_length,'
              'gateway,mtu,type_l10n,ip_version_l10n'
}

# Role details
ROLE_DETAILS_QUERY = {
    'select': 'id,name,is_built_in,description'
}

# IP pool details
IP_DETAILS_QUERY = {
    'select': 'id,network_id,ip_port_id,appliance_id,node_id,address,'
              'purposes,purposes_l10n'
}

# CHAP config details
CHAP_CONFIG_DETAILS_QUERY = {
    'select': 'id,mode,mode_l10n'
}

# Service config details
SERVICE_CONFIG_DETAILS_QUERY = {
    'select': 'id,appliance_id,is_ssh_enabled'
}

# Service user details
SERVICE_USER_DETAILS_QUERY = {
    'select': 'id,name,is_built_in,is_default_password'
}

# Local user details
LOCAL_USER_DETAILS_QUERY = {
    'select': 'id,name,is_built_in,is_locked,is_default_password,role_id'
}

# IP port details
IP_PORT_DETAILS_QUERY = {
    'select': 'id,partner_id,target_iqn,available_usages,current_usages,'
              'bond_id,eth_port_id,veth_port_id,available_usages_l10n,'
              'current_usages_l10n'
}

# vCenter details
VCENTER_DETAILS_QUERY = {
    'select': 'id,instance_uuid,address,username'
}

# Appliance details
APPLIANCE_DETAILS_QUERY = {
    'select': 'id,name,service_tag,express_service_code,model,nodes,'
              'veth_ports,maintenance_windows,fc_ports,sas_ports,eth_ports,'
              'software_installed,virtual_volumes,hardware,volumes,'
              'ip_pool_addresses'
}

# Remote System
REMOTE_SYSTEM_DETAILS_QUERY = {
    'select': 'id,name,description,serial_number,management_address,type,'
              'user_name,state,data_connection_state,iscsi_addresses,'
              'discovery_chap_mode,session_chap_mode,data_network_latency,'
              'data_connections,type_l10n,state_l10n,'
              'data_connection_state_l10n,discovery_chap_mode_l10n,'
              'session_chap_mode_l10n,data_network_latency_l10n,'
              'import_sessions,replication_sessions'
}
REMOTE_SYSTEM_FHP_DETAILS_QUERY = {
    'select': 'id,name,description,serial_number,version,management_address,'
              'management_port,type,user_name,state,data_connection_type,'
              'data_connection_state,iscsi_addresses,fc_target_wwns,'
              'discovery_chap_mode,session_chap_mode,data_network_latency,'
              'data_connections,capabilities,file_connection_address,'
              'file_connection_state,vnx_file_username,import_sessions,'
              'appliance_details,type_l10n,replication_sessions,'
              'state_l10n,data_connection_type_l10n,file_connection_state_l10n,'
              'data_connection_state_l10n,discovery_chap_mode_l10n,'
              'session_chap_mode_l10n,data_network_latency_l10n,'
              'capabilities_l10n,storage_container_destinations'
}

# Certificate details
CERTIFICATE_DETAILS_QUERY = {
    'select': 'id,type,type_l10n,service,service_l10n,scope,is_current,'
               'is_valid,members(subject,serial_number,signature_algorithm,'
               'issuer,valid_from,valid_to,public_key_algorithm,key_length,'
               'thumbprint_algorithm,thumbprint_algorithm_l10n,thumbprint,'
               'certificate,depth,subject_alternative_names)'
}

# Security config details
SECURITY_CONFIG_DETAILS_QUERY = {
    'select': 'id,idle_timeout,protocol_mode,protocol_mode_l10n'
}

# Email details
EMAIL_DETAILS_QUERY = {
     'select': 'id,email_address,notify_critical,notify_major,notify_minor,notify_info'
}

# SMTP details
SMTP_DETAILS_QUERY = {
      'select': 'id,address,port,source_email'
}

# DNS details
DNS_DETAILS_QUERY = {
      'select': 'id,addresses'
}
# NTP details
NTP_DETAILS_QUERY = {
    'select': 'id,addresses'
}

# Remote Support details
REMOTE_SUPPORT_DETAILS_QUERY = {
    'select': 'id,type,is_cloudiq_enabled,is_support_assist_license_accepted,'
              'is_rsc_enabled,connectivity_status,last_update,remote_support_servers,'
              'proxy_address,proxy_port,proxy_username,policy_manager_address,'
              'policy_manager_port,type_l10n,connectivity_status_l10n'
}

# Remote Support Contact details
REMOTE_SUPPORT_CONTACT_DETAILS_QUERY = {
    'select': 'id,email,first_name,last_name,phone'
}

# LDAP Domain details
LDAP_DOMAIN_DETAILS_QUERY = {
    'select': 'id,domain_name,ldap_servers,port,ldap_server_type,protocol,bind_user,ldap_timeout,'
              'is_global_catalog,user_id_attribute,user_object_class,user_search_path,'
              'group_name_attribute,group_member_attribute,group_object_class,'
              'group_search_path,group_search_level,ldap_server_type_l10n,protocol_l10n'
}
# LDAP Account details
LDAP_ACCOUNT_DETAILS_QUERY = {
    'select': 'id,role_id,domain_id,name,type,type_l10n,dn'
}
# Select all Snapshot

EQUALS = 'eq.'

# API endpoints

# Software version
GET_SOFTWARE_VERSION = 'https://{0}/api/rest/software_installed'

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
CLONE_VOLUME_URL = 'https://{0}/api/rest/volume/{1}/clone'
REFRESH_VOLUME_URL = 'https://{0}/api/rest/volume/{1}/refresh'
RESTORE_VOLUME_URL = 'https://{0}/api/rest/volume/{1}/restore'
CONFIGURE_METRO_VOLUME = 'https://{0}/api/rest/volume/{1}/configure_metro'
END_METRO_VOLUME = 'https://{0}/api/rest/volume/{1}/end_metro'

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
CLONE_VOLUME_GROUP_URL = 'https://{0}/api/rest/volume_group/{1}/clone'
REFRESH_VOLUME_GROUP_URL = 'https://{0}/api/rest/volume_group/{1}/refresh'
RESTORE_VOLUME_GROUP_URL = 'https://{0}/api/rest/volume_group/{1}/restore'
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

# Replication rule endpoints
REPLICATION_RULE_LIST_URL = 'https://{0}/api/rest/replication_rule'
REPLICATION_RULE_OBJECT_URL = 'https://{0}/api/rest/replication_rule/{1}'

# Replication session endpoints
REPLICATION_SESSION_LIST_URL = 'https://{0}/api/rest/replication_session'
REPLICATION_SESSION_OBJECT_URL = 'https://{0}/api/rest/replication_session/{1}'
REPLICATION_SESSION_SYNC_URL = 'https://{0}/api/rest/replication_session/{1}/sync'
REPLICATION_SESSION_PAUSE_URL = 'https://{0}/api/rest/replication_session/{1}/pause'
REPLICATION_SESSION_RESUME_URL = 'https://{0}/api/rest/replication_session/{1}/resume'
REPLICATION_SESSION_FAILOVER_URL = 'https://{0}/api/rest/replication_session/{1}/failover'
REPLICATION_SESSION_REPROTECT_URL = 'https://{0}/api/rest/replication_session/{1}/reprotect'
MODIFY_REPLICATION_SESSION_URL = REPLICATION_SESSION_OBJECT_URL

# Remote system endpoints
GET_REMOTE_SYSTEM_LIST_URL = 'https://{0}/api/rest/remote_system'
GET_REMOTE_SYSTEM_DETAILS_URL = 'https://{0}/api/rest/remote_system/{1}'
CREATE_REMOTE_SYSTEM_URL = GET_REMOTE_SYSTEM_LIST_URL
MODIFY_REMOTE_SYSTEM_URL = GET_REMOTE_SYSTEM_DETAILS_URL
DELETE_REMOTE_SYSTEM_URL = GET_REMOTE_SYSTEM_DETAILS_URL
GET_REMOTE_APPLIANCE_URL = 'https://{0}/api/rest/remote_system/{1}/query_appliances'


# Protection Policy endpoint
PROTECTION_POLICY_LIST_URL = 'https://{0}/api/rest/policy'
PROTECTION_POLICY_OBJECT_URL = 'https://{0}/api/rest/policy/{1}'

# Host Volume Mapping endpoints
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

# Network endpoints
GET_NETWORK_DETAILS_URL = 'https://{0}/api/rest/network/{1}'
GET_NETWORK_LIST_URL = 'https://{0}/api/rest/network'
MODIFY_NETWORK_URL = GET_NETWORK_DETAILS_URL
ADD_REMOVE_IP_PORTS = 'https://{0}/api/rest/network/{1}/scale'

# Role endpoints
GET_ROLE_LIST_URL = 'https://{0}/api/rest/role'
GET_ROLE_DETAILS_URL = 'https://{0}/api/rest/role/{1}'

# Logout endpoint
LOGOUT_URL = 'https://{0}/api/rest/logout'

# Login session endpoint
LOGIN_SESSION = 'https://{0}/api/rest/login_session'

# Local_user endpoints
GET_LOCAL_USER_LIST_URL = 'https://{0}/api/rest/local_user'

# IP Pool Address endpoint
GET_IP_POOL_LIST_URL = 'https://{0}/api/rest/ip_pool_address'

# Cluster endpoints
GET_CLUSTER_DETAILS_URL = 'https://{0}/api/rest/cluster/{1}'
GET_CLUSTER_LIST_URL = 'https://{0}/api/rest/cluster'
MODIFY_CLUSTER_URL = GET_CLUSTER_DETAILS_URL
CREATE_CLUSTER_URL = GET_CLUSTER_LIST_URL
CREATE_CLUSTER_VALIDATE_URL = 'https://{0}/api/rest/cluster/validate_create'

# CHAP config endpoints
GET_CHAP_CONFIG_LIST_URL = 'https://{0}/api/rest/chap_config'
GET_CHAP_CONFIG_DETAILS_URL = 'https://{0}/api/rest/chap_config/{1}'
MODIFY_CHAP_CONFIG_URL = GET_CHAP_CONFIG_DETAILS_URL

# Service config endpoints
GET_SERVICE_CONFIG_LIST_URL = 'https://{0}/api/rest/service_config'
GET_SERVICE_CONFIG_DETAILS_URL = 'https://{0}/api/rest/service_config/{1}'
MODIFY_SERVICE_CONFIG_URL = GET_SERVICE_CONFIG_DETAILS_URL

# Service user endpoints
GET_SERVICE_USER_LIST_URL = 'https://{0}/api/rest/service_user'
GET_SERVICE_USER_DETAILS_URL = 'https://{0}/api/rest/service_user/{1}'
MODIFY_SERVICE_USER_URL = GET_SERVICE_USER_DETAILS_URL

# Local user endpoints
GET_LOCAL_USER_LIST_URL = 'https://{0}/api/rest/local_user'
GET_LOCAL_USER_DETAILS_URL = 'https://{0}/api/rest/local_user/{1}'
MODIFY_LOCAL_USER_URL = GET_LOCAL_USER_DETAILS_URL
DELETE_LOCAL_USER_URL = GET_LOCAL_USER_DETAILS_URL
CREATE_LOCAL_USER_URL = GET_LOCAL_USER_LIST_URL

# IP port endpoints
GET_IP_PORT_DETAILS_URL = 'https://{0}/api/rest/ip_port/{1}'

# Job endpoints
GET_JOB_DETAILS_URL = 'https://{0}/api/rest/job/{1}'

# vCenter endpoints
GET_VCENTER_LIST_URL = 'https://{0}/api/rest/vcenter'
GET_VCENTER_DETAILS_URL = 'https://{0}/api/rest/vcenter/{1}'
MODIFY_VCENTER_URL = GET_VCENTER_DETAILS_URL

# Appliance endpoints
GET_APPLIANCE_LIST_URL = 'https://{0}/api/rest/appliance'
GET_APPLIANCE_DETAILS_URL = 'https://{0}/api/rest/appliance/{1}'

# Certificate endpoints
GET_CERTIFICATE_LIST_URL = 'https://{0}/api/rest/x509_certificate'
GET_CERTIFICATE_DETAILS_URL = 'https://{0}/api/rest/x509_certificate/{1}'
EXCHANGE_CERTIFICATE_URL = 'https://{0}/api/rest/x509_certificate/exchange'
CREATE_CERTIFICATE_URL = GET_CERTIFICATE_LIST_URL
MODIFY_CERTIFICATE_URL = GET_CERTIFICATE_DETAILS_URL
RESET_CERTIFICATE_URL = 'https://{0}/api/rest/x509_certificate/reset_certificates'

# Security config endpoints
GET_SECURITY_CONFIG_LIST_URL = 'https://{0}/api/rest/security_config'
GET_SECURITY_CONFIG_DETAILS_URL = 'https://{0}/api/rest/security_config/{1}'
MODIFY_SECURITY_CONFIG_URL = GET_SECURITY_CONFIG_DETAILS_URL

# ads endpoints
GET_AD_LIST_URL = 'https://{0}/api/rest/file_ftp'

# ldap endpoints
GET_LDAP_LIST_URL = 'https://{0}/api/rest/file_ldap'

# Email endpoints
GET_EMAIL_LIST_URL = 'https://{0}/api/rest/email_notify_destination'
GET_EMAIL_DETAILS_URL = 'https://{0}/api/rest/email_notify_destination/{1}'
CREATE_EMAIL_URL = GET_EMAIL_LIST_URL
MODIFY_EMAIL_URL = GET_EMAIL_DETAILS_URL
DELETE_EMAIL_URL = GET_EMAIL_DETAILS_URL
TEST_EMAIL_URL = 'https://{0}/api/rest/email_notify_destination/{1}/test'

# SMTP endpoints
GET_SMTP_LIST_URL = 'https://{0}/api/rest/smtp_config'
GET_SMTP_DETAILS_URL = 'https://{0}/api/rest/smtp_config/{1}'
MODIFY_SMTP_URL = GET_SMTP_DETAILS_URL
TEST_SMTP_URL = 'https://{0}/api/rest/smtp_config/{1}/test'

# DNS endpoints
GET_DNS_LIST_URL = 'https://{0}/api/rest/dns'
GET_DNS_DETAILS_URL = 'https://{0}/api/rest/dns/{1}'
MODIFY_DNS_URL = GET_DNS_DETAILS_URL

# NTP endpoints
GET_NTP_LIST_URL = 'https://{0}/api/rest/ntp'
GET_NTP_DETAILS_URL = 'https://{0}/api/rest/ntp/{1}'
MODIFY_NTP_URL = GET_NTP_DETAILS_URL

# Remote Support endpoints
GET_REMOTE_SUPPORT_LIST_URL = 'https://{0}/api/rest/remote_support'
GET_REMOTE_SUPPORT_DETAILS_URL = 'https://{0}/api/rest/remote_support/{1}'
MODIFY_REMOTE_SUPPORT_URL = GET_REMOTE_SUPPORT_DETAILS_URL
VERIFY_REMOTE_SUPPORT_URL = 'https://{0}/api/rest/remote_support/{1}/verify'
SEND_ALERT_REMOTE_SUPPORT_URL = 'https://{0}/api/rest/remote_support/{1}/send_test_alert'

# Remote Support Contact endpoints
GET_REMOTE_SUPPORT_CONTACT_LIST_URL = 'https://{0}/api/rest/remote_support_contact'
GET_REMOTE_SUPPORT_CONTACT_DETAILS_URL = 'https://{0}/api/rest/remote_support_contact/{1}'
MODIFY_REMOTE_SUPPORT_CONTACT_URL = GET_REMOTE_SUPPORT_CONTACT_DETAILS_URL

# LDAP Domain endpoints
GET_LDAP_DOMAIN_LIST_URL = 'https://{0}/api/rest/ldap_domain'
GET_LDAP_DOMAIN_DETAILS_URL = 'https://{0}/api/rest/ldap_domain/{1}'
CREATE_LDAP_DOMAIN_URL = GET_LDAP_DOMAIN_LIST_URL
MODIFY_LDAP_DOMAIN_URL = GET_LDAP_DOMAIN_DETAILS_URL
DELETE_LDAP_DOMAIN_URL = GET_LDAP_DOMAIN_DETAILS_URL
VERIFY_LDAP_DOMAIN_URL = 'https://{0}/api/rest/ldap_domain/{1}/verify'

# LDAP Account endpoints
GET_LDAP_ACCOUNT_LIST_URL = 'https://{0}/api/rest/ldap_account'
GET_LDAP_ACCOUNT_DETAILS_URL = 'https://{0}/api/rest/ldap_account/{1}'
CREATE_LDAP_ACCOUNT_URL = GET_LDAP_ACCOUNT_LIST_URL
MODIFY_LDAP_ACCOUNT_URL = GET_LDAP_ACCOUNT_DETAILS_URL
DELETE_LDAP_ACCOUNT_URL = GET_LDAP_ACCOUNT_DETAILS_URL
