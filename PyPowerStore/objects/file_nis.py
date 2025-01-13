# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

"""Collection of file NIS related functions for PowerStore"""

from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

SELECT_ALL_FILE_NIS = {
    "select": "id, nas_server_id, domain, ip_addresses,"
    "is_destination_override_enabled, nas_server(id,name)"
}

# File NIS endpoints
GET_FILE_NIS_LIST_URL = "https://{0}/api/rest/file_nis"
GET_FILE_NIS_DETAILS_URL = "https://{0}/api/rest/file_nis/{1}"
GET_FILE_NIS_DETAILS_BY_NAS_SERVER_URL = GET_FILE_NIS_LIST_URL
MODIFY_FILE_NIS_URL = GET_FILE_NIS_DETAILS_URL
CREATE_FILE_NIS_URL = GET_FILE_NIS_LIST_URL
DELETE_FILE_NIS_URL = GET_FILE_NIS_DETAILS_URL


class FileNIS:
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
        self.file_nis_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # File NIS methods begin
    def get_file_nis_list(self, filter_dict=None, all_pages=False):
        """Get a list of file NIS .

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: file NISs
        :rtype: list of dict
        """
        LOG.info(
            "Getting file NISs with filter: '%s' and all_pages: %s"
            % (filter_dict, all_pages)
        )
        querystring = helpers.prepare_querystring(SELECT_ALL_FILE_NIS, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.file_nis_client.request(
            constants.GET,
            GET_FILE_NIS_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_file_nis_details(self, file_nis_id):
        """Details of a file NIS.

        :param file_nis_id: The file NIS ID
        :type file_nis_id: str
        :return:file NIS details
        :rtype: dict
        """
        querystring = SELECT_ALL_FILE_NIS

        LOG.info("Getting file NIS details by ID: '%s'" % file_nis_id)
        return self.file_nis_client.request(
            constants.GET,
            GET_FILE_NIS_DETAILS_URL.format(self.server_ip, file_nis_id),
            payload=None,
            querystring=querystring,
        )

    def get_file_nis_by_nas_server_id(self, nas_server_id):
        """Get details of a file NIS by NAS server ID.

        :param nas_server_id: The unique identifier of the NAS Server
        :type nas_server_id: str
        :return: file NIS details
        :rtype: dict
        """
        querystring = SELECT_ALL_FILE_NIS

        LOG.info("Getting file NIS details by nas server id: '%s'" % nas_server_id)
        return self.file_nis_client.request(
            constants.GET,
            GET_FILE_NIS_DETAILS_BY_NAS_SERVER_URL.format(self.server_ip),
            payload=None,
            querystring=helpers.prepare_querystring(
                querystring,
                nas_server_id=constants.EQUALS + nas_server_id,
            ),
        )

    def create_file_nis(self, payload):
        """Create a file NIS.

        :param payload: The payload to create the file NIS
        :type payload: dict
        :return: file NIS ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating file NIS")
        return self.file_nis_client.request(
            constants.POST, CREATE_FILE_NIS_URL.format(self.server_ip), payload=payload
        )

    def modify_file_nis(self, file_nis_id, modify_parameters):
        """Modify file NIS attributes.

        :param file_nis_id: The ID of the file NIS
        :type file_nis_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying file NIS: '%s'" % file_nis_id)
        if modify_parameters:
            payload = {}
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.file_nis_client.request(
                    constants.PATCH,
                    MODIFY_FILE_NIS_URL.format(self.server_ip, file_nis_id),
                    payload=payload,
                )

        raise ValueError("Nothing to modify")

    def delete_file_nis(self, file_nis_id):
        """Delete a file NIS.

        :param file_nis_id: The ID of the file NIS to delete
        :type file_nis_id: str
        :return: None on success else raise exception
        :rtype: None
        """
        LOG.info("Deleting file NIS: '%s'" % file_nis_id)
        return self.file_nis_client.request(
            constants.DELETE, DELETE_FILE_NIS_URL.format(self.server_ip, file_nis_id)
        )

    # File NIS methods end
