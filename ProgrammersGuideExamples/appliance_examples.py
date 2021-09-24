# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

""" Appliance operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Get appliances list
appliances_list = CONN.config_mgmt.get_appliances()
print(appliances_list)

# Get appliance details
appliance_details = CONN.config_mgmt.get_appliance_details(appliance_id=appliances_list[0]['id'])
print(appliance_details)

# Get appliance by name
appliance_details_by_name = CONN.config_mgmt.get_appliance_by_name(appliance_name=appliances_list[0]['name'])
print(appliance_details_by_name)
