# Copyright: (c) 2024, Dell Technologies

"""File Tree Quota Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
    timeout=180.0,
)
print(CONN)

FS_ID = "5f4e57d3-2f6e-5fb4-3ac9-c6f547282e76"
PATH = "/sample_fs"
OTHER_PARAM = {"hard_limit": 2097152, "soft_limit": 1048576}

# Create treequota
QUOTA = CONN.provisioning.create_tree_quota(FS_ID, PATH, OTHER_PARAM)
print(QUOTA)

# Get treequota list
quota_id = QUOTA["id"]
filter_dict = {"id": f"eq.{quota_id}"}
QUOTA_LIST = CONN.provisioning.get_file_tree_quotas(filter_dict=filter_dict)
print(QUOTA_LIST)

# Get treequota details
QUOTA_DETAIL = CONN.provisioning.get_tree_quota(QUOTA["id"])
print(QUOTA_DETAIL)

# Modify treequota
MODIFY_PARAM = {"description": "My Description"}
MODIFY_QUOTA = CONN.provisioning.update_tree_quota(QUOTA["id"], MODIFY_PARAM)
print(MODIFY_QUOTA)

# Delete treequota
DELETE_QUOTA = CONN.provisioning.delete_tree_quota(QUOTA["id"])
print(DELETE_QUOTA)
