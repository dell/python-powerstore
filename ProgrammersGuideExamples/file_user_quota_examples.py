# Copyright: (c) 2024, Dell Technologies

"""File User Quota Operations"""
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
OTHER_PARAM = {"uid": 2147483650}

# Create userquota
QUOTA = CONN.provisioning.create_user_quota(FS_ID, OTHER_PARAM)
print(QUOTA)

# Get userquota list
filter_dict = {"id": "eq.{0}".format(QUOTA["id"])}
QUOTA_LIST = CONN.provisioning.get_file_user_quotas(filter_dict=filter_dict)
print(QUOTA_LIST)

# Get userquota details
QUOTA_DETAIL = CONN.provisioning.get_user_quota(QUOTA["id"])
print(QUOTA_DETAIL)

# Modify userquota
MODIFY_PARAM = {"hard_limit": 2097152, "soft_limit": 1048576}
MODIFY_QUOTA = CONN.provisioning.update_user_quota(QUOTA["id"], MODIFY_PARAM)
print(MODIFY_QUOTA)
