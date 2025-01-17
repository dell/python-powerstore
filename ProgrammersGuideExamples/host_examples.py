# Copyright: (c) 2024, Dell Technologies

"""Host Module Operations"""

from PyPowerStore import powerstore_conn

REMOVE_INITIATORS = ["iqn.1998-01.com.vmware:lgloc187-4cfa37b6"]

INITIATORS = [
    {
        "port_name": "iqn.1998-01.com.vmware:lgloc187-4cfa37b6",
        "port_type": "iSCSI",
        "chap_single_username": "chapuserSingle",
        "chap_single_password": "chappasswd12345",
        "chap_mutual_username": "chapuserMutual",
        "chap_mutual_password": "chappasswd12345",
    },
]


MODIFY_INITIATORS = [
    {
        "port_name": "iqn.1998-01.com.vmware:lgloc187-4cfa37b6",
        "chap_single_username": "prashantrakheja",
        "chap_single_password": "prashantrakheja",
        "chap_mutual_username": "chapuserMutual",
        "chap_mutual_password": "chappasswd12345",
    },
]

REMOVE_INITIATORS = ["iqn.1998-01.com.vmware:lgloc187-4cfa37b6"]

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
)
print(CONN)

# Get Host list
RESP = CONN.provisioning.get_hosts()
print(RESP)

# Register a new Host
RESP = CONN.provisioning.create_host(
    name="pr-sdk-host", os_type="Linux", initiators=INITIATORS,
)

print(RESP)

# Get details of a particular host
HOST_DETAILS = CONN.provisioning.get_host_details(host_id=RESP["id"])
print(HOST_DETAILS)

# Modify the Host
HOST_MODIFIED = CONN.provisioning.modify_host(
    host_id=RESP["id"],
    name="powerstore_renamed",
    description="This is a new description ",
    host_connectivity="Metro_Optimize_Both",
)
print(HOST_MODIFIED)

# Remove Initiators from Host
HOST_REMOVE_INITIATOR = CONN.provisioning.remove_initiators_from_host(
    host_id=RESP["id"], remove_initiators=REMOVE_INITIATORS,
)
print(HOST_REMOVE_INITIATOR)

# Add initiators to Host
HOST_ADD_INITIATOR = CONN.provisioning.add_initiators_to_host(
    host_id=RESP["id"], add_initiators=INITIATORS,
)
print(HOST_ADD_INITIATOR)

# Get Host by name
HOST_BY_NAME = CONN.provisioning.get_host_by_name(host_name="powerstore_renamed")
print(HOST_BY_NAME)

# Delete the Host
DELETE_HOST = CONN.provisioning.delete_host(host_id=RESP["id"])
print(DELETE_HOST)
