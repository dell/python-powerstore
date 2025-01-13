# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

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
cluster_details = CONN.config_mgmt.get_cluster_details(
    cluster_id=cluster[0]['id'])
print(cluster_details)

# Modify MTU and name of the cluster
updated_cluster_details = CONN.config_mgmt.modify_cluster(
    cluster_id=cluster[0]['id'], physical_mtu=1500, name="AB-C1234")
print(updated_cluster_details)

# Validate create cluster
cluster = {"name": "test_cluster", "ignore_network_warnings": True}
appliances = [{"link_local_address": "4x.3x.2x.1x"}]
dns_servers = ["4x.3x.2x.1x"]
ntp_servers = ["4x.3x.2x.1x"]
networks = [
    {
        "type": "Management",
        "prefix_length": 24,
        "addresses": ["4x.3x.2x.1x", "1xx.2xx.3xx.4xx"]
    }
]
is_http_redirect_enabled = True
validate_resp = CONN.config_mgmt.cluster_create_validate(
    cluster=cluster, appliances=appliances, dns_servers=dns_servers,
    ntp_servers=ntp_servers, networks=networks,
    is_http_redirect_enabled=is_http_redirect_enabled)
print(validate_resp)

# Create Cluster
Create_resp = CONN.config_mgmt.cluster_create(
    cluster=cluster, appliances=appliances, dns_servers=dns_servers,
    ntp_servers=ntp_servers, networks=networks,
    is_http_redirect_enabled=is_http_redirect_enabled)
print(Create_resp)
