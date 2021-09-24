class CommonData(object):
    size_used = 1623195648
    size_total = 5368709120
    uuid = "5f474e2d-1a45-5980-5175-9245647c527e"

    # Volume
    vol_id1 = "007a5fad-7520-4f2a-a364-6c243d8d4ecf"
    vol_name1 = "my_vol1"
    size = 1048576

    vol_id2 = "00c2c300-cf6e-4cf0-9bf4-037173496913"
    vol_name2 = "my_vol2"

    volume_list = [{"id": vol_id1, "name": vol_name1},
                   {"id": vol_id2, "name": vol_name2}]

    create_volume = {"id": vol_id1}

    hlu_details = []

    volume1 = {'appliance_id': 'A1', 'creation_timestamp': '2020-08-10T13:'
                                                           '20:57.899845+00:00',
               'description': '', 'hlu_details':
                   hlu_details, 'host': [], 'host_group': [], 'id': vol_id1,
               'is_replication_destination': False, 'location_history': None,
               'migration_session_id': None, 'name': vol_name1,
               'performance_policy_id': 'default_medium',
               'protection_data': {
                   'copy_signature': '1a482103-0476-4530-b209-7e0bf483ad0a',
                   'created_by_rule_id': None, 'created_by_rule_name': None,
                   'creator_type': 'System', 'creator_type_l10n': 'System',
                   'expiration_timestamp': None, 'is_app_consistent': None,
                   'family_id': '60b27a31-4121-42b7-97c6-fb24c4074864',
                   'parent_id': '60b27a31-4121-42b7-97c6-fb24c4074864',
                   'source_id': '60b27a31-4121-42b7-97c6-fb24c4074864',
                   'source_timestamp': '2020-08-10T13:20:57.899845+00:00'},
               'protection_policy_id': None, 'size': 1073741824,
               'type': 'Snapshot', 'state_l10n': 'Ready',
               'type_l10n': 'Snapshot', 'volume_groups': [], 'wwn': None,
               'state': 'Ready'}

    vol_snap_id = uuid

    create_vol_snap = {'id': vol_snap_id}

    vol_snap_detail = volume1

    volume_snap_list = volume_list

    # Volume End

    # VolumeGroup
    vg_id1 = "007a5fad-7520-4f2a-a364-6c243d8d4ecf"
    vg_name1 = "my_vg1"

    vg_id2 = "007a5fad-7520-4f2a-a364-6c243d8d4ecf"
    vg_name2 = "my_vg2"

    volumegroup_list = [{"id": vg_id1, "name": vg_name1},
                        {"id": vg_id2, "name": vg_name2}]

    volume_group1 = {'type': 'Primary', 'protection_policy': None,
                     'is_protectable': True, 'is_importing': False,
                     'creation_timestamp': '2020-08-27T02:47:57.467+00:00',
                     'protection_policy_id': None,
                     'placement_rule': 'Same_Appliance',
                     'protection_data': {
                         'created_by_rule_name': None,
                         'family_id': '530fe228-30ce-4e20-a529-8532b28f31e8',
                         'source_id': None, 'source_timestamp': None,
                         'creator_type_l10n': 'User', 'creator_type': 'User',
                         'created_by_rule_id': None, 'copy_signature': None,
                         'parent_id': None, 'is_app_consistent': False,
                         'expiration_timestamp': None},
                     'volumes': [
                         {
                             'name': vol_name1,
                             'id': vol_id1
                         }
                     ],
                     'name': vg_name1,
                     'is_write_order_consistent': True,
                     'migration_session_id': None, 'type_l10n': 'Primary',
                     'is_replication_destination': False,
                     'description': None, 'location_history': None,
                     'id': vg_id1
                     }

    invalid_vol_id = vol_id1[:len(vol_id1) - 3] + 'x' * 3
    volume_error = {
        404: {'messages': [{'arguments': ['{0}'.format(invalid_vol_id)],
                            'code': '0xE0A07001000C',
                            'message_l10n': 'The volume {0} is not '
                                            'found.'.format(invalid_vol_id),
                            'severity': 'Error'}]}
    }

    # VolumeGroup End

    # Host
    host_id1 = "ce15c82e-6e01-45ac-9886-49e3c55cca3c"
    host_name1 = "my_host1"

    host_id2 = "ccceadef-4c04-4b1b-a242-718eb68da7f8"
    host_name2 = "my_host2"

    host_list = [{"id": host_id1, "name": host_name1},
                 {"id": host_id2, "name": host_name2}]

    lun = 1

    initiator1 = "iqn.1998-01.com.vmware:lgloc1.52d1"
    create_host = {"id": host_id1}
    host1 = {'description': None, 'host_group_id': None,
             'os_type_l10n': 'ESXi', 'os_type': 'ESXi',
             'host_initiators': [
                 {'port_type': 'iSCSI',
                  'active_sessions': [],
                  'chap_single_username': '',
                  'chap_mutual_username': '',
                  'port_name': initiator1}
             ],
             'name': host_name1,
             'id': host_id1
             }

    invalid_initiator = {
        "name": "iqn.1998-01.com.vmware:lgloc187-4cfa37z6",
        "port_type": "iSCSI"
    }

    add_invalid_initiator_error = {
        400: {'messages': [{
            'code': '0xE0A01001000C',
            'message_l10n': 'Cannot add iqn since it already exists as part '
                            'of the host',
            'severity': 'Error'
        }]}}

    remove_invalid_initiator_error = {
        400: {'messages': [{
            'code': '0xE0A010010014',
            'message_l10n': 'Cannot remove the specified iqn since it does '
                            'not exist as part of the host.',
            'severity': 'Error'
        }]}}

    # Host End

    # HostGroup
    hg_id1 = "6066230c-cb5a-4cf2-90c6-92c5948af3d2"
    hg_name1 = "my_hostgroup1"

    hg_id2 = "938434c6-8bd3-4552-b540-702eab2a91e1"
    hg_name2 = "my_hostgroup2"

    hg_list = [{"id": hg_id1, "name": hg_name1},
               {"id": hg_id2, "name": hg_name2}]

    create_hg = {"id": hg_id1}
    hg1 = {
        'description': None, 'name': hg_name1,
        'hosts': [
            {'name': host_name1,
             'id': host_id1}
        ],
        'id': hg_id1
    }

    existing_hg_name = "Ansible_hg"
    invalid_host_id = host_id1[:len(host_id1) - 3] + 'x' * 3

    invalid_rename_error = {
        400: {
            'messages': [{'arguments': ['{0}'.format(existing_hg_name)],
                          'code': '0xE0A030010010',
                          'message_l10n': 'Host Group with name {0} already'
                                          ' exists'.format(existing_hg_name),
                          'severity': 'Error'
                          }]}}

    add_invalid_host_error = {
        400: {
            'messages': [{
                'arguments': ['{0}'.format(invalid_host_id)],
                'code': '0xE0A030010001',
                'message_l10n': 'Invalid host IDs provided '
                                '{0}'.format(invalid_host_id)
            }]}}

    # HostGroup End

    # ProtectionPolicy
    pol_id = "a78c08b0-d956-405f-aff8-d1d4c416a54d"

    pol_id1 = "f2803de5-e01f-4fd0-b3f3-aabf6d828a33"
    pol_name1 = "my_pp1"

    pol_id2 = "fdc44636-e735-42bc-8d93-e5855c32d71f"
    pol_name2 = "my_pp2"

    pol_list = [{"id": pol_id1, "name": pol_name1},
                {"id": pol_id2, "name": pol_name2}]

    invalid_pol_id = pol_id1[:len(pol_id1) - 3] + 'x' * 3

    policy_error = {
        404: {'messages': [{'arguments': ['{0}'.format(invalid_pol_id)],
                            'code': '0xE0A090010001',
                            'message_l10n': 'Unable to find the policy with ID '
                                            '{0}'.format(invalid_pol_id),
                            'severity': 'Error'}]}}

    pol_snap_rule_id = "f24c1295-f73f-48f3-8e82-3e45c5444fcc"
    pol_snap_rule_name = "my_sn_rule1"
    invalid_sr_id = pol_snap_rule_id[:len(pol_snap_rule_id) - 3] + 'x' * 3
    modify_description = "policy modified"

    protection_policy1 = {'type': 'Protection', 'description': '',
                          'replication_rules': [],
                          'name': pol_name1,
                          'id': pol_id1,
                          'snapshot_rules': [
                              {'name': pol_snap_rule_name,
                               'id': pol_snap_rule_id}]
                          }

    protection_policy1_modified = {'type': 'Protection',
                                   'description': modify_description,
                                   'replication_rules': [],
                                   'name': pol_name1,
                                   'id': pol_id1,
                                   'snapshot_rules': [
                                       {
                                           'name': pol_snap_rule_name,
                                           'id': pol_snap_rule_id}]
                                   }

    add_invalid_sr_error = {
        404: {'messages': [{'arguments': ['{0}'.format(invalid_sr_id)],
                            'code': '0xE0203001000B',
                            'message_l10n': 'The specified snapshot '
                                            'rule {0} is not found'.format(
                                invalid_sr_id),
                            'severity': 'Error'}]}
    }

    remove_invalid_sr_error = {
        404: {'messages': [{'arguments': ['{0}'.format(invalid_sr_id)],
                            'code': '0xE02020010007',
                            'message_l10n': 'Rule {0} does not exist in the '
                                            'policy'.format(invalid_sr_id),
                            'severity': 'Error'}]}
    }

    # ProtectionPolicy End

    # SnapshotRule
    snap_rule_id1 = "f24c1295-f73f-48f3-8e82-3e45c5444fcc"
    snap_rule_name1 = "my_sn_rule1"

    snap_rule_id2 = "f9362134-7f2a-43f0-98c4-48ad4ab2214f"
    snap_rule_name2 = "my_sn_rule2"

    snap_rule_list = [{"id": snap_rule_id1, "name": snap_rule_name1},
                      {"id": snap_rule_id2, "name": snap_rule_name2}]

    desired_retention1 = 40
    desired_retention2 = 72
    interval = "One_Day"
    invalid_interval = "Ten_Minutes"

    snap_rule1 = {'interval': interval, 'time_of_day': None,
                  'policies': [],
                  'desired_retention': desired_retention1,
                  'id': snap_rule_id1,
                  'name': snap_rule_name1,
                  'days_of_week': ['Sunday', 'Monday', 'Tuesday',
                                   'Wednesday', 'Thursday', 'Friday',
                                   'Saturday']}

    snap_rule1_modified = {'interval': interval, 'time_of_day': None,
                           'policies': [],
                           'desired_retention': desired_retention2,
                           'id': snap_rule_id1, 'name': snap_rule_name1,
                           'days_of_week': ['Sunday', 'Monday', 'Tuesday',
                                            'Wednesday', 'Thursday',
                                            'Friday', 'Saturday']}

    interval_error = {
        400: {'messages': [{
            'severity': 'Error', 'message_l10n': 'Invalid REST request.',
            'code': '0xE04040010005'
        }]}}

    # SnapshotRule End

    # NASServer
    nas_id1 = "5ef3ade5-b532-27a5-1f2d-3286ff9e3ccf"
    nas_name1 = "my_nas1"

    nas_id2 = "fdc44636-e735-42bc-8d93-e5855c32d71f"
    nas_name2 = "my_pp2"

    nas_list = [{"id": nas_id1, "name": nas_name1},
                {"id": nas_id2, "name": nas_name2}]

    nas_detail = {'backup_IPv4_interface_id': None, 'id': nas_id1,
                  'backup_IPv6_interface_id': None, 'name': nas_name1,
                  'current_node_id': 'WN-D0169-appliance-1-node-B',
                  'current_preferred_IPv4_interface_id': uuid,
                  'current_preferred_IPv6_interface_id': None,
                  'current_unix_directory_service': 'Local_Files',
                  'current_unix_directory_service_l10n': 'Local Files',
                  'default_unix_user': 'admin1', 'description': '',
                  'default_windows_user': 'admin1', 'file_nises': [],
                  'file_interfaces': [{'id': uuid, 'ip_address': '1.1.1.1',
                                       'name': 'test_name'}],
                  'file_ldaps': [{'id': uuid}], 'smb_servers': [{'id': uuid}],
                  'file_systems': [{'id': uuid, 'name': 'test_name'}],
                  'is_auto_user_mapping_enabled': True,
                  'is_username_translation_enabled': False,
                  'nfs_servers': [{'id': uuid}], 'preferred_node_id': 'A',
                  'operational_status': 'Started',
                  'operational_status_l10n': 'Started',
                  'production_IPv4_interface_id': None,
                  'production_IPv6_interface_id': None}

    nas_valid_param_list = [
        'name', 'description', 'current_node_id', 'preferred_node_id',
        'current_unix_directory_service', 'default_unix_user',
        'default_windows_user', 'is_username_translation_enabled',
        'is_auto_user_mapping_enabled', 'production_IPv4_interface_id',
        'production_IPv6_interface_id', 'backup_IPv4_interface_id',
        'backup_IPv6_interface_id']

    nas_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    nas_error = {
        400: {'messages': [{'arguments': ['Object instance has properties '
                                          'which are not allowed by the '
                                          'schema.'],
                            'code': '0xE04040030001',
                            'message_l10n': 'Validation failed: Object '
                                            'instance has properties which '
                                            'are not allowed by the schema.',
                            'severity': 'Error'}]},
        404: {'messages': [{'code': '0xE080100D0001',
                            'message_l10n': 'Operation failed because '
                                            'NAS Server ID is invalid.',
                            'severity': 'Error'}]}
    }

    # NASServer End

    # NFSExport
    nfs_id1 = "5f3510ba-8691-5793-a9c3-3ec8892935fb"
    nfs_name1 = "my_nfs1"

    nfs_id2 = "5f351150-76c7-f0cf-fcc8-3ec8892935fb"
    nfs_name2 = "my_nfs2"

    nfs_list = [{"id": nfs_id1, "name": nfs_name1},
                {"id": nfs_id2, "name": nfs_name2}]

    create_nfs = {'id': nfs_id1}

    invalid_nfs = nfs_id1[:len(nfs_id1) - 3] + 'x' * 3

    nfs_detail = {'anonymous_GID': -2, 'anonymous_UID': -2,
                  'default_access': 'Root', 'default_access_l10n': 'Root',
                  'description': None,
                  'file_system': {'filesystem_type': 'Primary',
                                  'id': uuid,
                                  'name': 'nfs_ans_filesystem_sub',
                                  'nas_server': {'id': uuid,
                                                 'name': 'my_nas'}},
                  'id': nfs_id1, 'is_no_SUID': False, 'min_security': 'Sys',
                  'min_security_l10n': 'Sys', 'name': nfs_name1,
                  'nfs_owner_username': '0', 'no_access_hosts': [],
                  'path': '/nfs_ans_filesystem_sub', 'read_only_hosts': [],
                  'read_only_root_hosts': [], 'read_write_hosts': [],
                  'read_write_root_hosts': []}

    nfs_error = {
        400: {'messages': [{'arguments': ['Object instance has properties '
                                          'which are not allowed by the '
                                          'schema.'],
                            'code': '0xE04040030001',
                            'message_l10n': 'Validation failed: Object '
                                            'instance has properties which '
                                            'are not allowed by the schema.',
                            'severity': 'Error'}]},
        404: {'messages': [{'code': '0xE080100F0001',
                            'message_l10n': 'Operation failed because NFS '
                                            'Export ID is invalid. Enter a '
                                            'valid NFS Export ID and '
                                            'try again.',
                            'severity': 'Error'}]}
    }

    nfs_valid_param = (
        'description', 'default_access', 'min_security', 'no_access_hosts',
        'add_no_access_hosts', 'remove_no_access_hosts', 'read_only_hosts',
        'add_read_only_hosts', 'remove_read_only_hosts', 'anonymous_GID',
        'read_only_root_hosts', 'add_read_only_root_hosts', 'anonymous_UID',
        'remove_read_only_root_hosts', 'read_write_hosts', 'is_no_SUID',
        'add_read_write_hosts', 'remove_read_write_hosts',
        'read_write_root_hosts', 'add_read_write_root_hosts',
        'remove_read_write_root_hosts')

    # NFSExport End

    # SMBShare
    smb_id1 = "5efc3ec5-ea0d-58d9-e21b-42079d64ae37"
    smb_name1 = "my_smb1"

    smb_id2 = "5f293c02-4466-8e0b-14df-024f80ecffb0"
    smb_name2 = "my_smb2"

    smb_list = [{"id": smb_id1, "name": smb_name1},
                {"id": smb_id2, "name": smb_name2}]

    create_smb = {'id': smb_id1}

    invalid_smb_id = smb_id1[:len(smb_id1) - 3] + 'x' * 3

    smb_detail = {'description': None, 'id': smb_id1, 'name': smb_name1,
                  'file_system': {'filesystem_type': 'Primary',
                                  'id': uuid, 'name': 'sample_test',
                                  'nas_server': {'id': uuid, 'name': 'test'}},
                  'is_ABE_enabled': False, 'is_branch_cache_enabled': False,
                  'is_continuous_availability_enabled': True, 'umask': '022',
                  'is_encryption_enabled': False, 'path': '/sample',
                  'offline_availability': 'Manual'}

    smb_error = {
        404: {'messages': [{'code': '0xE08010140001',
                            'message_l10n': 'Operation failed because SMB '
                                            'Share ID is invalid. Enter a '
                                            'valid SMB Share ID and '
                                            'try again.',
                            'severity': 'Error'}]}
    }

    # SMBShare End

    # FileSystem
    fs_id1 = "5efc3ec5-ea0d-58d9-e21b-42079d64ae37"
    fs_name1 = "my_fs1"

    fs_id2 = "5f293c02-4466-8e0b-14df-024f80ecffb0"
    fs_name2 = "my_fs2"

    fs_list = [{"id": fs_id1, "name": fs_name1},
               {"id": fs_id2, "name": fs_name2}]

    create_filesystem = {'id': fs_id1}
    fs_detail = {'access_policy': 'Native', 'access_policy_l10n': 'Native',
                 'access_type': None, 'access_type_l10n': None,
                 'creation_timestamp': None, 'creator_type': None,
                 'creator_type_l10n': None, 'default_hard_limit': 0,
                 'default_soft_limit': 0, 'description': None,
                 'expiration_timestamp': None, 'filesystem_type': 'Primary',
                 'filesystem_type_l10n': 'Primary File system',
                 'folder_rename_policy': 'All_Forbidden',
                 'folder_rename_policy_l10n': 'All Renames Forbidden',
                 'grace_period': 604800, 'id': fs_id1,
                 'is_async_MTime_enabled': False, 'is_modified': None,
                 'is_quota_enabled': False, 'is_smb_no_notify_enabled': False,
                 'is_smb_notify_on_access_enabled': False,
                 'is_smb_notify_on_write_enabled': False,
                 'is_smb_op_locks_enabled': True,
                 'is_smb_sync_writes_enabled': False,
                 'last_refresh_timestamp': None, 'parent_id': None,
                 'last_writable_timestamp': None,
                 'locking_policy': 'Advisory', 'name': fs_name1,
                 'locking_policy_l10n': 'Advisory',
                 'nas_server': {'id': nas_id1, 'name': nas_name1},
                 'protection_policy': None, 'size_total': size_total,
                 'size_used': size_used, 'smb_notify_on_change_dir_depth': 512}

    fs_snap_id = "5efc3ec5-ea0d-58d9-e21b-42079d64ae37"
    fs_snap_name = "my_fs_snap"
    create_filesystem_snap = {'id': fs_snap_id}
    fs_snap_detail = fs_detail
    fs_snap_list = [{'id': fs_snap_id, 'name': fs_snap_name}]

    # fs which does not exists
    invalid_fs_id = fs_id1[:len(fs_id1) - 3] + 'x' * 3
    # fs which has snapshot created on it
    fs_id_with_snap = "5f488eb1-c75e-a704-e53a-c6f547282e76"
    fs_error = {
        404: {'messages': [{'code': '0xE08010080001',
                            'message_l10n': 'Operation failed because File '
                                            'System ID is invalid. Enter a valid File System '
                                            'ID and try again.',
                            'severity': 'Error'}]},
        422: {'messages': [{'arguments': ['[File system delete rejected due '
                                          'to existing snap(s).]'],
                            'code': '0xE08010080003',
                            'message_l10n': 'Deletion of File System failed '
                                            'as, [File system delete rejected '
                                            'due to existing snap (s).]',
                            'severity': 'Error'}]}}

    # FileSystem End

    # TreeQuota
    tq_id1 = "00000004-05eb-0000-0d00-000000000000"
    tq_path1 = "/my_tq1"

    tq_id2 = "00000004-05eb-0000-0e00-000000000000"
    tq_path2 = "/my_tq2"

    tq_list = [{"id": tq_id1, "name": tq_path1},
               {"id": tq_id2, "name": tq_path2}]

    create_tree_quota = {'id': tq_id1}

    invalid_tq_id = tq_id1[:len(tq_id1) - 3] + 'x' * 3

    tq_valid_param = ('file_system_id', 'path', 'description', 'hard_limit',
                      'soft_limit', 'is_user_quotas_enforced')

    tq_error = {
        400: {'messages': [{'arguments': ['Object instance has properties '
                                          'which are not allowed by the '
                                          'schema'],
                            'code': '0xE04040030001',
                            'message_l10n': 'Validation failed: Object '
                                            'instance has properties which '
                                            'are not allowed by the schema',
                            'severity': 'Error'}]},
        404: {'messages': [{'code': '0xE08010090001',
                            'message_l10n': 'Operation failed because File '
                                            'Tree Quota ID is invalid. Enter '
                                            'a valid File Tree Quota id and '
                                            'try again.',
                            'severity': 'Error'}]}
    }

    tq_detail = {'description': 'sample', 'hard_limit': 0, 'id': tq_id1,
                 'file_system': {'filesystem_type': 'Primary',
                                 'id': uuid,
                                 'name': 'f1s',
                                 'nas_server': {'id': uuid, 'name': 'nas1'}},
                 'is_user_quotas_enforced': False, 'path': '/sample',
                 'remaining_grace_period': -1, 'size_used': 0,
                 'soft_limit': 0, 'state': 'Ok'}

    # TreeQuota End

    # UserQuota
    uq_id1 = "00000003-0066-0000-0100-000039300000"
    uq_id2 = "00000003-0066-0000-0100-0000d2040000"

    uq_list = [{'id': uq_id1}, {'id': uq_id2}]

    create_user_quota = {'id': uq_id1}

    uq_valid_param = ('file_system_id', 'tree_quota_id', 'uid', 'unix_name',
                      'windows_name', 'windows_sid', 'hard_limit',
                      'soft_limit')

    uq_error = {
        400: {'messages': [{'arguments': ['Object instance has properties '
                                          'which are not allowed by the '
                                          'schema'],
                            'code': '0xE04040030001',
                            'message_l10n': 'Validation failed: Object '
                                            'instance has properties which '
                                            'are not allowed by the schema',
                            'severity': 'Error'}]}
    }

    uq_detail = {'file_system': {'filesystem_type': 'Primary', 'id': uuid,
                                 'name': 'sample',
                                 'nas_server': {'id': uuid, 'name': 'nas1'}},
                 'hard_limit': 0, 'id': uq_id1, 'remaining_grace_period': -1,
                 'size_used': 2097152, 'soft_limit': 4194304, 'state': 'Ok',
                 'state_l10n': 'Ok', 'tree_quota': None, 'tree_quota_id': None,
                 'uid': 1, 'unix_name': None, 'windows_name': None,
                 'windows_sid': None}

    # Replication session
    rep_session_id_1 = "2754bad0-cfcd-4796-a06b-78368bad1cd7"
    rep_session_id_2 = "3186cad5-brej-8016-s53c-69457cad3ej9"

    rep_session_list = [{'id': rep_session_id_1}, {'id': rep_session_id_2}]

    rep_session_valid_param = ('volume_group', 'volume', 'session_id',
                               'session_state')
    rep_session_error = {

        400: {"messages": [{"code": "0xE04040030001", "severity": "Error",
                            "message_l10n": "Validation failed: Object instance"
                                            " has properties which are not "
                                            "allowed by the schema: [dupe_is"
                                            "_planned].",
                            "arguments": ["Object instance has properties w"
                                          "hich are not allowed by the schema:"
                                          " [dupe_is_planned]"]}]},
        404: {"messages": [{
            "code": "0xE04040020009",
            "severity": "Error",
            "message_l10n": "Instance with id "
                            "2754bad0-cfcd-4796-a06b-78368bad1cd "
                            "was not found.",
            "arguments": [
                "2754bad0-cfcd-4796-a06b-78368bad1cd"
            ]}]}
    }
    rep_session_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"

    rep_session_details_1 = {
        "id": "2754bad0-cfcd-4796-a06b-78368bad1cd7",
        "state": "OK",
        "role": "Source",
        "resource_type": "volume_group",
        "last_sync_timestamp": "2021-06-11T02:16:22.909+00:00",
        "local_resource_id": "aa352e0d-8048-423f-b50a-8b61f482365e",
        "remote_resource_id": "21f7ae54-0639-4b09-af4f-183d26b31237",
        "remote_system_id": "f07be373-dafd-4a46-8b21-f7cf790c287f",
        "progress_percentage": None,
        "estimated_completion_timestamp": None,
        "replication_rule_id": "55d14477-de22-4d39-b24d-07cf08ba329f",
        "last_sync_duration": 218,
        "next_sync_timestamp": None,
        "storage_element_pairs": None,
        "failover_test_in_progress": None,
        "state_l10n": "OK",
        "role_l10n": "Source",
        "resource_type_l10n": "Volume Group",
        "replication_rule": {
            "name": "ansible_rep_rule",
            "id": "55d14477-de22-4d39-b24d-07cf08ba329f"
        },
        "migration_session": None,
        "remote_system": {
            "name": "WN-D8978",
            "id": "f07be373-dafd-4a46-8b21-f7cf790c287f"
        }
    }

    # replication session end

    # replication rule start
    rep_rule_id_1 = "55d14477-de22-4d39-b24d-07cf08ba329f"
    rep_rule_name_1 = "ansible_rep_rule_1"

    rep_rule_id_2 = "20242441-4d8b-424f-b6b3-058ad02f5f9d"
    rep_rule_name_2 = "ansible_rep_rule_2"

    rep_rule_list = [{"id": rep_rule_id_1, "name": rep_rule_name_1},
                     {"id": rep_rule_id_2, "name": rep_rule_name_2}]

    create_rep_rule = {'id': rep_rule_id_1}

    alert_threshold = 30
    invalid_alert_threshold = "36"
    new_alert_threshold = 40
    remote_system_id = "f07be373-dafd-4a46-8b21-f7cf790c287f"
    rpo = "One_Hour"

    rep_rule_error = {
        400: {"messages": [{"code": "0xE04040030001",
                            "severity": "Error",
                            "message_l10n":
                                "Validation failed: [Path '/alert_threshold'] "
                                "Instance type (string) does not match any "
                                "allowed primitive type (allowed: [integer])."
                               , "arguments":
                                ["[Path '/alert_threshold'] Instance type "
                                 "(string) does not match any allowed "
                                 "primitive type (allowed: [integer])"]}]}
    }

    rep_rule_details_1 = {
        "id": "55d14477-de22-4d39-b24d-07cf08ba329f",
        "name": "ansible_rep_rule",
        "rpo": "One_Hour",
        "remote_system_id": "f07be373-dafd-4a46-8b21-f7cf790c287f",
        "is_replica": False,
        "alert_threshold": 30,
        "rpo_l10n": "One Hour"
    }
    # replication rule end

    # network start

    network_id2 = "NW1"
    network_name2 = "Default Management Network"

    network_id1 = "NW2"
    network_name1 = "Default Storage Network"
    network_list = [
        {"id": network_id1, "name": network_name1},
        {"id": network_id2, "name": network_name2}
    ]

    add_ip_ports = ["IP9"]

    network_details_1 = {
        "id": "NW2",
        "type": "Storage",
        "name": "Default Storage Network",
        "ip_version": "IPv4",
        "purposes": [
            "ISCSI"
        ],
        "vlan_id": 0,
        "prefix_length": 24,
        "gateway": "10.230.42.1",
        "mtu": 1400,
        "type_l10n": "Storage",
        "ip_version_l10n": "IPv4",
        "purposes_l10n": [
            "iSCSI"
        ]
    }

    network_valid_param_list = [
        'name', 'vlan_id', 'gateway', 'prefix_length', 'mtu',
        'new_cluster_mgmt_address', 'storage_discovery_address', 'addresses',
        'ports', 'vasa_provider_credentials', 'esxi_credentials',
        'add_port_ids', 'remove_port_ids']

    network_does_not_exist = 'NW20'
    network_error = {
        400: {'messages': [{'arguments': ['Object instance has properties '
                                          'which are not allowed by the '
                                          'schema.'],
                            'code': '0xE04040030001',
                            'message_l10n': 'Validation failed: Object '
                                            'instance has properties which '
                                            'are not allowed by the schema.',
                            'severity': 'Error'}]},
        404: {'messages': [{'code': '0xE04040020009',
                            'message_l10n': 'Instance with id NW20 was not '
                                            'found.',
                            'severity': 'Error'}]}
    }
    # network end

    # installed software start

    software_list = [{'release_version': '2.0.0.0'},
                     {'release_version': '2.0.0.0'}]

    # installed software end

    # job start

    job_id1 = 'dfb47ef3-7ade-4b75-951a-34163c4e55d6'
    job_does_not_exist = 'dfb47ef3-7ade-4b75-951a-34163c4e55d9'
    job_details = {
        "id": "dfb47ef3-7ade-4b75-951a-34163c4e55d6",
        "resource_action": "modify",
        "resource_type": "network",
        "resource_id": "NW1",
        "resource_name": None,
        "description_l10n": "Modify network parameters.",
        "state": "COMPLETED",
        "start_time": "2021-08-30T06:06:25.846+00:00",
        "phase": "Completed",
        "end_time": "2021-08-30T06:06:46.828+00:00",
        "estimated_completion_time": None,
        "progress_percentage": 100,
        "parent_id": None,
        "root_id": "dfb47ef3-7ade-4b75-951a-34163c4e55d6",
        "user": "admin",
        "response_body": None,
        "response_status": None,
        "step_order": 2093821,
        "resource_action_l10n": "modify",
        "resource_type_l10n": "network",
        "state_l10n": "Completed",
        "phase_l10n": "Completed",
        "response_status_l10n": None
    }

    job_error = {
        404: {
            'messages':
                [{'code': '0xE04040020009',
                  'message_l10n': 'Instance with id '
                                  'dfb47ef3-7ade-4b75-951a-34163c4e55d9 was '
                                  'not found.',
                  'severity': 'Error'}]}
    }
    # job end

    # vcenter start

    vcenter_id1 = '42d08c86-f958-4fbb-82f0-3ce1a5d99d1e'
    vcenter_list = [{"id": '42d08c86-f958-4fbb-82f0-3ce1a5d99d1e'}]
    vasa_provider_credentials = {
        "username": "vmadmin",
        "password": "Password123!"
    }
    vcenter_details = {
        "id": "42d08c86-f958-4fbb-82f0-3ce1a5d99d1e",
        "instance_uuid": "3b33039f-908f-4d1a-a0ca-1d2fd050a09b",
        "address": "vpi2197.pie.lab.emc.com",
        "username": "administrator@vsphere.local",
        "vendor_provider_status": "Online",
        "vendor_provider_status_l10n": "Online"
    }

    # vcenter end

    # IP pool address start

    ip_pool_list = [
        {'id': 'IP16', 'name': 'iSCI (10.230.42.94)', 'network_id': 'NW6',
         'ip_port_id': 'IP_PORT16', 'appliance_id': 'A1', 'node_id': 'N2',
         'address': '10.230.42.94',
         'purposes': ['Storage_Iscsi_Target', 'External_Replication_Iscsi'],
         'purposes_l10n': ['Storage Iscsi Target',
                           'External Replication iSCSI Port']},
        {'id': 'IP17', 'name': 'iSCI (10.230.42.95)', 'network_id': 'NW6',
         'ip_port_id': 'IP_PORT6', 'appliance_id': 'A1', 'node_id': 'N1',
         'address': '10.230.42.95',
         'purposes': ['Storage_Iscsi_Target', 'External_Replication_Iscsi'],
         'purposes_l10n': ['Storage Iscsi Target',
                           'External Replication iSCSI Port']},
        {'id': 'IP22', 'name': 'iSCI (10.230.42.96)', 'network_id': 'NW6',
         'ip_port_id': 'IP_PORT8', 'appliance_id': 'A1', 'node_id': 'N2',
         'address': '10.230.42.96', 'purposes': ['Storage_Iscsi_Target'],
         'purposes_l10n': ['Storage Iscsi Target']},
        {'id': 'IP23', 'name': 'iSCI (10.230.42.97)', 'network_id': 'NW6',
         'ip_port_id': 'IP_PORT15', 'appliance_id': 'A1', 'node_id': 'N1',
         'address': '10.230.42.97', 'purposes': ['Storage_Iscsi_Target'],
         'purposes_l10n': ['Storage Iscsi Target']}
    ]

    # IP pool address end

    # IP port start

    ip_port_id = "IP_PORT1"
    ip_port_details = {
        "id": "IP_PORT1",
        "partner_id": "IP_PORT14",
        "target_iqn": "iqn.2015-10.com.dell:dellemc-powerstore-fnm00194601320-a-2fa9868f",
        "available_usages": [
            "ISCSI"
        ],
        "current_usages": [],
        "bond_id": None,
        "eth_port_id": "c16f9febf1704297a0a3c721e71864d0",
        "veth_port_id": None,
        "available_usages_l10n": [
            "iSCSI"
        ],
        "current_usages_l10n": None
    }

    # IP port end

    # Local user start

    local_user_id1 = "7"
    local_user_name1 = "ansibleuser7"

    local_user_id2 = "8"
    local_user_name2 = "ansibleuser8"

    local_user_does_not_exist = "20"
    local_user_list = [
        {"id": local_user_id1, "name": local_user_name1},
        {"id": local_user_id2, "name": local_user_name2}
    ]

    local_user_details = {
        "id": "7",
        "name": "ansibleuser7",
        "is_built_in": False,
        "is_locked": True,
        "is_default_password": False,
        "local_domain_id": "1",
        "role_id": "3",
        "user_preference": None
    }

    local_user_create_params = {
        "name": "ansibleuser7",
        "password": "Password123!",
        "role_id": "3"
    }

    local_user_create_response = {
        "id": local_user_id1
    }

    local_user_valid_param_list = [
        'role_id', 'is_locked', 'current_password', 'password'
    ]

    local_user_error = {
        404: {
            "messages": [
                {
                    "code": "0xE09040040001",
                    "severity": "Error",
                    "message_l10n": "Error while getting local users!"
                }
            ]
        },

        400: {
            "messages": [{"code": "0xE04040030001", "severity": "Error",
                          "message_l10n": "Validation failed: Object instance"
                                          " has properties which are not "
                                          "allowed by the schema: "
                                          "[\"invalid_key\"].",
                          "arguments": [
                              "Object instance has properties which are not "
                              "allowed by the schema: [\"invalid_key\"]"]}]
        }
    }

    # Local user end

    # role start

    role_id2 = "1"
    role_name2 = "Administrator"

    role_id1 = "2"
    role_name1 = "Storage Administrator"
    role_list = [
        {"id": role_id1, "name": role_name1},
        {"id": role_id2, "name": role_name2}
    ]

    role_details_1 = {
        "id": "2",
        "name": "Storage Administrator",
        "is_built_in": True,
        "description": "Can view status and performance information and can"
                       " modify most systemsettings, but cannot configure new"
                       " storage hosts or manage local user"
    }

    role_does_not_exist = '20'
    role_error = {
        404: {
            "messages": [
                {
                    "code": "0xE09040050001",
                    "severity": "Error",
                    "message_l10n": "Role object does not exist!"
                }
            ]
        }
    }
    # role end

    # appliance start
    appliance_id1 = "A1"
    appliance_name1 = "Appliance-WND8977"
    appliance_list = [
        {"id": appliance_id1, "name": appliance_name1}
    ]
    appliance_details_1 = {
        "id": "A1",
        "name": "Appliance-WND8977",
        "service_tag": "FX60643",
        "express_service_code": "34657204467",
        "model": "PowerStore 1000T",
        "nodes": [
            {
                "id": "N1"
            },
            {
                "id": "N2"
            }
        ],
        "veth_ports": [],
        "maintenance_windows": [
            {
                "id": "1"
            }
        ],
        "fc_ports": [
            {
                "id": "303c29acbe394e26b297e6da808cd076"
            }
        ],
        "sas_ports": [
            {
                "id": "69227e02e17046c4a35d930010a12a71"
            }
        ],
        "eth_ports": [
            {
                "id": "7dd7a6f96af6430aaffe58ecd187909a"
            }
        ],
        "software_installed": [
            {
                "id": "8027d12c-db31-4c0f-9dcb-b9ee105bc753"
            }
        ],
        "virtual_volumes": [
            {
                "id": "2f22931c-5fdb-49f3-a733-85dacd389191"
            }
        ],
        "hardware": [
            {
                "id": "d594e3856aa145cba6af2f2c80856f7f"
            }
        ],
        "volumes": [
            {
                "id": "3a1666b1-8d72-42d2-9d58-fe2f4bf8e288"
            }

        ],
        "ip_pool_addresses": [
            {
                "id": "IP16"
            }
        ]
    }

    appliance_does_not_exist = 'A2'
    appliance_error = {
        404: {
            "messages": [
                {
                    "code": "0xE04040020009",
                    "severity": "Error",
                    "message_l10n": "Instance with id A2 was not found.",
                    "arguments": [
                        "A2"
                    ]
                }
            ]
        }
    }
    # appliance end
    # cluster start
    cluster_name_1 = "WN-D8977"
    cluster_id_1 = "0"
    cluster_list = [
        {"id": cluster_id_1, "name": cluster_name_1}
    ]
    cluster_details_1 = {
        "id": "0",
        "global_id": "PS00d01e1bb312",
        "name": "WN-D8977",
        "physical_mtu": 1500,
        "master_appliance_id": "A1",
        "state": "Configured",
        "appliance_count": 1,
        "management_address": "10.230.24.33",
        "is_encryption_enabled": True,
        "storage_discovery_address": "10.230.42.228",
        "compatibility_level": 10,
        "state_l10n": "Configured"
    }
    invalid_cluster_id = '10'
    cluster_error = {
        404: {
            "messages": [
                {
                    "code": "0xE0C01003000E",
                    "severity": "Error",
                    "message_l10n": "Invalid Cluster ID provided,"
                                    " Cluster ID: 10",
                    "arguments": [
                        "10"
                    ]
                }
            ]
        }
    }

    # cluster end

    # service config start
    service_config_id_1 = "A1"
    service_config_appliance_id = 'A1'
    service_config_list = [
        {"id": service_config_id_1}
    ]
    service_config_details_1 = {
        "id": "A1",
        "appliance_id": "A1",
        "is_ssh_enabled": True
    }
    invalid_service_config_id = '10'
    service_config_error = {
        404: {
            "messages": [
                {
                    "code": "0xE09030010003",
                    "severity": "Error",
                    "message_l10n": "Appliance id does not exist"
                }
            ]
        }
    }
    # service config end

    # service user start
    service_user_id_1 = "1"
    service_user_name_1 = 'service'
    service_user_list = [
        {"id": service_user_id_1, 'name': service_user_name_1}
    ]
    service_user_details_1 = {
        "id": "1",
        "name": "service",
        "is_built_in": True,
        "is_default_password": False
    }
    invalid_service_user_id = '10'
    service_user_error = {
        404: {
            "messages": [
                {
                    "code": "0xE09040070001",
                    "severity": "Error",
                    "message_l10n": "Service User object with given id "
                                    "does not exist!"
                }
            ]
        }
    }
    # service user end

    # chap config start
    chap_config_id_1 = "0"
    chap_config_list = [
        {"id": chap_config_id_1}
    ]
    chap_config_details_1 = {
        "id": "0",
        "mode": "Disabled",
        "mode_l10n": "Disabled"
    }
    invalid_chap_config_id = '3'
    chap_config_error = {
        404: {
            "messages": [
                {
                    "code": "0xE0C01003000D",
                    "severity": "Error",
                    "message_l10n": "CHAP Configuration 3 not found",
                    "arguments": [
                        "3"
                    ]
                }
            ]
        }
    }

    # chap config end
