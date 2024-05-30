# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

""" Volume Module Operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

INITIATORS = [
    {
        "port_name": "iqn.1998-01.com.vmware:lgloc187-4cfa37b6",
        "port_type": "iSCSI",
        "chap_single_username": "chapuserSingle",
        "chap_single_password": "chappasswd12345",
        "chap_mutual_username": "chapuserMutual",
        "chap_mutual_password": "chappasswd12345"
    }
]

# Get volume list
VOL_LIST = CONN.provisioning.get_volumes()
print(VOL_LIST)

# Create volume
CONN.provisioning.create_volume(name="pr-sdk-lun-6", size=1073741824)

# Get volume by name
VOL = CONN.provisioning.get_volume_by_name(volume_name="pr-sdk-lun-6")
print(VOL)

# Modify volume
MODIFY_VOL = CONN.provisioning.modify_volume(volume_id=VOL[0]['id'],
                                             name="modified-volume-name-1")
print(MODIFY_VOL)

# Register a new Host
HOST = CONN.provisioning.create_host(name="pr-sdk-host",
                                     os_type="Linux",
                                     initiators=INITIATORS)
print(HOST)

# Map volume to Host
CONN.provisioning.map_volume_to_host(volume_id=VOL[0]['id'],
                                     host_id=HOST['id'])

# Get Host Volume mapping information
HOST_VOLUME_MAPPING = CONN.provisioning.get_host_volume_mapping(
    volume_id=VOL[0]['id'])
print(HOST_VOLUME_MAPPING)

# Unmap volume from Host
CONN.provisioning.unmap_volume_from_host(volume_id=VOL[0]['id'],
                                         host_id=HOST['id'])

# Create a Host Group
HG = CONN.provisioning.create_host_group(name="pr-sdk-hg",
                                         host_ids=[HOST['id']],
                                         description="HG from SDK")
print(HG)

# Map volume to Host Group
CONN.provisioning.map_volume_to_host_group(volume_id=VOL[0]['id'],
                                           host_group_id=HG['id'])

# Unmap volume from Host Group
CONN.provisioning.unmap_volume_from_host_group(volume_id=VOL[0]['id'],
                                               host_group_id=HG['id'])

# Get volume details
VOL_DETAILS = CONN.provisioning.get_volume_details(
    volume_id=VOL[0]['id'])
print(VOL_DETAILS)

# Delete volume
DEL_VOL = CONN.provisioning.delete_volume(volume_id=VOL[0]['id'])
print(DEL_VOL)

# Delete a Host Group
HG_DELETE = CONN.provisioning.delete_host_group(host_group_id=HG['id'])
print(HG_DELETE)

# Clone Volume
CLONE_VOLUME = CONN.provisioning.clone_volume(volume_id=VOL[0]['id'],
                                              name='test_clone_volume',
                                              description='Testing', 
                                              host_group_id=HG['id'])
print(CLONE_VOLUME)

# Refresh Volume
REFRESH_VOLUME_SNAPSHOT = CONN.provisioning.refresh_volume(volume_id=VOL[0]['id'],
                                                           volume_id_to_refresh_from=CLONE_VOLUME['id'])
print(REFRESH_VOLUME_SNAPSHOT)

# Restore Volume
RESTORE_VOLUME_SNAPSHOT = CONN.provisioning.restore_volume(volume_id=VOL[0]['id'],
                                                           snap_id_to_restore_from=REFRESH_VOLUME_SNAPSHOT['id'])
print(RESTORE_VOLUME_SNAPSHOT)

# Configure a metro volume
CONN.provisioning.configure_metro_volume(
    volume_id=VOL[0]['id'],
    remote_system_id='434f534e-7009-4e60-8e1e-5cf721ae40df')

# End a volume metro session
CONN.provisioning.end_volume_metro_config(volume_id=VOL[0]['id'],
                                          delete_remote_volume=True)
