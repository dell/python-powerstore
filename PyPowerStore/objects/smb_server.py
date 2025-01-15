# Copyright: (c) 2024, Dell Technologies

"""Collection of SMB server related functions for PowerStore"""

from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

SELECT_ALL_SMB_SERVER = {
    "select": "id, nas_server_id, computer_name, domain,"
    "netbios_name, workgroup, description, is_standalone,"
    "is_joined, nas_server(id,name)",
}

# SMB server endpoints
GET_SMB_SERVER_LIST_URL = "https://{0}/api/rest/smb_server"
GET_SMB_SERVER_DETAILS_URL = "https://{0}/api/rest/smb_server/{1}"
GET_SMB_SERVER_DETAILS_BY_NAS_SERVER_URL = GET_SMB_SERVER_LIST_URL
MODIFY_SMB_SERVER_URL = GET_SMB_SERVER_DETAILS_URL
CREATE_SMB_SERVER_URL = GET_SMB_SERVER_LIST_URL
DELETE_SMB_SERVER_URL = GET_SMB_SERVER_DETAILS_URL


class SMBServer:
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
        self.smb_server_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # SMB server methods begin
    def get_smb_server_list(self, filter_dict=None, all_pages=False):
        """Get a list of SMB servers.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: SMB servers
        :rtype: list of dict
        """
        LOG.info(
            f"Getting SMB servers with filter: '{filter_dict}' and all_pages: {all_pages}",
        )
        querystring = helpers.prepare_querystring(SELECT_ALL_SMB_SERVER, filter_dict)
        LOG.info(f"Querystring: '{querystring}'")
        return self.smb_server_client.request(
            constants.GET,
            GET_SMB_SERVER_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_smb_server_details(self, smb_server_id):
        """Details of a SMB server.

        :param smb_server_id: The SMB server ID
        :type smb_server_id: str
        :return:SMB server details
        :rtype: dict
        """
        querystring = SELECT_ALL_SMB_SERVER

        LOG.info(f"Getting SMB server details by ID: '{smb_server_id}'")
        return self.smb_server_client.request(
            constants.GET,
            GET_SMB_SERVER_DETAILS_URL.format(self.server_ip, smb_server_id),
            payload=None,
            querystring=querystring,
        )

    def get_smb_server_by_nas_server_id(self, nas_server_id):
        """Get details of a SMB server by NAS server ID.

        :param nas_server_id: The unique identifier of the NAS Server
        :type nas_server_id: str
        :return: SMB server details
        :rtype: dict
        """
        querystring = SELECT_ALL_SMB_SERVER

        LOG.info(f"Getting SMB server details by nas server id: '{nas_server_id}'")
        return self.smb_server_client.request(
            constants.GET,
            GET_SMB_SERVER_DETAILS_BY_NAS_SERVER_URL.format(self.server_ip),
            payload=None,
            querystring=helpers.prepare_querystring(
                querystring,
                nas_server_id=constants.EQUALS + nas_server_id,
            ),
        )

    def create_smb_server(self, payload):
        """Create a SMB server.

        :param payload: The payload to create the SMB server
        :type payload: dict
        :return: SMB server ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating SMB server")
        return self.smb_server_client.request(
            constants.POST,
            CREATE_SMB_SERVER_URL.format(self.server_ip),
            payload=payload,
        )

    def modify_smb_server(self, smb_server_id, modify_parameters):
        """Modify SMB server attributes.

        :param smb_server_id: The ID of the SMB server
        :type smb_server_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info(f"Modifying SMB server: '{smb_server_id}'")
        if modify_parameters:
            payload = {}
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.smb_server_client.request(
                    constants.PATCH,
                    MODIFY_SMB_SERVER_URL.format(self.server_ip, smb_server_id),
                    payload=payload,
                )

        raise ValueError("Nothing to modify")

    def delete_smb_server(self, smb_server_id):
        """Delete a SMB server.

        :param smb_server_id: The ID of the SMB server to delete
        :type smb_server_id: str
        :return: None on success else raise exception
        :rtype: None
        """
        LOG.info(f"Deleting SMB server: '{smb_server_id}'")
        return self.smb_server_client.request(
            constants.DELETE,
            DELETE_SMB_SERVER_URL.format(self.server_ip, smb_server_id),
        )

    # SMB server methods end
