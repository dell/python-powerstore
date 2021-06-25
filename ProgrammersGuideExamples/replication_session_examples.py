# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

""" Replication session Operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>")
print(CONN)

# Get replication session details using ID
RESP = CONN.protection.get_replication_session_details(
    session_id="24f4236f-f7b6-4ae1-8130-8463b256fae6")
print(RESP)

# Pause the replication session
RESP = CONN.protection.pause_replication_session(
    session_id="24f4236f-f7b6-4ae1-8130-8463b256fae6")
print(RESP)

# Failover the replication session
RESP = CONN.protection.failover_replication_session(
    session_id="24f4236f-f7b6-4ae1-8130-8463b256fae6")
print(RESP)

# Sync the replication session
RESP = CONN.protection.sync_replication_session(
    session_id="24f4236f-f7b6-4ae1-8130-8463b256fae6")
print(RESP)

