# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" DNS operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<server_ip>",
    verify=False,
    timeout=180.0,
)

# Getting DNS list
dns_list = CONN.config_mgmt.get_dns_list()
print(dns_list)

# Getting DNS instance details
dns_details = CONN.config_mgmt.get_dns_details(dns_id=dns_list[0]["id"])
print(dns_details)

# Modifying the DNS addresses
modify_dict = {"addresses": ["XX.XX.XX.XX", "XX.XX.XX.YY"]}

resp_modify = CONN.config_mgmt.modify_dns_details(
    dns_id=dns_list[0]["id"], modify_parameters=modify_dict
)
print(resp_modify)
