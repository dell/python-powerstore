# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" Storage container destination operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<server_ip>",
    verify=False,
    timeout=180.0,
)
print(CONN)

# Create storage container destination
create_dict = {
    "storage_container_id": "5f4e57d3-2f6e-5fb4-3ac9-c6f547282e76",
    "remote_system_id": "5f4e57d3-2f6e-5fb4-3ac9-c6f547282e77",
    "remote_storage_container_id": "5f4e57d3-2f6e-5fb4-3ac9-c6f547282e78",
}
create_resp = CONN.config_mgmt.create_storage_container_destination(create_dict)
print(create_resp)

# Get storage container destination list
storage_container_list = CONN.config_mgmt.get_storage_container_destination_list()
print(storage_container_list)

# Get storage container destination details
storage_container_details = CONN.config_mgmt.get_storage_container_destination_details(
    create_resp["id"]
)
print(storage_container_details)

# Delete storage container destination
resp = CONN.config_mgmt.delete_storage_container_destination(create_resp["id"])
print(resp)
