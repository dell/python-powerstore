# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Collection of provisioning related functions for PowerStore"""

from PyPowerStore.client import Client
from PyPowerStore.utils import constants, helpers


class Provisioning():
    """Provisioning related functionality for PowerStore."""
    def __init__(self, server_ip, username, password, verify,
                 application_type, timeout):
        self.server_ip = server_ip
        self.client = Client(username, password, verify, application_type,
                             timeout)

    def create_volume(self, name, size, description=None,
                      volume_group_id=None, protection_policy_id=None,
                      performance_policy_id=None):
        """Create a volume.

        :param name: The name of the volume
        :param size: The size of the volume
        :param description: The description given to the volume
        :param volume_group_id: The volume group ID
        :param protection_policy_id: The protection policy ID
        :param performance_policy_id: The performance policy ID
        """
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
        """

        return self.client.request(constants.DELETE,
                                   constants.DELETE_VOLUME_URL.format(
                                       self.server_ip, volume_id),
                                   payload=None)

    def modify_volume(self, volume_id, name=None, description=None, size=None,
                      protection_policy_id=None,
                      performance_policy_id=None):
        """Modify a volume.

        :param volume_id: The volume ID
        :param name: The name of the volume
        :param description: The description of the volume
        :param size: The size of the volume
        :param protection_policy_id: The protection policy ID
        :param performance_policy_id: The performance policy ID
        """

        payload = self.\
            _prepare_modify_volume_payload(name,
                                           description,
                                           size,
                                           protection_policy_id,
                                           performance_policy_id)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_VOLUME_URL.format(
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
        :param protection_policy_id: The protection policy ID
        """

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
        """

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
        :param host_id: The host ID
        :param logical_unit_number: The logical unit number
        """

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
        :param host_group_id: The host group ID
        :param logical_unit_number: The logical unit number
        """

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
        :param host_id: The host ID
        """

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
        :param host_group_id: The host group ID
        """

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

    def get_volumes(self):
        """Get a list of volumes."""

        return self.client.request(constants.GET,
                                   constants.GET_VOLUME_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=constants.SELECT_ID_AND_NAME)

    def get_volume_details(self, volume_id):
        """Get details of a volume."""

        resp = self.client.request(constants.GET,
                                   constants.GET_VOLUME_DETAILS_URL.format
                                   (self.server_ip, volume_id), payload=None,
                                   querystring=constants.SELECT_ALL_VOLUME)

        hlu_details = self.get_host_volume_mapping(volume_id=volume_id)

        resp['hlu_details'] = hlu_details

        return resp

    def get_volume_by_name(self, volume_name):
        """Get details of a volume by name."""

        resp = self.client.request(
            constants.GET,
            constants.GET_VOLUME_BY_NAME_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_VOLUME,
                name=constants.EQUALS + volume_name
            )
        )

        hlu_details = self.get_host_volume_mapping(volume_id=resp[0]['id'])
        resp[0]['hlu_details'] = hlu_details

        return resp

    def get_hosts(self):
        """Get a list of all the registered hosts."""

        return self.client.request(constants.GET,
                                   constants.GET_HOST_LIST_URL.format
                                   (self.server_ip), payload=None,
                                   querystring=constants.SELECT_ID_AND_NAME)

    def create_host(self, name, os_type, initiators,
                    description=None):
        """Register a host on the array.

        :param name: The name of the host
        :param description: The description for the host
        :param os_type: The OS type of the host
        :param initiators: Contains a list of dictionaries of host initiators
        :return: Dict containing host ID
        """

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
        :return: Dict containing host details
        """

        return self.client.request(constants.GET,
                                   constants.GET_HOST_DETAILS_URL.format(
                                       self.server_ip, host_id), payload=None,
                                   querystring=constants.SELECT_ALL_HOST)

    def modify_host(self, host_id, name=None, description=None,
                    remove_initiators=None, add_initiators=None,
                    modify_initiators=None
                    ):
        """Modify a given host - Only one of add, remove
        or update in the same request.

        :param host_id: The host ID
        :param name: The host name
        :param description: The description for the host
        :param remove_initiators: List of initiators to be removed
        :param add_initiators: List of initiators to be added
        :param modify_initiators: List of initiators to be modified
        """
        payload = self._prepare_modify_host_payload(name,
                                                    description,
                                                    remove_initiators,
                                                    add_initiators,
                                                    modify_initiators)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_URL.format(
                                       self.server_ip, host_id), payload)

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
        :param add_initiators: List of initiators to be added.
        """
        payload = self._prepare_modify_host_payload(
            add_initiators=add_initiators)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_URL.format(
                                       self.server_ip, host_id), payload)

    def remove_initiators_from_host(self, host_id, remove_initiators=None):
        """Remove initiators from Host.

        :param host_id: The host ID
        :param remove_initiators: List of initiators to be added
        """
        payload = self._prepare_modify_host_payload(
            remove_initiators=remove_initiators)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_URL.format(
                                       self.server_ip, host_id), payload)

    def delete_host(self, host_id, force=None):
        """Delete a host.

        :param host_id: The host ID.
        :param force: The force_internal flag (optional).
        """
        if force:
            payload = {
                "force_internal": force
            }
        else:
            payload = None
        return self.client.request(constants.DELETE,
                                   constants.DELETE_HOST_URL.format(
                                       self.server_ip, host_id), payload)

    def get_host_by_name(self, host_name):
        """Get details of a Host with its name.

        :param host_name: The Host name.
        :return: Host details
        """
        return self.client.request(
            constants.GET,
            constants.GET_HOST_BY_NAME_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_HOST, name=constants.EQUALS + host_name
            )
        )

    def get_host_group_list(self):
        """Get a list of all host groups."""

        return self.client.request(constants.GET,
                                   constants.GET_HOST_GROUP_LIST_URL.format(
                                       self.server_ip), payload=None,
                                   querystring=constants.SELECT_ID_AND_NAME
                                   )

    def create_host_group(self, name, host_ids, description=None):
        """Create a Host Group.

        :param name: The name of the host group
        :param host_ids: List containing host IDs
        :param description: The description for the host group
        :return: Dict containing host group ID
        """

        payload = self._prepare_create_host_group_payload(name,
                                                          host_ids,
                                                          description)

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
        """Get details of a particular host group."""

        return self.client.request(constants.GET,
                                   constants.GET_HOST_GROUP_DETAILS_URL.format(
                                       self.server_ip, host_group_id),
                                   payload=None,
                                   querystring=constants.SELECT_ALL_HOST_GROUP)

    def get_host_group_by_name(self, host_group_name):
        """Get details of a Host Group with its name.

        :param host_group_name: The Host Group name
        :return: Host Group details
        """
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
        :return: Host List which are part of Host Group
        """
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
        :param name: The modified name of the host group
        :param remove_host_ids: The hosts to be removed from host group
        :param add_host_ids: The hosts to be added to the host group
        :param description: The modified description for the host group
        """

        payload = self._prepare_modify_host_group_payload(name,
                                                          remove_host_ids,
                                                          add_host_ids,
                                                          description)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_GROUP_URL.format(
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
        :param add_host_ids: The hosts to be added to the host group.
        """

        payload = self._prepare_modify_host_group_payload(
            add_host_ids=add_host_ids)
        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_GROUP_URL.format(
                                       self.server_ip, host_group_id),
                                   payload)

    def remove_hosts_from_host_group(self, host_group_id,
                                     remove_host_ids=None):
        """Remove Hosts from Host Group.

        :param host_group_id: The ID of the host group to be modified
        :param remove_host_ids: The hosts to be removed from host group
        """

        payload = self._prepare_modify_host_group_payload(
            remove_host_ids=remove_host_ids)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_HOST_GROUP_URL.format(
                                       self.server_ip, host_group_id),
                                   payload)

    def delete_host_group(self, host_group_id):
        """Delete a host group.

        :param host_group_id: The ID of the host group
        """

        return self.client.request(constants.DELETE,
                                   constants.DELETE_HOST_GROUP_URL.format(
                                       self.server_ip, host_group_id),
                                   payload=None)

    def get_volumes_from_volume_group(self, vol_group_name):
        """Get a list of volumes which belong to Volume Group.

        :param vol_group_name: The Volume group name
        :return: Vol list which are part of Volume Group
        """
        return self.client.request(
            constants.GET,
            constants.GET_VOLUMES_FROM_VOLUME_GROUP.format(self.server_ip,
                                                           vol_group_name),
            payload=None, querystring=helpers.prepare_querystring(
                name=constants.EQUALS + vol_group_name, select='volumes(name)'
            )
        )

    def get_volume_group_list(self):
        """Get a list of all the volume groups."""

        return self.client.request(constants.GET,
                                   constants.GET_VOLUME_GROUP_LIST_URL.format(
                                       self.server_ip),
                                   payload=None,
                                   querystring=helpers.prepare_querystring
                                   (constants.SELECT_ID_AND_NAME))

    def create_volume_group(self, name, description=None,
                            volume_ids=None,
                            is_write_order_consistent=None,
                            protection_policy_id=None):
        """Create a volume group.

        :param name: The name of the volume group.
        :param description: The description of the VG.
        :param volume_ids: The volume IDs to be added to the VG
        :param is_write_order_consistent: boolean to indicate whether snapshot
                                          sets of the volume group will be
                                          write-order consistent.
        :param protection_policy_id: Unique identifier of an optional
                                     protection policy to assign
                                     to the volume group.
        """

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
        :return: Details of the volume group
        """

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
        """
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
        :param name: The name of the volume group
        :param description: The description of the VG
        :param is_write_order_consistent: A boolean flag to indicate whether
                                          snapshot sets of the volume group
                                          will be write-order consistent.
        :param protection_policy_id: Unique identifier of the protection
                                     policy to assign to a primary or clone
                                     volume group.
                                     If an empty string is specified,
                                     protection policy will be removed
                                     from the volume group.
        """

        payload = self._prepare_modify_vg_payload(name,
                                                  description,
                                                  is_write_order_consistent,
                                                  protection_policy_id)

        return self.client.request(constants.PATCH,
                                   constants.MODIFY_VOLUME_GROUP_URL.
                                   format(
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
        """

        return self.client.request(constants.DELETE,
                                   constants.DELETE_VOLUME_GROUP_URL
                                   .format(
                                       self.server_ip, volume_group_id),
                                   payload=None)

    def add_members_to_volume_group(self, volume_group_id, volume_ids,
                                    force_internal=False):
        """Add members to volume group.

        :param volume_ids: The list of volume IDs to be added
        :param force_internal: The force internal flag
        """

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
        :param force_internal: The force internal flag
        """

        payload = self._prepare_remove_members_from_volume_group_payload(
            volume_ids,
            force_internal)

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

    def get_nodes(self):
        """Returns a list of nodes."""

        return self.client.request(constants.GET,
                                   constants.GET_NODE.format
                                   (self.server_ip), payload=None,
                                   querystring=constants.
                                   SELECT_ID_AND_NAME)

    def get_cluster_list(self):
        """Returns a list of clusters."""

        return self.client.request(constants.GET,
                                   constants.GET_CLUSTER.format
                                   (self.server_ip), payload=None,
                                   querystring=constants.
                                   SELECT_ID_AND_NAME)

    def get_host_volume_mapping(self, volume_id):
        """Get Host volume mapping details.

        :param volume_id: The Volume ID
        """

        return self.client.request(
            constants.GET,
            constants.HOST_VOLUME_MAPPING_URL.format(self.server_ip),
            payload=None, querystring=helpers.prepare_querystring(
                constants.SELECT_ALL_HOST_VOLUME_MAPPING,
                volume_id=constants.EQUALS +
                volume_id
            )
        )
