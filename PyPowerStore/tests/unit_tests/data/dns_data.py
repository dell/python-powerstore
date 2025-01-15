class DnsData:

    dns_id = "DNS1"

    dns_list = [{"id": dns_id}]

    modify_dns_dict = {"addresses": ["XX.XX.XX.XX", "XX.XX.XX.YY"]}

    dns_valid_param_list = ["id", "addresses"]

    dns_error = {
        400: {
            "messages": [
                {
                    "code": "0xE04040030001",
                    "severity": "Error",
                    "message_l10n": 'Validation failed: Object instance has \
                        properties which are not allowed by the schema: ["invalid_param"].',
                    "arguments": [
                        'Object instance has properties which are not allowed by \
                            the schema: ["invalid_param"]',
                    ],
                },
            ],
        },
    }

    dns_details = {"id": "dns_id", "addresses": ["XX.XX.XX.XX", "XX.XX.XX.YY"]}
