# Copyright: (c) 2024, Dell Technologies

"""SMB Share Operations"""
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

SMB_NAME = "sample_smb"
FS_ID = "5f4e57d3-2f6e-5fb4-3ac9-c6f547282e76"
PATH = "/sample_fs"

# Create smbshare
SMB = CONN.provisioning.create_smb_share(
    FS_ID, PATH, SMB_NAME, description="Description",
)
print(SMB)

# Get smbshare list
filter_dict = {"name": f"eq.{SMB_NAME}"}
SMB_LIST = CONN.provisioning.get_smb_shares(filter_dict=filter_dict)
print(SMB_LIST)

# Get smbshare details by name
SMB_DETAIL = CONN.provisioning.get_smb_share_by_name(SMB_NAME)
print(SMB_DETAIL)

# Get smbshare details by ID
SMB_DETAIL = CONN.provisioning.get_smb_share(SMB["id"])
print(SMB_DETAIL)

# Modify smbshare
SMB = CONN.provisioning.update_smb_share(SMB["id"], is_encryption_enabled=True)
print(SMB)

# Delete smbshare
DELETE_SMB = CONN.provisioning.delete_smb_share(SMB_DETAIL["id"])
print(DELETE_SMB)
