# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

""" Host Group Module Operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>")
print(CONN)

HOST_IDS = ["c9fe4478-7260-4abc-afcf-d4203d37004f"]

INITIATORS = [
    {
        "port_name": "iqn.1998-01.com.vmware:lgloc187-4cfa37b6",
        "port_type": "iSCSI",
        "chap_single_username": "chapuserSingle",
        "chap_single_password": "chappasswd12345",
        "chap_mutual_username": "chapuserMutual",
        "chap_mutual_password": "chappasswd12345"
    }
]

# Get list of Host Groups
RESP = CONN.provisioning.get_host_group_list()
print(RESP)

# Register a new Host
HOST = CONN.provisioning.create_host(name="pr-sdk-host",
                                     os_type="Linux",
                                     initiators=INITIATORS)
print(HOST)

# Create a Host Group
RESP = CONN.provisioning.create_host_group(name="pr-sdk-hg",
                                           host_ids=[HOST['id']],
                                           description="HG from SDK")
print(RESP)

# Get Host Group details
HG_DETAILS = CONN.provisioning.get_host_group_details(
    host_group_id=RESP['id'])
print(HG_DETAILS)

# Get Host Group by name
HG_BY_NAME = CONN.provisioning.get_host_group_by_name(
    host_group_name="pr-sdk-hg")
print(HG_BY_NAME)

# Modify Host Group
HG_MODIFIED = CONN.provisioning.modify_host_group(
    host_group_id=RESP["id"],
    name="modified-pr-hg-name-x1",
    remove_host_ids=[HOST['id']],
    description="Modified desc from sdk")
print(HG_MODIFIED)

# Add Hosts to Host Group
ADD_HOSTS_TO_HG = CONN.provisioning.add_hosts_to_host_group(
    host_group_id=RESP["id"], add_host_ids=[HOST['id']])
print(ADD_HOSTS_TO_HG)

# Remove Hosts from Host Group
REMOVE_HOSTS_FROM_HG = CONN.provisioning.remove_hosts_from_host_group(
    host_group_id=RESP["id"], remove_host_ids=[HOST['id']])
print(REMOVE_HOSTS_FROM_HG)

# Get Hosts from Host Group
HOSTS_FROM_HG = CONN.provisioning.get_hosts_from_host_group(
    host_group_name="modified-pr-hg-name-x1")
print(HOSTS_FROM_HG)

# Delete a Host Group
HG_DELETE = CONN.provisioning.delete_host_group(host_group_id=RESP['id'])
print(HG_DELETE)

HOST_DELETE = CONN.provisioning.delete_host(host_id=HOST['id'])
print(HOST_DELETE)
