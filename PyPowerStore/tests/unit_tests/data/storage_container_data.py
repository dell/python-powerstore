class StorageContainerData:
    storage_container_list = [
        "37b76535-612b-456a-a694-1389f17632c7",
        "37b76535-612b-456a-a694-1389f17632c",
    ]

    storage_container_list = [
        {
            "datastores": [],
            "destinations": [],
            "id": "e0ccd953-5650-41d8-9bce-f36d876d6a2a",
            "name": "Sample_storage_container_1",
            "quota": 21474836480,
            "replication_groups": [],
            "storage_protocol": "NVMe",
            "storage_protocol_l10n": "NVMe",
            "virtual_volumes": [],
        },
    ]

    storage_container_details = {
        "datastores": [],
        "destinations": [],
        "id": "e0ccd953-5650-41d8-9bce-f36d876d6a2a",
        "name": "Sample_storage_container_1",
        "quota": 21474836480,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": [],
    }

    create_storage_container_dict = {
        "name": "Sample_storage_container_1",
        "quota": 0,
        "storage_protocol": "SCSI",
        "high_water_mark": "60",
    }

    modify_storage_container_dict = {"role_id": "2"}

    create_storage_container_response = {"name": "Sample_storage_container_1"}
