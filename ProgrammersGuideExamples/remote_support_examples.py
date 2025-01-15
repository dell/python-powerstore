# Copyright: (c) 2024, Dell Technologies

"""Remote Support operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<Password>",
    server_ip="<server_ip>",
    verify=False,
    timeout=180.0,
)

# Getting Remote Support configurations
remote_support_list = CONN.config_mgmt.get_remote_support_list()
print(remote_support_list)

# Getting Remote Support configuration instance details
remote_support_details = CONN.config_mgmt.get_remote_support_details(
    remote_support_id=remote_support_list[0]["id"],
)
print(remote_support_details)

# Modifying the Remote Support configuration details
modify_dict = {
    "type": "SRS_Integrated_Tier2",
    "proxy_address": "10.10.10.10",
    "proxy_port": 3128,
    "proxy_username": "user",
    "proxy_password": "pass123",
}

resp_modify = CONN.config_mgmt.modify_remote_support_details(
    remote_support_id=remote_support_list[0]["id"], modify_parameters=modify_dict,
)
print(resp_modify)

verify_dict = {"type": "SRS_Gateway_Tier3", "address": "10.10.10.10", "port": 9443}

resp_verify = CONN.config_mgmt.verify_remote_support_config(
    remote_support_id=remote_support_list[0]["id"], verify_parameters=verify_dict,
)
print(resp_verify)

# Sending test mail for Remote Support
resp_test = CONN.config_mgmt.test_remote_support_config(
    remote_support_id=remote_support_list[0]["id"],
)
print(resp_test)
