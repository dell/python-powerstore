# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" Remote system operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
    timeout=180.0,
)

rs_list = CONN.protection.get_remote_systems()
print(rs_list)

rs_details = CONN.protection.get_remote_system_by_name(name=rs_list[0]["name"])
print(rs_details)

rs_details = CONN.protection.get_remote_system_by_mgmt_address(
    remote_address=rs_list[0]["management_address"]
)
print(rs_details)

rs_details = CONN.protection.get_remote_system_details(
    remote_system_id=rs_list[0]["id"]
)
print(rs_details)

exchange_dict = {
    "address": "<remote_address>",
    "port": 443,
    "username": "<remote_user>",
    "password": "<remote_password>",
    "service": "Replication_HTTP",
}

resp = CONN.config_mgmt.exchange_certificate(exchange_cert_dict=exchange_dict)
print(resp)

create_dict = {
    "management_address": "<remote_address>",
    "description": "add remote system",
    "data_network_latency": "Low",
}

resp = CONN.protection.create_remote_system(create_remote_sys_dict=create_dict)
print(resp)

modify_dict = {"description": "modify_description", "network_latency": "High"}

resp = CONN.protection.modify_remote_system(
    remote_system_id=resp["id"], modify_remote_sys_dict=modify_dict
)
print(resp)

resp = CONN.protection.delete_remote_system(remote_system_id=resp["id"])
print(resp)
