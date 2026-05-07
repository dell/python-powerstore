# Copyright: (c) 2024, Dell Technologies

"""Volume Group Module Operations"""

# pylint: disable=duplicate-code

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
)
print(CONN)

VOLUMES = ["664ae002-651f-4c42-9236-a10277f93b3e"]

# Get Volume Group list
RESP = CONN.provisioning.get_volume_group_list()
print(RESP)

# Create Volume Group
AG = CONN.provisioning.create_volume_group(
    name="pr-sdk-ag-new-1", description="Created this VG from SDK",
)
print(AG)

# Get Volume Group details
AG_DETAILS = CONN.provisioning.get_volume_group_details(volume_group_id=AG["id"])
print(AG_DETAILS)

# Create volume
print("Creating new volume\n")
CONN.provisioning.create_volume(name="pr-sdk-lun-6", size=1073741824)

# Get volume by name
print("Get volume by name\n")
VOL = CONN.provisioning.get_volume_by_name(volume_name="pr-sdk-lun-6")
print(VOL)

# Add volumes to Volume Group
ADD_VOL_TO_AG = CONN.provisioning.add_members_to_volume_group(
    volume_group_id=AG["id"], volume_ids=[VOL[0]["id"]],
)
print(ADD_VOL_TO_AG)

# Remove volumes from Volume Group
REMOVE_VOL_FROM_AG = CONN.provisioning.remove_members_from_volume_group(
    volume_group_id=AG["id"], volume_ids=[VOL[0]["id"]],
)
print(REMOVE_VOL_FROM_AG)

# Modify Volume Group
CONN.provisioning.modify_volume_group(
    volume_group_id=AG["id"],
    name="modified-ag-name-sdk",
    description="modified description sdk",
)

# Get Volume group by name
AG_BY_NAME = CONN.provisioning.get_volume_group_by_name(
    volume_group_name="modified-ag-name-sdk",
)
print(AG_BY_NAME)

# Delete Volume Group
DEL_AG = CONN.provisioning.delete_volume_group(volume_group_id=AG["id"])
print(DEL_AG)

# Delete volume
DEL_VOL = CONN.provisioning.delete_volume(volume_id=VOL[0]["id"])
print(DEL_VOL)
