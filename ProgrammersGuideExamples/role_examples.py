# Copyright: (c) 2024, Dell Technologies

"""Role operations"""

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

# Get roles list
roles_list = CONN.config_mgmt.get_roles()
print(roles_list)

# Get role details
role_details = CONN.config_mgmt.get_role_details(role_id=roles_list[0]["id"])
print(role_details)

# Get role details by name
role_details = CONN.config_mgmt.get_role_by_name(name=roles_list[0]["name"])
print(role_details)
