# Copyright: (c) 2024, Dell Technologies

"""LDAP Account operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<server_ip>",
    verify=False,
    timeout=180.0,
)
print(CONN)

# Create LDAP account
create_dict = {
    "domain_id": "2",
    "name": "ldap_test_user_1",
    "type": "User",
    "role_id": "1",
}
resp = CONN.config_mgmt.create_ldap_account(create_dict)
print(resp)

# Modify LDAP account
modify_dict = {"role_id": "2"}
resp = CONN.config_mgmt.modify_ldap_account_details(resp["id"], modify_dict)
print(resp)

# Get LDAP account list
ldap_account_list = CONN.config_mgmt.get_ldap_account_list()
print(ldap_account_list)

# Get LDAP account details
ldap_account_details = CONN.config_mgmt.get_ldap_account_details(
    ldap_account_list[0]["id"],
)
print(ldap_account_details)

# Get LDAP account details by name
ldap_account_details = CONN.config_mgmt.get_ldap_account_details_by_name(
    ldap_account_list[0]["name"],
)
print(ldap_account_details)

# Delete LDAP domain configuration
resp = CONN.config_mgmt.delete_ldap_account(ldap_account_details["id"])
print(resp)
