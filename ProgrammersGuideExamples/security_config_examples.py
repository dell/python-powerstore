# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" Security config operations"""

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

security_config_list = CONN.config_mgmt.get_security_configs()
print(security_config_list)

security_config_details = CONN.config_mgmt.get_security_config_details(
    security_config_id=security_config_list[0]["id"]
)
print(security_config_details)

security_config_details = CONN.config_mgmt.modify_security_config(
    security_config_id=security_config_list[0]["id"], protocol_mode="TLSv1_2"
)
print(security_config_details)
