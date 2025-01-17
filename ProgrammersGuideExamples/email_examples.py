# Copyright: (c) 2024, Dell Technologies

"""Email operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
    timeout=180.0,
)

# Getting destination email addresses
email_list = CONN.config_mgmt.get_destination_emails()
print(email_list)

# Getting destination email instance details
email_details = CONN.config_mgmt.get_destination_email_details(
    email_id=email_list[0]["id"],
)
print(email_details)

# Getting destination email instance details using address
email_details = CONN.config_mgmt.get_destination_email_by_address(
    email_address=email_details["email_address"],
)
print(email_details)

# Adding a destination email address
create_dict = {"email_address": "abc_xyz@dell.com", "notify_critical": True}

resp_create = CONN.config_mgmt.create_destination_email(create_params=create_dict)
print(resp_create)

# Modifying the destination email details
modify_dict = {"notify_major": True}

resp_modify = CONN.config_mgmt.modify_destination_email_details(
    email_id=resp_create["id"], modify_parameters=modify_dict,
)
print(resp_modify)

# Sending test mail to a destination email instance
resp_test = CONN.config_mgmt.test_destination_email(email_id=resp_create["id"])
print(resp_test)

# Delete a destination email instance
resp_delete = CONN.config_mgmt.delete_destination_email(email_id=resp_create["id"])
print(resp_delete)
