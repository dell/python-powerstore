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
VOL_LIST = CONN.provisioning.get_volumes()
print(VOL_LIST)

# Get list of Host Groups
RESP = CONN.provisioning.get_host_group_list()
print(RESP)

# Get Host list
RESP = CONN.provisioning.get_hosts()
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
RESP = CONN.protection.get_snapshot_rules()
print(RESP)

# Get protection policies list
RESP = CONN.protection.get_protection_policies()
print(RESP)
