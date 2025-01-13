class FileInterfaceData():

    file_interface_id = "file_interface_id_1"

    file_interface_list = [
        {
            "id": "651067ea-dff5-099d-6aea-0e1089268650",
            "nas_server_id": "651067dc-5a14-a3c2-d031-0e1089268650",
            "ip_address": "10.10.10.10",
            "prefix_length": 21,
            "gateway": "10.10.10.1",
            "vlan_id": 0,
            "name": "PROD001_19c8adfb1d41_4",
            "role": "Production",
            "is_disabled": False,
            "is_destination_override_enabled": False,
            "ip_port_id": "IP_PORT6",
            "source_parameters": None,
            "is_dr_test": False,
            "role_l10n": "Production"}]

    nas_server_id = "651067dc-5a14-a3c2-d031-0e1089268650"
    nas_server_name = "my_nas1"
    ip_address = "10.10.10.10"

    file_interface_detail = {
        "id": "651067ea-dff5-099d-6aea-0e1089268650",
        "nas_server_id": "651067dc-5a14-a3c2-d031-0e1089268650",
        "ip_address": "10.10.10.10",
        "prefix_length": 21,
        "gateway": "10.10.10.1",
        "vlan_id": 0,
        "name": "PROD001_19c8adfb1d41_4",
        "role": "Production",
        "is_disabled": False,
        "is_destination_override_enabled": False,
        "ip_port_id": "IP_PORT6",
        "source_parameters": None,
        "is_dr_test": False,
        "role_l10n": "Production"}

    file_interface_valid_param_list = [
        "nas_server_id", "ip_address", "prefix_length",
        "gateway", "vlan_id", "role", "is_disabled", "ip_port_id"]

    file_interface_id_not_exist = "5f4a3017-0bad-899e-e1eb-c6f547282e66"
    file_interface_error = {
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
                                            'file interface ID is invalid.',
                            'severity': 'Error'}]}
    }
