"""Data for vCenter unit tests."""

# pylint: disable=too-few-public-methods

class VcenterData:
    """This class contains data for vCenter unit tests."""
    vcenter_id = "42d08c86-f958-4fbb-82f0-3ce1a5d99d1e"
    vcenter_list = [
        {
            "id": "42d08c86-f958-4fbb-82f0-3ce1a5d99d1e",
            "instance_uuid": "3b33039f-908f-4d1a-a0ca-1d2fd050a09b",
            "address": "vpi7.lab.comp.com",
            "username": "vcenter_admin",
            "vendor_provider_status": "Online",
            "vendor_provider_status_l10n": "Online",
        },
    ]
    add_vcenter_params = {
        "address": "dummy ip",
        "username": "user",
        "password": "vcenter_Password",
        "vasa_provider_credentials": {
            "username": "sample_vasa_user",
            "password": "sample_vasa_password",
        },
    }
    vasa_provider_credentials = {
        "username": "sample_vasa_user",
        "password": "sample_vasa_password",
    }
    vcenter_details = {
        "id": "42d08c86-f958-4fbb-82f0-3ce1a5d99d1e",
        "instance_uuid": "3b33039f-908f-4d1a-a0ca-1d2fd050a09b",
        "address": "vpi7.lab.comp.com",
        "username": "vcenter_admin",
        "vendor_provider_status": "Online",
        "vendor_provider_status_l10n": "Online",
    }

    delete_vasa_provider = True
