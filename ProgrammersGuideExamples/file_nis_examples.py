# Copyright: (c) 2024, Dell Technologies

"""File NIS Operations"""
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
    timeout=180.0,
)
print(CONN)

MODIFY_PARAMS = {
    "domain": "stringa",
    "add_ip_addresses": ["10.10.10.11"],
    "remove_ip_addresses": ["10.10.10.10"],
}

CREATE_PARAMS = {
    "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
    "domain": "string",
    "ip_addresses": ["10.10.10.10"],
}

# create file NIS
FILE_NIS = CONN.file_nis.create_file_nis(CREATE_PARAMS)
print(FILE_NIS)

# Get file NIS list
FILE_NISES = CONN.file_nis.get_file_nis_list(all_pages=True)
print(FILE_NISES)

# get file NIS details by ID
FILE_NIS = CONN.file_nis.get_file_nis_details(FILE_NIS["id"])
print(FILE_NIS)

# get file NIS details by NAS server
FILE_NIS = CONN.file_nis.get_file_nis_by_nas_server_id(CREATE_PARAMS["nas_server_id"])
print(FILE_NIS)

# modify file NIS
MODIFY_FILE_NIS = CONN.file_nis.modify_file_nis(FILE_NIS[0]["id"], MODIFY_PARAMS)
print(MODIFY_FILE_NIS)

# delete file NIS
DELETE_FILE_NIS = CONN.file_nis.delete_file_nis(FILE_NIS[0]["id"])
print(DELETE_FILE_NIS)
