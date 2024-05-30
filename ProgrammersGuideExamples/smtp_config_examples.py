# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" SMTP Config operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<server_ip>",
                                      verify=False,
                                      timeout=180.0)

# Getting SMTP configurations
smtp_config_list = CONN.config_mgmt.get_smtp_configs()
print(smtp_config_list)

# Getting SMTP configuration instance details
smtp_config_details = CONN.config_mgmt.get_smtp_config_details(smtp_id=smtp_config_list[0]['id'])
print(smtp_config_details)

# Modifying the SMTP configuration details
modify_dict = { "address": "sample.smtp.com", "port": 25,"source_email": "def@dell.com" }

resp_modify = CONN.config_mgmt.modify_smtp_config_details(smtp_id=smtp_config_list[0]['id'], modify_parameters=modify_dict)
print(resp_modify)

# Sending test mail through an SMTP configuration
test_dict = { "email_address": "xyz@dell.com" }

resp_test = CONN.config_mgmt.test_smtp_config(smtp_id=smtp_config_list[0]['id'], test_parameters=test_dict)
print(resp_test)
