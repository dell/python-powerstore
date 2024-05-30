# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" CHAP config operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Get chap config list
chap_configs_list = CONN.config_mgmt.get_chap_configs()
print(chap_configs_list)

# Get chap config details
chap_config_details = CONN.config_mgmt.get_chap_config_details(chap_config_id=chap_configs_list[0]['id'])
print(chap_config_details)

# Modify chap config
updated_chap_config_details = CONN.config_mgmt.modify_chap_config(chap_config_id=chap_configs_list[0]['id'], mode='Disabled')
print(updated_chap_config_details)
