# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" File Interface Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)


MODIFY_PARAMS = {
  "ip_address": "10.10.10.10",
  "prefix_length": 21,
  "gateway": "10.10.10.1",
  "vlan_id": 0,
  "is_disabled": False
}

CREATE_PARAMS = {
  "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
  "ip_address": "10.10.10.11",
  "prefix_length": 21,
  "gateway": "10.10.10.1",
  "vlan_id": 0,
  "role": "Production",
  "is_disabled": False
}

# create file interface
FILE_INTERFACE = CONN.file_interface.create_file_interface(payload=CREATE_PARAMS)
print(FILE_INTERFACE)

# Get file interfaces list
FILE_INTERFACES = CONN.file_interface.get_file_interface_list(all_pages=True)
print(FILE_INTERFACES)

# get file interface details by ID
FILE_INTERFACE =CONN.file_interface.get_file_interface_details(FILE_INTERFACE['id'])
print(FILE_INTERFACE)

# get file interface details by NAS server
FILE_INTERFACE = CONN.file_interface.get_file_interface_by_nas_server_id(nas_server_id=CREATE_PARAMS['nas_server_id'],
	                                                                       ip_address="10.10.10.11")
print(FILE_INTERFACE)

# modify file interface
MODIFY_FILE_INTERFACE = CONN.file_interface.modify_file_interface(FILE_INTERFACE[0]['id'],
                                                                  MODIFY_PARAMS)
print(MODIFY_FILE_INTERFACE)

# delete file interface
DELETE_FILE_INTERFACE = CONN.file_interface.delete_file_interface(FILE_INTERFACE[0]['id'])
print(DELETE_FILE_INTERFACE)
