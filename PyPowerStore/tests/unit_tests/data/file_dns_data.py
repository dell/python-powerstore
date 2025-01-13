class FileDNSData():

    file_dns_id = "file_dns_id_1"

    file_dns_list = [{
        "id": "659803db-6efb-7f98-ea8d-62b767ad9845",
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "domain": "abcd",
        "ip_addresses": [
            "10.10.10.10"
        ],
        "transport": "UDP",
        "is_destination_override_enabled": False,
        "source_parameters": None,
        "transport_l10n": "UDP"
    }]

    nas_server_id = "6581683c-61a3-76ab-f107-62b767ad9845"
    nas_server_name = "my_nas1"

    file_dns_detail = {
        "id": "659803db-6efb-7f98-ea8d-62b767ad9845",
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "domain": "abcd",
        "ip_addresses": [
            "10.10.10.10"
        ],
        "transport": "UDP",
        "is_destination_override_enabled": False,
        "source_parameters": None,
        "transport_l10n": "UDP"
    }

    file_dns_valid_param_list = [
        "nas_server_id",
        "domain",
        "ip_addresses",
        "add_ip_addresses",
        "remove_ip_addresses",
        "transport",
        "is_destination_override_enabled"]

    file_dns_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    file_dns_error = {
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
                                            'file DNS ID is invalid.',
                            'severity': 'Error'}]}
    }
