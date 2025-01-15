# Copyright: (c) 2024, Dell Technologies

"""Collection of configuration related functions for PowerStore"""

from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)


class Configuration:
    """Configuration related functionality for PowerStore."""

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
        self.config_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    # Network Operations Start

    def get_networks(self, filter_dict=None, all_pages=False):
        """Get all networks.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all elements
                          or not
        :type all_pages: bool
        :return: List of networks
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting networks with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )

        querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)

        if helpers.is_foot_hill_or_higher():
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME, filter_dict,
            )

        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_NETWORK_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_network_details(self, network_id):
        """Get details of a particular network.

        :param network_id: ID of the network
        :type network_id: str
        :return: Network details
        :rtype: dict
        """
        LOG.info("Getting network details by ID: '%s'", network_id)
        querystring = constants.NETWORK_DETAILS_QUERY

        if helpers.is_foot_hill_or_higher():
            querystring = {
                "select": "id,name,type,ip_version,vlan_id,prefix_length,"
                "gateway,mtu,purposes,type_l10n,ip_version_l10n,"
                "purposes_l10n",
            }

        return self.config_client.request(
            constants.GET,
            constants.GET_NETWORK_DETAILS_URL.format(self.server_ip, network_id),
            querystring=querystring,
        )

    def get_network_by_name(self, name):
        """Get network details by name.

        :param name: Name of the network
        :type name: str
        :return: Network details
        :rtype: list[dict]
        """
        LOG.info("Getting network details by name: '%s'", name)

        NETWORK_DETAILS_QUERY_BY_NAME = {
            "select": "id,name,type,ip_version,vlan_id,prefix_length,"
            "gateway,mtu,purposes,type_l10n,ip_version_l10n,"
            "purposes_l10n",
        }

        return self.config_client.request(
            constants.GET,
            constants.GET_NETWORK_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                NETWORK_DETAILS_QUERY_BY_NAME, name=constants.EQUALS + name,
            ),
        )

    def modify_network(self, network_id, network_other_params, is_async=False):
        """Modify network properties.

        :param network_id: ID of the network
        :type network_id: str
        :param is_async: Flag to indicate sync/async operation
        :type is_async: bool
        :param network_other_params: Dictionary containing attributes to be
                                    modified for the network
        :type network_other_params: dict
        :return: Network details
        :rtype : dict
        """
        LOG.info(
            f"Modifying network properties: '{network_id}' with params '{network_other_params}'",
        )

        network_url = constants.MODIFY_NETWORK_URL
        if is_async:
            network_url = network_url + "?is_async=true"
        return self.config_client.request(
            constants.PATCH,
            network_url.format(self.server_ip, network_id),
            payload=network_other_params,
        )

    def add_remove_ports(self, network_id, add_port_ids=None, remove_port_ids=None):
        """Add/remove IP ports from storage network.

        :param network_id: ID of the network
        :type network_id: str
        :param add_port_ids: List of IP ports to be added to the
                             storage network
        :type add_port_ids: list[str]
        :param remove_port_ids: List of IP ports to be removed from the
                                storage network
        :type remove_port_ids: list[str]
        """
        LOG.info("Add/remove IP ports: '%s'", network_id)
        payload = self._prepare_add_remove_network_payload(
            add_port_ids=add_port_ids, remove_port_ids=remove_port_ids,
        )
        self.config_client.request(
            constants.POST,
            constants.ADD_REMOVE_IP_PORTS.format(self.server_ip, network_id),
            payload,
        )
        return self.get_network_details(network_id)

    # Network Operations End

    # Role Operations Start

    def get_roles(self, filter_dict=None, all_pages=None):
        """Get all roles.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) All pages
        :type all_pages: bool
        :return: List of roles
        :rtype: list[dict]
        """
        LOG.info("Getting roles with filter: '%s'", filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported for roles.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID_AND_NAME)
            return self.config_client.request(
                constants.GET,
                constants.GET_ROLE_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        resp = self.config_client.request(
            constants.GET,
            constants.GET_ROLE_LIST_URL.format(self.server_ip),
            querystring=constants.ROLE_DETAILS_QUERY,
            all_pages=False,
        )

        filterable_keys = ["name", "id", "is_built_in"]
        return helpers.filtered_details(filterable_keys, filter_dict, resp, "roles")

    def get_role_details(self, role_id):
        """Get details of a particular role.

        :param role_id: ID of the role
        :type role_id: str
        :return: Role details
        :rtype: dict
        """
        LOG.info("Getting role details by ID: '%s'", role_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_ROLE_DETAILS_URL.format(self.server_ip, role_id),
            querystring=constants.ROLE_DETAILS_QUERY,
        )

    def get_role_by_name(self, name):
        """Get role details by name.

        :param name: Name of the role
        :type name: str
        :return: Role details
        :rtype: dict
        """
        LOG.info("Getting role details by name: '%s'", name)
        resp = self.get_roles()
        for role in resp:
            if role["name"] == name:
                return self.get_role_details(role["id"])

        raise ValueError("role name not found")

    # Role Operations End

    # Local User operations start

    def get_local_users(self, filter_dict=None, all_pages=None):
        """Get all local users.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) All pages
        :type all_pages: bool
        :return: List of local users
        :rtype: list[dict]
        """
        LOG.info("Getting local users with filter: '%s'", filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported for local users.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID_AND_NAME)
            return self.config_client.request(
                constants.GET,
                constants.GET_LOCAL_USER_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )
        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.LOCAL_USER_DETAILS_QUERY, filter_dict,
        )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_LOCAL_USER_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )

        filterable_keys = ["name", "id", "is_locked"]
        return helpers.filtered_details(
            filterable_keys, filter_dict, resp, "local user",
        )

    def get_local_user_details(self, user_id):
        """Get details of a particular local user.

        :param user_id: ID of the role
        :type user_id: str
        :return: local user details
        :rtype: dict
        """
        LOG.info("Getting local user details by user ID: '%s'", user_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_LOCAL_USER_DETAILS_URL.format(self.server_ip, user_id),
            querystring=constants.LOCAL_USER_DETAILS_QUERY,
        )

    def get_local_user_by_name(self, name):
        """Get local user details by name.

        :param name: Name of the local user
        :type name: str
        :return: local user details
        :rtype: list[dict]
        """
        LOG.info("Getting local user details by name: '%s'", name)
        resp = self.get_local_users()

        for user in resp:
            if user["name"] == name:
                return self.get_local_user_details(user["id"])

    def delete_local_user(self, user_id):
        """Delete a local user.

        :param user_id: The user ID
        :type user_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting local user id: '%s'", user_id)
        return self.config_client.request(
            constants.DELETE,
            constants.DELETE_LOCAL_USER_URL.format(self.server_ip, user_id),
            payload=None,
        )

    def create_local_user(self, create_params):
        """Create a local user.

        :param create_params: The create params
        :type create_params: list<dict>
        :return: user id if success else raise exception
        :rtype: None
        """
        LOG.info("creating local user name: '%s'", create_params['name'])

        payload = {}
        if create_params:
            for key, value in create_params.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST,
            constants.CREATE_LOCAL_USER_URL.format(
                self.server_ip,
            ),
            payload=payload,
        )

    def modify_local_user(self, local_user_id, modify_parameters):
        """Modify local user properties.

        :param local_user_id: ID of the local user
        :type local_user_id: str
        :param modify_parameters: Dict containing local user attributes to be
                                  modified
        :type modify_parameters: dict
        :return: local user details
        :rtype : dict
        """
        LOG.info("Modifying local user properties: '%s'", local_user_id)

        if modify_parameters:
            if (
                "password" in modify_parameters.keys()
                and "current_password" in modify_parameters.keys()
            ):
                payload = {}
                payload["password"] = modify_parameters["password"]
                payload["current_password"] = modify_parameters["current_password"]
                self.config_client.request(
                    constants.PATCH,
                    constants.MODIFY_LOCAL_USER_URL.format(
                        self.server_ip, local_user_id,
                    ),
                    payload=payload,
                )
                del modify_parameters["password"]
                del modify_parameters["current_password"]
                LOG.info("Modifying passwords: '%s'", payload)

            for key, value in modify_parameters.items():
                if value is not None:
                    payload = {}
                    payload[key] = value
                    LOG.info("Modifying localuser: '%s'", payload)
                    self.config_client.request(
                        constants.PATCH,
                        constants.MODIFY_LOCAL_USER_URL.format(
                            self.server_ip, local_user_id,
                        ),
                        payload=payload,
                    )
            return
        raise ValueError("Nothing to modify")

    # Local User Operations End

    # IP Pool Operations Start

    def get_ip_pool_address(self, filter_dict=None, all_pages=False):
        """Get all IP addresses.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all
            elements or not
        :type all_pages: bool
        :return: List of IP addresses
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting IP's with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(
            constants.IP_DETAILS_QUERY, filter_dict,
        )
        if helpers.is_foot_hill_or_higher():
            querystring = {
                "select": "id,name,network_id,ip_port_id,appliance_id,"
                "node_id,address,purposes,purposes_l10n",
            }
            querystring = helpers.prepare_querystring(querystring, filter_dict)

        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_IP_POOL_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    # IP Pool Operations End

    # Cluster operations start
    def get_clusters(self, filter_dict=None, all_pages=None):
        """Get all clusters.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all clusters
                          or not
        :type all_pages: bool
        :return: List of clusters
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting clusters with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        if all_pages:
            raise Exception("Pagination is not supported for clusters.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID_AND_NAME)
            LOG.info("Querystring: '%s'", querystring)
            return self.config_client.request(
                constants.GET,
                constants.GET_CLUSTER_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.CLUSTER_DETAILS_QUERY, filter_dict,
        )
        if helpers.is_foot_hill_or_higher():
            details_query_string = {
                "select": "id,global_id,name,management_address,"
                "storage_discovery_address,master_appliance_id,"
                "appliance_count,physical_mtu,"
                "is_encryption_enabled,system_time,"
                "compatibility_level,state,state_l10n",
            }
            querystring = helpers.prepare_querystring(details_query_string, filter_dict)

        resp = self.config_client.request(
            constants.GET,
            constants.GET_CLUSTER_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )

        filterable_keys = ["name", "id", "physical_mtu"]
        return helpers.filtered_details(filterable_keys, filter_dict, resp, "cluster")

    def get_cluster_details(self, cluster_id):
        """Get details of a particular cluster.

        :param cluster_id: ID of the cluster
        :type cluster_id: str
        :return: Cluster details
        :rtype: dict
        """
        LOG.info("Getting cluster details by ID: '%s'", cluster_id)
        querystring = constants.CLUSTER_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                "select": "id,global_id,name,management_address,"
                "storage_discovery_address,master_appliance_id,"
                "appliance_count,physical_mtu,is_encryption_enabled,"
                "compatibility_level,state,state_l10n,system_time",
            }
        return self.config_client.request(
            constants.GET,
            constants.GET_CLUSTER_DETAILS_URL.format(self.server_ip, cluster_id),
            querystring=querystring,
        )

    def get_cluster_by_name(self, name):
        """Get cluster details by name.

        :param name: Name of the cluster
        :type name: str
        :return: Cluster details
        :rtype: list[dict]
        """
        LOG.info("Getting cluster details by name: '%s'", name)
        querystring = constants.CLUSTER_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                "select": "id,global_id,name,management_address,"
                "storage_discovery_address,master_appliance_id,"
                "appliance_count,physical_mtu,is_encryption_enabled,"
                "compatibility_level,state,state_l10n,system_time",
            }
        resp = self.config_client.request(
            constants.GET,
            constants.GET_CLUSTER_LIST_URL.format(self.server_ip),
            querystring=querystring,
        )
        filterable_keys = ["name", "id", "physical_mtu"]
        filter_dict = {"name": f"eq.{name}"}
        return helpers.filtered_details(filterable_keys, filter_dict, resp, "cluster")

    def modify_cluster(self, cluster_id, physical_mtu=None, name=None):
        """Modify cluster properties.

        :param cluster_id: ID of the cluster
        :type cluster_id: str
        :param physical_mtu: MTU for ethernet ports in the cluster
        :type physical_mtu: int
        :param name: The new name for the cluster
        :type name: str
        :return: Cluster details
        :rtype : dict
        """
        LOG.info("Modifying cluster properties: '%s'", cluster_id)
        payload = {}
        if physical_mtu is not None:
            payload["physical_mtu"] = physical_mtu
        if name is not None:
            payload["name"] = name
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_CLUSTER_URL.format(self.server_ip, cluster_id),
            payload,
        )
        return self.get_cluster_details(cluster_id)

    def cluster_create_validate(
        self,
        cluster,
        appliances,
        dns_servers,
        ntp_servers,
        networks,
        is_http_redirect_enabled,
        physical_switches=None,
        vcenters=None,
    ):
        """Validate the creation of cluster configuration
        :param cluster: Dict containing parameters for the cluster
        :type cluster: dict
        :param appliances: List containing appliances
        :type appliances: list[dict]
        :param dns_servers: List containing IP addresses for DNS Servers
        :type dns_servers: list[str]
        :param ntp_servers: List containing IP addresses for NTP Servers
        :type ntp_servers: list[dict]
        :param physical_switches: List containing physical switches
        :type physical_switches: list[dict]
        :param networks: List containing networks
        :type networks: list[dict]
        :param vcenters: List of vCenters
        :type vcenters: list[dict]
        :param is_http_redirect_enabled: Whether to redirect the http requests
            to https
        :type is_http_redirect_enabled: bool
        :return: None
        :rtype: None
        """
        LOG.info("Validating the create cluster configuration")
        cluster_url = constants.CREATE_CLUSTER_VALIDATE_URL

        cluster_payload = self._prepare_create_cluster_payload(
            is_http_redirect_enabled=is_http_redirect_enabled,
            cluster=cluster,
            appliances=appliances,
            dns_servers=dns_servers,
            ntp_servers=ntp_servers,
            physical_switches=physical_switches,
            networks=networks,
            vcenters=vcenters,
        )
        return self.config_client.request(
            constants.POST, cluster_url.format(self.server_ip), payload=cluster_payload,
        )

    def cluster_create(
        self,
        cluster,
        appliances,
        dns_servers,
        ntp_servers,
        networks,
        is_http_redirect_enabled,
        physical_switches=None,
        vcenters=None,
        is_async=False,
    ):
        """Create a Cluster of one or more appliances
        :param cluster: Dict containing parameters for the cluster
        :type cluster: dict
        :param appliances: List containing appliances
        :type appliances: list[dict]
        :param dns_servers: List containing IP addresses for DNS Servers
        :type dns_servers: list[str]
        :param ntp_servers: List containing IP addresses for NTP Servers
        :type ntp_servers: list[dict]
        :param physical_switches: List containing physical switches
        :type physical_switches: list[dict]
        :param networks: List containing networks
        :type networks: list[dict]
        :param vcenters: List of vCenters
        :type vcenters: list[dict]
        :param is_http_redirect_enabled: Whether to redirect the http requests
            to https
        :type is_http_redirect_enabled: bool
        :param is_async: Flag to indicate sync/async operation
        :type is_async: bool
        :return: Unique identifier of the new instance created
        :rtype: str
        """
        LOG.info("Creating new cluster configuration")
        cluster_url = constants.CREATE_CLUSTER_URL
        if is_async:
            cluster_url = cluster_url + "?is_async=true"
        cluster_payload = self._prepare_create_cluster_payload(
            is_http_redirect_enabled=is_http_redirect_enabled,
            cluster=cluster,
            appliances=appliances,
            dns_servers=dns_servers,
            ntp_servers=ntp_servers,
            physical_switches=physical_switches,
            networks=networks,
            vcenters=vcenters,
        )
        return self.config_client.request(
            constants.POST, cluster_url.format(self.server_ip), payload=cluster_payload,
        )

    # Cluster operations end

    # CHAP config operations start
    def get_chap_configs(self, filter_dict=None, all_pages=None):
        """Get all CHAP configurations.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all CHAP
                            configurations or not
        :type all_pages: bool
        :return: List of CHAP configurations
        :rtype: list[dict]
        """
        LOG.info("Getting CHAP configurations with filter: '%s'", filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported for CHAP configuration.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID)
            return self.config_client.request(
                constants.GET,
                constants.GET_CHAP_CONFIG_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.CHAP_CONFIG_DETAILS_QUERY, filter_dict,
        )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_CHAP_CONFIG_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )

        filterable_keys = ["id", "mode"]
        return helpers.filtered_details(
            filterable_keys, filter_dict, resp, "CHAP config",
        )

    def get_chap_config_details(self, chap_config_id):
        """Get details of a particular CHAP configuration.

        :param chap_config_id: ID of the CHAP configuration
        :type chap_config_id: str
        :return: CHAP configuration details
        :rtype: dict
        """
        LOG.info("Getting CHAP configuration details by ID: '%s'", chap_config_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_CHAP_CONFIG_DETAILS_URL.format(
                self.server_ip, chap_config_id,
            ),
            querystring=constants.CHAP_CONFIG_DETAILS_QUERY,
        )

    def modify_chap_config(self, chap_config_id, mode):
        """Modify CHAP configuration properties.

        :param chap_config_id: ID of the CHAP configuration
        :type chap_config_id: str
        :param mode: Modes that describes or sets the iSCSI CHAP mode
        :type mode: str
        :return: CHAP configuration details
        :rtype : dict
        """
        LOG.info("Modifying CHAP configuration properties: '%s'", chap_config_id)
        payload = {}
        if mode is not None:
            payload["mode"] = mode
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_CHAP_CONFIG_URL.format(self.server_ip, chap_config_id),
            payload,
        )
        return self.get_chap_config_details(chap_config_id)

    # CHAP config operations end
    # Service config operations start

    def get_service_configs(self, filter_dict=None, all_pages=None):
        """Get all service configurations.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all service
                            configurations or not
        :type all_pages: bool
        :return: List of service configurations
        :rtype: list[dict]
        """
        LOG.info("Getting service configurations with filter: '%s'", filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported for service configuration.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SERVICE_CONFIG_DETAILS_QUERY,
            )
            return self.config_client.request(
                constants.GET,
                constants.GET_SERVICE_CONFIG_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.SERVICE_CONFIG_DETAILS_QUERY, filter_dict,
        )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_CONFIG_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )

        filterable_keys = ["id", "appliance_id", "is_ssh_enabled"]

        service_config_resp = helpers.filtered_details(
            filterable_keys, filter_dict, resp, "service config",
        )

        if service_config_resp:
            src_cfg_list = []
            for resp in service_config_resp:
                config_details = self.get_service_config_details(resp["id"])
                src_cfg_list.append(config_details)
            return src_cfg_list
        return service_config_resp

    def get_service_config_by_appliance_id(self, appliance_id):
        """Get service configuration for appliance.

        :param appliance_id: ID of the appliance
        :type appliance_id: str
        :return: List of service configurations for the appliance
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting service config details for appliance with id: '{appliance_id}'",
        )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_CONFIG_LIST_URL.format(self.server_ip),
            querystring=constants.SERVICE_CONFIG_DETAILS_QUERY,
        )
        filterable_keys = ["id", "appliance_id", "is_ssh_enabled"]
        filter_dict = {"appliance_id": f"eq.{appliance_id}"}
        return helpers.filtered_details(
            filterable_keys, filter_dict, resp, "service config",
        )

    def get_service_config_details(self, service_config_id):
        """Get details of a particular service config.

        :param service_config_id: ID of the service config
        :type service_config_id: str
        :return: service config details
        :rtype: dict
        """
        LOG.info("Getting service config details by ID: '%s'", service_config_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_CONFIG_DETAILS_URL.format(
                self.server_ip, service_config_id,
            ),
            querystring=constants.SERVICE_CONFIG_DETAILS_QUERY,
        )

    def modify_service_config(self, service_config_id, is_ssh_enabled=None):
        """Modify service config properties.

        :param service_config_id: ID of the service config
        :type service_config_id: str
        :param is_ssh_enabled: Current SSH service access state
        :type is_ssh_enabled: bool
        :return: service config details
        :rtype : dict
        """
        LOG.info("Modifying service config properties: '%s'", service_config_id)
        payload = {}
        if is_ssh_enabled is not None:
            payload["is_ssh_enabled"] = is_ssh_enabled
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_SERVICE_CONFIG_URL.format(
                self.server_ip, service_config_id,
            ),
            payload,
        )
        return self.get_service_config_details(service_config_id)

    # Service config operations end

    # Service user operations start

    def get_service_users(self, filter_dict=None, all_pages=None):
        """Get all service users.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all service
                            users or not
        :type all_pages: bool
        :return: List of service users
        :rtype: list[dict]
        """
        LOG.info("Getting service users with filter: '%s'", filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported for service users.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID)
            return self.config_client.request(
                constants.GET,
                constants.GET_SERVICE_USER_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.SERVICE_USER_DETAILS_QUERY, filter_dict,
        )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_USER_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )

        filterable_keys = ["id", "is_built_in", "name", "is_default_password"]
        return helpers.filtered_details(
            filterable_keys, filter_dict, resp, "service user",
        )

    def get_service_user_details(self, service_user_id):
        """Get details of a particular service user.

        :param service_user_id: ID of the service user
        :type service_user_id: str
        :return: service user details
        :rtype: dict
        """
        LOG.info("Getting service user details by ID: '%s'", service_user_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_USER_DETAILS_URL.format(
                self.server_ip, service_user_id,
            ),
            querystring=constants.SERVICE_USER_DETAILS_QUERY,
        )

    def get_service_user_by_name(self, name):
        """Get service user details by name.

        :param name: Name of the service user
        :type name: str
        :return: service user details
        :rtype: list[dict]
        """
        LOG.info("Getting service user details by name: '%s'", name)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_USER_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.SERVICE_USER_DETAILS_QUERY, name=constants.EQUALS + name,
            ),
        )
        filterable_keys = ["id", "is_built_in", "name", "is_default_password"]
        filter_dict = {"name": f"eq.{name}"}
        return helpers.filtered_details(
            filterable_keys, filter_dict, resp, "service user",
        )

    def modify_service_user(self, service_user_id, password):
        """Modify service user properties.

        :param service_user_id: ID of the service user
        :type service_user_id: str
        :param password: The new password for the service user
        :type password: str
        :return: service user details
        :rtype : dict
        """
        LOG.info("Modifying service user properties: '%s'", service_user_id)
        payload = {}
        if password is not None:
            payload["password"] = password
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_SERVICE_USER_URL.format(self.server_ip, service_user_id),
            payload,
        )
        return self.get_service_user_details(service_user_id)

    # Service user operations end

    # IP ports operations start

    def get_ip_port_details(self, ip_port_id):
        """Get IP port details.

        :param ip_port_id: IP port ID
        :type ip_port_id: str
        :return: IP port details
        :rtype : dict
        """
        LOG.info("Getting IP port details by ID: '%s'", ip_port_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_IP_PORT_DETAILS_URL.format(self.server_ip, ip_port_id),
            querystring=constants.IP_PORT_DETAILS_QUERY,
        )

    # IP ports operations end

    # vCenter operations start
    def get_vcenters(self, filter_dict=None, all_pages=False):
        """Get all vcenters.
        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all vcenters
        :type all_pages: bool
        :return: List of vcenters
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting vcenters with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'", querystring)
        vcenter_list = self.config_client.request(
            constants.GET,
            constants.GET_VCENTER_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

        if vcenter_list:
            resp_list = []
            for vcenter in vcenter_list:
                resp_dict = self.get_vcenter_details(vcenter["id"])
                resp_list.append(resp_dict)
            return resp_list
        return vcenter_list

    def get_vcenter_details(self, vcenter_id):
        """Get vcenter details.
        :param vcenter_id: ID of the vcenter
        :type vcenter_id: str
        :return: Details of vcenter
        :rtype: dict
        """
        LOG.info("Getting vcenter details by ID: '%s'", vcenter_id)
        querystring = constants.VCENTER_DETAILS_QUERY
        if helpers.is_foot_hill_prime_or_higher():
            querystring = constants.FHP_VCENTER_QUERY
        elif helpers.is_foot_hill_or_higher():
            querystring = constants.FHC_MALKA_VCENTER_QUERY

        return self.config_client.request(
            constants.GET,
            constants.GET_VCENTER_DETAILS_URL.format(self.server_ip, vcenter_id),
            querystring=querystring,
        )

    def modify_vcenter(self, vcenter_id, modify_param_dict):
        """Modify vcenter attributes.
        :param vcenter_id: ID of the vcenter
        :type vcenter_id: str
        :param modify_param_dict: Dict containing parameters for modification
        :type modify_param_dict: dict
        :return: Details of vcenter
        :rtype: dict
        """
        LOG.info("Modifying vCenter attributes: '%s'", vcenter_id)
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_VCENTER_URL.format(self.server_ip, vcenter_id),
            payload=modify_param_dict,
        )
        return self.get_vcenter_details(vcenter_id)

    def add_vcenter(self, add_params):
        """Add a vcenter to the unified PowerStore model.
        vcenter can not be added to unified+ deployment
        :param add_params: the parameters to add vcenter
        :type add_params:dict
        :return: ID of the vcenter if addition is successful
        :rtype: dict
        """
        LOG.info("Adding a vcenter.")

        payload = {}
        if add_params:
            for key, values in add_params.items():
                payload[key] = values

        return self.config_client.request(
            constants.POST,
            constants.ADD_VCENTER_URL.format(self.server_ip),
            payload=payload,
        )

    def remove_vcenter(self, vcenter_id, delete_vasa_provider=None):
        """Remove vcenter from Unified PowerStore model.
        vcenter can not be removed from unified+ deployment
        :param vcenter_id: ID of the vcenter
        :type vcenter_id: str
        :param delete_vasa_provider: whether to remove a VASA provider.
                                     Removal will only happen if the provider
                                     is not connected to any other PowerStore
                                     system
        :type delete_vasa_provider: bool
        :return: None if success
        :rtype: None
        """
        LOG.info("Removing vcenter: %s.", vcenter_id)
        payload = {}
        if delete_vasa_provider is not None:
            payload["delete_vendor_provider"] = delete_vasa_provider

        return self.config_client.request(
            constants.DELETE,
            constants.REMOVE_VCENTER_URL.format(self.server_ip, vcenter_id),
            payload=payload,
        )

    # vCenter operations end

    # Appliance operations start
    def get_appliances(self, filter_dict=None, all_pages=False):
        """Get all appliances.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all appliances
                            or not
        :type all_pages: bool
        :return: List of appliances
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all appliances with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(
            constants.APPLIANCE_DETAILS_QUERY, filter_dict,
        )
        if helpers.is_foot_hill_prime_or_higher():
            querystring = helpers.prepare_querystring(
                constants.APPLIANCE_DETAILS_FHP_QUERY, filter_dict,
            )
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_APPLIANCE_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_appliance_details(self, appliance_id):
        """Get details of a particular appliance.

        :param appliance_id: ID of the appliance
        :type appliance_id: str
        :return: appliance details
        :rtype: dict
        """
        LOG.info("Getting appliance details by ID: '%s'", appliance_id)
        querystring = constants.APPLIANCE_DETAILS_QUERY
        if helpers.is_foot_hill_prime_or_higher():
            querystring = constants.APPLIANCE_DETAILS_FHP_QUERY
        elif helpers.is_foot_hill_or_higher():
            querystring = {
                "select": "id,name,service_tag,express_service_code,model,"
                "drive_failure_tolerance_level,nodes,"
                "ip_pool_addresses(id,name),veth_ports(id,name),"
                "maintenance_windows,fc_ports(id,name),"
                "sas_ports(id,name),eth_ports(id,name),"
                "software_installed(id,release_version),"
                "virtual_volumes(id,name),hardware(id,name),"
                "volumes(id,name)",
            }
        return self.config_client.request(
            constants.GET,
            constants.GET_APPLIANCE_DETAILS_URL.format(self.server_ip, appliance_id),
            querystring=querystring,
        )

    def get_appliance_by_name(self, appliance_name):
        """Get appliance details by name.

        :param appliance_name: Name of the appliance
        :type appliance_name: str
        :return: appliance details
        :rtype: list[dict]
        """
        LOG.info("Getting appliance details by name: '%s'", appliance_name)
        querystring = constants.APPLIANCE_DETAILS_QUERY
        if helpers.is_foot_hill_prime_or_higher():
            querystring = constants.APPLIANCE_DETAILS_FHP_QUERY
        elif helpers.is_foot_hill_or_higher():
            querystring = {
                "select": "id,name,service_tag,express_service_code,model,"
                "drive_failure_tolerance_level,nodes,"
                "ip_pool_addresses(id,name),veth_ports(id,name),"
                "maintenance_windows,fc_ports(id,name),"
                "sas_ports(id,name),eth_ports(id,name),"
                "software_installed(id,release_version),"
                "virtual_volumes(id,name),hardware(id,name),"
                "volumes(id,name)",
            }

        return self.config_client.request(
            constants.GET,
            constants.GET_APPLIANCE_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                querystring, name=constants.EQUALS + appliance_name,
            ),
        )

    # Discovered Appliances methods
    def get_discovered_appliances(self, filter_dict=None, all_pages=False):
        """Get discovered appliances.

        Parameters
        ----------
        - filter_dict (dict): (optional) Filter details
        - all_pages (bool): (optional) Indicates whether to return all
                            appliances or not

        Returns
        -------
        - List of discovered appliances (list)[dict]

        """
        LOG.info(
            "Getting discovered appliances with filter: '%s' and all_pages: '%s'",
            filter_dict,
            all_pages,
        )

        if all_pages:
            raise ValueError("Pagination is not supported for discovered appliances.")

        querystring = constants.DISCOVERED_APPLIANCE_DETAILS_QUERY.copy()

        if not filter_dict:
            querystring = helpers.prepare_querystring(querystring)

            LOG.info("Querystring without filters dict: '%s'", querystring)
            return self.config_client.request(
                constants.GET,
                constants.GET_DISCOVERED_APPLIANCE_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_DISCOVERED_APPLIANCE_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )
        filterable_keys = [
            "id",
            "link_local_address",
            "service_name",
            "state",
            "is_unified_capable",
            "mode",
            "is_local",
            "management_service_ready",
            "build_version",
            "node_count",
            "express_service_code",
        ]
        return helpers.filtered_details(
            filterable_keys, filter_dict, resp, "discovered_appliances",
        )

    # Appliance operations end

    # Certificate operations start
    def get_certificates(self, filter_dict=None, all_pages=None):
        """Get all certificates.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all certificates or not
        :type all_pages: bool
        :return: List of certificates
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting certificates with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_CERTIFICATE_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_certificate_details(self, certificate_id):
        """Get details of a particular certificate.

        :param certificate_id: ID of the certificate
        :type certificate_id: str
        :return: certificate details
        :rtype: dict
        """
        LOG.info("Getting certificate details by ID: '%s'", certificate_id)
        querystring = constants.CERTIFICATE_DETAILS_QUERY

        return self.config_client.request(
            constants.GET,
            constants.GET_CERTIFICATE_DETAILS_URL.format(
                self.server_ip, certificate_id,
            ),
            querystring=querystring,
        )

    def exchange_certificate(self, exchange_cert_dict):
        """Exchange the certificates between peers for remote system
        :param exchange_cert_dict: Exchange certificate dict includes
        address, port, service, username and password
        :type exchange_cert_dict: dict
        :return: None
        :rtype: NoneType
        """
        LOG.info("Exchanging certificates")
        if "port" not in exchange_cert_dict.keys():
            exchange_cert_dict["port"] = 443
        self.config_client.request(
            constants.POST,
            constants.EXCHANGE_CERTIFICATE_URL.format(self.server_ip),
            exchange_cert_dict,
        )

    def create_certificate(self, create_cert_dict):
        """Create a certificate.
        :param create_cert_dict: The create parameters which includes type, service,
        scope,certificate,private_key,passphrase and is_current
        :type create_cert_dict: dict
        :return: certificate_id if success else raise exception
        :rtype: dict
        """
        LOG.info("Creating certificate")
        payload = {}
        if create_cert_dict:
            for key, value in create_cert_dict.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST,
            constants.CREATE_CERTIFICATE_URL.format(
                self.server_ip,
            ),
            payload=payload,
        )

    def modify_certificate(self, certificate_id, modify_cert_dict):
        """ "Modify certificate properties.

        :param certificate_id: ID of the certificate
        :type certificate_id: str
        :param modify_cert_dict: The modify parameters which include certificate and is_current
        :type modify_cert_dict: dict
        :return: None
        :rtype : NoneType
        """
        LOG.info("Modifying certificate properties")

        return self.config_client.request(
            constants.PATCH,
            constants.MODIFY_CERTIFICATE_URL.format(self.server_ip, certificate_id),
            payload=modify_cert_dict,
        )

    def reset_certificates(self, reset_cert_dict):
        """Reset certificates.

        :param reset_cert_dict: Contains service parameter
        :type reset_cert_dict: dict
        :return: None
        :rtype : NoneType
        """
        LOG.info(
            f"Resetting certificates of the service: '{(reset_cert_dict['service'])}'",
        )
        payload = {}
        if reset_cert_dict:
            for key, value in reset_cert_dict.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST,
            constants.RESET_CERTIFICATE_URL.format(
                self.server_ip,
            ),
            payload=payload,
        )

    # Certificate operations end

    # security configuration operations start

    def get_security_configs(self, filter_dict=None, all_pages=False):
        """Get all security configurations.

        :param filter_dict: (optional) filter dict
        :type filter_dict: dict
        :param all_pages: (optional) indicate whether to return all elements
                          or not
        :type all_pages: bool
        :return: List of all security configs
        :rtype: list[dict]
        """
        LOG.info("Getting security configs with filter: '%s'", filter_dict)
        if all_pages:
            raise Exception("Pagination is not supportedfor security configs.")

        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID)
            return self.config_client.request(
                constants.GET,
                constants.GET_SECURITY_CONFIG_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )
        querystring = helpers.prepare_querystring(
            constants.SECURITY_CONFIG_DETAILS_QUERY, filter_dict,
        )
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SECURITY_CONFIG_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=False,
        )

        filterable_key = ["id"]
        if helpers.is_foot_hill_or_higher():
            filterable_key = ["id", "protocol_mode"]
        return helpers.filtered_details(
            filterable_key, filter_dict, resp, "security config",
        )

    def get_security_config_details(self, security_config_id):
        """Get details of particular security configuration.

        :param security_config_id: id of security config
        :type security_config_id: str
        :return: security config details
        :rtype: dict
        """
        LOG.info("Getting security config details by ID: '%s'", security_config_id)

        querystring = constants.SECURITY_CONFIG_DETAILS_QUERY
        if not helpers.is_foot_hill_or_higher():
            querystring = {"select": "id,idle_timeout"}
        return self.config_client.request(
            constants.GET,
            constants.GET_SECURITY_CONFIG_DETAILS_URL.format(
                self.server_ip, security_config_id,
            ),
            querystring=querystring,
        )

    def modify_security_config(self, security_config_id, protocol_mode):
        """Modify Security configuration.

        :param security_config_id: id of security config
        :type security_config_id: str
        :param protocol_mode: protocol mode of security config
        :type protocol_mode: str
        :return: None
        :rtype: None
        """
        LOG.info(
            f"Modify security config properties: '{security_config_id}' with params '{protocol_mode}'",
        )

        payload = {}
        payload["protocol_mode"] = protocol_mode
        return self.config_client.request(
            constants.PATCH,
            constants.MODIFY_SECURITY_CONFIG_URL.format(
                self.server_ip, security_config_id,
            ),
            payload=payload,
        )

    # security configuration operations end

    # email operations start

    def get_destination_emails(self, filter_dict=None, all_pages=False):
        """Get all destination email addresses.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all elements
                          or not
        :type all_pages: bool
        :return: destination emails.
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting email addresses with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_ADDRESS, filter_dict,
        )
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_EMAIL_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_destination_email_details(self, email_id):
        """Get details of particular email notification destination.

        :param email_id: id of email notification destination
        :type email_id: str
        :return: email details
        :rtype: dict
        """
        LOG.info("Getting email details by ID: '%s'", email_id)

        querystring = constants.EMAIL_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_EMAIL_DETAILS_URL.format(self.server_ip, email_id),
            querystring=querystring,
        )

    def get_destination_email_by_address(self, email_address):
        """Get destination email details by address.

        :param email_address: Destination email address.
        :type email_address: str
        :return: Destination email details with corresponding email_address.
        :rtype: list[dict]
        """
        LOG.info("Getting destination email details by address: '%s'", email_address)
        return self.config_client.request(
            constants.GET,
            constants.GET_EMAIL_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.EMAIL_DETAILS_QUERY,
                email_address=constants.EQUALS + email_address,
            ),
        )

    def modify_destination_email_details(self, email_id, modify_parameters):
        """Modify destination_email properties.

        :param email_id: ID of the email destination
        :type email_id: str
        :param modify_parameters: Dictionary containing attributes to be
                                    modified for the email address
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info(
            f"Modifying destination email properties: '{email_id}' with params '{modify_parameters}'",
        )

        email_url = constants.MODIFY_EMAIL_URL
        return self.config_client.request(
            constants.PATCH,
            email_url.format(self.server_ip, email_id),
            payload=modify_parameters,
        )

    def delete_destination_email(self, email_id):
        """Delete a destination_email.

        :param email_id: ID of the email destination
        :type email_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting email id: '%s'", email_id)
        return self.config_client.request(
            constants.DELETE,
            constants.DELETE_EMAIL_URL.format(self.server_ip, email_id),
            payload=None,
        )

    def test_destination_email(self, email_id):
        """Send a test mail to the destination.

        :param email_id: ID of the email destination
        :type email_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Testing email id: '%s'", email_id)
        return self.config_client.request(
            constants.POST,
            constants.TEST_EMAIL_URL.format(self.server_ip, email_id),
            payload=None,
        )

    def create_destination_email(self, create_params):
        """Create a destination_email.

        :param create_params: The create params
        :type create_params: list<dict>
        :return: email id if success else raise exception
        :rtype: dict
        """
        LOG.info("creating email notification destination")

        payload = {}
        if create_params:
            for key, value in create_params.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST,
            constants.CREATE_EMAIL_URL.format(
                self.server_ip,
            ),
            payload=payload,
        )

    # email operations end

    # smtp operations start

    def get_smtp_configs(self, filter_dict=None, all_pages=None):
        """Get all SMTP configurations.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all smtp servers or not
        :type all_pages: bool
        :return: List of SMTP servers
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting SMTP configs with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_SMTP_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_smtp_config_details(self, smtp_id):
        """Get details of an SMTP configuration instance.

        :param smtp_id: Unique identifier of smtp configuration
        :type smtp_id: str
        :return: smtp details
        :rtype: dict
        """
        LOG.info("Getting SMTP config details by ID: '%s'", smtp_id)

        querystring = constants.SMTP_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_SMTP_DETAILS_URL.format(self.server_ip, smtp_id),
            querystring=querystring,
        )

    def modify_smtp_config_details(self, smtp_id, modify_parameters):
        """Modify SMTP configuration properties.

        :param smtp_id: ID of the SMTP configuration
        :type smtp_id: str
        :param modify_parameters: Dictionary containing attributes to be
                                    modified for the SMTP configuration
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info(
            f"Modifying SMTP configuration properties: '{smtp_id}' with params '{modify_parameters}'",
        )

        smtp_url = constants.MODIFY_SMTP_URL
        return self.config_client.request(
            constants.PATCH,
            smtp_url.format(self.server_ip, smtp_id),
            payload=modify_parameters,
        )

    def test_smtp_config(self, smtp_id, test_parameters):
        """Send a test mail from the SMTP configuration.

        :param smtp_id: ID of the SMTP configuration
        :type smtp_id: str
        :param test_parameters: Dictionary containing destination
                                email address for the SMTP configuration
        :type test_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Testing smtp id: '%s'", smtp_id)
        return self.config_client.request(
            constants.POST,
            constants.TEST_SMTP_URL.format(self.server_ip, smtp_id),
            payload=test_parameters,
        )

    # smtp operations end

    # dns operations start

    def get_dns_list(self, filter_dict=None, all_pages=None):
        """Get all DNS servers available on array.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all DNS or not
        :type all_pages: bool
        :return: List of DNS on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all DNS servers with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_DNS_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_dns_details(self, dns_id):
        """Get details of a DNS instance.

        :param dns_id: Unique identifier of the DNS setting
        :type dns_id: str
        :return: DNS setting details
        :rtype: dict
        """
        LOG.info("Getting DNS details by ID: '%s'", dns_id)

        querystring = constants.DNS_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_DNS_DETAILS_URL.format(self.server_ip, dns_id),
            querystring=querystring,
        )

    def modify_dns_details(self, dns_id, modify_parameters):
        """Modify DNS properties.

        :param dns_id: Unique identifier of the DNS setting
        :type dns_id: str
        :param modify_parameters: Dictionary containing list of
                                  DNS server addresses in IPv4 format
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info("Modifying DNS : '%s' with params '%s'", dns_id, modify_parameters)

        dns_url = constants.MODIFY_DNS_URL
        return self.config_client.request(
            constants.PATCH,
            dns_url.format(self.server_ip, dns_id),
            payload=modify_parameters,
        )

    # dns operations end

    # NTP operations start
    def get_ntp_list(self, filter_dict=None, all_pages=None):
        """Get all NTP servers available on array.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all NTP
                          or not
        :type all_pages: bool
        :return: List of NTP on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all NTP servers with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_NTP_LIST_URL.format(self.server_ip),
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_ntp_details(self, ntp_id):
        """Get details of a NTP instance.

        :param ntp_id: Unique identifier of the NTP setting
        :type ntp_id: str
        :return: NTP setting details
        :rtype: dict
        """
        LOG.info("Getting NTP details by ID: '%s'", ntp_id)

        querystring = constants.NTP_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_NTP_DETAILS_URL.format(self.server_ip, ntp_id),
            querystring=querystring,
        )

    def modify_ntp_details(self, ntp_id, modify_parameters):
        """Modify NTP properties.

        :param ntp_id: Unique identifier of the NTP setting
        :type ntp_id: str
        :param modify_parameters: Dictionary containing list of
                                  NTP server addresses, could be host names or
                                  IPv4 addresses
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info("Modifying NTP : '%s' with params '%s'", ntp_id, modify_parameters)

        ntp_url = constants.MODIFY_NTP_URL
        return self.config_client.request(
            constants.PATCH,
            ntp_url.format(self.server_ip, ntp_id),
            payload=modify_parameters,
        )

    # NTP operations end

    # Remote Support operations start

    def get_remote_support_list(self, filter_dict=None, all_pages=None):
        """Get all Remote Support configurations available on array.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all remote
                          support configurations or not
        :type all_pages: bool
        :return: List of remote support configurations on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all remote_support with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        if helpers.is_foot_hill_or_higher():
            querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
            LOG.info("Querystring: '%s'", querystring)
            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=all_pages,
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def get_remote_support_details(
        self, remote_support_id, return_support_license_text=False,
    ):
        """Get details of a remote support configuration instance.

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :return: remote support configuration details
        :rtype: dict
        """
        LOG.info("Getting remote_support details by ID: '%s'", remote_support_id)
        if helpers.is_foot_hill_or_higher():
            querystring = constants.REMOTE_SUPPORT_DETAILS_QUERY
            if return_support_license_text is True:
                querystring["select"] = (
                    querystring["select"] + ",support_assist_license_agreement_text"
                )

            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_DETAILS_URL.format(
                    self.server_ip, remote_support_id,
                ),
                querystring=querystring,
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def modify_remote_support_details(
        self, remote_support_id, modify_parameters, is_async=False,
    ):
        """Modify remote support configuration properties.

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :param modify_parameters: Dictionary containing list of parameters of
                                  remote support configuration to be modified.
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info(
            f"Modifying remote_support : '{remote_support_id}' with params '{modify_parameters}'",
        )
        if helpers.is_foot_hill_or_higher():
            remote_support_url = constants.MODIFY_REMOTE_SUPPORT_URL
            if is_async:
                remote_support_url = remote_support_url + "?is_async=true"
            return self.config_client.request(
                constants.PATCH,
                remote_support_url.format(self.server_ip, remote_support_id),
                payload=modify_parameters,
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def verify_remote_support_config(self, remote_support_id, verify_parameters):
        """Verify remote support configuration .

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :param verify_parameters: Dictionary containing list of
                                  parameters to verify the remote
                                  support configuration
        :type verify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info(
            f"Verifying remote_support : '{remote_support_id}' with params '{verify_parameters}'",
        )
        if helpers.is_foot_hill_or_higher():
            remote_support_url = constants.VERIFY_REMOTE_SUPPORT_URL
            return self.config_client.request(
                constants.POST,
                remote_support_url.format(self.server_ip, remote_support_id),
                payload=verify_parameters,
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def test_remote_support_config(self, remote_support_id):
        """Send a test alert for the remote support configuration.

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :return: None
        :rtype : None
        """
        LOG.info("Sending a test alert for remote_support : '%s'", (remote_support_id))
        if helpers.is_foot_hill_or_higher():
            remote_support_url = constants.SEND_ALERT_REMOTE_SUPPORT_URL
            return self.config_client.request(
                constants.POST,
                remote_support_url.format(self.server_ip, remote_support_id),
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    # Remote Support operations end

    # Remote Support contact operations start

    def get_remote_support_contact_list(self, filter_dict=None, all_pages=None):
        """Get all remote support contacts available on array.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all
                          remote support contacts or not
        :type all_pages: bool
        :return: List of remote support contacts on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all remote support contact with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )
        if helpers.is_foot_hill_or_higher():
            querystring = helpers.prepare_querystring(constants.SELECT_ID, filter_dict)
            LOG.info("Querystring: '%s'", querystring)
            array_version = self.provisioning.get_array_version()
            if array_version == "2.0.0.0":
                resp = self.config_client.request(
                    constants.GET,
                    constants.GET_REMOTE_SUPPORT_CONTACT_LIST_URL.format(
                        self.server_ip,
                    ),
                    querystring=constants.REMOTE_SUPPORT_CONTACT_DETAILS_QUERY,
                    all_pages=False,
                )

                filterable_keys = ["id", "email", "first_name", "last_name", "phone"]
                return helpers.filtered_details(
                    filterable_keys, filter_dict, resp, "remote_support_contact",
                )
            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_CONTACT_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=all_pages,
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def get_remote_support_contact_details(self, remote_support_contact_id):
        """Get details of a remote support contact instance.

        :param remote_support_contact_id: Unique identifier of the remote support contacts
        :type remote_support_contact_id: str
        :return: remote support contacts details
        :rtype: dict
        """
        LOG.info(
            f"Getting remote support contact details by ID: '{remote_support_contact_id}'",
        )
        if helpers.is_foot_hill_or_higher():
            querystring = constants.REMOTE_SUPPORT_CONTACT_DETAILS_QUERY
            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_CONTACT_DETAILS_URL.format(
                    self.server_ip, remote_support_contact_id,
                ),
                querystring=querystring,
            )

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def modify_remote_support_contact_details(
        self, remote_support_contact_id, modify_parameters,
    ):
        """Modify remote support contacts properties.

        :param remote_support_contact_id: Unique identifier of the remote support contacts
        :type remote_support_contact_id: str
        :param modify_parameters: Dictionary containing list of parameters of
                                  remote support contact to be modified.
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info(
            f"Modifying remote support contact : '{remote_support_contact_id}' with params '{modify_parameters}'",
        )
        if helpers.is_foot_hill_or_higher():
            remote_support_contact_url = constants.MODIFY_REMOTE_SUPPORT_CONTACT_URL
            return self.config_client.request(
                constants.PATCH,
                remote_support_contact_url.format(
                    self.server_ip, remote_support_contact_id,
                ),
                payload=modify_parameters,
            )
        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    # Remote Support contact operations end

    # LDAP Domain operations start

    def get_ldap_domain_configuration_list(self, filter_dict=None, all_pages=None):
        """Get all LDAP domain configurations available on array.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all ldap
                          domain configurations or not
        :type all_pages: bool
        :return: List of ldap domain configurations on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all ldap domain with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )

        if all_pages:
            raise Exception("Pagination is not supported for LDAP domain.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.LDAP_DOMAIN_DETAILS_QUERY,
            )
            return self.config_client.request(
                constants.GET,
                constants.GET_LDAP_DOMAIN_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        resp = self.config_client.request(
            constants.GET,
            constants.GET_LDAP_DOMAIN_LIST_URL.format(self.server_ip),
            querystring=constants.LDAP_DOMAIN_DETAILS_QUERY,
            all_pages=False,
        )

        filterable_keys = ["domain_name", "id", "protocol", "ldap_server_type"]
        ldap_domain_resp = helpers.filtered_details(
            filterable_keys, filter_dict, resp, "ldap_domain",
        )

        if ldap_domain_resp:
            filter_list = []
            ldap_domain_dict = self.get_ldap_domain_configuration_details(
                ldap_domain_resp[0]["id"],
            )
            filter_list.append(ldap_domain_dict)
            return filter_list
        return ldap_domain_resp

    def get_ldap_domain_configuration_details(self, ldap_domain_id):
        """Get details of a ldap domain instance.

        :param ldap_domain_id: Unique identifier of the ldap domain
        :type ldap_domain_id: str
        :return: ldap domain details
        :rtype: dict
        """
        LOG.info("Getting ldap domain details by ID: '%s'", ldap_domain_id)

        return self.config_client.request(
            constants.GET,
            constants.GET_LDAP_DOMAIN_DETAILS_URL.format(
                self.server_ip, ldap_domain_id,
            ),
            querystring=constants.LDAP_DOMAIN_DETAILS_QUERY,
        )

    def get_ldap_domain_configuration_details_by_name(self, ldap_domain_name):
        """Get details of a ldap domain instance.

        :param ldap_domain_name: LDAP domain name
        :type ldap_domain_name: str
        :return: ldap domain details
        :rtype: dict
        """
        LOG.info("Getting ldap domain details by name")

        resp = self.config_client.request(
            constants.GET,
            constants.GET_LDAP_DOMAIN_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.LDAP_DOMAIN_DETAILS_QUERY,
                domain_name=constants.EQUALS + ldap_domain_name,
            ),
        )

        filterable_keys = ["domain_name", "id", "protocol", "ldap_server_type"]
        filter_dict = {"domain_name": f"eq.{ldap_domain_name}"}
        resp = helpers.filtered_details(
            filterable_keys, filter_dict, resp, "ldap_domain",
        )
        if resp:
            return self.get_ldap_domain_configuration_details(resp[0]["id"])

    def create_ldap_domain_configuration(self, create_parameters):
        """Create LDAP domain configuration.

        :param create_parameters: Parameters for creating LDAP domain
        :type create_parameters: dict
        :return: Unique identifier of the new LDAP domain instance created
        :rtype: dict
        """
        LOG.info("creating LDAP domain")

        return self.config_client.request(
            constants.POST,
            constants.CREATE_LDAP_DOMAIN_URL.format(self.server_ip),
            payload=create_parameters,
        )

    def modify_ldap_domain_configuration(self, ldap_domain_id, modify_parameters):
        """Modify LDAP domain configuration.

        :param ldap_domain_id: Unique ID of the LDAP domain instance
        :type ldap_domain_id: str
        :param modify_parameters: Parameters for modifying LDAP domain
        :type modify_parameters: dict
        :return: None
        :rtype: None
        """
        LOG.info("Modifying LDAP domain configuration id: '%s'", ldap_domain_id)

        return self.config_client.request(
            constants.PATCH,
            constants.MODIFY_LDAP_DOMAIN_URL.format(self.server_ip, ldap_domain_id),
            payload=modify_parameters,
        )

    def delete_ldap_domain_configuration(self, ldap_domain_id):
        """Delete LDAP domain configuration.

        :param ldap_domain_id: Unique ID of the LDAP domain instance
        :type ldap_domain_id: str
        :return: None
        :rtype: None
        """
        LOG.info("Deleting LDAP domain configuration id: '%s'", ldap_domain_id)

        return self.config_client.request(
            constants.DELETE,
            constants.DELETE_LDAP_DOMAIN_URL.format(self.server_ip, ldap_domain_id),
        )

    def verify_ldap_domain_configuration(self, ldap_domain_id):
        """Verify LDAP domain configuration.

        :param ldap_domain_id: Unique ID of the LDAP domain instance
        :type ldap_domain_id: str
        :return: None
        :rtype: None
        """
        LOG.info("Verifying LDAP domain configuration id: '%s'", ldap_domain_id)

        return self.config_client.request(
            constants.POST,
            constants.VERIFY_LDAP_DOMAIN_URL.format(self.server_ip, ldap_domain_id),
        )

    # LDAP Domain operations end

    # LDAP Account operations begin

    def get_ldap_account_list(self, filter_dict=None, all_pages=None):
        """Get all LDAP accounts available on array.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all LDAP
                          accounts or not
        :type all_pages: bool
        :return: List of LDAP accounts on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting all ldap accounts with filter: '{filter_dict}' and all_pages: '{all_pages}'",
        )

        if all_pages:
            raise Exception("Pagination is not supported for LDAP accounts.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.LDAP_ACCOUNT_DETAILS_QUERY,
            )
            return self.config_client.request(
                constants.GET,
                constants.GET_LDAP_ACCOUNT_LIST_URL.format(self.server_ip),
                querystring=querystring,
                all_pages=False,
            )

        resp = self.config_client.request(
            constants.GET,
            constants.GET_LDAP_ACCOUNT_LIST_URL.format(self.server_ip),
            querystring=constants.LDAP_ACCOUNT_DETAILS_QUERY,
            all_pages=False,
        )

        filterable_keys = ["name", "id", "role_id", "type"]
        ldap_account_resp = helpers.filtered_details(
            filterable_keys, filter_dict, resp, "ldap_accounts",
        )

        # Return all the details for each LDAP account
        if ldap_account_resp:
            resp_list = []
            for resp in ldap_account_resp:
                resp_dict = self.get_ldap_account_details(resp["id"])
                resp_list.append(resp_dict)
            return resp_list
        return ldap_account_resp

    def get_ldap_account_details(self, ldap_account_id):
        """Get details of a LDAP account instance.

        :param ldap_account_id: Unique identifier of the LDAP Account
        :type ldap_account_id: str
        :return: LDAP account details
        :rtype: dict
        """
        LOG.info("Getting LDAP account details by ID: '%s'", ldap_account_id)

        return self.config_client.request(
            constants.GET,
            constants.GET_LDAP_ACCOUNT_DETAILS_URL.format(
                self.server_ip, ldap_account_id,
            ),
            querystring=constants.LDAP_ACCOUNT_DETAILS_QUERY,
        )

    def get_ldap_account_details_by_name(self, ldap_account_name):
        """Get details of an ldap account instance.

        :param ldap_account_name: LDAP account name
        :type ldap_account_name: str
        :return: ldap account details
        :rtype: dict
        """
        LOG.info("Getting LDAP Account details by name: '%s'", ldap_account_name)
        resp = self.get_ldap_account_list()

        for account in resp:
            if account["name"] == ldap_account_name:
                return self.get_ldap_account_details(account["id"])

    def create_ldap_account(self, create_parameters):
        """Create LDAP account configuration.

        :param create_parameters: Parameters for creating LDAP account
        :type create_parameters: dict
        :return: Unique identifier of the new LDAP account instance created
        :rtype: dict
        """
        LOG.info("creating LDAP account")

        return self.config_client.request(
            constants.POST,
            constants.CREATE_LDAP_ACCOUNT_URL.format(self.server_ip),
            payload=create_parameters,
        )

    def modify_ldap_account_details(self, ldap_account_id, modify_parameters):
        """Modify LDAP account configuration.

        :param ldap_account_id: Unique ID of the LDAP account instance
        :type ldap_account_id: str
        :param modify_parameters: Parameters for modifying LDAP account
        :type modify_parameters: dict
        :return: None
        :rtype: None
        """
        LOG.info("Modifying LDAP account id: '%s'", ldap_account_id)

        return self.config_client.request(
            constants.PATCH,
            constants.MODIFY_LDAP_ACCOUNT_URL.format(self.server_ip, ldap_account_id),
            payload=modify_parameters,
        )

    def delete_ldap_account(self, ldap_account_id):
        """Delete LDAP account.

        :param ldap_account_id: Unique ID of the LDAP account instance
        :type ldap_account_id: str
        :return: None
        :rtype: None
        """
        LOG.info("Deleting LDAP account configuration id: '%s'", ldap_account_id)

        return self.config_client.request(
            constants.DELETE,
            constants.DELETE_LDAP_ACCOUNT_URL.format(self.server_ip, ldap_account_id),
        )

    # LDAP Account operations end

    # Virtual volume operations begin

    def get_virtual_volume_list(self, filter_dict=None, all_pages=None):
        """Get all virtual volumes available on array.
        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all
                          virtual volumes or not
        :type all_pages: bool
        :return: List of virtual volumes on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting volumes with filter: '{filter_dict}' and all_pages: {all_pages}",
        )
        querystring = helpers.prepare_querystring(
            constants.VIRTUAL_VOLUME_DETAILS_QUERY, filter_dict,
        )
        if helpers.is_foot_hill_prime_or_higher():
            querystring = helpers.prepare_querystring(
                constants.VIRTUAL_VOLUME_FHP_DETAILS_QUERY, filter_dict,
            )
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_VIRTUAL_VOLUME_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    # Virtual volume operations end

    # Storage container operations begin

    def get_storage_container_list(self, filter_dict=None, all_pages=None):
        """Get all storage container available on array.
        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all
                          Storage containers or not
        :type all_pages: bool
        :return: List of storage containers on array
        :rtype: list[dict]
        """
        LOG.info(
            f"Getting storage containers with filter: '{filter_dict}' and all_pages: {all_pages}",
        )
        querystring = helpers.prepare_querystring(
            constants.STORAGE_CONTAINER_DETAILS_QUERY, filter_dict,
        )
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_STORAGE_CONTAINER_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_storage_container_details(self, storage_container_id):
        """Get details of a storage container instance.

        :param storage_container_id: Unique identifier of the storage_container
        :type storage_container_id: str
        :return: storage container details
        :rtype: dict
        """
        LOG.info("Getting storage container details by ID: '%s'", storage_container_id)

        return self.config_client.request(
            constants.GET,
            constants.GET_STORAGE_CONTAINER_DETAILS_URL.format(
                self.server_ip, storage_container_id,
            ),
            querystring=constants.STORAGE_CONTAINER_DETAILS_QUERY,
        )

    def get_storage_container_details_by_name(self, storage_container_name):
        """Get details of a storage container instance.

        :param storage_container_name: storage container name
        :type storage_container_name: str
        :return: storage container details
        :rtype: dict
        """
        LOG.info(
            f"Getting storage container details by name: '{storage_container_name}'",
        )
        resp = self.get_storage_container_list()

        for container in resp:
            if container["name"] == storage_container_name:
                return self.get_storage_container_details(container["id"])

    def create_storage_container(self, create_parameters):
        """Create a storage_container.

        :param create_parameters: Parameters for creating a storage_container
        :type create_parameters: dict
        :return: Unique identifier of the new storage container instance created
        :rtype: dict
        """
        LOG.info("creating storage container")

        return self.config_client.request(
            constants.POST,
            constants.CREATE_STORAGE_CONTAINER_URL.format(self.server_ip),
            payload=create_parameters,
        )

    def modify_storage_container_details(self, storage_container_id, modify_parameters):
        """Modifying storage container configuration.

        :param storage_container_id: Unique ID of the storage container instance
        :type storage_container_id: str
        :param modify_parameters: Parameters for modifying storage container
        :type modify_parameters: dict
        :return: None
        :rtype: None
        """
        LOG.info("Modifying storage containert id: '%s'", storage_container_id)

        return self.config_client.request(
            constants.PATCH,
            constants.MODIFY_STORAGE_CONTAINER_URL.format(
                self.server_ip, storage_container_id,
            ),
            payload=modify_parameters,
        )

    def delete_storage_container(self, storage_container_id, delete_parameters):
        """Delete a storage container.

        :param storage_container_id: Unique ID of the storage container instance
        :type storage_container_id: str
        :return: None
        :rtype: None
        """
        LOG.info("Deleting storage container with id: '%s'", storage_container_id)

        return self.config_client.request(
            constants.DELETE,
            constants.DELETE_STORAGE_CONTAINER_URL.format(
                self.server_ip, storage_container_id,
            ),
            payload=delete_parameters,
        )

    # Storage container operations end

    # Storage container destination operations start
    def get_storage_container_destination_list(self, filter_dict=None, all_pages=None):
        """Get all storage container destination.
        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all
                          Storage containers destination or not
        :type all_pages: bool
        :return: List of storage containers destination
        :rtype: list[dict]
        """
        LOG.info(
            "Getting storage containers destination with filter: '%s' "
            "and all_pages: %s" % (filter_dict, all_pages),
        )
        querystring = helpers.prepare_querystring(
            constants.STORAGE_CONTAINER_DETAILS_DESTINATION_QUERY, filter_dict,
        )
        LOG.info("Querystring: '%s'", querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_STORAGE_CONTAINER_DESTINATION_LIST_URL.format(self.server_ip),
            payload=None,
            querystring=querystring,
            all_pages=all_pages,
        )

    def get_storage_container_destination_details(
        self, storage_container_destination_id,
    ):
        """Get details of a storage container destination instance.

        :param storage_container_destination_id: Unique identifier of the
                                                 storage container destination
        :type storage_container_destination_id: str
        :return: storage container destination details
        :rtype: dict
        """
        LOG.info(
            "Getting storage container destination details by "
            "ID: '%s'" % storage_container_destination_id,
        )

        return self.config_client.request(
            constants.GET,
            constants.GET_STORAGE_CONTAINER_DESTINATION_DETAILS_URL.format(
                self.server_ip, storage_container_destination_id,
            ),
            querystring=constants.STORAGE_CONTAINER_DETAILS_DESTINATION_QUERY,
        )

    def create_storage_container_destination(self, create_destination_params):
        """Create a Storage Container Destination
        :param create_destination_params: parameter to create storage container
                                          destination
        :type create_destination_params: dict
        :return: Unique identifier of newly created storage container destination
        :rtype: dict
        """
        LOG.info("Creating storage container destination.")
        return self.config_client.request(
            constants.POST,
            constants.CREATE_STORAGE_CONTAINER_DESTINATION_URL.format(self.server_ip),
            payload=create_destination_params,
        )

    def delete_storage_container_destination(self, storage_container_destination_id):
        """Delete a storage container destination
        :param storage_container_destination_id: ID of storage container destination
        :type storage_container_destination_id: str
        :rtype: None
        """
        LOG.info(
            "Deleting storage container destination with "
            "id: '%s'" % storage_container_destination_id,
        )
        return self.config_client.request(
            constants.DELETE,
            constants.DELETE_STORAGE_CONTAINER_DESTINATION_URL.format(
                self.server_ip, storage_container_destination_id,
            ),
        )

    # Storage container destination operations end

    @staticmethod
    def _prepare_local_user_payload(**kwargs):
        """Prepare a local user request body using provided arguments.

        :return: Request body
        :rtype: dict
        """
        payload = {}
        for argname in ("name", "role_id", "is_locked", "current_password", "password"):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload

    @staticmethod
    def _prepare_add_remove_network_payload(**kwargs):
        """Prepare add/remove network request body using provided arguments.

        :return: Request body
        :rtype: dict
        """
        payload = {}
        for argname in ("add_port_ids", "remove_port_ids"):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload

    @staticmethod
    def _prepare_create_cluster_payload(is_http_redirect_enabled, **kwargs):
        """Prepare payload for creation of cluster
        :return: Request body
        :rtype: dict
        """
        payload = {}
        for agrname in (
            "cluster",
            "appliances",
            "dns_servers",
            "ntp_servers",
            "physical_switches",
            "networks",
            "vcenters",
        ):
            if kwargs.get(agrname) is not None:
                payload[agrname] = kwargs[agrname]

        if is_http_redirect_enabled is not None:
            security_config = {}
            security_config["is_http_redirect_enabled"] = is_http_redirect_enabled
            payload["security_config"] = security_config

        return payload
