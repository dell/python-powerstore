class EmailData():

    email_id_1 = "55d14477-de22-4d39-b24d-07cf08ba329f"
    email_address_1 = "abc_xyz@dell.com"

    email_id_2 = "20242441-4d8b-424f-b6b3-058ad02f5f9d"
    email_address_2 = "def_xyz@dell.com"

    email_list = [{"id": email_id_1, "email_address": email_address_1}, {
        "id": email_id_2, "email_address": email_address_2}]

    create_email_dict = {
        "email_address": "abc_xyz@dell.com",
        "notify_critical": False,
        "notify_major": False,
    }

    email_valid_param_list = [
        'id', 'email_address', 'notify_critical', 'notify_major', 'notify_minor', 'notify_info'
    ]

    email_error = {
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

    email_details_1 = {
        "id": "ee3c94d9-8c7d-46bd-9382-469dacee1456",
        "email_address": "abc_xyz@dell.com",
        "notify_critical": False,
        "notify_major": False,
        "notify_minor": False,
        "notify_info": False
    }

    modify_email_dict = {
        "notify_critical": True,
        "notify_major": True,
    }
