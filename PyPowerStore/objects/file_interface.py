# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

"""Collection of file interface related functions for PowerStore"""

from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

SELECT_ALL_FILE_INTERFACE = {
    "select": "id, nas_server_id, ip_address, prefix_length,"
    "gateway, vlan_id, name, role, is_disabled,"
    "is_destination_override_enabled, ip_port_id,"
    "source_parameters, is_dr_test, nas_server(id,name)"
}

# File Interface endpoints
GET_FILE_INTERFACE_LIST_URL = "https://{0}/api/rest/file_interface"
GET_FILE_INTERFACE_DETAILS_URL = "https://{0}/api/rest/file_interface/{1}"
GET_FILE_INTERFACE_DETAILS_BY_NAS_SERVER_URL = GET_FILE_INTERFACE_LIST_URL
MODIFY_FILE_INTERFACE_URL = GET_FILE_INTERFACE_DETAILS_URL
CREATE_FILE_INTERFACE_URL = GET_FILE_INTERFACE_LIST_URL
DELETE_FILE_INTERFACE_URL = GET_FILE_INTERFACE_DETAILS_URL


class FileInterface:
    """Provisioning related functionality for PowerStore."""

    def __init__(self, provisioning, enable_log=False):
        """Initializes ProtectionFunctions Class.

        :param provisioning: Provisioning class object
        :type provisioning: Provisioning
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        """
        global LOG
        self.provisioning = provisioning
        self.server_ip = provisioning.server_ip
        self.file_interface_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # File interface methods begin
    def get_file_interface_list(self, filter_dict=None, all_pages=False):
        """Get a list of file interfaces.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: File interfaces
        :rtype: list of dict
        """
        LOG.info(
            "Getting file interfaces with filter: '%s' and all_pages: %s"
            % (filter_dict, all_pages)
        )
        querystring = helpers.prepare_querystring(
            SELECT_ALL_FILE_INTERFACE, filter_dict
        )
        LOG.info("Querystring: '%s'" % querystring)
        return self.file_interface_client.request(
            constants.GET,
            GET_FILE_INTERFACE_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_file_interface_details(self, file_interface_id):
        """Details of a file interface.

        :param file_interface_id: The file interface ID
        :type file_interface_id: str
        :return:file interface details
        :rtype: dict
        """
        querystring = SELECT_ALL_FILE_INTERFACE

        LOG.info("Getting file interface details by ID: '%s'" %
                 file_interface_id)
        return self.file_interface_client.request(
            constants.GET,
            GET_FILE_INTERFACE_DETAILS_URL.format(
                self.server_ip, file_interface_id),
            payload=None,
            querystring=querystring,
        )

    def get_file_interface_by_nas_server_id(self, nas_server_id, ip_address):
        """Get details of a file interface by NAS server ID.

        :param nas_server_id: The unique identifier of the NAS Server
        :type nas_server_id: str
        :return: file interface details
        :rtype: dict
        """
        querystring = SELECT_ALL_FILE_INTERFACE

        LOG.info(
            "Getting file interface details by nas server id: '%s'" % nas_server_id
        )
        return self.file_interface_client.request(
            constants.GET,
            GET_FILE_INTERFACE_DETAILS_BY_NAS_SERVER_URL.format(
                self.server_ip),
            payload=None,
            querystring=helpers.prepare_querystring(
                querystring,
                nas_server_id=constants.EQUALS + nas_server_id,
                ip_address=constants.EQUALS + ip_address,
            ),
        )

    def create_file_interface(self, payload):
        """Create a File interface.

        :param payload: The payload to create the file interface
        :type payload: dict
        :return: file interface ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating file interface")
        return self.file_interface_client.request(
            constants.POST,
            CREATE_FILE_INTERFACE_URL.format(self.server_ip),
            payload=payload,
        )

    def modify_file_interface(self, file_interface_id, modify_parameters):
        """Modify File interface attributes.

        :param file_interface_id: The ID of the file interface
        :type file_interface_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying file interface: '%s'" % file_interface_id)
        if modify_parameters:
            payload = {}
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.file_interface_client.request(
                    constants.PATCH,
                    MODIFY_FILE_INTERFACE_URL.format(
                        self.server_ip, file_interface_id),
                    payload=payload,
                )

        raise ValueError("Nothing to modify")

    def delete_file_interface(self, file_interface_id):
        """Delete a file interface.

        :param file_interface_id: The ID of the File interface to delete
        :type file_interface_id: str
        :return: None on success else raise exception
        :rtype: None
        """
        LOG.info("Deleting file interface: '%s'" % file_interface_id)
        return self.file_interface_client.request(
            constants.DELETE,
            DELETE_FILE_INTERFACE_URL.format(
                self.server_ip, file_interface_id),
        )

    # File interface methods end
