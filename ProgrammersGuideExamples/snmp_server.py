# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" SNMP server Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)

print(CONN)

MODIFY_PARAMS = {
	"ip_address": "10.**.**.**",
	"port": 162,
	"trap_community": "community",
	"alert_severity": "Info"
}

CREATE_PARAMS = {
	"ip_address": "10.**.**.**",
	"port": 162,
	"version": "V2c",
	"alert_severity": "Info",
	"trap_community": "public"
}

# create SNMP server
SNMP_SERVER = CONN.snmp_server.create_snmp_server(CREATE_PARAMS)
print(SNMP_SERVER)

# Get SNMP server list
SNMP_SERVERS = CONN.snmp_server.get_snmp_server_list(all_pages=True)
print(SNMP_SERVERS)

# get SNMP server details by ID
SNMP_SERVER = CONN.snmp_server.get_snmp_server_details(SNMP_SERVER['id'])
print(SNMP_SERVER)

# modify SNMP server
MODIFY_SNMP_SERVER = CONN.snmp_server.modify_snmp_server(SNMP_SERVERS[0]['id'],
                                                         MODIFY_PARAMS)
print(MODIFY_SNMP_SERVER)

# delete SNMP server
DELETE_SNMP_SERVER = CONN.snmp_server.delete_snmp_server(SNMP_SERVERS[0]['id'])
print(DELETE_SNMP_SERVER)
