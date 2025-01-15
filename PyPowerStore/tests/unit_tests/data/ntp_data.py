class NtpData:

    ntp_id = "NTP1"

    ntp_list = [{"id": ntp_id}]

    modify_ntp_dict = {"addresses": ["XX.XX.XX.XX", "XX.XX.XX.YY"]}

    ntp_valid_param_list = ["id", "addresses"]

    ntp_error = {
        400: {
            "messages": [
                {
                    "code": "0xE04040030001",
                    "severity": "Error",
                    "message_l10n": 'Validation failed: Object instance has properties which are not allowed by the schema: ["invalid_param"].',
                    "arguments": [
                        'Object instance has properties which are not allowed by the schema: ["invalid_param"]',
                    ],
                },
            ],
        },
    }

    ntp_details = {"id": "ntp_id", "addresses": ["XX.XX.XX.XX", "XX.XX.XX.YY"]}
