# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

"""Collection of NFS server related functions for PowerStore"""

from PyPowerStore.client import Client
from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

SELECT_ALL_NFS_SERVER = {"select": "id, nas_server_id, host_name, is_nfsv3_enabled,"
                         "is_nfsv4_enabled, is_secure_enabled, is_use_smb_config_enabled,"
                         "service_principal_name, is_joined, is_extended_credentials_enabled,"
                         "credentials_cache_TTL"
                        }

# NFS server endpoints
GET_NFS_SERVER_LIST_URL = 'https://{0}/api/rest/nfs_server'
GET_NFS_SERVER_DETAILS_URL = 'https://{0}/api/rest/nfs_server/{1}'
GET_NFS_SERVER_DETAILS_BY_NAS_SERVER_URL = GET_NFS_SERVER_LIST_URL
MODIFY_NFS_SERVER_URL = GET_NFS_SERVER_DETAILS_URL
CREATE_NFS_SERVER_URL = GET_NFS_SERVER_LIST_URL
DELETE_NFS_SERVER_URL = GET_NFS_SERVER_DETAILS_URL

class NFSServer:
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
        self.nfs_server_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # NFS server methods begin
    def get_nfs_server_list(self, filter_dict=None, all_pages=False):
        """Get a list of NFS servers.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: NFS servers
        :rtype: list of dict
        """
        LOG.info("Getting NFS servers with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(SELECT_ALL_NFS_SERVER, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.nfs_server_client.request(constants.GET,
                                   GET_NFS_SERVER_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_nfs_server_details(self, nfs_server_id):
        """Details of a NFS server.

        :param nfs_server_id: The NFS server ID
        :type nfs_server_id: str
        :return:NFS server details
        :rtype: dict
        """
        querystring = SELECT_ALL_NFS_SERVER

        LOG.info("Getting NFS server details by ID: '%s'" % nfs_server_id)
        return self.nfs_server_client.request(
            constants.GET,
            GET_NFS_SERVER_DETAILS_URL.format(self.server_ip,
                                              nfs_server_id),
            payload=None,
            querystring=querystring)

    def get_nfs_server_by_nas_server_id(self, nas_server_id):
        """Get details of a NFS server by NAS server ID.

        :param nas_server_id: The unique identifier of the NAS Server
        :type nas_server_id: str
        :return: NFS server details
        :rtype: dict
        """
        querystring = SELECT_ALL_NFS_SERVER

        LOG.info("Getting NFS server details by nas server id: '%s'" % nas_server_id)
        return self.nfs_server_client.request(
            constants.GET,
            GET_NFS_SERVER_DETAILS_BY_NAS_SERVER_URL.format(
                self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                querystring,
                nas_server_id=constants.EQUALS + nas_server_id,
            )
        )

    def create_nfs_server(self, payload):
        """Create a NFS server.

        :param payload: The payload to create the NFS server
        :type payload: dict
        :return: NFS server ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating NFS server")
        return self.nfs_server_client.request(
            constants.POST,
            CREATE_NFS_SERVER_URL.format(self.server_ip),
            payload=payload)

    def modify_nfs_server(self, nfs_server_id, modify_parameters):
        """Modify NFS server attributes.

        :param nfs_server_id: The ID of the NFS server
        :type nfs_server_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying NFS server: '%s'" % nfs_server_id)
        if modify_parameters:
            payload = dict()
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.nfs_server_client.request(
                    constants.PATCH,
                    MODIFY_NFS_SERVER_URL.format(
                        self.server_ip, nfs_server_id),
                    payload=payload)

        raise ValueError("Nothing to modify")

    def delete_nfs_server(self, nfs_server_id):
        """Delete a NFS server.

        :param nfs_server_id: The ID of the NFS server to delete
        :type nfs_server_id: str
        :return: None on success else raise exception
        :rtype: None
        """
        LOG.info("Deleting NFS server: '%s'" % nfs_server_id)
        return self.nfs_server_client.request(
            constants.DELETE,
            DELETE_NFS_SERVER_URL.format(self.server_ip, nfs_server_id))

    # NFS server methods end
