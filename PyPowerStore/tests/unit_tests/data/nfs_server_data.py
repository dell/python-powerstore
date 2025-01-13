class NFSServerData():

    nfs_server_id = "nfs_server_id_1"

    nfs_server_list = [{
        "id": "651067eb-a31c-0111-beb2-aa9ad36bce41",
        "host_name": None,
        "nas_server_id": "651067dc-5a14-a3c2-d031-0e1089268650",
        "is_nfsv3_enabled": True,
        "is_nfsv4_enabled": True,
        "is_secure_enabled": False,
        "is_use_smb_config_enabled": None,
        "service_principal_name": None,
        "is_joined": False,
        "is_extended_credentials_enabled": False,
        "credentials_cache_TTL": 15
    }]

    nas_server_id = "651067dc-5a14-a3c2-d031-0e1089268650"
    nas_server_name = "my_nas1"

    nfs_server_detail = {
        "id": "651067eb-a31c-0111-beb2-aa9ad36bce41",
        "host_name": None,
        "nas_server_id": "651067dc-5a14-a3c2-d031-0e1089268650",
        "is_nfsv3_enabled": True,
        "is_nfsv4_enabled": True,
        "is_secure_enabled": False,
        "is_use_smb_config_enabled": None,
        "service_principal_name": None,
        "is_joined": False,
        "is_extended_credentials_enabled": False,
        "credentials_cache_TTL": 15
    }

    nfs_server_valid_param_list = [
        "nas_server_id","host_name","is_nfsv3_enabled","is_nfsv4_enabled",
        "is_secure_enabled","is_use_smb_config_enabled","is_extended_credentials_enabled",
        "is_skip_unjoin", "credentials_cache_TTL"]

    nfs_server_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    nfs_server_error = {
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
                                            'NFS Server ID is invalid.',
                            'severity': 'Error'}]}
    }
