class RemoteSystemData():

    remote_system_id_1 = "55d14477-de22-4d39-b24d-07cf08ba329f"
    remote_system_name_1 = "AB-C1001"
    mgmt_ip_1 = "1xx.2xx.3xx.4xx"

    remote_system_id_2 = "20242441-4d8b-424f-b6b3-058ad02f5f9d"
    remote_system_name_2 = "DE-F1001"

    remote_system_list = [{"id": remote_system_id_1, "name": remote_system_name_1},
                     {"id": remote_system_id_2, "name": remote_system_name_2}]

    create_remote_sys_dict={
        'management_address': '1xx.2xx.3xx.4xx',
        'description': 'added via sdk',
        "type": "PowerStore",
        'data_network_latency': 'Low'
    }


    create_remote_system_error = {
        400: {
            "messages": [
                {
                    "code": "0xE0201002004A",
                    "severity": "Error",
                    "message_l10n": "Failed to create a new remote system. No iSCSI Targets configured."
                }
            ]
        }
    }

    remote_system_details_1 = {
            "id": "f07be373-dafd-4a46-8b21-f7cf790c287f",
            "name": "DE-F1001",
            "description": "Adding remote system",
            "serial_number": "PS4ef018459192",
            "version": "1.0.3.1.3.143",
            "management_address": "1xx.2xx.3xx.4xx",
            "type": "PowerStore",
            "user_name": "",
            "state": "OK",
            "data_connection_state": "OK",
            "iscsi_addresses": [
                "1xx.2xx.3xx.4xx"
            ],
            "discovery_chap_mode": "Disabled",
            "session_chap_mode": "Single",
            "data_network_latency": "Low",
            "data_connections": [
                {
                    "status": "Login_Success",
                    "node_id": "N2",
                    "target_address": "1xx.2xx.3xx.4xx",
                    "initiator_address": "1xx.2xx.3xx.4xx"
                }
            ],
            "type_l10n": "PowerStore",
            "state_l10n": "OK",
            "data_connection_state_l10n": "OK",
            "discovery_chap_mode_l10n": "Disabled",
            "session_chap_mode_l10n": "Single",
            "data_network_latency_l10n": "Low"
    }

    modify_remote_system_dict={
        'description': 'updated via sdk',
        'data_network_latency': 'Low'
    }

    modify_job_id_1 = "55d1-de22-4d39-b24d-08ba329f"

    remote_app_details = [
        {
            "id": "A1",
            "name": "Appliance-RS-000",
            "model": "PowerStore 1000T"
        }
    ]
