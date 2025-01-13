class SecurityConfigData():

    security_config_id_1 = 1
    security_config_list = [
        {"id": security_config_id_1}
    ]
    security_config_details_1 = {
        "id": "1",
        "idle_timeout": 3600,
        "protocol_mode": "TLSv1_2",
        "protocol_mode_l10n": "TLSv1_2"
    }
    invalid_security_config_id = 10
    invalid_protocol_mode = 'TLSv1.222'

    security_config_error = {
        400: {
            "messages": [
                {
                    "code": "0xE04040010005",
                    "severity": "Error",
                    "message_l10n": "Invalid REST request."
                }
            ]
        },
        404: {
            "messages": [
                {
                    "code": "0xE09040060004",
                    "severity": "Error",
                    "message_l10n": "Security configuration object does "
                                    "not exist!"
                }
            ]
        }
    }
