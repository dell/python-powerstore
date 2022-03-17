class RemoteSupportData():

    remote_support_id = "0"

    remote_support_list = [{"id": remote_support_id}]

    modify_remote_support_dict={
        "type": "SRS_Integrated_Tier3"
    }

    verify_remote_support_dict={
        "type": "SRS_Integrated_Tier2"
    }

    remote_support_valid_param_list = [
        'id', 'type', 'remote_support_server', 'proxy_address', 'proxy_port', 'proxy_username', 'proxy_password',
        'is_cloudiq_enabled', 'is_rc_enabled', 'is_icw_configured'
    ]

    remote_support_error = {
        400: {
               "messages": [
                {
                    "code": "0xE04040030001",
                    "severity": "Error",
                    "message_l10n": "Validation failed: Object instance has properties which are not allowed by the schema: [\"invalid_param\"].",
                    "arguments": [
                        "Object instance has properties which are not allowed by the schema: [\"invalid_param\"]"
                    ]
                }
                ]
        }
    }

    remote_support_details = {
        "id": "0",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": True,
        "last_update": "2022-01-24T14:26:54.662+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "localhost",
                "port": 9443,
                "is_primary": True,
                "connectivity_qos": [
                    {
                        "id": "d72c0231-6d26-4170-a468-0b9d4af56f22",
                        "appliance_id": "A1",
                        "remote_support_servers_id": "0",
                        "last_update": "2022-01-24T14:27:01.239+00:00",
                        "connectivity_qos_value": 1.00,
                        "connectivity_qos": "Good",
                        "connectivity_qos_priority": 8
                     }
                 ]
             },
            {
                "id": "1",
                "remote_support_id": "0",
                "address": None,
                "port": None,
                "is_primary": False,
                "connectivity_qos": None
             }
        ],
        "proxy_address": "10.10.10.10",
        "proxy_port": 3128,
        "proxy_username": "user",
        "policy_manager_address": None,
        "policy_manager_port": None
    }

