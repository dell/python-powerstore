# Copyright: (c) 2024, Dell Technologies

"""Service user module operations"""

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

# Get service user list
service_users_list = CONN.config_mgmt.get_service_users()
print(service_users_list)

# Get service user details
service_user_details = CONN.config_mgmt.get_service_user_details(
    service_user_id=service_users_list[0]["id"],
)
print(service_user_details)

# Get service user details by appliance id
service_user_details_by_name = CONN.config_mgmt.get_service_user_by_name(
    name=service_user_details["name"],
)
print(service_user_details)

# Modify service user
updated_service_user_details = CONN.config_mgmt.modify_service_user(
    service_user_id=service_users_list[0]["id"], password="<Enter your Password>",
)
print(updated_service_user_details)
