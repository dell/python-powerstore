# Copyright: (c) 2024, Dell Technologies

"""Discovered Appliance operations"""

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

# Get Discovered appliances list
discovered_appliances_list = CONN.config_mgmt.get_discovered_appliances()
print(discovered_appliances_list)
