# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

""" Certificate operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>",
                                      timeout=180.0)
print(CONN)

certificate_list = CONN.config_mgmt.get_certificates()
print(certificate_list)

certificate_details = CONN.config_mgmt.get_certificate_details(certificate_list[0]['id'])
print(certificate_details)

create_dict = {
    "type": "CA_Client_Validation",
    "service": "VASA_HTTP",
    "scope": "",
    "certificate": "<certificate string>",
    "private_key" : "",
    "passphrase": "<passphrase>",
    "is_current": True
}
resp = CONN.config_mgmt.create_certificate(create_cert_dict=create_dict)
print(resp)

reset_dict = {
    "service": "VASA_HTTP"
}
resp = CONN.config_mgmt.reset_certificates(reset_cert_dict=reset_dict)
print(resp)

modify_dict = {
  "certificate": "<passphrase>",
  "is_current": True
}

resp = CONN.config_mgmt.modify_certificate(certificate_id=resp['id'], modify_cert_dict=modify_dict)
print(resp)
