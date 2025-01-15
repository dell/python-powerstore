class SNMPServerData:

    snmp_server_id = "snmp_server_id_1"

    snmp_server_list = [
        {
            "id": "2bf5709d-0466-437a-a28f-9d31f2fdfcc5",
            "ip_address": "127.0.0.1",
            "port": 162,
            "version": "V2c",
            "trap_community": "commnity",
            "alert_severity": "Info",
            "user_name": None,
            "auth_protocol": None,
            "privacy_protocol": None,
        },
        {
            "id": "54261519-c5c2-446a-ad76-5f4ca63581df",
            "ip_address": "100.96.32.85",
            "port": 162,
            "version": "V2c",
            "trap_community": "public",
            "alert_severity": "Info",
            "user_name": None,
            "auth_protocol": None,
            "privacy_protocol": None,
        },
        {
            "id": "789f4c09-9e15-4b44-a9f3-baf716172140",
            "ip_address": "10.250.230.45",
            "port": 162,
            "version": "V3",
            "trap_community": None,
            "alert_severity": "Info",
            "user_name": "test",
            "auth_protocol": "None",
            "privacy_protocol": "None",
        },
    ]

    snmp_server_detail = {
        "id": "789f4c09-9e15-4b44-a9f3-baf716172140",
        "ip_address": "10.250.230.45",
        "port": 162,
        "version": "V3",
        "trap_community": None,
        "alert_severity": "Info",
        "user_name": "test",
        "auth_protocol": "None",
        "privacy_protocol": "None",
    }

    snmp_server_valid_param_list = [
        "ip_address",
        "port",
        "version",
        "alert_severity",
        "trap_community",
    ]

    snmp_server_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    snmp_server_error = {
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
        422: {
            "messages": [
                {
                    "code": "0xE0F0101D0024",
                    "severity": "Error",
                    "message_l10n": "Server Record Not Found, id: c5fdeb93-42ed-4ec9-988e-daec2974f2fk",
                    "arguments": ["c5fdeb93-42ed-4ec9-988e-daec2974f2fk"],
                }
            ]
        },
    }
