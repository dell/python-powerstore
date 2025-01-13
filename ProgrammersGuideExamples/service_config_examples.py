# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" Service config operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Get service config list
service_configs_list = CONN.config_mgmt.get_service_configs()
print(service_configs_list)

# Get service config details
service_config_details = CONN.config_mgmt.get_service_config_details(
    service_config_id=service_configs_list[0]['id'])
print(service_config_details)

# Get service config details by appliance id
service_config_details_by_appliance_id = CONN.config_mgmt.get_service_config_by_appliance_id(
    appliance_id=service_config_details['appliance_id'])
print(service_config_details)

# Modify service config
updated_service_config_details = CONN.config_mgmt.modify_service_config(
    service_config_id=service_configs_list[0]['id'], is_ssh_enabled=False)
print(updated_service_config_details)
