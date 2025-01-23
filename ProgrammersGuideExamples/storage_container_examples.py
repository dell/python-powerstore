# Copyright: (c) 2024, Dell Technologies

"""Storage container operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<server_ip>",
    verify=False,
    timeout=180.0,
)
print(CONN)

# Create storage container
create_dict = {
    "name": "Sample_storage_container_1",
    "quota": 0,
    "storage_protocol": "NVMe",
    "high_water_mark": 50,
}
create_resp = CONN.config_mgmt.create_storage_container(create_dict)
print(create_resp)

# Modify storage container
modify_dict = {"storage_protocol": "SCSI", "quota": 10737418240}
modify_resp = CONN.config_mgmt.modify_storage_container_details(
    create_resp["id"], modify_dict,
)
print(modify_resp)

# Get storage container list
storage_container_list = CONN.config_mgmt.get_storage_container_list()
print(storage_container_list)

# Get storage container details
storage_container_details = CONN.config_mgmt.get_storage_container_details(
    storage_container_list[0]["id"],
)
print(storage_container_details)

# Get storage container details by name
storage_container_details = CONN.config_mgmt.get_storage_container_details_by_name(
    storage_container_list[0]["name"],
)
print(storage_container_details)

# Delete storage container configuration
resp = CONN.config_mgmt.delete_storage_container(create_resp["id"], False)
print(resp)
