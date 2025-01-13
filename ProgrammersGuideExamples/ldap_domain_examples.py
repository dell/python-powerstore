# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" LDAP domain operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Create LDAP domain configuration
create_dict = {
    "domain_name": "<<domain_name>>",
    "ldap_servers": [
        "<<ldap_server_ip>>"
    ],
    "protocol": "LDAP",
    "ldap_server_type": "OpenLDAP",
    "bind_user": "<<LDAP_user_DN>>",
    "bind_password": "<<password>>",
    "is_global_catalog": False,
    "user_search_path": "cn=Users",
    "group_search_path": "cn=Users"
}
resp = CONN.config_mgmt.create_ldap_domain_configuration(create_dict)
print(resp)

# Verify LDAP domain configuration
print(CONN.config_mgmt.verify_ldap_domain_configuration(resp['id']))

# Modify LDAP domain configuration
modify_dict = {
    "ldap_server_type": "AD"
}
resp = CONN.config_mgmt.modify_ldap_domain_configuration(
    resp['id'], modify_dict)
print(resp)

# Get LDAP domain configuration list
ldap_domain_list = CONN.config_mgmt.get_ldap_domain_configuration_list()
print(ldap_domain_list)

# Get LDAP domain configuration details
ldap_domain_details = CONN.config_mgmt.get_ldap_domain_configuration_details(
    ldap_domain_list[0]['id'])
print(ldap_domain_details)

# Get LDAP domain configuration details by name
ldap_domain_details = CONN.config_mgmt.get_ldap_domain_configuration_details_by_name(
    ldap_domain_details['domain_name'])
print(ldap_domain_details)

# Delete LDAP domain configuration
resp = CONN.config_mgmt.delete_ldap_domain_configuration(resp['id'])
print(resp)
