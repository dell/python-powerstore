# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

""" Cluster Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)

print(CONN)

# Get clusters list
clusters_list = CONN.config_mgmt.get_clusters()
print(clusters_list)

# Get cluster id by cluster_name
cluster = CONN.config_mgmt.get_cluster_by_name(name=clusters_list[0]['name'])
print(cluster[0]['id'])

# Get cluster details by cluster_id
cluster_details = CONN.config_mgmt.get_cluster_details(cluster_id=cluster[0]['id'])
print(cluster_details)

# Modify MTU and name of the cluster
updated_cluster_details = CONN.config_mgmt.modify_cluster(cluster_id=cluster[0]['id'], physical_mtu=1500, name="AB-C1234")
print(updated_cluster_details)
