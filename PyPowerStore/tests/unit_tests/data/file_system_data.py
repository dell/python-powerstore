class FileSystemData:
    # FileSystem
    fs_id1 = "5efc3ec5-ea0d-58d9-e21b-42079d64ae37"
    fs_name1 = "my_fs1"

    fs_id2 = "5f293c02-4466-8e0b-14df-024f80ecffb0"
    fs_name2 = "my_fs2"

    fs_list = [{"id": fs_id1, "name": fs_name1}, {"id": fs_id2, "name": fs_name2}]
    nas_id1 = "5ef3ade5-b532-27a5-1f2d-3286ff9e3ccf"
    nas_name1 = "my_nas1"
    size_used = 1623195648
    size_total = 5368709120
    size = 1048576
    create_filesystem = {"id": fs_id1}
    fs_detail = {
        "access_policy": "Native",
        "access_policy_l10n": "Native",
        "access_type": None,
        "access_type_l10n": None,
        "creation_timestamp": None,
        "creator_type": None,
        "creator_type_l10n": None,
        "default_hard_limit": 0,
        "default_soft_limit": 0,
        "description": None,
        "expiration_timestamp": None,
        "filesystem_type": "Primary",
        "filesystem_type_l10n": "Primary File system",
        "folder_rename_policy": "All_Forbidden",
        "folder_rename_policy_l10n": "All Renames Forbidden",
        "grace_period": 604800,
        "id": fs_id1,
        "is_async_MTime_enabled": False,
        "is_modified": None,
        "is_quota_enabled": False,
        "is_smb_no_notify_enabled": False,
        "is_smb_notify_on_access_enabled": False,
        "is_smb_notify_on_write_enabled": False,
        "is_smb_op_locks_enabled": True,
        "is_smb_sync_writes_enabled": False,
        "last_refresh_timestamp": None,
        "parent_id": None,
        "last_writable_timestamp": None,
        "locking_policy": "Advisory",
        "name": fs_name1,
        "locking_policy_l10n": "Advisory",
        "nas_server": {"id": nas_id1, "name": nas_name1},
        "protection_policy": None,
        "size_total": size_total,
        "size_used": size_used,
        "smb_notify_on_change_dir_depth": 512,
    }

    fs_snap_id = "5efc3ec5-ea0d-58d9-e21b-42079d64ae37"
    fs_snap_name = "my_fs_snap"
    create_filesystem_snap = {"id": fs_snap_id}
    fs_snap_detail = fs_detail
    fs_snap_list = [{"id": fs_snap_id, "name": fs_snap_name}]

    # fs which does not exists
    invalid_fs_id = fs_id1[: len(fs_id1) - 3] + "x" * 3
    # fs which has snapshot created on it
    fs_id_with_snap = "5f488eb1-c75e-a704-e53a-c6f547282e76"
    fs_error = {
        404: {
            "messages": [
                {
                    "code": "0xE08010080001",
                    "message_l10n": "Operation failed because File "
                    "System ID is invalid. Enter a valid File System "
                    "ID and try again.",
                    "severity": "Error",
                }
            ]
        },
        422: {
            "messages": [
                {
                    "arguments": [
                        "[File system delete rejected due " "to existing snap(s).]"
                    ],
                    "code": "0xE08010080003",
                    "message_l10n": "Deletion of File System failed "
                    "as, [File system delete rejected "
                    "due to existing snap (s).]",
                    "severity": "Error",
                }
            ]
        },
    }

    # FileSystem End
