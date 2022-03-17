# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Dell EMC

"""Collection of configuration related functions for PowerStore"""

from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)


class Configuration:
    """Configuration related functionality for PowerStore."""

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
            "Getting networks with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))

        querystring = helpers.prepare_querystring(
            constants.SELECT_ID, filter_dict)

        if helpers.is_foot_hill_or_higher():
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME, filter_dict)

        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_NETWORK_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_network_details(self, network_id):
        """ Get details of a particular network.

        :param network_id: ID of the network
        :type network_id: str
        :return: Network details
        :rtype: dict
        """

        LOG.info("Getting network details by ID: '%s'" % network_id)
        querystring = constants.NETWORK_DETAILS_QUERY

        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,name,type,ip_version,vlan_id,prefix_length,'
                          'gateway,mtu,purposes,type_l10n,ip_version_l10n,'
                          'purposes_l10n'
            }

        return self.config_client.request(
            constants.GET,
            constants.GET_NETWORK_DETAILS_URL.format(self.server_ip,
                                                     network_id),
            querystring=querystring
        )

    def get_network_by_name(self, name):
        """Get network details by name.
        
        :param name: Name of the network
        :type name: str
        :return: Network details
        :rtype: list[dict]
        """
        LOG.info("Getting network details by name: '%s'" % name)

        NETWORK_DETAILS_QUERY_BY_NAME = {
            'select': 'id,name,type,ip_version,vlan_id,prefix_length,'
                      'gateway,mtu,purposes,type_l10n,ip_version_l10n,'
                      'purposes_l10n'
        }

        return self.config_client.request(
            constants.GET,
            constants.GET_NETWORK_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                NETWORK_DETAILS_QUERY_BY_NAME,
                name=constants.EQUALS + name))

    def modify_network(self, network_id, network_other_params,
                       is_async=False):
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
        LOG.info("Modifying network properties: '%s' with params '%s'" % (
            network_id, network_other_params))

        network_url = constants.MODIFY_NETWORK_URL
        if is_async:
            network_url = network_url + "?is_async=true"
        return self.config_client.request(
            constants.PATCH,
            network_url.format(self.server_ip, network_id),
            payload=network_other_params
        )

    def add_remove_ports(self, network_id, add_port_ids=None,
                         remove_port_ids=None):
        """ Add/remove IP ports from storage network.

        :param network_id: ID of the network
        :type network_id: str
        :param add_port_ids: List of IP ports to be added to the
                             storage network
        :type add_port_ids: list[str]
        :param remove_port_ids: List of IP ports to be removed from the
                                storage network
        :type remove_port_ids: list[str]
        """
        LOG.info("Add/remove IP ports: '%s'" % network_id)
        payload = self._prepare_add_remove_network_payload(
            add_port_ids=add_port_ids, remove_port_ids=remove_port_ids)
        self.config_client.request(constants.POST,
                                   constants.ADD_REMOVE_IP_PORTS.format(
                                       self.server_ip, network_id), payload)
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
        LOG.info("Getting roles with filter: '%s'" % filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported for roles.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME)
            return self.config_client.request(
                constants.GET, constants.GET_ROLE_LIST_URL.format(
                    self.server_ip), querystring=querystring, all_pages=False)

        resp = self.config_client.request(
            constants.GET,
            constants.GET_ROLE_LIST_URL.format(self.server_ip),
            querystring=constants.ROLE_DETAILS_QUERY, all_pages=False)

        filterable_keys = ['name', 'id', 'is_built_in']
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'roles')

    def get_role_details(self, role_id):
        """ Get details of a particular role.

        :param role_id: ID of the role
        :type role_id: str
        :return: Role details
        :rtype: dict
        """
        LOG.info("Getting role details by ID: '%s'" % role_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_ROLE_DETAILS_URL.format(self.server_ip, role_id),
            querystring=constants.ROLE_DETAILS_QUERY
        )

    def get_role_by_name(self, name):
        """Get role details by name.

        :param name: Name of the role
        :type name: str
        :return: Role details
        :rtype: dict
        """
        LOG.info("Getting role details by name: '%s'" % name)
        resp = self.get_roles()
        for role in resp:
            if role['name'] == name:
                return self.get_role_details(role['id'])

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
        LOG.info("Getting local users with filter: '%s'" % filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported"
                            " for local users.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME)
            return self.config_client.request(
                constants.GET, constants.GET_LOCAL_USER_LIST_URL.format(
                    self.server_ip), querystring=querystring, all_pages=False)
        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.LOCAL_USER_DETAILS_QUERY, filter_dict)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_LOCAL_USER_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=False)

        filterable_keys = ['name', 'id', 'is_locked']
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'local user')

    def get_local_user_details(self, user_id):
        """ Get details of a particular local user.

        :param user_id: ID of the role
        :type user_id: str
        :return: local user details
        :rtype: dict
        """
        LOG.info("Getting local user details by user ID: '%s'" % user_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_LOCAL_USER_DETAILS_URL.format(
                self.server_ip, user_id),
            querystring=constants.LOCAL_USER_DETAILS_QUERY
        )

    def get_local_user_by_name(self, name):
        """Get local user details by name.

        :param name: Name of the local user
        :type name: str
        :return: local user details
        :rtype: list[dict]
        """
        LOG.info("Getting local user details by name: '%s'" % name)
        resp = self.get_local_users()

        for user in resp:
            if user['name'] == name:
                return self.get_local_user_details(user['id'])

    def delete_local_user(self, user_id):
        """Delete a local user.

        :param user_id: The user ID
        :type user_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting local user id: '%s'" % user_id)
        return self.config_client.request(
            constants.DELETE, constants.DELETE_LOCAL_USER_URL.format(
                self.server_ip, user_id),
            payload=None)

    def create_local_user(self, create_params):
        """create a local user.

        :param create_params: The create params
        :type create_params: list<dict>
        :return: user id if success else raise exception
        :rtype: None
        """
        LOG.info("creating local user name: '%s'" % create_params['name'])

        payload = dict()
        if create_params:
            for key, value in create_params.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST, constants.CREATE_LOCAL_USER_URL.format(
                self.server_ip,),
            payload=payload)

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
        LOG.info("Modifying local user properties: '%s'" % local_user_id)

        if modify_parameters:
            if 'password' in modify_parameters.keys() \
                    and 'current_password' in modify_parameters.keys():
                payload = dict()
                payload['password'] = modify_parameters['password']
                payload['current_password'] = \
                    modify_parameters['current_password']
                self.config_client.request(
                    constants.PATCH,
                    constants.MODIFY_LOCAL_USER_URL.format(
                        self.server_ip, local_user_id), payload=payload)
                del modify_parameters['password']
                del modify_parameters['current_password']
                LOG.info(
                    "Modifying passwords: '%s'" % payload)

            for key, value in modify_parameters.items():
                if value is not None:
                    payload = dict()
                    payload[key] = value
                    LOG.info(
                        "Modifying localuser: '%s'" % payload)
                    self.config_client.request(
                        constants.PATCH,
                        constants.MODIFY_LOCAL_USER_URL.format(
                            self.server_ip, local_user_id), payload=payload)
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

        LOG.info("Getting IP's with filter: '%s' and all_pages: '%s'" % (
            filter_dict, all_pages))
        querystring = helpers.prepare_querystring(constants.IP_DETAILS_QUERY,
                                                  filter_dict)
        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,name,network_id,ip_port_id,appliance_id,'
                          'node_id,address,purposes,purposes_l10n'
            }
            querystring = helpers.prepare_querystring(querystring,
                                                      filter_dict)

        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET, constants.GET_IP_POOL_LIST_URL.format(
                self.server_ip), querystring=querystring, all_pages=all_pages)

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
            "Getting clusters with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        if all_pages:
            raise Exception("Pagination is not supported"
                            " for clusters.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME)
            LOG.info("Querystring: '%s'" % querystring)
            return self.config_client.request(
                constants.GET,
                constants.GET_CLUSTER_LIST_URL.format(self.server_ip),
                querystring=querystring, all_pages=False)

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.CLUSTER_DETAILS_QUERY, filter_dict)
        if helpers.is_foot_hill_or_higher():
            details_query_string = {
                'select': 'id,global_id,name,management_address,'
                          'storage_discovery_address,master_appliance_id,'
                          'appliance_count,physical_mtu,'
                          'is_encryption_enabled,system_time,'
                          'compatibility_level,state,state_l10n'
            }
            querystring = helpers.prepare_querystring(
                details_query_string, filter_dict)

        resp = self.config_client.request(
            constants.GET,
            constants.GET_CLUSTER_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=False)

        filterable_keys = ['name', 'id', 'physical_mtu']
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'cluster')

    def get_cluster_details(self, cluster_id):
        """ Get details of a particular cluster.

        :param cluster_id: ID of the cluster
        :type cluster_id: str
        :return: Cluster details
        :rtype: dict
        """

        LOG.info("Getting cluster details by ID: '%s'" % cluster_id)
        querystring = constants.CLUSTER_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,global_id,name,management_address,'
                          'storage_discovery_address,master_appliance_id,'
                          'appliance_count,physical_mtu,is_encryption_enabled,'
                          'compatibility_level,state,state_l10n,system_time'
            }
        return self.config_client.request(
            constants.GET,
            constants.GET_CLUSTER_DETAILS_URL.format(self.server_ip,
                                                     cluster_id),
            querystring=querystring
        )

    def get_cluster_by_name(self, name):
        """Get cluster details by name.

        :param name: Name of the cluster
        :type name: str
        :return: Cluster details
        :rtype: list[dict]
        """
        LOG.info("Getting cluster details by name: '%s'" % name)
        querystring = constants.CLUSTER_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,global_id,name,management_address,'
                          'storage_discovery_address,master_appliance_id,'
                          'appliance_count,physical_mtu,is_encryption_enabled,'
                          'compatibility_level,state,state_l10n,system_time'
            }
        resp = self.config_client.request(
            constants.GET,
            constants.GET_CLUSTER_LIST_URL.format(self.server_ip),
            querystring=querystring)
        filterable_keys = ['name', 'id', 'physical_mtu']
        filter_dict = {'name': 'eq.{0}'.format(name)}
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'cluster')

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
        LOG.info("Modifying cluster properties: '%s'" % cluster_id)
        payload = dict()
        if physical_mtu is not None:
            payload['physical_mtu'] = physical_mtu
        if name is not None:
            payload['name'] = name
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_CLUSTER_URL.format(self.server_ip, cluster_id),
            payload
        )
        return self.get_cluster_details(cluster_id)

    # Cluster operations end

    # CHAP config operations start
    def get_chap_configs(self, filter_dict=None, all_pages=None):
        """ Get all CHAP configurations.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all CHAP
                            configurations or not
        :type all_pages: bool
        :return: List of CHAP configurations
        :rtype: list[dict]
        """
        LOG.info("Getting CHAP configurations with filter: '%s'" % filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported"
                            " for CHAP configuration.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID)
            return self.config_client.request(
                constants.GET,
                constants.GET_CHAP_CONFIG_LIST_URL.format(self.server_ip),
                querystring=querystring, all_pages=False)

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.CHAP_CONFIG_DETAILS_QUERY, filter_dict)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_CHAP_CONFIG_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=False)

        filterable_keys = ['id', 'mode']
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'CHAP config')

    def get_chap_config_details(self, chap_config_id):
        """ Get details of a particular CHAP configuration.

        :param chap_config_id: ID of the CHAP configuration
        :type chap_config_id: str
        :return: CHAP configuration details
        :rtype: dict
        """

        LOG.info("Getting CHAP configuration details by ID: '%s'" %
                 chap_config_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_CHAP_CONFIG_DETAILS_URL.format(self.server_ip,
                                                         chap_config_id),
            querystring=constants.CHAP_CONFIG_DETAILS_QUERY
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
        LOG.info("Modifying CHAP configuration properties: '%s'" %
                 chap_config_id)
        payload = dict()
        if mode is not None:
            payload['mode'] = mode
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_CHAP_CONFIG_URL.format(self.server_ip,
                                                    chap_config_id),
            payload
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
        LOG.info("Getting service configurations with filter: '%s'" %
                 filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported"
                            " for service configuration.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID)
            return self.config_client.request(
                constants.GET,
                constants.GET_SERVICE_CONFIG_LIST_URL.format(self.server_ip),
                querystring=querystring, all_pages=False)

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.SERVICE_CONFIG_DETAILS_QUERY, filter_dict)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_CONFIG_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=False)

        filterable_keys = ['id', 'appliance_id', 'is_ssh_enabled']
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'service config')

    def get_service_config_by_appliance_id(self, appliance_id):
        """Get service configuration for appliance.

        :param appliance_id: ID of the appliance
        :type appliance_id: str
        :return: List of service configurations for the appliance
        :rtype: list[dict]
        """
        LOG.info("Getting service config details for appliance with id:"
                 " '%s'" % appliance_id)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_CONFIG_LIST_URL.format(self.server_ip),
            querystring=constants.SERVICE_CONFIG_DETAILS_QUERY)
        filterable_keys = ['id', 'appliance_id', 'is_ssh_enabled']
        filter_dict = {'appliance_id': 'eq.{0}'.format(appliance_id)}
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'service config')

    def get_service_config_details(self, service_config_id):
        """ Get details of a particular service config.

        :param service_config_id: ID of the service config
        :type service_config_id: str
        :return: service config details
        :rtype: dict
        """

        LOG.info("Getting service config details by ID: '%s'" %
                 service_config_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_CONFIG_DETAILS_URL.format(self.server_ip,
                                                            service_config_id),
            querystring=constants.SERVICE_CONFIG_DETAILS_QUERY
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
        LOG.info("Modifying service config properties: '%s'" %
                 service_config_id)
        payload = dict()
        if is_ssh_enabled is not None:
            payload['is_ssh_enabled'] = is_ssh_enabled
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_SERVICE_CONFIG_URL.format(self.server_ip,
                                                       service_config_id),
            payload
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
        LOG.info("Getting service users with filter: '%s'" % filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported"
                            " for service users.")
        if not filter_dict:
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID)
            return self.config_client.request(
                constants.GET,
                constants.GET_SERVICE_USER_LIST_URL.format(self.server_ip),
                querystring=querystring, all_pages=False)

        # query string if filter dict is passed
        querystring = helpers.prepare_querystring(
            constants.SERVICE_USER_DETAILS_QUERY, filter_dict)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_USER_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=False)

        filterable_keys = ['id', 'is_built_in', 'name', 'is_default_password']
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'service user')

    def get_service_user_details(self, service_user_id):
        """ Get details of a particular service user.

        :param service_user_id: ID of the service user
        :type service_user_id: str
        :return: service user details
        :rtype: dict
        """

        LOG.info("Getting service user details by ID: '%s'" % service_user_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_USER_DETAILS_URL.format(self.server_ip,
                                                          service_user_id),
            querystring=constants.SERVICE_USER_DETAILS_QUERY
        )

    def get_service_user_by_name(self, name):
        """Get service user details by name.

        :param name: Name of the service user
        :type name: str
        :return: service user details
        :rtype: list[dict]
        """
        LOG.info("Getting service user details by name: '%s'" % name)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SERVICE_USER_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.SERVICE_USER_DETAILS_QUERY,
                name=constants.EQUALS + name))
        filterable_keys = ['id', 'is_built_in', 'name', 'is_default_password']
        filter_dict = {'name': 'eq.{0}'.format(name)}
        return helpers.filtered_details(filterable_keys, filter_dict,
                                        resp, 'service user')

    def modify_service_user(self, service_user_id, password):
        """Modify service user properties.

        :param service_user_id: ID of the service user
        :type service_user_id: str
        :param password: The new password for the service user
        :type password: str
        :return: service user details
        :rtype : dict
        """
        LOG.info("Modifying service user properties: '%s'" % service_user_id)
        payload = dict()
        if password is not None:
            payload['password'] = password
        self.config_client.request(
            constants.PATCH,
            constants.MODIFY_SERVICE_USER_URL.format(self.server_ip,
                                                     service_user_id),
            payload
        )
        return self.get_service_user_details(service_user_id)

    # Service user operations end

    # IP ports operations start

    def get_ip_port_details(self, ip_port_id):
        """ Get IP port details.

        :param ip_port_id: IP port ID
        :type ip_port_id: str
        :return: IP port details
        :rtype : dict
        """

        LOG.info("Getting IP port details by ID: '%s'" % ip_port_id)
        return self.config_client.request(
            constants.GET,
            constants.GET_IP_PORT_DETAILS_URL.format(self.server_ip,
                                                     ip_port_id),
            querystring=constants.IP_PORT_DETAILS_QUERY)

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
        LOG.info("Getting vcenters with filter: '%s' and all_pages: '%s'" % (
            filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_VCENTER_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages
        )

    def get_vcenter_details(self, vcenter_id):
        """Get vcenter details.
        :param vcenter_id: ID of the vcenter
        :type vcenter_id: str
        :return: Details of vcenter
        :rtype: dict
        """
        LOG.info("Getting vcenter details by ID: '%s'" % vcenter_id)
        querystring = constants.VCENTER_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,instance_uuid,address,username,'
                          'vendor_provider_status,'
                          'vendor_provider_status_l10n'
            }
        return self.config_client.request(
            constants.GET,
            constants.GET_VCENTER_DETAILS_URL.format(self.server_ip,
                                                     vcenter_id),
            querystring=querystring
        )

    def modify_vcenter(self, vcenter_id, modify_param_dict):
        """Register VASA provider.
        :param vcenter_id: ID of the vcenter
        :type vcenter_id: str
        :param modify_param_dict: Dict containing VASA provider credentials
        :type modify_param_dict: dict
        :return: Details of vcenter
        :rtype: dict
        """
        LOG.info("Registering VASA provider: '%s'" % vcenter_id)
        self.config_client.request(constants.PATCH,
                                   constants.MODIFY_VCENTER_URL.format(
                                       self.server_ip, vcenter_id),
                                   payload=modify_param_dict)
        return self.get_vcenter_details(vcenter_id)
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
            "Getting all appliances with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_NAME_AND_MODEL, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_APPLIANCE_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_appliance_details(self, appliance_id):
        """ Get details of a particular appliance.

        :param appliance_id: ID of the appliance
        :type appliance_id: str
        :return: appliance details
        :rtype: dict
        """

        LOG.info("Getting appliance details by ID: '%s'" % appliance_id)
        querystring = constants.APPLIANCE_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,name,service_tag,express_service_code,model,'
                          'drive_failure_tolerance_level,nodes,'
                          'ip_pool_addresses,veth_ports,maintenance_windows,'
                          'fc_ports,sas_ports,eth_ports,software_installed,'
                          'virtual_volumes,hardware,volumes'
            }
        return self.config_client.request(
            constants.GET,
            constants.GET_APPLIANCE_DETAILS_URL.format(self.server_ip,
                                                       appliance_id),
            querystring=querystring
        )

    def get_appliance_by_name(self, appliance_name):
        """Get appliance details by name.

        :param appliance_name: Name of the appliance
        :type appliance_name: str
        :return: appliance details
        :rtype: list[dict]
        """
        LOG.info("Getting appliance details by name: '%s'" % appliance_name)
        querystring = constants.APPLIANCE_DETAILS_QUERY
        if helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,name,service_tag,express_service_code,model,'
                          'drive_failure_tolerance_level,nodes,'
                          'ip_pool_addresses,veth_ports,maintenance_windows,'
                          'fc_ports,sas_ports,eth_ports,software_installed,'
                          'virtual_volumes,hardware,volumes'
            }

        return self.config_client.request(
            constants.GET,
            constants.GET_APPLIANCE_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                querystring,
                name=constants.EQUALS + appliance_name))
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
            "Getting certificates with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_CERTIFICATE_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)
    
    def get_certificate_details(self, certificate_id):
        """ Get details of a particular certificate.

        :param certificate_id: ID of the certificate
        :type certificate_id: str
        :return: certificate details
        :rtype: dict
        """

        LOG.info("Getting certificate details by ID: '%s'" % certificate_id)
        querystring = constants.CERTIFICATE_DETAILS_QUERY

        return self.config_client.request(
            constants.GET,
            constants.GET_CERTIFICATE_DETAILS_URL.format(self.server_ip,
                                                       certificate_id),
            querystring=querystring
        )

    def exchange_certificate(self, exchange_cert_dict):
        """
        Exchange the certificates between peers for remote system
        :param exchange_cert_dict: Exchange certificate dict includes
        address, port, service, username and password
        :type exchange_cert_dict: dict
        :return: None
        :rtype: NoneType
        """
        LOG.info("Exchanging certificates")
        if 'port' not in exchange_cert_dict.keys():
            exchange_cert_dict['port'] = 443
        self.config_client.request(
            constants.POST,
            constants.EXCHANGE_CERTIFICATE_URL.format(self.server_ip),
            exchange_cert_dict
        )
    def create_certificate(self, create_cert_dict):
        """create a certificate.
        :param create_cert_dict: The create parameters which includes type, service,
        scope,certificate,private_key,passphrase and is_current
        :type create_cert_dict: dict
        :return: certificate_id if success else raise exception
        :rtype: dict
        """
        LOG.info("Creating certificate")
        payload = dict()
        if create_cert_dict:
            for key, value in create_cert_dict.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST, constants.CREATE_CERTIFICATE_URL.format(
                self.server_ip,),
            payload=payload)

    def modify_certificate(self, certificate_id, modify_cert_dict):
        """"Modify certificate properties.

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
            payload=modify_cert_dict
        )

    def reset_certificates(self, reset_cert_dict):
        """Reset certificates.

        :param reset_cert_dict: Contains service parameter
        :type reset_cert_dict: dict
        :return: None
        :rtype : NoneType
        """
        LOG.info("Resetting certificates of the service: '%s'"%(
            reset_cert_dict['service']))
        payload = dict()
        if reset_cert_dict:
            for key, value in reset_cert_dict.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST, constants.RESET_CERTIFICATE_URL.format(
                self.server_ip,),
            payload=payload)

    # Certificate operations end


    # security configuration operations start

    def get_security_configs(self, filter_dict=None, all_pages=False):
        """ Get all security configurations.

        :param filter_dict: (optional) filter dict
        :type filter_dict: dict
        :param all_pages: (optional) indicate whether to return all elements
                          or not
        :type all_pages: bool
        :return: List of all security configs
        :rtype: list[dict]
        """
        LOG.info("Getting security configs with filter: '%s'" % filter_dict)
        if all_pages:
            raise Exception("Pagination is not supported"
                            "for security configs.")

        if not filter_dict:
            querystring = helpers.prepare_querystring(constants.SELECT_ID)
            return self.config_client.request(
                constants.GET, constants.GET_SECURITY_CONFIG_LIST_URL.format(
                    self.server_ip), querystring=querystring, all_pages=False)
        querystring = helpers.prepare_querystring(
            constants.SECURITY_CONFIG_DETAILS_QUERY, filter_dict)
        resp = self.config_client.request(
            constants.GET,
            constants.GET_SECURITY_CONFIG_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=False)

        filterable_key = ['id']
        if helpers.is_foot_hill_or_higher():
            filterable_key = ['id', 'protocol_mode']
        return helpers.filtered_details(filterable_key, filter_dict, resp,
                                        'security config')

    def get_security_config_details(self, security_config_id):
        """ Get details of particular security configuration.

        :param security_config_id: id of security config
        :type security_config_id: str
        :return: security config details
        :rtype: dict
        """
        LOG.info("Getting security config details by ID: '%s'"
                 % security_config_id)

        querystring = constants.SECURITY_CONFIG_DETAILS_QUERY
        if not helpers.is_foot_hill_or_higher():
            querystring = {
                'select': 'id,idle_timeout'
            }
        return self.config_client.request(
            constants.GET,
            constants.GET_SECURITY_CONFIG_DETAILS_URL.format(
                self.server_ip, security_config_id),
            querystring=querystring)

    def modify_security_config(self, security_config_id, protocol_mode):
        """ Modify Security configuration.

        :param security_config_id: id of security config
        :type security_config_id: str
        :param protocol_mode: protocol mode of security config
        :type protocol_mode: str
        :return: None
        :rtype: None
        """
        LOG.info("Modify security config properties: '%s' with params '%s'"
                 % (security_config_id, protocol_mode))

        payload = dict()
        payload['protocol_mode'] = protocol_mode
        return self.config_client.request(
            constants.PATCH,
            constants.MODIFY_SECURITY_CONFIG_URL.format(
                self.server_ip, security_config_id), payload=payload
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
            "Getting email addresses with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_ADDRESS, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_EMAIL_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_destination_email_details(self, email_id):
        """ Get details of particular email notification destination.

        :param email_id: id of email notification destination
        :type email_id: str
        :return: email details
        :rtype: dict
        """
        LOG.info("Getting email details by ID: '%s'"
                 % email_id)

        querystring = constants.EMAIL_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_EMAIL_DETAILS_URL.format(
                self.server_ip, email_id),
            querystring=querystring)

    def get_destination_email_by_address(self, email_address):
        """Get destination email details by address.

        :param email_address: Destination email address.
        :type email_address: str
        :return: Destination email details with corresponding email_address.
        :rtype: list[dict]
        """
        LOG.info("Getting destination email details by address: '%s'" % email_address)
        return self.config_client.request(
            constants.GET,
            constants.GET_EMAIL_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.EMAIL_DETAILS_QUERY,
                email_address=constants.EQUALS + email_address))

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
        LOG.info("Modifying destination email properties: '%s' with params '%s'" % (
            email_id, modify_parameters))

        email_url = constants.MODIFY_EMAIL_URL
        return self.config_client.request(
            constants.PATCH,
            email_url.format(self.server_ip, email_id),
            payload=modify_parameters
        )

    def delete_destination_email(self, email_id):
        """Delete a destination_email.

        :param email_id: ID of the email destination
        :type email_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting email id: '%s'" % email_id)
        return self.config_client.request(
            constants.DELETE, constants.DELETE_EMAIL_URL.format(
                self.server_ip, email_id),
            payload=None)

    def test_destination_email(self, email_id):
        """Send a test mail to the destination.

        :param email_id: ID of the email destination
        :type email_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Testing email id: '%s'" % email_id)
        return self.config_client.request(
            constants.POST, constants.TEST_EMAIL_URL.format(
                self.server_ip, email_id),
            payload=None)

    def create_destination_email(self, create_params):
        """create a destination_email.

        :param create_params: The create params
        :type create_params: list<dict>
        :return: email id if success else raise exception
        :rtype: dict
        """
        LOG.info("creating email notification destination")

        payload = dict()
        if create_params:
            for key, value in create_params.items():
                payload[key] = value

        return self.config_client.request(
            constants.POST, constants.CREATE_EMAIL_URL.format(
                self.server_ip,),
            payload=payload)

    # email operations end

    # smtp operations start

    def get_smtp_configs(self, filter_dict=None, all_pages=None):
        """Get all SMTP configurationss.

        :param filter_dict: (optional) Filter details
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all smtp servers or not
        :type all_pages: bool
        :return: List of SMTP servers
        :rtype: list[dict]
        """
        LOG.info(
            "Getting SMTP configs with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_SMTP_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_smtp_config_details(self, smtp_id):
        """ Get details of an SMTP configuration instance.

        :param smtp_id: Unique identifier of smtp configuration
        :type smtp_id: str
        :return: smtp details
        :rtype: dict
        """
        LOG.info("Getting SMTP config details by ID: '%s'"
                 % smtp_id)

        querystring = constants.SMTP_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_SMTP_DETAILS_URL.format(
                self.server_ip, smtp_id),
            querystring=querystring)

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
        LOG.info("Modifying SMTP configuration properties: '%s' with params '%s'" % (
            smtp_id, modify_parameters))

        smtp_url = constants.MODIFY_SMTP_URL
        return self.config_client.request(
            constants.PATCH,
            smtp_url.format(self.server_ip, smtp_id),
            payload=modify_parameters)

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
        LOG.info("Testing smtp id: '%s'" % smtp_id)
        return self.config_client.request(
            constants.POST, constants.TEST_SMTP_URL.format(
                self.server_ip, smtp_id),
            payload=test_parameters)

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
            "Getting all DNS servers with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_DNS_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_dns_details(self, dns_id):
        """ Get details of a DNS instance.

        :param dns_id: Unique identifier of the DNS setting
        :type dns_id: str
        :return: DNS setting details
        :rtype: dict
        """
        LOG.info("Getting DNS details by ID: '%s'"
                 % dns_id)

        querystring = constants.DNS_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_DNS_DETAILS_URL.format(
                self.server_ip, dns_id),
            querystring=querystring)


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
        LOG.info("Modifying DNS : '%s' with params '%s'" % (
            dns_id, modify_parameters))

        dns_url = constants.MODIFY_DNS_URL
        return self.config_client.request(
            constants.PATCH,
            dns_url.format(self.server_ip, dns_id),
            payload=modify_parameters) 

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
            "Getting all NTP servers with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.config_client.request(
            constants.GET,
            constants.GET_NTP_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_ntp_details(self, ntp_id):
        """ Get details of a NTP instance.

        :param ntp_id: Unique identifier of the NTP setting
        :type ntp_id: str
        :return: NTP setting details
        :rtype: dict
        """
        LOG.info("Getting NTP details by ID: '%s'"
                 % ntp_id)

        querystring = constants.NTP_DETAILS_QUERY
        return self.config_client.request(
            constants.GET,
            constants.GET_NTP_DETAILS_URL.format(
                self.server_ip, ntp_id),
            querystring=querystring)

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
        LOG.info("Modifying NTP : '%s' with params '%s'" % (
            ntp_id, modify_parameters))

        ntp_url = constants.MODIFY_NTP_URL
        return self.config_client.request(
            constants.PATCH,
            ntp_url.format(self.server_ip, ntp_id),
            payload=modify_parameters)
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
            "Getting all remote_support with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        if helpers.is_foot_hill_or_higher():
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID, filter_dict)
            LOG.info("Querystring: '%s'" % querystring)
            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_LIST_URL.format(self.server_ip),
                querystring=querystring, all_pages=all_pages)

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def get_remote_support_details(self, remote_support_id,
                                   return_support_license_text=False):
        """ Get details of a remote support configuration instance.

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :return: remote support configuration details
        :rtype: dict
        """
        LOG.info("Getting remote_support details by ID: '%s'"
                 % remote_support_id)
        if helpers.is_foot_hill_or_higher():
            querystring = constants.REMOTE_SUPPORT_DETAILS_QUERY
            if return_support_license_text is True:
                querystring['select'] = querystring['select']+',support_assist_license_agreement_text'

            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_DETAILS_URL.format(
                    self.server_ip, remote_support_id),
                querystring=querystring)

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def modify_remote_support_details(self, remote_support_id, modify_parameters,
                                      is_async=False):
        """Modify remote support configuration properties.

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :param modify_parameters: Dictionary containing list of parameters of 
                                  remote support configuration to be modified.
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info("Modifying remote_support : '%s' with params '%s'" % (
            remote_support_id, modify_parameters))
        if helpers.is_foot_hill_or_higher():
            remote_support_url = constants.MODIFY_REMOTE_SUPPORT_URL
            if is_async:
                remote_support_url = remote_support_url + "?is_async=true"
            return self.config_client.request(
                constants.PATCH,
                remote_support_url.format(self.server_ip, remote_support_id),
                payload=modify_parameters)

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
        LOG.info("Verifying remote_support : '%s' with params '%s'" % (
            remote_support_id, verify_parameters))
        if helpers.is_foot_hill_or_higher():
            remote_support_url = constants.VERIFY_REMOTE_SUPPORT_URL
            return self.config_client.request(
                constants.POST,
                remote_support_url.format(self.server_ip, remote_support_id),
                payload=verify_parameters)

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def test_remote_support_config(self, remote_support_id):
        """Send a test alert for the remote support configuration.

        :param remote_support_id: Unique identifier of the remote support configuration
        :type remote_support_id: str
        :return: None
        :rtype : None
        """
        LOG.info("Sending a test alert for remote_support : '%s'" % (
            remote_support_id))
        if helpers.is_foot_hill_or_higher():
            remote_support_url = constants.SEND_ALERT_REMOTE_SUPPORT_URL
            return self.config_client.request(
                constants.POST,
                remote_support_url.format(self.server_ip, remote_support_id))

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    # Remote Support operations end

    # Remote Support conatct operations start

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
            "Getting all remote support contact with filter: '%s' and all_pages: '%s'"
            % (filter_dict, all_pages))
        if helpers.is_foot_hill_or_higher():
            querystring = helpers.prepare_querystring(
                constants.SELECT_ID, filter_dict)
            LOG.info("Querystring: '%s'" % querystring)
            array_version = self.provisioning.get_array_version()
            if array_version == '2.0.0.0':
                resp = self.config_client.request(
                    constants.GET,
                    constants.GET_REMOTE_SUPPORT_CONTACT_LIST_URL.format(self.server_ip),
                    querystring=constants.REMOTE_SUPPORT_CONTACT_DETAILS_QUERY, all_pages=False)

                filterable_keys = ['id', 'email', 'first_name', 'last_name', 'phone']
                return helpers.filtered_details(filterable_keys, filter_dict,
                                                resp, 'remote_support_contact')
            else:
                return self.config_client.request(
                    constants.GET,
                    constants.GET_REMOTE_SUPPORT_CONTACT_LIST_URL.format(self.server_ip),
                    querystring=querystring, all_pages=all_pages)

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def get_remote_support_contact_details(self, remote_support_contact_id):
        """ Get details of a remote support contact instance.

        :param remote_support_contact_id: Unique identifier of the remote support contacts
        :type remote_support_contact_id: str
        :return: remote support contacts details
        :rtype: dict
        """
        LOG.info("Getting remote support contact details by ID: '%s'"
                 % remote_support_contact_id)
        if helpers.is_foot_hill_or_higher():
            querystring = constants.REMOTE_SUPPORT_CONTACT_DETAILS_QUERY
            return self.config_client.request(
                constants.GET,
                constants.GET_REMOTE_SUPPORT_CONTACT_DETAILS_URL.format(
                    self.server_ip, remote_support_contact_id),
                querystring=querystring)

        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    def modify_remote_support_contact_details(self, remote_support_contact_id, modify_parameters):
        """Modify remote support contacts properties.

        :param remote_support_contact_id: Unique identifier of the remote support contacts
        :type remote_support_contact_id: str
        :param modify_parameters: Dictionary containing list of parameters of
                                  remote support contact to be modified.
        :type modify_parameters: dict
        :return: None
        :rtype : None
        """
        LOG.info("Modifying remote support contact : '%s' with params '%s'" % (
            remote_support_contact_id, modify_parameters))
        print(remote_support_contact_id)
        if helpers.is_foot_hill_or_higher():
            remote_support_contact_url = constants.MODIFY_REMOTE_SUPPORT_CONTACT_URL
            return self.config_client.request(
                constants.PATCH,
                remote_support_contact_url.format(self.server_ip, remote_support_contact_id),
                payload=modify_parameters)
        raise Exception("Not supported for PowerStore versions less than 2.0.0.0")

    # Remote Support conatct operations end

    @staticmethod
    def _prepare_local_user_payload(**kwargs):
        """Prepare a local user request body using provided arguments.

        :return: Request body
        :rtype: dict
        """
        payload = dict()
        for argname in ('name', 'role_id', 'is_locked', 'current_password',
                        'password'):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload

    @staticmethod
    def _prepare_add_remove_network_payload(**kwargs):
        """Prepare add/remove network request body using provided arguments.

        :return: Request body
        :rtype: dict
        """
        payload = dict()
        for argname in ('add_port_ids', 'remove_port_ids'):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload
