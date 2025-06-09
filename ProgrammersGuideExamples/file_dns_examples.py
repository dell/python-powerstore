# Copyright: (c) 2024, Dell Technologies

# pylint: disable=duplicate-code

"""File DNS Operations"""
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
    "transport": "TCP",
}

CREATE_PARAMS = {
    "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
    "domain": "string",
    "ip_addresses": ["10.10.10.10"],
    "transport": "UDP",
}

# create file DNS
FILE_DNS = CONN.file_dns.create_file_dns(CREATE_PARAMS)
print(FILE_DNS)

# Get file DNS list
FILE_DNSES = CONN.file_dns.get_file_dns_list(all_pages=True)
print(FILE_DNSES)

# get file DNS details by ID
FILE_DNS = CONN.file_dns.get_file_dns_details(FILE_DNS["id"])
print(FILE_DNS)

# get file DNS details by NAS server
FILE_DNS = CONN.file_dns.get_file_dns_by_nas_server_id(CREATE_PARAMS["nas_server_id"])
print(FILE_DNS)

# modify file DNS
MODIFY_FILE_DNS = CONN.file_dns.modify_file_dns(FILE_DNS[0]["id"], MODIFY_PARAMS)
print(MODIFY_FILE_DNS)

# delete file DNS
DELETE_FILE_DNS = CONN.file_dns.delete_file_dns(FILE_DNS[0]["id"])
print(DELETE_FILE_DNS)
