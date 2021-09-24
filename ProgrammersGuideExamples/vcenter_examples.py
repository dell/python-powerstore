# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

""" Vcenter Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

# Get Vcenter list
vcenters_list = CONN.config_mgmt.get_vcenters()
print(vcenters_list)

# Get Vcenter details by vcenter_id
vcenter_details = CONN.config_mgmt.get_vcenter_details(vcenter_id=vcenters_list[0]['id'])
print(vcenter_details)

# Register VASA provider
param_dict = {
'vasa_provider_credentials': {
'username': "<<admin_user>>",
'password': "<<admin_password>>"
}
}
vcenter_details = CONN.config_mgmt.modify_vcenter(vcenter_id=vcenters_list[0]['id'], modify_param_dict=param_dict)
print(vcenter_details)