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

# Query params

SELECT_ALL_VOLUME = {"select": "id,name,description,type,wwn,appliance_id,"
                               "state,size,creation_timestamp,"
                               "protection_policy_id,performance_policy_id,"
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
                                  "migration_session_id,"
                                  "is_write_order_consistent,"
                                  "placement_rule,type,"
                                  "is_replication_destination,protection_data,"
                                  "is_importing,location_history,"
                                  "type_l10n,volumes"}

SELECT_ID_AND_NAME = {"select": "id,name"}

SELECT_ALL_HOST_VOLUME_MAPPING = {"select": "id, host_id, host_group_id,"
                                            "logical_unit_number"}

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
