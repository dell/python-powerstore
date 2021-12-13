# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

""" Network Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Get network list
NETWORKS = CONN.config_mgmt.get_networks()
print(NETWORKS)

# Get network details by name
NETWORK = CONN.config_mgmt.get_network_by_name(name="Default Management Network")
print(NETWORK)

# Get network details by ID
NETWORK = CONN.config_mgmt.get_network_details(network_id=NETWORK[0]['id'])
print(NETWORK)

network_other_params = {
    "vlan_id": 0,
    "gateway": "100.231.x.x",
    "mtu": 1500,
    "prefix_length": 24,
    "cluster_mgmt_address": "10.230.x.x",
    "remove_addresses": ["10.230.x.x", "", "10.230.x.x", "10.230.x.x"],
    "add_addresses": ["10.231.x.x", "10.231.x.x", "10.231.x.x"],
    "vasa_provider_credentials": {
        "username": "<<admin_username>>",
        "password": "<<admin_password"
    }
}

# Modify cluster management address and replace the existing IP address
JOB_DETAILS = CONN.config_mgmt.modify_network(network_id=NETWORK['id'], network_other_params=network_other_params,
                                              is_async=True)
print(JOB_DETAILS)

# Rename storage network
rename_dict = {"name": "iSCSI Network"}
NETWORK = CONN.config_mgmt.modify_network(network_id="NW2", network_other_params=rename_dict)
print(NETWORK)

# Map storage network to IP port
NETWORK = CONN.config_mgmt.add_remove_ports(network_id="NW2", add_port_ids=["IP_PORT9"])
print(NETWORK)

# Unmap storage network from IP port
NETWORK = CONN.config_mgmt.add_remove_ports(network_id="NW2", remove_port_ids=["IP_PORT9"])
print(NETWORK)
