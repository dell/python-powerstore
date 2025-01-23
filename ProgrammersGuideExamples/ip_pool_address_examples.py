# Copyright: (c) 2024, Dell Technologies

"""IP Pool Address Operations"""
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

# Retrieve the IP's which are associated with particular network
filters = {"network_id": "eq." + "NW6"}
IP_POOL_LIST = CONN.config_mgmt.get_ip_pool_address(filter_dict=filters)
print(IP_POOL_LIST)
