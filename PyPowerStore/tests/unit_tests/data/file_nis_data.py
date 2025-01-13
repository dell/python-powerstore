class FileNISData():

    file_nis_id = "file_nis_id_1"

    file_nis_list = [{"id": "65980542-4726-58be-a83c-62b767ad9845",
                      "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
                      "domain": "sample_nas_1",
                      "ip_addresses": [
                          "10.10.10.10"
                      ],
                      "is_destination_override_enabled": False,
                      "source_parameters": None}]

    nas_server_id = "6581683c-61a3-76ab-f107-62b767ad9845"
    nas_server_name = "my_nas1"

    file_nis_detail = {"id": "65980542-4726-58be-a83c-62b767ad9845",
                       "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
                       "domain": "sample_nas_1",
                       "ip_addresses": [
                           "10.10.10.10"
                       ],
                       "is_destination_override_enabled": False,
                       "source_parameters": None}

    file_nis_valid_param_list = [
        "nas_server_id",
        "domain",
        "ip_addresses",
        "add_ip_addresses",
        "remove_ip_addresses"]

    file_nis_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    file_nis_error = {
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
                                            'file NIS ID is invalid.',
                            'severity': 'Error'}]}
    }
