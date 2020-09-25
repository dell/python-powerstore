# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Collection of provisioning related functions for PowerStore"""

from PyPowerStore.client import Client
from PyPowerStore.utils import constants, helpers

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)


class Provisioning:
    """Provisioning related functionality for PowerStore."""
    def __init__(self, server_ip, username, password, verify,
                 application_type, timeout, enable_log=False):
        """ Initializes Provisioning Class

        :param server_ip: The array IP
        :type server_ip: str
        :param username: array username
        :type username: str
        :param password: array password
        :type password: str
        :param verify: Whether the SSL cert will be verified
        :type verify: bool
        :param application_type: Application Type
        :type application_type: str
        :param timeout: How long to wait for the server to send data before
                        giving up
        :type timeout: float
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        """
        global LOG
        self.server_ip = server_ip
        self.client = Client(username, password, verify, application_type,
                             timeout, enable_log=enable_log)
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    def create_volume(self, name, size, description=None,
                      volume_group_id=None, protection_policy_id=None,
                      performance_policy_id=None):
        """Create a volume.

        :param name: The name of the volume
        :param size: The size of the volume
        :param description: (optional) The description given to the volume
        :param volume_group_id: (optional) The volume group ID
        :param protection_policy_id: (optional) The protection policy ID
        :param performance_policy_id: (optional) The performance policy ID
        """
        LOG.info("Creating volume: '%s'" % name)
        payload = self._prepare_create_volume_payload(name, size,
                                                      description,
                                                      volume_group_id,
                                                      protection_policy_id,
                                                      performance_policy_id)
        self.client.request(constants.POST,
                            constants.VOLUME_CREATE_URL.format(
                                self.server_ip), payload)

    def _prepare_create_volume_payload(self, name, size,
                                       description,
                                       volume_group_id,
                                       protection_policy_id,
                                       performance_policy_id):

        create_volume_dict = dict()
        if name is not None:
            create_volume_dict['name'] = name
        if size is not None:
            create_volume_dict['size'] = size
        if description is not None:
            create_volume_dict['description'] = description
        if volume_group_id is not None:
            create_volume_dict['volume_group_id'] = volume_group_id
        if protection_policy_id is not None:
            create_volume_dict['protection_policy_id'] = protection_policy_id
        if performance_policy_id is not None:
            create_volume_dict['performance_policy_id'] = \
                performance_policy_id

        return create_volume_dict

    def delete_volume(self, volume_id):
        """Delete a volume.

        :param volume_id: The Volume ID
        :type volume_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting volume: '%s'" % volume_id)
        return self.client.request(
            constants.DELETE, constants.DELETE_VOLUME_URL.format(
                self.server_ip, volume_id),
            payload=None)

    def modify_volume(self, volume_id, name=None, description=None, size=None,
                      protection_policy_id=None,
                      performance_policy_id=None):
        """Modify a volume.

        :param volume_id: The volume ID
        :type volume_id: str
        :param name: The name of the volume
        :type name: str
        :param description: The description of the volume
        :type description: str
        :param size: The size of the volume
        :type size: str
        :param protection_policy_id: The protection policy ID
        :type protection_policy_id: str
        :param performance_policy_id: The performance policy ID
        :type performance_policy_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying volume: '%s'" % volume_id)
        payload = self.\
            _prepare_modify_volume_payload(name,
                                           description,
                                           size,
                                           protection_policy_id,
                                           performance_policy_id)
        return self.client.request(
            constants.PATCH, constants.MODIFY_VOLUME_URL.format(
                self.server_ip, volume_id),
            payload)

    def _prepare_modify_volume_payload(self, name=None, description=None,
                                       size=None,
                                       protection_policy_id=None,
                                       performance_policy_id=None):

        modify_volume_dict = dict()
        if name is not None:
            modify_volume_dict['name'] = name
        if description is not None:
            modify_volume_dict['description'] = description
        if size is not None:
            modify_volume_dict['size'] = size
        if protection_policy_id is not None:
            modify_volume_dict['protection_policy_id'] = protection_policy_id
        if performance_policy_id is not None:
            modify_volume_dict['performance_policy_id'] = \
                performance_policy_id

        return modify_volume_dict

    def add_protection_policy_for_volume(self, volume_id,
                                         protection_policy_id):
        """Add protection policy for volume.

        :param volume_id: The volume ID
        :type volume_id: str
        :param protection_policy_id: The protection policy ID
        :type protection_policy_id: str
        :return: None if success else raise exception
        :rtype: None
        """

        LOG.info("Adding protection policy: '%s' for volume: '%s'"
                 % (protection_policy_id, volume_id))
        payload = self.\
            _prepare_modify_volume_payload(
                protection_policy_id=protection_policy_id)
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_VOLUME_URL.format(
                                       self.server_ip, volume_id),
                                   payload)

    def remove_protection_policy_for_volume(self, volume_id):
        """Remove protection policy for volume.

        :param volume_id: The volume ID
        :type volume_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Removing protection policy for volume: '%s'" % volume_id)
        payload = {
            'protection_policy_id': ''
        }
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_VOLUME_URL.format(
                                       self.server_ip, volume_id),
                                   payload)

    def map_volume_to_host(self, volume_id, host_id=None,
                           logical_unit_number=None):
        """Map a volume to a Host.

        :param volume_id: The volume ID
        :type volume_id: str
        :param host_id: (optional) The host ID
        :type host_id: str
        :param logical_unit_number: (optional) The logical unit number
        :type logical_unit_number: str
        """
        LOG.info("Mapping volume: '%s' to host" % volume_id)
        payload = self._prepare_map_vol_to_host_payload(host_id,
                                                        logical_unit_number)
        self.client.request(constants.POST,
                            constants.MAP_VOLUME_TO_HOST_URL.format(
                                self.server_ip, volume_id), payload)

    def _prepare_map_vol_to_host_payload(self, host_id, logical_unit_number):

        map_volume_to_host_dict = dict()
        if host_id is not None:
            map_volume_to_host_dict['host_id'] = host_id
        if logical_unit_number is not None:
            map_volume_to_host_dict['logical_unit_number'] = \
                logical_unit_number

        return map_volume_to_host_dict

    def map_volume_to_host_group(self, volume_id, host_group_id=None,
                                 logical_unit_number=None):
        """Map a volume to a Host.

        :param volume_id: The volume ID
        :type volume_id: str
        :param host_group_id: (optional) The host group ID
        :type host_group_id: str
        :param logical_unit_number: (optional) The logical unit number
        :type logical_unit_number: str
        """
        LOG.info("Mapping volume: '%s' to host group" % volume_id)
        payload = self._prepare_map_vol_to_host_grp_payload(
            host_group_id, logical_unit_number)
        self.client.request(constants.POST,
                            constants.MAP_VOLUME_TO_HOST_URL.format(
                                self.server_ip, volume_id), payload)

    def _prepare_map_vol_to_host_grp_payload(self, host_grp_id,
                                             logical_unit_number):

        map_volume_to_host_dict = dict()
        if host_grp_id is not None:
            map_volume_to_host_dict['host_group_id'] = host_grp_id
        if logical_unit_number is not None:
            map_volume_to_host_dict['logical_unit_number'] = \
                logical_unit_number

        return map_volume_to_host_dict

    def unmap_volume_from_host(self, volume_id, host_id):
        """Unmap a Volume from a Host.

        :param volume_id: The volume ID
        :type volume_id: str
        :param host_id: The host ID
        :type host_id: str
        """
        LOG.info("Unmapping volume: '%s' from host: '%s'"
                 % (volume_id, host_id))
        payload = self._prepare_unmap_vol_from_host_payload(host_id)
        self.client.request(constants.POST,
                            constants.UNMAP_VOLUME_FROM_HOST_URL.format(
                                self.server_ip, volume_id), payload)

    def _prepare_unmap_vol_from_host_payload(self, host_id):

        unmap_vol_from_host_dict = dict()
        if host_id is not None:
            unmap_vol_from_host_dict['host_id'] = host_id

        return unmap_vol_from_host_dict

    def unmap_volume_from_host_group(self, volume_id, host_group_id):
        """Unmap a Volume from a Host.

        :param volume_id: The volume ID
        :type volume_id: str
        :param host_group_id: The host group ID
        :type host_group_id: str
        """
        LOG.info("Unmapping volume: '%s' from host group: '%s'"
                 % (volume_id, host_group_id))
        payload = self.\
            _prepare_unmap_vol_from_host_grp_payload(host_group_id)
        self.client.request(constants.POST,
                            constants.UNMAP_VOLUME_FROM_HOST_URL.format(
                                self.server_ip, volume_id), payload)

    def _prepare_unmap_vol_from_host_grp_payload(self, host_group_id):

        unmap_vol_from_host_dict = dict()
        if host_group_id is not None:
            unmap_vol_from_host_dict['host_group_id'] = host_group_id

        return unmap_vol_from_host_dict

    def get_volumes(self, filter_dict=None, all_pages=False):
        """Get a list of volumes.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Volume details
        :rtype: list of dict
        """
        LOG.info("Getting volumes with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME,
            filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_VOLUME_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_volume_details(self, volume_id):
        """Get details of a volume.

        :param volume_id: The volume ID
        :type volume_id: str
        :return: Volume details
        :rtype: dict
        """
        LOG.info("Getting volume details by ID: '%s'" % volume_id)
        resp = self.client.request(constants.GET,
                                   constants.GET_VOLUME_DETAILS_URL.format
                                   (self.server_ip, volume_id), payload=None,
                                   querystring=constants.SELECT_ALL_VOLUME)

        hlu_details = self.get_host_volume_mapping(volume_id=volume_id)

        resp['hlu_details'] = hlu_details

        return resp

    def get_volume_by_name(self, volume_name):
        """Get details of a volume by name.

        :param volume_name: The volume name
        :type volume_name: str
        :return: Volume details
        :rtype: dict
        """
        LOG.info("Getting volume details by name: '%s'" % volume_name)
        resp = self.client.request(
            constants.GET,
            constants.GET_VOLUME_BY_NAME_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_VOLUME,
                name=constants.EQUALS + volume_name
            )
        )

        if resp:
            LOG.info("Getting host volume mapping from vol ID: '%s'"
                     % resp[0]['id'])
            hlu_details = self.get_host_volume_mapping(volume_id=resp[0]['id'])
            resp[0]['hlu_details'] = hlu_details

        return resp

    def get_hosts(self, filter_dict=None, all_pages=False):
        """Get a list of all the registered hosts.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Hosts
        :rtype: list of dict
        """
        LOG.info("Getting hosts with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(constants.SELECT_ID_AND_NAME,
                                                  filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_HOST_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def create_host(self, name, os_type, initiators,
                    description=None):
        """Register a host on the array.

        :param name: The name of the host
        :type name: str
        :param os_type: The OS type of the host
        :type name: str
        :param initiators: Host initiators
        :type name: list of dict
        :param description: (optional) The description for the host
        :type name: str
        :return: Host ID if success else raise exception
        :rtype: dict
        """
        LOG.info("Creating host with name: '%s' os_type: '%s' initiators: '%s'"
                 % (name, os_type, initiators))
        payload = self._prepare_create_host_payload(name, description,
                                                    os_type,
                                                    initiators)
        return self.client.request(constants.POST,
                                   constants.CREATE_HOST_URL.format(
                                       self.server_ip), payload)

    def _prepare_create_host_payload(self, name, description,
                                     os_type, initiators):
        create_host_dict = dict()
        if name is not None:
            create_host_dict['name'] = name
        if description is not None:
            create_host_dict['description'] = description
        if os_type is not None:
            create_host_dict['os_type'] = os_type
        if initiators is not None:
            create_host_dict['initiators'] = initiators

        return create_host_dict

    def get_host_details(self, host_id):
        """Get details of a particular host.

        :param host_id: The host ID
        :type host_id: str
        :return: Host details
        :rtype: dict
        """
        LOG.info("Getting host details by ID: '%s'" % host_id)
        return self.client.request(constants.GET,
                                   constants.GET_HOST_DETAILS_URL.format(
                                       self.server_ip, host_id), payload=None,
                                   querystring=constants.SELECT_ALL_HOST)

    def modify_host(self, host_id, name=None, description=None,
                    remove_initiators=None, add_initiators=None,
                    modify_initiators=None):
        """Modify a given host - Only one of add, remove
           or update in the same request.

        :param host_id: The host ID
        :type host_id: str
        :param name: (optional) The host name
        :type name: str
        :param description: (optional) The description for the host
        :type description: str
        :param remove_initiators: (optional) Initiators to be removed
        :type remove_initiators: list
        :param add_initiators: (optional) Initiators to be added
        :type add_initiators: list
        :param modify_initiators: (optional) Initiators to be modified
        :type modify_initiators: list
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying host: '%s'" % host_id)
        payload = self._prepare_modify_host_payload(name,
                                                    description,
                                                    remove_initiators,
                                                    add_initiators,
                                                    modify_initiators)
        return self.client.request(
            constants.PATCH, constants.MODIFY_HOST_URL.format(
                self.server_ip, host_id),
            payload)

    def _prepare_modify_host_payload(self, name=None, description=None,
                                     remove_initiators=None,
                                     add_initiators=None,
                                     modify_initiators=None
                                     ):

        modify_host_dict = dict()
        if name is not None:
            modify_host_dict['name'] = name
        if description is not None:
            modify_host_dict['description'] = description
        if remove_initiators is not None:
            modify_host_dict['remove_initiators'] = remove_initiators
        elif add_initiators is not None:
            modify_host_dict['add_initiators'] = add_initiators
        elif modify_initiators is not None:
            modify_host_dict['modify_initiators'] = modify_initiators

        return modify_host_dict

    def add_initiators_to_host(self, host_id, add_initiators=None
                               ):
        """Add initiators to host.

        :param host_id: The host ID.
        :type host_id: str
        :param add_initiators: (optional) Initiators to be added.
        :type add_initiators: list
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Adding initiators to host: '%s'" % host_id)
        payload = self._prepare_modify_host_payload(
            add_initiators=add_initiators)
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_URL.format(
                                       self.server_ip, host_id), payload)

    def remove_initiators_from_host(self, host_id, remove_initiators=None):
        """Remove initiators from Host.

        :param host_id: The host ID
        :type host_id: str
        :param remove_initiators: (optional) Initiators to be removed
        :type remove_initiators: list
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Removing initiators to host: '%s'" % host_id)
        payload = self._prepare_modify_host_payload(
            remove_initiators=remove_initiators)
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_URL.format(
                                       self.server_ip, host_id), payload)

    def delete_host(self, host_id, force=None):
        """Delete a host.

        :param host_id: The host ID.
        :type host_id: str
        :param force: (optional) The force_internal flag.
        :type force: bool
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting host: '%s'" % host_id)
        if force:
            payload = {"force_internal": force}
        else:
            payload = None
        return self.client.request(
            constants.DELETE, constants.DELETE_HOST_URL.format(
                self.server_ip, host_id),
            payload)

    def get_host_by_name(self, host_name):
        """Get details of a Host with its name.

        :param host_name: The Host name.
        :type host_name: str
        :return: Host details
        :rtype: dict
        """
        LOG.info("Getting host details by name: '%s'" % host_name)
        return self.client.request(
            constants.GET,
            constants.GET_HOST_BY_NAME_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_HOST, name=constants.EQUALS + host_name
            )
        )

    def get_host_group_list(self, filter_dict=None, all_pages=False):
        """Get a list of all host groups.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Hosts
        :rtype: list of dict
        """
        LOG.info("Getting hostgroup with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME,
            filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_HOST_GROUP_LIST_URL.format(
                                       self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def create_host_group(self, name, host_ids, description=None):
        """Create a Host Group.

        :param name: The name of the host group
        :type name: str
        :param host_ids: Host IDs
        :type host_ids: list
        :param description: (optional) The description for the host group
        :type description: str
        :return: Host group ID if success else raise exception
        :rtype: dict
        """
        LOG.info("Creating hostgroup: '%s' with host_ids: '%s'"
                 % (name, host_ids))
        payload = self._prepare_create_host_group_payload(
            name, host_ids, description)
        return self.client.request(constants.POST,
                                   constants.CREATE_HOST_GROUP_URL.format(
                                       self.server_ip), payload)

    def _prepare_create_host_group_payload(self, name, host_ids, description):
        create_host_group_dict = dict()
        if name is not None:
            create_host_group_dict['name'] = name
        if host_ids is not None:
            create_host_group_dict['host_ids'] = host_ids
        if description is not None:
            create_host_group_dict['description'] = description

        return create_host_group_dict

    def get_host_group_details(self, host_group_id):
        """Get details of a particular host group.

        :param host_group_id: The Host Group ID
        :type host_group_id: str
        :return: Host group details
        :rtype: dict
        """
        LOG.info("Getting hostgroup details by ID: '%s'" % host_group_id)
        return self.client.request(constants.GET,
                                   constants.GET_HOST_GROUP_DETAILS_URL.format(
                                       self.server_ip, host_group_id),
                                   payload=None,
                                   querystring=constants.SELECT_ALL_HOST_GROUP)

    def get_host_group_by_name(self, host_group_name):
        """Get details of a Host Group with its name.

        :param host_group_name: The Host Group name
        :type host_group_name: str
        :return: Host group details
        :rtype: dict
        """
        LOG.info("Getting hostgroup details by name: '%s'" % host_group_name)
        return self.client.request(
            constants.GET,
            constants.GET_HOST_GROUP_BY_NAME_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_HOST_GROUP,
                name=constants.EQUALS + host_group_name
            )
        )

    def get_hosts_from_host_group(self, host_group_name):
        """Get list of hosts which belong to Host Group.

        :param host_group_name: The Host Group name
        :type host_group_name: str
        :return: Hosts which are part of Host Group
        :rtype: list
        """
        LOG.info("Getting hosts from host_group: '%s'" % host_group_name)
        return self.client.request(
            constants.GET,
            constants.GET_HOSTS_BY_HOST_GROUP.format(self.server_ip,
                                                     host_group_name),
            payload=None, querystring=helpers.prepare_querystring(
                name=constants.EQUALS + host_group_name,
                select='hosts(name,id)'
            )
        )

    def modify_host_group(self, host_group_id, name=None,
                          remove_host_ids=None,
                          add_host_ids=None, description=None):
        """Modify a Host group.

        :param host_group_id: The ID of the host group to be modified
        :type host_group_id: str
        :param name: (optional) The modified name of the host group
        :type name: str
        :param remove_host_ids: (optional) The hosts to be removed from
                                host group
        :type remove_host_ids: list
        :param add_host_ids: (optional) The hosts to be added to the host group
        :type add_host_ids: list
        :param description: (optional) The modified description for the
                            host group
        :type description: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying hostgroup: '%s'" % host_group_id)
        payload = self._prepare_modify_host_group_payload(
            name, remove_host_ids, add_host_ids, description)
        return self.client.request(
            constants.PATCH, constants.MODIFY_HOST_GROUP_URL.format(
                self.server_ip, host_group_id),
            payload)

    def _prepare_modify_host_group_payload(self, name=None,
                                           remove_host_ids=None,
                                           add_host_ids=None,
                                           description=None):

        modify_host_group_dict = dict()
        if name is not None:
            modify_host_group_dict['name'] = name
        if description is not None:
            modify_host_group_dict['description'] = description

        if remove_host_ids is not None:
            modify_host_group_dict['remove_host_ids'] = remove_host_ids
        elif add_host_ids is not None:
            modify_host_group_dict['add_host_ids'] = add_host_ids

        return modify_host_group_dict

    def add_hosts_to_host_group(self, host_group_id, add_host_ids=None):
        """Add Hosts to Host Group.

        :param host_group_id: The ID of the host group to be modified.
        :type host_group_id: str
        :param add_host_ids: (optional) The hosts to be added to the host group
        :type add_host_ids: list
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Adding hosts to host_group: '%s'" % host_group_id)
        payload = self._prepare_modify_host_group_payload(
            add_host_ids=add_host_ids)
        return self.client.request(
            constants.PATCH, constants.MODIFY_HOST_GROUP_URL.format(
                self.server_ip, host_group_id),
            payload)

    def remove_hosts_from_host_group(self, host_group_id,
                                     remove_host_ids=None):
        """Remove Hosts from Host Group.

        :param host_group_id: The ID of the host group to be modified
        :type host_group_id: str
        :param remove_host_ids: (optional) Hosts to be removed from host group
        :type remove_host_ids: list
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Removing hosts from host_group: '%s'" % host_group_id)
        payload = self._prepare_modify_host_group_payload(
            remove_host_ids=remove_host_ids)
        return self.client.request(
            constants.PATCH, constants.MODIFY_HOST_GROUP_URL.format(
                self.server_ip, host_group_id),
            payload)

    def delete_host_group(self, host_group_id):
        """Delete a host group.

        :param host_group_id: The ID of the host group
        :type host_group_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting hostgroup: '%s'" % host_group_id)
        return self.client.request(
            constants.DELETE, constants.DELETE_HOST_GROUP_URL.format(
                self.server_ip, host_group_id),
            payload=None)

    def get_volumes_from_volume_group(self, vol_group_name):
        """Get a list of volumes which belong to Volume Group.

        :param vol_group_name: The Volume group name
        :type vol_group_name: str
        :return: Volumes which are part of Volume Group
        :rtype: list
        """
        LOG.info("Getting volumes from volumegroup: %s" % vol_group_name)
        return self.client.request(
            constants.GET,
            constants.GET_VOLUMES_FROM_VOLUME_GROUP.format(self.server_ip,
                                                           vol_group_name),
            payload=None, querystring=helpers.prepare_querystring(
                name=constants.EQUALS + vol_group_name, select='volumes(name)'
            )
        )

    def get_volume_group_list(self, filter_dict=None, all_pages=False):
        """Get a list of all the volume groups.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Volume Groups
        :rtype: list of dict
        """
        LOG.info("Getting volumegroups with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_VOLUME_GROUP_LIST_URL.format(
                                       self.server_ip),
                                   payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def create_volume_group(self, name, description=None,
                            volume_ids=None,
                            is_write_order_consistent=None,
                            protection_policy_id=None):
        """Create a volume group.

        :param name: The name of the volume group.
        :type name: str
        :param description: (optional) The description of the VG.
        :type description: str
        :param volume_ids: (optional) The volume IDs to be added to the VG
        :type volume_ids: list
        :param is_write_order_consistent: (optional) Indicate whether snapshot
                                          sets of the volume group will be
                                          write-order consistent.
        :type is_write_order_consistent: vool
        :param protection_policy_id: (optional) Unique identifier of a
                                     protection policy to assign
                                     to the volume group.
        :type protection_policy_id: str
        :return: Volume ID if success else raise exception
        :rtype: dict
        """
        LOG.info("Creating volumegroup: '%s'" % name)
        payload = self._prepare_create_vg_payload(name, description,
                                                  volume_ids,
                                                  is_write_order_consistent,
                                                  protection_policy_id)
        return self.client.request(constants.POST,
                                   constants.CREATE_VOLUME_GROUP_URL.format(
                                       self.server_ip), payload=payload)

    def _prepare_create_vg_payload(self, name, description, volume_ids,
                                   is_write_order_consistent,
                                   protection_policy_id):

        create_volume_group_dict = dict()
        if name is not None:
            create_volume_group_dict['name'] = name
        if description is not None:
            create_volume_group_dict['description'] = description
        if volume_ids is not None:
            create_volume_group_dict['volume_ids'] = volume_ids
        if is_write_order_consistent is not None:
            create_volume_group_dict['is_write_order_consistent'] = \
                is_write_order_consistent
        if protection_policy_id is not None:
            create_volume_group_dict['protection_policy_id'] = \
                protection_policy_id

        return create_volume_group_dict

    def get_volume_group_details(self, volume_group_id):
        """Get details of a volume group.

        :param volume_group_id: The volume group ID
        :type volume_group_id: str
        :return: Details of the volume group
        :rtype: dict
        """
        LOG.info("Getting volumegroup details by ID: '%s'" % volume_group_id)
        return self.client.request(constants.GET,
                                   constants.GET_VOLUME_GROUP_DETAILS_URL
                                   .format(
                                       self.server_ip, volume_group_id),
                                   payload=None,
                                   querystring=helpers.prepare_querystring
                                   (constants.SELECT_ALL_VOL_GROUP))

    def get_volume_group_by_name(self, volume_group_name):
        """Get details of a volume group by name.

        :param volume_group_name: The name of the volume group
        :type volume_group_name: str
        :return: Details of the volume group
        :rtype: dict
        """
        LOG.info("Getting volumegroup details by name: '%s'"
                 % volume_group_name)
        return self.client.request(
            constants.GET,
            constants.GET_VOLUME_GROUP_BY_NAME_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_VOL_GROUP, name=constants.EQUALS +
                volume_group_name
            )
        )

    def modify_volume_group(self, volume_group_id,
                            name=None, description=None,
                            is_write_order_consistent=None,
                            protection_policy_id=None):
        """Modify a volume group.

        :param volume_group_id: The id of the volume group
        :type volume_group_id: str
        :param name: (optional) The name of the volume group
        :type name: str
        :param description: (optional) The description of the VG
        :type description: str
        :param is_write_order_consistent: (optional) Indicate whether snapshot
                                          sets of the volume group will be
                                          write-order consistent.
        :type is_write_order_consistent: bool
        :param protection_policy_id: (optional) Unique identifier of the
                                     protection policy to assign to a primary
                                     or clone volume group. If an empty string
                                     is specified, protection policy will be
                                     removed from the volume group.
        :type protection_policy_id: str
        """
        LOG.info("Modifying volumegroup: '%s'" % volume_group_id)
        payload = self._prepare_modify_vg_payload(name,
                                                  description,
                                                  is_write_order_consistent,
                                                  protection_policy_id)
        self.client.request(
            constants.PATCH, constants.MODIFY_VOLUME_GROUP_URL.format(
                self.server_ip, volume_group_id),
            payload)

    def _prepare_modify_vg_payload(self, name, description,
                                   is_write_order_consistent,
                                   protection_policy_id):
        modify_vg_dict = dict()
        if name is not None:
            modify_vg_dict['name'] = name
        if description is not None:
            modify_vg_dict['description'] = description
        if is_write_order_consistent is not None:
            modify_vg_dict['is_write_order_consistent'] = \
                is_write_order_consistent
        if protection_policy_id is not None:
            modify_vg_dict['protection_policy_id'] = protection_policy_id

        return modify_vg_dict

    def delete_volume_group(self, volume_group_id):
        """Delete a volume group.

        :param: volume_group_id: The volume group ID
        :type: volume_group_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting volumegroup: '%s'" % volume_group_id)
        return self.client.request(constants.DELETE,
                                   constants.DELETE_VOLUME_GROUP_URL
                                   .format(
                                       self.server_ip, volume_group_id),
                                   payload=None)

    def add_members_to_volume_group(self, volume_group_id, volume_ids,
                                    force_internal=False):
        """Add members to volume group.

        :param volume_ids: The volume IDs to be added
        :type volume_ids: list
        :param force_internal: (optional) The force internal flag
        :type force_internal: bool
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Adding volumes: '%s' to volumegroup: '%s'"
                 % (volume_ids, volume_group_id))
        payload = self._prepare_add_members_to_volume_group_payload(
            volume_ids,
            force_internal)
        return self.client.request(constants.POST,
                                   constants.ADD_MEMBERS_TO_VOLUME_GROUP_URL
                                   .format(
                                       self.server_ip, volume_group_id),
                                   payload=payload)

    def _prepare_add_members_to_volume_group_payload(self, volume_ids,
                                                     force_internal):

        add_members_to_vg_dict = dict()
        if volume_ids is not None:
            add_members_to_vg_dict['volume_ids'] = volume_ids
        if force_internal is not None:
            add_members_to_vg_dict['force_internal'] = force_internal

        return add_members_to_vg_dict

    def remove_members_from_volume_group(self, volume_group_id, volume_ids,
                                         force_internal=False):
        """Remove members from volume group.

        :param volume_ids: The list of volume IDs to be removed
        :type volume_ids: str
        :param force_internal: (optional) The force internal flag
        :type force_internal: bool
        :return: None if success else raise exception
        :rtype: None
        :rtype None or dict
        """
        LOG.info("Removing volumes: '%s' from volumegroup: '%s'"
                 % (volume_ids, volume_group_id))
        payload = self._prepare_remove_members_from_volume_group_payload(
            volume_ids, force_internal)
        return self.client.request(constants.POST,
                                   constants.
                                   REMOVE_MEMBERS_FROM_VOLUME_GROUP_URL
                                   .format(
                                       self.server_ip, volume_group_id),
                                   payload=payload)

    def _prepare_remove_members_from_volume_group_payload(self, volume_ids,
                                                          force_internal):
        remove_members_from_vg_dict = dict()
        if volume_ids is not None:
            remove_members_from_vg_dict['volume_ids'] = volume_ids
        if force_internal is not None:
            remove_members_from_vg_dict['force_internal'] = force_internal

        return remove_members_from_vg_dict

    def get_nodes(self, filter_dict=None, all_pages=False):
        """Returns a list of nodes.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Nodes
        :rtype: list of dict
        """
        LOG.info("Getting nodes with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_NODE.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_cluster_list(self):
        """Returns a list of clusters.

        :return: Clusters
        :rtype: list of dict
        """
        LOG.info("Getting clusters")
        return self.client.request(constants.GET,
                                   constants.GET_CLUSTER.format
                                   (self.server_ip), payload=None,
                                   querystring=constants.
                                   SELECT_ID_AND_NAME)

    def get_host_volume_mapping(self, volume_id):
        """Get Host volume mapping details.

        :param volume_id: The Volume ID
        :type volume_id: str
        :return: Host volume mapping details
        :rtype: dict
        """
        LOG.info("Getting host mapping with vol: '%s'" % volume_id)
        return self.client.request(
            constants.GET,
            constants.HOST_VOLUME_MAPPING_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_HOST_VOLUME_MAPPING,
                volume_id=constants.EQUALS +
                volume_id
            )
        )

    # NAS Server methods
    def get_nas_servers(self, filter_dict=None, all_pages=False):
        """Get a list of nas servers.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: NAS servers
        :rtype: list of dict
        """
        LOG.info("Getting nasservers with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: %s" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_NAS_SERVER_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_nas_server_details(self, nas_server_id):
        """Details of a Nas Server.

        :param nas_server_id: The NAS Server ID
        :type nas_server_id: str
        :return: NAS server details
        :rtype: dict
        """
        LOG.info("Getting nasserver details by ID: '%s'" % nas_server_id)
        return self.client.request(
            constants.GET,
            constants.GET_NAS_SERVER_DETAILS_URL.format(self.server_ip,
                                                        nas_server_id),
            payload=None,
            querystring=constants.SELECT_ALL_NAS_SERVER)

    def get_nas_server_by_name(self, nas_server_name):
        """Get details of a NAS Server by name.

        :param nas_server_name: The name of the NAS Server
        :type nas_server_name: str
        :return: NAS server details
        :rtype: dict
        """
        LOG.info("Getting nasserver details by name: '%s'" % nas_server_name)
        return self.client.request(
            constants.GET,
            constants.GET_NAS_SERVER_DETAILS_BY_NAME_URL.format(
                self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_NAS_SERVER,
                name=constants.EQUALS + nas_server_name
            )
        )

    def modify_nasserver(self, nasserver_id, modify_parameters):
        """Modify NAS Server attributes.

        :param nasserver_id: The ID of the NAS Server
        :type nasserver_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying nasserver: '%s'" % nasserver_id)
        if modify_parameters:
            payload = dict()
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.client.request(
                    constants.PATCH,
                    constants.MODIFY_NAS_SERVER_URL.format(
                        self.server_ip, nasserver_id),
                    payload=payload)

        raise ValueError("Nothing to modify")

    # NAS Server methods end

    # File System Methods
    def get_file_systems(self, filter_dict=None, all_pages=False):
        """Get a list of file systems.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool

        :returns: File systems
        :rtype: list of dict
        """
        LOG.info("Getting filesystems with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_FILE_SYSTEM_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_filesystem_details(self, filesystem_id):
        """Details of a Filesystem.

        :param filesystem_id: The File System ID
        :type filesystem_id: str
        :returns: File system details
        :rtype: dict
        """
        LOG.info("Getting filesystem details by ID: '%s'" % filesystem_id)
        return self.client.request(
            constants.GET,
            constants.GET_FILESYSTEM_DETAILS_URL.format(self.server_ip,
                                                        filesystem_id),
            payload=None,
            querystring=constants.SELECT_ALL_FILESYSTEM)

    def get_filesystem_by_name(self, filesystem_name, nas_server_id):
        """Get details of a filesystem by name.

        :param filesystem_name: The name of the File System
        :type filesystem_name: str
        :returns: File system details
        :rtype: dict
        """
        LOG.info("Getting filesystem details by name: '%s' and NAS Server: "
                 "'%s'" % (filesystem_name, nas_server_id))
        return self.client.request(
            constants.GET,
            constants.GET_FILESYSTEM_DETAILS_BY_NAME_URL.format(
                self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_FILESYSTEM,
                nas_server_id=constants.EQUALS + nas_server_id,
                name=constants.EQUALS + filesystem_name
            )
        )

    def create_filesystem(self, name, nas_server_id, size_total,
                          advance_parameters):
        """Create a filesystem.

        :param name: The name of the File System
        :type name: str
        :param nas_server_id: The ID of the NAS Server
        :type name: str
        :param size_total: Total size of the file system in bytes
        :type name: str
        :param advance_parameters: Advance attributes
        :type advance_parameters: str
        :return: Filesystem ID on success else raise exception
        :rtype: dict
        """
        LOG.info("Creating filesystem: '%s'" % name)
        payload = dict()
        payload['name'] = name
        payload['nas_server_id'] = nas_server_id
        payload['size_total'] = size_total

        if advance_parameters:
            for key, value in advance_parameters.items():
                payload[key] = value
        return self.client.request(constants.POST,
                                   constants.CREATE_FILESYSTEM_URL.format(
                                       self.server_ip), payload=payload)

    def delete_filesystem(self, filesystem_id):
        """Delete a File System.

        :param filesystem_id: The FileSystem ID
        :type filesystem_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting filesystem: '%s'" % filesystem_id)
        return self.client.request(constants.DELETE,
                                   constants.DELETE_FILESYSTEM_URL.format(
                                       self.server_ip, filesystem_id),
                                   payload=None)

    def get_snapshots_filesystem(self, filesystem_id):
        """Get Snapshots of a Filesystem.

        :param filesystem_id: The File System ID
        :type filesystem_id: str
        :returns: Snapshots of a FileSystem
        :rtype: list
        """
        LOG.info("Getting snapshots of filesystem: '%s'" % filesystem_id)
        return self.client.request(
            constants.GET,
            constants.GET_SNAPSHOTS_FILESYSTEM_URL.format(
                self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME,
                parent_id=constants.EQUALS + filesystem_id
            )
        )

    def modify_filesystem(self, filesystem_id, modify_parameters):
        """Modify FileSystem attributes.
        :param filesystem_id: The ID of the FileSystem
        :type filesystem_id: str
        :param modify_parameters: Attributes to be modified
        :type modify_parameters: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying filesystem: '%s'" % filesystem_id)
        if modify_parameters:
            payload = dict()
            for key, value in modify_parameters.items():
                if value is not None:
                    payload[key] = value

            if payload:
                return self.client.request(
                    constants.PATCH,
                    constants.MODIFY_FILESYSTEM_URL.format(
                        self.server_ip, filesystem_id),
                    payload=payload)

        raise ValueError("Nothing to modify")

    # File System methods end

    # NFS Export Methods
    def get_nfs_exports(self, filter_dict=None, all_pages=False):
        """Get a list of nfs exports.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: NFS exports
        :rtype: list of dict
        """
        LOG.info("Getting nfsexports with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: %s" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_NFS_EXPORT_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_nfs_export_details(self, nfs_export_id):
        """Get details of a particular NFS Export.

        :param nfs_export_id: The ID of the NFS Export
        :type nfs_export_id: str
        :returns: NFS Export details
        :rtype: dict
        """
        LOG.info("Getting nfsexport details by ID: '%s'" % nfs_export_id)
        return self.client.request(constants.GET,
                                   constants.GET_NFS_EXPORT_DETAILS_URL.
                                   format(self.server_ip, nfs_export_id),
                                   querystring=constants.SELECT_ALL_NFS_EXPORT
                                   )

    def get_nfs_export_details_by_name(self, nfs_export_name):
        """Get details of a NFS Export by name.

        :param nfs_export_name: The name of the NFS Export
        :type nfs_export_name: str
        :returns: NFS Export details
        :rtype: list
        """
        LOG.info("Getting nfsexport details by name: '%s'" % nfs_export_name)
        return self.client.request(
            constants.GET,
            constants.GET_NFS_EXPORT_DETAILS_BY_NAME_URL.format(
                self.server_ip), querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_NFS_EXPORT,
                name=constants.EQUALS + nfs_export_name))

    def create_nfs_export(self, file_system_id, path, name, nfs_other_params):
        """Create NFS Export of filesystem.

        :param file_system_id: The ID of the filesystem on which NFS Export
                               will be created
        :type file_system_id: str
        :param path: Local path to export relative to the NAS server root
        :type path: str
        :param name: The name of the NFS Export
        :type name: str
        :param nfs_other_params: Dictionary containing attributes with
                                    which NFS Export will be created
        :type nfs_other_params: dict
        :returns: The ID of the NFS export
        :rtype: dict
        """
        LOG.info("Creating NFSExport: '%s'" % name)
        payload = dict()
        payload['name'] = name
        payload['file_system_id'] = file_system_id
        payload['path'] = path
        if nfs_other_params:
            payload.update(nfs_other_params)
        return self.client.request(constants.POST,
                                   constants.CREATE_NFS_EXPORT_URL.format(
                                       self.server_ip), payload=payload)

    def modify_nfs_export(self, nfs_export_id, nfs_other_params):
        """Modify NFS Export attributes.

        :param nfs_export_id: The ID of the NFS Export
        :type nfs_export_id: str
        :param nfs_other_params: Dictionary containing attributes to be
                                    modified of the NFS Export
        :type nfs_other_params: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying nfsexport: '%s' with params: '%s'"
                 % (nfs_export_id, nfs_other_params))
        return self.client.request(
            constants.PATCH, constants.MODIFY_NFS_EXPORT_URL.format(
                self.server_ip, nfs_export_id), payload=nfs_other_params)

    def delete_nfs_export(self, nfs_export_id):
        """Delete NFS Export.

        :param nfs_export_id: The ID of the NFS Export
        :type nfs_export_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting nfsexport: '%s'" % nfs_export_id)
        return self.client.request(
            constants.DELETE, constants.DELETE_NFS_EXPORT_URL.format(
                self.server_ip, nfs_export_id))

    # NFS Export Method ENDs

    # SMB Share Methods
    def get_smb_shares(self, filter_dict=None, all_pages=False):
        """Get a list of smb shares.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool

        :returns: SMB shares
        :rtype: list of dict
        """
        LOG.info("Getting smbshares with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_SMB_SHARE_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_smb_share_by_name(self, share_name):
        """Get details of a SMB Share with its name.

        :param share_name: The name of the smb share.
        :type share_name: str
        :return: SMB share details
        :rtype: dict
        """
        LOG.info("Getting smbshare details by name: '%s'" % share_name)
        return self.client.request(
            constants.GET,
            constants.GET_SMB_SHARE_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_SMB_SHARE,
                name=constants.EQUALS + share_name
            )
        )

    def get_smb_share(self, share_id):
        """Get details of a SMB Share with its id.

        :param share_id: The Id of the SMB share.
        :type share_id: str
        :return: SMB share details
        :rtype: dict
        """
        LOG.info("Getting smbshare details by ID: '%s'" % share_id)
        return self.client.request(
            constants.GET,
            constants.GET_SMB_SHARE_DETAILS_URL.format(self.server_ip,
                                                       share_id),
            querystring=constants.SELECT_ALL_SMB_SHARE)

    def create_smb_share(
            self, file_system_id, path, name, **kw_smb_other_params):
        """ Create SMB share

        :param file_system_id: The ID of the File System.
        :type file_system_id: str
        :param path: Local path to the file system or any existing sub-folder
         of the file system that is shared over the network.
        :type path: str
        :param name: Name of the SMB Share.
        :type name: str
        :param kw_smb_other_params: Advance parameters.
        :type name: dict
        :return: The ID of the smb share if successful else error.
        :rtype: dict
        """
        LOG.info("Creating smbshare: '%s'" % name)
        payload = dict()
        payload['name'] = name
        payload['file_system_id'] = file_system_id
        payload['path'] = path
        if kw_smb_other_params:
            for key, value in kw_smb_other_params.items():
                payload[key] = value
        return self.client.request(
            constants.POST, constants.CREATE_SMB_SHARE_URL.format(
                self.server_ip), payload=payload)

    def update_smb_share(self, id, **kw_smb_other_params):
        """Modify a SMB Share.

        :param id: The ID of SMB Share.
        :param kw_smb_other_params: Parameters which are to be modified.
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying smbshare: '%s' with params: '%s'"
                 % (id, kw_smb_other_params))
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_SMB_SHARE_URL.
                                   format(self.server_ip, id),
                                   payload=kw_smb_other_params)

    def delete_smb_share(self, share_id):
        """Delete a SMB Share.

        :param share_id: The ID of the SMB share.
        :type share_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting smbshare: '%s'" % share_id)
        return self.client.request(constants.DELETE,
                                   constants.DELETE_SMB_SHARE_URL
                                   .format(
                                       self.server_ip, share_id))
    # SMB Share Methods End

    # FS Quota Methods
    def get_file_tree_quotas(self, filter_dict=None, all_pages=False):
        """Get a list of file tree quotas.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: File tree quotas
        :rtype: list of dict
        """
        LOG.info("Getting tree quotas with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            constants.SELECT_ID_AND_PATH, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_TREE_QUOTA_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_file_user_quotas(self, filter_dict=None, all_pages=False):
        """Get a list of file user quotas.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :returns: File user quotas
        :rtype: list of dict
        """
        LOG.info("Getting user quotas with filter: '%s' and all_pages: %s"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.client.request(constants.GET,
                                   constants.GET_USER_QUOTA_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=querystring,
                                   all_pages=all_pages)

    def get_tree_quota(self, tree_quota_id, path=None, file_system_id=None):
        """ Get details of Tree Quota either by its ID or
            by path and the filesystem_id.

        :param tree_quota_id: The Id of the Tree Quota.
        :type tree_quota_id: str
        :param path: (optional) Path of the tree relative to the root of the
                     associated filesystem.
        :type path: str
        :param file_system_id: (optional) ID of the associated filesystem.
        :type file_system_id: str
        :return: Tree quota details
        :rtype: dict
        """
        if tree_quota_id:
            LOG.info("Getting tree quota details by ID: '%s'" % tree_quota_id)
            return self.client.request(
                constants.GET,
                constants.GET_TREE_QUOTA_DETAILS_URL.format(self.server_ip,
                                                            tree_quota_id),
                querystring=constants.SELECT_ALL_TREE_QUOTA)
        else:
            LOG.info("Getting tree quota details by path: '%s' and fs_id: '%s'"
                     % (tree_quota_id, file_system_id))
            return self.client.request(
                constants.GET,
                constants.GET_TREE_QUOTA_LIST_URL.format(self.server_ip),
                querystring=helpers.prepare_querystring(
                    constants.SELECT_ALL_TREE_QUOTA,
                    path=constants.EQUALS + path,
                    file_system_id=constants.EQUALS + file_system_id
                )
            )

    def get_user_quota(self, user_quota_id, query_params=None):
        """ Get details of User Quota with its id or by other user quota
            parameters.

        :param user_quota_id: The Id of the User Quota.
        :type user_quota_id: str
        :param query_params: (optional) Other parameters of User Quota
        :type query_params: dict
        :return: User Quota details
        :rtype: dict
        """

        if user_quota_id:
            LOG.info("Getting user quota details by ID: '%s'" % user_quota_id)
            return self.client.request(
                constants.GET,
                constants.GET_USER_QUOTA_DETAILS_URL.format(self.server_ip,
                                                            user_quota_id),
                querystring=constants.SELECT_ALL_USER_QUOTA)
        else:
            if query_params:
                for key, value in query_params.items():
                    query_params[key] = constants.EQUALS + value
            LOG.info("Getting user quota details by params: '%s'"
                     % query_params)
            return self.client.request(
                constants.GET,
                constants.GET_USER_QUOTA_LIST_URL.format(self.server_ip),
                querystring=helpers.prepare_querystring(
                    constants.SELECT_ALL_USER_QUOTA,
                    query_params)
            )

    def create_tree_quota(self, file_system_id, path, tree_quota_params):
        """ Create a Tree Quota.

        :param file_system_id: The ID of the File System.
        :type file_system_id: str
        :param path: Path relative to the root of the associated filesystem.
        :type path: str
        :param tree_quota_params: Remaining Tree Quota parameters.
        :type tree_quota_params: dict
        :return: The ID of the Tree Quota if successful else error.
        :rtype: dict
        """
        LOG.info("Creating tree quota on filesystem ID: '%s'" % file_system_id)
        payload = dict()
        payload['file_system_id'] = file_system_id
        payload['path'] = path
        if tree_quota_params:
            payload.update(tree_quota_params)
        return self.client.request(
            constants.POST, constants.CREATE_TREE_QUOTA_URL.format(
                self.server_ip), payload=payload)

    def create_user_quota(self, file_system_id, user_quota_params):
        """ Create a User Quota.

        :param file_system_id: The ID of the File System.
        :type file_system_id: str
        :param user_quota_params: Remaining User Quota parameters.
        :type user_quota_params: dict
        :return: The ID of the User Quota if successful else error.
        :rtype: dict
        """
        LOG.info("Creating user quota on filesystem ID: '%s'" % file_system_id)
        payload = dict()
        payload['file_system_id'] = file_system_id
        if user_quota_params:
            payload.update(user_quota_params)
        return self.client.request(
            constants.POST, constants.CREATE_USER_QUOTA_URL.format(
                self.server_ip), payload=payload)

    def update_tree_quota(self, tree_quota_id, tree_quota_params):
        """ Update a Tree Quota.

        :param tree_quota_id: The ID of Tree Quota.
        :type tree_quota_id: str
        :param tree_quota_params: Tree Quota parameters to be modified.
        :type tree_quota_params: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying tree quota: '%s' with params: '%s'"
                 % (tree_quota_id, tree_quota_params))
        return self.client.request(
            constants.PATCH, constants.MODIFY_TREE_QUOTA_URL.format(
                self.server_ip, tree_quota_id),
            payload=tree_quota_params)

    def update_user_quota(self, user_quota_id, user_quota_params):
        """ Update a User Quota.

        :param user_quota_id: The ID of User Quota.
        :type user_quota_id: str
        :param user_quota_params: User Quota parameters to be modified.
        :type user_quota_params: dict
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Modifying user quota: '%s' with params: '%s'"
                 % (user_quota_id, user_quota_params))
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_USER_QUOTA_URL.
                                   format(self.server_ip, user_quota_id),
                                   payload=user_quota_params)

    def delete_tree_quota(self, tree_quota_id):
        """ Delete a Tree Quota.
        :param tree_quota_id: The ID of the Tree Quota.
        :type tree_quota_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting tree quota: '%s'" % tree_quota_id)
        return self.client.request(constants.DELETE,
                                   constants.DELETE_TREE_QUOTA_URL
                                   .format(self.server_ip, tree_quota_id))

    # FS Quota Methods end
