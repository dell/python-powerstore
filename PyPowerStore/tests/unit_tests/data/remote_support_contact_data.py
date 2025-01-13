class RemoteSupportContactData():

    remote_support_contact_id = "0"

    remote_support_contact_list = [{"id": remote_support_contact_id}]

    modify_remote_support_contact_dict = {
        "first_name": "abc"
    }

    remote_support_contact_valid_param_list = [
        'id', 'first_name', 'last_name', 'email', 'phone'
    ]

    remote_support_contact_error = {
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

    remote_support_contact_details = {
        "id": "0",
        "first_name": "abc",
        "last_name": "xyz",
        "email": "abc_xyz@dell.com",
        "phone": "111-222-333-444",
        "system_location": ""
    }
