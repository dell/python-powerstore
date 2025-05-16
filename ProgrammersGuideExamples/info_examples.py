# Copyright: (c) 2024, Dell Technologies

"""Info Module Operations"""

# pylint: disable=duplicate-code

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

# Get volume list
filter_dict = {"name": "ilike.*vol*"}
VOL_LIST = CONN.provisioning.get_volumes(all_pages=True, filter_dict=filter_dict)
print(VOL_LIST)

# Get list of Host Groups
RESP = CONN.provisioning.get_host_group_list()
print(RESP)

# Get Host list
filter_dict = {"os_type": "neq.Linux"}
RESP = CONN.provisioning.get_hosts(filter_dict=filter_dict)
print(RESP)

# Get Volume Group list
RESP = CONN.provisioning.get_volume_group_list()
print(RESP)

# Get Nodes
RESP = CONN.provisioning.get_nodes()
print(RESP)

# Get cluster list
RESP = CONN.provisioning.get_cluster_list()
print(RESP)

# Get snapshot rules list
filter_dict = {"desired_retention": ["gt.100", "lt.500"]}
RESP = CONN.protection.get_snapshot_rules(filter_dict=filter_dict)
print(RESP)

# Get protection policies list
RESP = CONN.protection.get_protection_policies()
print(RESP)

# Get file systems list
RESP = CONN.provisioning.get_file_systems()
print(RESP)

# Get NAS servers list
RESP = CONN.provisioning.get_nas_servers()
print(RESP)

# Get NFS exports list
RESP = CONN.provisioning.get_nfs_exports()
print(RESP)

# Get SMB shares list
RESP = CONN.provisioning.get_smb_shares()
print(RESP)

# Get tree quotas list
RESP = CONN.provisioning.get_file_tree_quotas()
print(RESP)

# Get user quotas list
RESP = CONN.provisioning.get_file_user_quotas()
print(RESP)

# Get replication rules list
RESP = CONN.protection.get_replication_rules()
print(RESP)

# Get replication sessions list
RESP = CONN.protection.get_replication_sessions()
print(RESP)

# Get remote systems list
RESP = CONN.protection.get_remote_systems()
print(RESP)

# Get networks list
RESP = CONN.config_mgmt.get_networks()
print(RESP)

# Get clusters list
RESP = CONN.config_mgmt.get_clusters()
print(RESP)

# Get local users list
RESP = CONN.config_mgmt.get_local_users()
print(RESP)

# Get roles list
RESP = CONN.config_mgmt.get_roles()
print(RESP)

# Get appliances list
RESP = CONN.config_mgmt.get_appliances()
print(RESP)

# Get ip pool addresses list
RESP = CONN.config_mgmt.get_ip_pool_address()
print(RESP)

# Get chap configs list
RESP = CONN.config_mgmt.get_chap_configs()
print(RESP)

# Get service configs list
RESP = CONN.config_mgmt.get_service_configs()
print(RESP)

# Get service users list
RESP = CONN.config_mgmt.get_service_users()
print(RESP)

# Get vcenters list
RESP = CONN.config_mgmt.get_vcenters()
print(RESP)

# Get remote systems list
RESP = CONN.protection.get_remote_systems()
print(RESP)

# Get security config list
RESP = CONN.config_mgmt.get_security_configs()
print(RESP)

# Get certificate list
RESP = CONN.config_mgmt.get_certificates()
print(RESP)

# Get virtual volume list
RESP = CONN.config_mgmt.get_virtual_volume_list()
print(RESP)
