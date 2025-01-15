class SMBServerData:

    smb_server_id = "smb_server_id_1"

    smb_server_list = [
        {
            "id": "6597e7e8-50dc-7f52-1556-62b767ad9845",
            "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
            "computer_name": None,
            "domain": None,
            "netbios_name": "ABCD",
            "workgroup": "SAMPLE_NAS_1",
            "description": "sample_description",
            "is_standalone": True,
            "is_joined": False,
        }
    ]

    nas_server_id = "6581683c-61a3-76ab-f107-62b767ad9845"
    nas_server_name = "my_nas1"

    smb_server_detail = {
        "id": "6597e7e8-50dc-7f52-1556-62b767ad9845",
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "computer_name": None,
        "domain": None,
        "netbios_name": "ABCD",
        "workgroup": "SAMPLE_NAS_1",
        "description": "sample_description",
        "is_standalone": True,
        "is_joined": False,
    }

    smb_server_valid_param_list = [
        "nas_server_id",
        "is_standalone",
        "computer_name",
        "domain",
        "netbios_name",
        "workgroup",
        "description",
        "local_admin_password",
    ]

    smb_server_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    smb_server_error = {
        400: {
            "messages": [
                {
                    "arguments": [
                        "Object instance has properties "
                        "which are not allowed by the "
                        "schema."
                    ],
                    "code": "0xE04040030001",
                    "message_l10n": "Validation failed: Object "
                    "instance has properties which "
                    "are not allowed by the schema.",
                    "severity": "Error",
                }
            ]
        },
        404: {
            "messages": [
                {
                    "code": "0xE080100D0001",
                    "message_l10n": "Operation failed because "
                    "SMB server ID is invalid.",
                    "severity": "Error",
                }
            ]
        },
    }
