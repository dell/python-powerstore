# Copyright: (c) 2024, Dell Technologies

"""IP Port Operations"""

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

# Get IP port details by ip_port_id
IP_PORT_DETAILS = CONN.config_mgmt.get_ip_port_details(ip_port_id="IP_PORT1")
print(IP_PORT_DETAILS)
