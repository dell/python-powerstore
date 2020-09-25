# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

""" Gather Facts Module Operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Get volume list
filter_dict = {'name': 'ilike.*vol*'}
VOL_LIST = CONN.provisioning.get_volumes(all_pages=True,
                                         filter_dict=filter_dict)
print(VOL_LIST)

# Get list of Host Groups
RESP = CONN.provisioning.get_host_group_list()
print(RESP)

# Get Host list
filter_dict = {'os_type': 'neq.Linux'}
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
filter_dict = {'desired_retention': ['gt.100', 'lt.500']}
RESP = CONN.protection.get_snapshot_rules(filter_dict=filter_dict)
print(RESP)

# Get protection policies list
RESP = CONN.protection.get_protection_policies()
print(RESP)
