# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" NTP operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<server_ip>",
                                      verify=False,
                                      timeout=180.0)

# Getting NTP list
ntp_list = CONN.config_mgmt.get_ntp_list()
print(ntp_list)

# Getting NTP instance details
ntp_details = CONN.config_mgmt.get_ntp_details(ntp_id=ntp_list[0]['id'])
print(ntp_details)

# Modifying the NTP addresses
modify_dict = {"addresses": ["XX.XX.XX.XX","XX.XX.XX.YY"]}

resp_modify = CONN.config_mgmt.modify_ntp_details(ntp_id=ntp_list[0]['id'], modify_parameters=modify_dict)
print(resp_modify)
