# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

"""Collection of SNMP related functions for PowerStore"""

from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

SELECT_ALL_SNMP = {
    "select": "id, ip_address, port, version, trap_community,"
    "alert_severity, user_name, auth_protocol, privacy_protocol"
}

# SNMP server endpoints
GET_SNMP_LIST_URL = "https://{0}/api/rest/snmp_server"
GET_SNMP_DETAILS_URL = "https://{0}/api/rest/snmp_server/{1}"
GET_SNMP_DETAILS_BY_NAS_SERVER_URL = GET_SNMP_LIST_URL
MODIFY_SNMP_URL = GET_SNMP_DETAILS_URL
CREATE_SNMP_URL = GET_SNMP_LIST_URL
DELETE_SNMP_URL = GET_SNMP_DETAILS_URL


class SNMPServer:
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
        self.snmp_server_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # SNMP server methods begin
    def get_snmp_server_list(self, filter_dict=None, all_pages=False):
        """Get a list of SNMP servers.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: SNMP servers
        :rtype: list of dict
        """
        LOG.info(
            "Getting SNMP servers with filter: '%s' and all_pages: %s"
            % (filter_dict, all_pages)
        )
        querystring = helpers.prepare_querystring(SELECT_ALL_SNMP, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.snmp_server_client.request(
            constants.GET,
            GET_SNMP_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_snmp_server_details(self, snmp_server_id):
        """Details of a SNMP server.

        :param snmp_server_id: The SNMP server ID
        :type snmp_server_id: str
        :return:SNMP server details
        :rtype: dict
        """
        querystring = SELECT_ALL_SNMP

        LOG.info("Getting SNMP server details by ID: '%s'" % snmp_server_id)
        return self.snmp_server_client.request(
            constants.GET,
            GET_SNMP_DETAILS_URL.format(self.server_ip, snmp_server_id),
            payload=None,
            querystring=querystring,
        )

    def create_snmp_server(self, payload):
        """Create an SNMP server.

        :param payload: The payload to create the SNMP server
        :type payload: dict
        :return: SNMP server ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating SNMP server")
        return self.snmp_server_client.request(
            constants.POST, CREATE_SNMP_URL.format(self.server_ip), payload=payload
        )

    def modify_snmp_server(self, snmp_server_id, modify_parameters):
        """Modify SNMP server attributes.

        :param snmp_server_id: The ID of the SNMP server
        :type snmp_server_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying SNMP server: '%s'" % snmp_server_id)
        if modify_parameters:
            payload = {}
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.snmp_server_client.request(
                    constants.PATCH,
                    MODIFY_SNMP_URL.format(self.server_ip, snmp_server_id),
                    payload=payload,
                )

        raise ValueError("Nothing to modify")

    def delete_snmp_server(self, snmp_server_id):
        """Delete an SNMP server.

        :param snmp_server_id: The ID of the SNMP server to delete
        :type snmp_server_id: str
        :return: None on success else raise exception
        :rtype: None
        """
        LOG.info("Deleting SNMP server: '%s'" % snmp_server_id)
        return self.snmp_server_client.request(
            constants.DELETE, DELETE_SNMP_URL.format(
                self.server_ip, snmp_server_id)
        )

    # SNMP server methods end
