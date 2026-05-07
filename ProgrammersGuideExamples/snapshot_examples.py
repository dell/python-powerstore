# Copyright: (c) 2024, Dell Technologies

"""Snapshot Module Operations"""

# pylint: disable=duplicate-code

from datetime import datetime, timedelta

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
)

# Create volume
CONN.provisioning.create_volume(name="pr-sdk-vol", size=1073741824)

# Get volume by name
RESP = CONN.provisioning.get_volume_by_name(volume_name="pr-sdk-vol")
CREATED_VOL_ID = RESP[0].get("id")
print(RESP)

# Create volume snapshot
RESP = CONN.protection.create_volume_snapshot(
    volume_id=CREATED_VOL_ID, name="pr-sdk-snap", description="Snap from SDK",
)
CREATED_VOL_SNAP_ID = RESP.get("id")
print(RESP)

# Get volume snapshots list
RESP = CONN.protection.get_volume_snapshots(volume_id=CREATED_VOL_ID)
print(RESP)

# Get volume snapshot details
RESP = CONN.protection.get_volume_snapshot_details(snapshot_id=CREATED_VOL_SNAP_ID)
print(RESP)

# Modify volume snapshot
EXP_TIMESTAMP = (datetime.now() + timedelta(days=1)).isoformat() + "Z"
RESP = CONN.protection.modify_volume_snapshot(
    snapshot_id=CREATED_VOL_SNAP_ID,
    name="pr-sdk-snap-modified",
    expiration_timestamp=EXP_TIMESTAMP,
)
print(RESP)

# Delete volume snapshot
CONN.protection.delete_volume_snapshot(snapshot_id=CREATED_VOL_SNAP_ID)

# Create volume group
RESP = CONN.provisioning.create_volume_group(
    name="pr-sdk-vg", description="VG from SDK",
)
CREATED_VG_ID = RESP.get("id")
print(RESP)

# Add volumes to volume group
RESP = CONN.provisioning.add_members_to_volume_group(
    volume_group_id=CREATED_VG_ID, volume_ids=[CREATED_VOL_ID],
)
print(RESP)

# Create volume group snapshot
RESP = CONN.protection.create_volume_group_snapshot(
    volume_group_id=CREATED_VG_ID, name="pr-sdk-vg-snap", description="Snap from SDK",
)
CREATED_VG_SNAP_ID = RESP.get("id")
print(RESP)

# Get volume group snapshots list
RESP = CONN.protection.get_volume_group_snapshots(volume_group_id=CREATED_VG_ID)
print(RESP)

# Get volume group snapshot details
RESP = CONN.protection.get_volume_group_snapshot_details(snapshot_id=CREATED_VG_SNAP_ID)
print(RESP)

# Modify volume group snapshot
EXP_TIMESTAMP = (datetime.now() + timedelta(days=1)).isoformat() + "Z"
RESP = CONN.protection.modify_volume_group_snapshot(
    snapshot_id=CREATED_VG_SNAP_ID,
    name="pr-sdk-vg-snap-modified",
    expiration_timestamp=EXP_TIMESTAMP,
)
print(RESP)

# Delete volume group snapshot
CONN.protection.delete_volume_group_snapshot(snapshot_id=CREATED_VG_SNAP_ID)

# Remove volumes from volume group
RESP = CONN.provisioning.remove_members_from_volume_group(
    volume_group_id=CREATED_VG_ID, volume_ids=[CREATED_VOL_ID],
)
print(RESP)

# Delete volume
CONN.provisioning.delete_volume(volume_id=CREATED_VOL_ID)

# Delete volume group
CONN.provisioning.delete_volume_group(volume_group_id=CREATED_VG_ID)
