class SmtpConfigData:

    smtp_id = "0"

    smtp_list = [{"id": smtp_id}]

    modify_smtp_dict = {
        "address": "sample.smtp.com",
        "port": 587,
        "source_email": "def@dell.com",
    }

    test_smtp_dict = {"email_address": "xyz@dell.com"}

    smtp_valid_param_list = ["id", "email_address", "address", "port", "source_email"]

    smtp_error = {
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

    smtp_details = {
        "id": "0",
        "address": "sample.smtp.com",
        "port": 25,
        "source_email": "abc@dell.com",
    }
