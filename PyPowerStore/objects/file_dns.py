# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

"""Collection of file DNS related functions for PowerStore"""

from PyPowerStore.client import Client
from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

SELECT_ALL_FILE_DNS = {"select": "id, nas_server_id, domain, ip_addresses, transport, nas_server(id,name)"}

# File DNS endpoints
GET_FILE_DNS_LIST_URL = 'https://{0}/api/rest/file_dns'
GET_FILE_DNS_DETAILS_URL = 'https://{0}/api/rest/file_dns/{1}'
GET_FILE_DNS_DETAILS_BY_NAS_SERVER_URL = GET_FILE_DNS_LIST_URL
MODIFY_FILE_DNS_URL = GET_FILE_DNS_DETAILS_URL
CREATE_FILE_DNS_URL = GET_FILE_DNS_LIST_URL
DELETE_FILE_DNS_URL = GET_FILE_DNS_DETAILS_URL

class FileDNS:
    """Provisioning related functionality for PowerStore."""
    def __init__(self, provisioning, enable_log=False):
        """ Initializes ProtectionFunctions Class.

        :param provisioning: Provisioning class object
        :type provisioning: Provisioning
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        """
        global LOG
        self.provisioning = provisioning
        self.server_ip = provisioning.server_ip
        self.file_dns_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # File DNS methods begin
    def get_file_dns_list(self, filter_dict=None, all_pages=False):
        """Get a list of file DNS .

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: file DNSs
        :rtype: list of dict
        """
        LOG.info("Getting file DNSs with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(SELECT_ALL_FILE_DNS, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.file_dns_client.request(constants.GET,
                                   GET_FILE_DNS_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_file_dns_details(self, file_dns_id):
        """Details of a file DNS.

        :param file_dns_id: The file DNS ID
        :type file_dns_id: str
        :return:file DNS details
        :rtype: dict
        """
        querystring = SELECT_ALL_FILE_DNS

        LOG.info("Getting file DNS details by ID: '%s'" % file_dns_id)
        return self.file_dns_client.request(
            constants.GET,
            GET_FILE_DNS_DETAILS_URL.format(self.server_ip,
                                            file_dns_id),
            payload=None,
            querystring=querystring)

    def get_file_dns_by_nas_server_id(self, nas_server_id):
        """Get details of a file DNS by NAS server ID.

        :param nas_server_id: The unique identifier of the NAS Server
        :type nas_server_id: str
        :return: file DNS details
        :rtype: dict
        """
        querystring = SELECT_ALL_FILE_DNS

        LOG.info("Getting file DNS details by nas server id: '%s'" % nas_server_id)
        return self.file_dns_client.request(
            constants.GET,
            GET_FILE_DNS_DETAILS_BY_NAS_SERVER_URL.format(
                self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                querystring,
                nas_server_id=constants.EQUALS + nas_server_id,
            )
        )

    def create_file_dns(self, payload):
        """Create a file DNS.

        :param payload: The payload to create the file DNS
        :type payload: dict
        :return: file DNS ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating file DNS")
        return self.file_dns_client.request(
            constants.POST,
            CREATE_FILE_DNS_URL.format(self.server_ip),
            payload=payload)

    def modify_file_dns(self, file_dns_id, modify_parameters):
        """Modify file DNS attributes.

        :param file_dns_id: The ID of the file DNS
        :type file_dns_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying file DNS: '%s'" % file_dns_id)
        if modify_parameters:
            payload = dict()
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.file_dns_client.request(
                    constants.PATCH,
                    MODIFY_FILE_DNS_URL.format(
                        self.server_ip, file_dns_id),
                    payload=payload)

        raise ValueError("Nothing to modify")

    def delete_file_dns(self, file_dns_id):
        """Delete a file DNS.

        :param file_dns_id: The ID of the file DNS to delete
        :type file_dns_id: str
        :return: None on success else raise exception
        :rtype: None
        """
        LOG.info("Deleting file DNS: '%s'" % file_dns_id)
        return self.file_dns_client.request(
            constants.DELETE,
            DELETE_FILE_DNS_URL.format(self.server_ip, file_dns_id))

    # File DNS methods end
