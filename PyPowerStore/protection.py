# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC
# Copyright: (c) 2019, Ivan Pchelintsev <Ivan.Pchelintsev@emc.com>

"""Collection of protection related functions for PowerStore"""

from collections import namedtuple

from PyPowerStore.utils import constants, helpers

# Volume types
VOLUME_TYPE = namedtuple('VolumeType', 'primary '
                                       'clone '
                                       'snapshot')(primary='Primary',
                                                   clone='Clone',
                                                   snapshot='Snapshot')
# Policy types
POLICY_TYPE = namedtuple('PolicyType',
                         'protection '
                         'performance')(protection='Protection',
                                        performance='Performance')
SNAPSHOT_RULE_FILTER = {'is_replica': constants.EQUALS + 'false'}
SNAPSHOT_RULE_DETAILS_QUERY = {
    'select': 'id,name,interval,days_of_week,time_of_day,desired_retention,'
              'policies(id,name)'
}
PROTECTION_POLICY_FILTER = {'type': constants.EQUALS + POLICY_TYPE.protection}
PROTECTION_POLICY_DETAILS_QUERY = {
    'select': 'id,name,description,type,replication_rules(id,name),'
              'snapshot_rules(id,name)'
}

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)


class ProtectionFunctions():
    """Protection related functionality for PowerStore."""
    def __init__(self, provisioning, enable_log=False):
        """ Initializes ProtectionFunctions Class

        :param provisioning: Provisioning class object
        :type provisioning: Provisioning
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        """
        global LOG
        self.provisioning = provisioning
        self.server_ip = provisioning.server_ip
        self.rest_client = provisioning.client
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    def get_volume_snapshots(self, volume_id):
        """Get snapshots of a volume.

        :param volume_id: Volume unique identifier.
        :type volume_id: str
        :return: Volume snapshots.
        :rtype: list[dict]
        """
        LOG.info("Getting volume snapshots from vol id: '%s'" % volume_id)
        filter_by_source = {
            'protection_data->>source_id': constants.EQUALS + volume_id
        }
        return self.rest_client.request(
            constants.GET,
            constants.GET_VOLUME_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME, filter_by_source,
                type=constants.EQUALS + VOLUME_TYPE.snapshot
            )
        )

    def get_volume_snapshot_details(self, snapshot_id):
        """Get details of a particular volume snapshot.

        :param snapshot_id: Volume snapshot unique identifier.
        :type snapshot_id: str
        :return: Volume snapshot details.
        :rtype: dict
        """
        return self.provisioning.get_volume_details(volume_id=snapshot_id)

    def create_volume_snapshot(self, volume_id, name=None, description=None,
                               performance_policy_id=None,
                               expiration_timestamp=None):
        """Create a snapshot of a volume.

        :param volume_id: Volume unique identifier.
        :type volume_id: str
        :param name: (optional) Volume snapshot name. The default name is the
                     date and time when the snapshot is taken.
        :type name: str
        :param description: (optional) Volume snapshot description.
        :type description: str
        :param performance_policy_id: (optional) Performance policy unique
                                      identifier.
        :type performance_policy_id: str
        :param expiration_timestamp: (optional) Expiration time of the
                                     snapshot. Expired snapshots are deleted
                                     by the snapshot aging service that runs
                                     periodically in the background. If not
                                     specified, the snapshot never expires.
                                     Use the maximum timestamp value of
                                     '12:31:9999T23:59:59.999Z' to set an
                                     expiration to never expire.
        :type expiration_timestamp: str
        :return: Volume snapshot details.
        :rtype: dict
        """
        LOG.info("Creating snapshot of volume: '%s'" % volume_id)
        payload = self._prepare_create_modify_snapshot_payload(
            name=name, description=description,
            performance_policy_id=performance_policy_id,
            expiration_timestamp=expiration_timestamp
        )
        response = self.rest_client.request(
            constants.POST,
            constants.CREATE_VOLUME_SNAPSHOT_URL.format(self.server_ip,
                                                        volume_id),
            payload
        )
        if isinstance(response, dict) and response.get('id'):
            return self.get_volume_snapshot_details(response['id'])
        return response

    def modify_volume_snapshot(self, snapshot_id, name=None, description=None,
                               expiration_timestamp=None):
        """Modify a snapshot of a volume.

        :param snapshot_id: Volume snapshot unique identifier.
        :param name: (optional) Volume snapshot name.
        :type name: str
        :param description: (optional) Volume snapshot description.
        :type description: str
        :param expiration_timestamp: (optional) Expiration time of the
                                     snapshot. Expired snapshots are deleted
                                     by the snapshot aging service that runs
                                     periodically in the background. If not
                                     specified, the snapshot never expires. Use
                                     the maximum timestamp value of
                                     '12:31:9999T23:59:59.999Z' to set an
                                     expiration to never expire.
        :return: Volume snapshot details.
        :rtype: dict
        """
        LOG.info("Modifying volume snapshot: '%s'" % snapshot_id)
        payload = self._prepare_create_modify_snapshot_payload(
            name=name, description=description,
            expiration_timestamp=expiration_timestamp
        )
        self.rest_client.request(
            constants.PATCH,
            constants.MODIFY_VOLUME_URL.format(self.server_ip, snapshot_id),
            payload
        )
        return self.get_volume_snapshot_details(snapshot_id)

    def delete_volume_snapshot(self, snapshot_id):
        """Delete a snapshot of a volume.

        :param snapshot_id: Volume snapshot unique identifier.
        :type snapshot_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting volume snapshot: '%s'" % snapshot_id)
        return self.rest_client.request(
            constants.DELETE,
            constants.DELETE_VOLUME_URL.format(self.server_ip, snapshot_id))

    def get_volume_group_snapshots(self, volume_group_id):
        """Get snapshots of a volume group.

        :param volume_group_id: Volume Group unique identifier.
        :type volume_group_id: str
        :return: Volume Group snapshots.
        :rtype: list[dict]
        """
        LOG.info("Getting volumegroup snapshots: '%s'" % volume_group_id)
        filter_by_source = {
            'protection_data->>source_id': constants.EQUALS + volume_group_id
        }
        return self.rest_client.request(
            constants.GET,
            constants.GET_VOLUME_GROUP_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                constants.SELECT_ID_AND_NAME, filter_by_source,
                type=constants.EQUALS + VOLUME_TYPE.snapshot
            )
        )

    def get_volume_group_snapshot_details(self, snapshot_id):
        """Get details of a particular volume group snapshot.

        :param snapshot_id: Volume Group snapshot unique identifier.
        :type snapshot_id: str
        :return: Volume Group snapshot details.
        :rtype: dict
        """
        return self.provisioning.get_volume_group_details(
            volume_group_id=snapshot_id
        )

    def create_volume_group_snapshot(self, volume_group_id, name=None,
                                     description=None,
                                     expiration_timestamp=None):
        """Create a snapshot of a volume group.

        :param volume_group_id: Volume Group unique identifier.
        :type volume_group_id: str
        :param name: (optional) Volume Group snapshot name. The default name is
                     the date and time when the snapshot is taken.
        :type name: str
        :param description: (optional) Volume Group snapshot description.
        :type description: str
        :param expiration_timestamp: (optional) Time after which the snapshot
                                     set can be auto-purged. Time must be
                                     specified in Zulu time zone. Expiration
                                     time cannot be prior to current time. Use
                                     a maximum timestamp value to set an
                                     expiration to never expire. Valid format
                                     is yyyy-MM-dd'T'HH:mm:ssZ or
                                     yyyy-MM-dd'T'HH:mm:ss.SSSZ. By default,
                                     expiration time will not be set.
        :type expiration_timestamp: str
        :return: Volume Group snapshot details.
        :rtype: dict
        """
        LOG.info("Creating snapshot of volumegroup: '%s'" % volume_group_id)
        payload = self._prepare_create_modify_snapshot_payload(
            name=name, description=description,
            expiration_timestamp=expiration_timestamp
        )
        response = self.rest_client.request(
            constants.POST,
            constants.CREATE_VOLUME_GROUP_SNAPSHOT_URL.format(self.server_ip,
                                                              volume_group_id),
            payload
        )
        if isinstance(response, dict) and response.get('id'):
            return self.get_volume_group_snapshot_details(response['id'])
        return response

    def modify_volume_group_snapshot(self, snapshot_id, name=None,
                                     description=None,
                                     expiration_timestamp=None):
        """Modify a snapshot of a volume group.

        :param snapshot_id: Volume Group snapshot unique identifier.
        :type snapshot_id: str
        :param name: (optional) Volume Group snapshot name.
        :type name: str
        :param description: (optional) Volume Group snapshot description.
        :type description: str
        :param expiration_timestamp: (optional) Time after which the snapshot
                                     set can be auto-purged. Time must be
                                     specified in Zulu time zone. Expiration
                                     time cannot be prior to current time.
                                     Use a maximum timestamp value to set an
                                     expiration to never expire. Valid format
                                     is yyyy-MM-dd'T'HH:mm:ssZ or
                                     yyyy-MM-dd'T'HH:mm:ss.SSSZ. By default,
                                     expiration time will not be set.
        :return: Volume snapshot details.
        :rtype: dict
        """
        LOG.info("Modifying volumegroup snapshot: '%s'" % snapshot_id)
        payload = self._prepare_create_modify_snapshot_payload(
            name=name, description=description,
            expiration_timestamp=expiration_timestamp
        )
        self.rest_client.request(
            constants.PATCH,
            constants.MODIFY_VOLUME_GROUP_URL.format(self.server_ip,
                                                     snapshot_id),
            payload
        )
        return self.get_volume_group_snapshot_details(snapshot_id)

    def delete_volume_group_snapshot(self, snapshot_id):
        """Delete a snapshot of a volume group.

        :param snapshot_id: Volume Group snapshot unique identifier.
        :type snapshot_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting volumegroup snapshot: '%s'" % snapshot_id)
        return self.rest_client.request(
            constants.DELETE,
            constants.DELETE_VOLUME_GROUP_URL.format(self.server_ip,
                                                     snapshot_id))

    def get_snapshot_rules(self, filter_dict=None, all_pages=False):
        """Get all snapshot rules.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Snapshot rules.
        :rtype: list[dict]
        """
        LOG.info("Getting snapshot_rules with filter: '%s' and all_pages: '%s'"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            SNAPSHOT_RULE_FILTER, constants.SELECT_ID_AND_NAME, filter_dict)
        LOG.info("Querystring: '%s'" % querystring)
        return self.rest_client.request(
            constants.GET,
            constants.SNAPSHOT_RULE_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_snapshot_rule_by_name(self, name):
        """Get a snapshot rule by name.

        :param name: Snapshot rule name.
        :type name: str
        :return: Snapshot rule with corresponding name.
        :rtype: list[dict]
        """
        LOG.info("Getting snapshot_rule details by name: '%s'" % name)
        return self.rest_client.request(
            constants.GET,
            constants.SNAPSHOT_RULE_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                SNAPSHOT_RULE_FILTER, constants.SELECT_ID_AND_NAME,
                name=constants.EQUALS + name))

    def get_snapshot_rule_details(self, snapshot_rule_id):
        """Get details of a particular snapshot rule.

        :param snapshot_rule_id: Snapshot rule unique identifier.
        :type snapshot_rule_id: str
        :return: Snapshot rule details.
        :rtype: dict
        """
        LOG.info("Getting snapshot_rule details by ID: '%s'"
                 % snapshot_rule_id)
        return self.rest_client.request(
            constants.GET,
            constants.SNAPSHOT_RULE_OBJECT_URL.format(self.server_ip,
                                                      snapshot_rule_id),
            querystring=SNAPSHOT_RULE_DETAILS_QUERY
        )

    def create_snapshot_rule_by_interval(self, name, desired_retention,
                                         interval, days_of_week=None):
        """Create a new snapshot rule to take snapshots with time interval
        between.

        :param name: Snapshot rule name.
        :type name: str
        :param desired_retention: Desired snapshot retention period in hours.
                                  The system will retain snapshots for this
                                  time period, if space is available.
        :type desired_retention: int
        :param interval: Interval between snapshots e.g. Five_Minutes,
                         Fifteen_Minutes, Thirty_Minutes, One_Hour,
                         Two_Hours, Three_Hours, Four_Hours, Six_Hours,
                         Eight_Hours, Twelve_Hours, One_Day. You can either set
                         the interval parameter or the time_of_day parameter.
                         Setting one clears the other parameter.
        :type interval: str
        :param days_of_week: (optional) Days of the week on which the rule
                             should be applied. Applies only for rules where
                             the interval parameter is set.
        :type days_of_week: list[str]
        :return: Snapshot rule details.
        :rtype: dict
        """
        LOG.info("Creating a snaphot_rule: '%s' by interval" % name)
        return self._create_snapshot_rule(name=name,
                                          desired_retention=desired_retention,
                                          interval=interval,
                                          days_of_week=days_of_week)

    def create_snapshot_rule_by_time_of_day(self, name, desired_retention,
                                            time_of_day, days_of_week=None):
        """Create a new snapshot rule to take daily snapshots at the specified
        time of day.

        :param name: Snapshot rule name.
        :type name: str
        :param desired_retention: Desired snapshot retention period in hours.
                                  The system will retain snapshots for this
                                  time period, if space is available.
        :type desired_retention: int
        :param time_of_day: Time of the day to take a daily snapshot, with
                            format "hh:mm" in 24 hour time format.
                            Either the interval parameter or the time_of_day
                            parameter may be set, but not both.
        :type time_of_day: str
        :param days_of_week: (optional) Days of the week on which the rule
                             should be applied. Applies only for rules where
                             the time_of_day parameter is set.
        :type days_of_week: list[str]
        :return: Snapshot rule details.
        :rtype: dict
        """
        LOG.info("Creating a snapshot_rule: '%s' by time_of_day" % name)
        return self._create_snapshot_rule(name=name,
                                          desired_retention=desired_retention,
                                          time_of_day=time_of_day,
                                          days_of_week=days_of_week)

    def _create_snapshot_rule(self, **kwargs):
        """Create a new snapshot rule using provided arguments.

        :return: Snapshot rule details.
        :rtype: dict
        """
        payload = self._prepare_create_modify_snapshot_rule_payload(**kwargs)
        response = self.rest_client.request(
            constants.POST,
            constants.SNAPSHOT_RULE_LIST_URL.format(self.server_ip),
            payload
        )
        if isinstance(response, dict) and response.get('id'):
            return self.get_snapshot_rule_details(response['id'])
        return response

    def modify_snapshot_rule(self, snapshot_rule_id, name=None,
                             desired_retention=None, interval=None,
                             time_of_day=None, days_of_week=None):
        """Modify a snapshot rule. If the rule is associated with a policy that
        is currently applied to a storage resource, the modified rule is
        immediately applied to that associated storage resource.

        :param snapshot_rule_id: Snapshot rule unique identifier.
        :param name: (optional) Snapshot rule name.
        :type name: str
        :param desired_retention: (optional) Desired snapshot retention period
                                  in hours. The system will retain snapshots
                                  for this time period, if space is available.
        :type desired_retention: int
        :param interval: (optional) Interval between snapshots e.g.
                         Five_Minutes, Fifteen_Minutes, Thirty_Minutes,
                         One_Hour, Two_Hours, Three_Hours, Four_Hours,
                         Six_Hours, Eight_Hours, Twelve_Hours, One_Day. You
                         can either set the interval parameter or the
                         time_of_day parameter. Setting one clears the other
                         parameter.
        :type interval: str
        :param time_of_day: (optional) Time of the day to take a daily
                            snapshot, with format "hh:mm" in 24 hour time
                            format. Either the interval parameter or the
                            time_of_day parameter may be set, but not both.
        :type time_of_day: str
        :param days_of_week: (optional) Days of the week on which the rule
                             should be applied. Applies only for rules where
                             the time_of_day parameter is set.
        :type days_of_week: list[str]
        :return: Snapshot rule details.
        :rtype: dict
        """
        LOG.info("Modifying snapshot_rule: '%s'" % snapshot_rule_id)
        payload = self._prepare_create_modify_snapshot_rule_payload(
            name=name, desired_retention=desired_retention, interval=interval,
            time_of_day=time_of_day, days_of_week=days_of_week
        )
        self.rest_client.request(
            constants.PATCH,
            constants.SNAPSHOT_RULE_OBJECT_URL.format(self.server_ip,
                                                      snapshot_rule_id),
            payload
        )
        return self.get_snapshot_rule_details(snapshot_rule_id)

    def delete_snapshot_rule(self, snapshot_rule_id, delete_snaps=False):
        """Delete a snapshot rule.

        :param snapshot_rule_id: Snapshot rule unique identifier.
        :type snapshot_rule_id: str
        :param delete_snaps: (optional) Specify whether all snapshots
                             previously created by this rule should also be
                             deleted when this rule is removed. Default: False.
        :type delete_snaps: bool
        """
        payload = dict(delete_snaps=delete_snaps)
        LOG.info("Deleting snapshot_rule: '%s' payload: '%s'"
                 % (snapshot_rule_id, payload))
        return self.rest_client.request(
            constants.DELETE,
            constants.SNAPSHOT_RULE_OBJECT_URL.format(self.server_ip,
                                                      snapshot_rule_id),
            payload
        )

    def get_protection_policies(self, filter_dict=None, all_pages=False):
        """Get all protection policies.

        :param filter_dict: (optional) Filter detail
        :type filter_dict: dict
        :param all_pages: (optional) Indicates whether to return all element
                          or not
        :type all_pages: bool
        :return: Protection policies.
        :rtype: list[dict]
        """
        LOG.info("Getting policies with filter: '%s' and all_pages: '%s'"
                 % (filter_dict, all_pages))
        querystring = helpers.prepare_querystring(
            PROTECTION_POLICY_FILTER,
            constants.SELECT_ID_AND_NAME,
            filter_dict)
        LOG.info("Querystring: %s" % querystring)
        return self.rest_client.request(
            constants.GET,
            constants.PROTECTION_POLICY_LIST_URL.format(self.server_ip),
            querystring=querystring, all_pages=all_pages)

    def get_protection_policy_details(self, policy_id):
        """Get details of a particular protection policy.

        :param policy_id: Protection policy unique identifier.
        :type policy_id: str
        :return: Protection policy details.
        :rtype: dict
        """
        LOG.info("Getting policy details by ID: '%s'" % policy_id)
        return self.rest_client.request(
            constants.GET,
            constants.PROTECTION_POLICY_OBJECT_URL.format(self.server_ip,
                                                          policy_id),
            querystring=PROTECTION_POLICY_DETAILS_QUERY
        )

    def get_protection_policy_by_name(self, name):
        """Get a protection policy by name.

        :param name: Protection policy name.
        :type name: str
        :return: Protection policy with corresponding name.
        :rtype: list[dict]
        """
        LOG.info("Getting policy details by name: '%s'" % name)
        return self.rest_client.request(
            constants.GET,
            constants.PROTECTION_POLICY_LIST_URL.format(self.server_ip),
            querystring=helpers.prepare_querystring(
                PROTECTION_POLICY_FILTER, constants.SELECT_ID_AND_NAME,
                name=constants.EQUALS + name
            )
        )

    def create_protection_policy(self, name, description=None,
                                 snapshot_rule_ids=None,
                                 replication_rule_ids=None):
        """Create a new protection policy. Protection policies can be assigned
        to volumes or application groups. When a protection policy is assigned
        to a volume or application group:

        * If the policy is associated with one or more snapshot rules,
          scheduled snapshots are created based on the schedule specified in
          each snapshot rule.
        * If the policy is associated with a replication rule, a replication
          session is created and synchronized based on the schedule specified
          in the replication rule.

        :param name: Protection policy name.
        :type name: str
        :param description: (optional) Protection policy description.
        :type description: str
        :param snapshot_rule_ids: (optional) Snapshot rule identifiers included
                                  in this policy. At least one snapshot rule or
                                  one replication rule must be specified to
                                  create a protection policy.
        :type snapshot_rule_ids: list[str]
        :param replication_rule_ids: (optional) Replication rule identifiers
                                     included in this policy. At least one
                                     snapshot rule or one replication rule must
                                     be specified to create a protection policy
        :type replication_rule_ids: list[str]
        :return: Protection policy details.
        :rtype: dict
        """
        LOG.info("Creating policy: '%s'" % name)
        payload = self._prepare_create_modify_protection_policy_payload(
            name=name, description=description,
            snapshot_rule_ids=snapshot_rule_ids,
            replication_rule_ids=replication_rule_ids
        )
        response = self.rest_client.request(
            constants.POST,
            constants.PROTECTION_POLICY_LIST_URL.format(self.server_ip),
            payload
        )
        if isinstance(response, dict) and response.get('id'):
            return self.get_protection_policy_details(response['id'])
        return response

    def add_snapshot_rules_to_protection_policy(self, policy_id,
                                                add_snapshot_rule_ids):
        """
        Add snapshot rules to protection policy.

        :param policy_id: Protection policy unique identifier.
        :type policy_id: str
        :param add_snapshot_rule_ids: Snapshot rule identifiers to be added to
                                      this policy.
        :type add_snapshot_rule_ids: list[str]
        :return:
        """
        LOG.info("Adding snapshot_rules: '%s' to policy: '%s'"
                 % (add_snapshot_rule_ids, policy_id))
        return self.modify_protection_policy(
            policy_id=policy_id, add_snapshot_rule_ids=add_snapshot_rule_ids
        )

    def remove_snapshot_rules_from_protection_policy(self, policy_id,
                                                     remove_snapshot_rule_ids):
        """
        Remove snapshot rules from protection policy.

        :param policy_id: Protection policy unique identifier.
        :type policy_id: str
        :param remove_snapshot_rule_ids: Snapshot rule identifiers to be
                                         removed from this policy.
        :type remove_snapshot_rule_ids: list[str]
        :return: Protection policy details.
        :rtype: dict
        """
        LOG.info("Removing snapshot_rules: '%s' to policy: '%s'"
                 % (remove_snapshot_rule_ids, policy_id))
        return self.modify_protection_policy(
            policy_id=policy_id,
            remove_snapshot_rule_ids=remove_snapshot_rule_ids
        )

    def modify_protection_policy(self, policy_id, name=None, description=None,
                                 snapshot_rule_ids=None,
                                 replication_rule_ids=None,
                                 add_snapshot_rule_ids=None,
                                 add_replication_rule_ids=None,
                                 remove_snapshot_rule_ids=None,
                                 remove_replication_rule_ids=None):
        """Modify a protection policy.

        :param policy_id: Protection policy unique identifier.
        :type policy_id: str
        :param name: (optional) Protection policy name.
        :type name: str
        :param description: (optional) Protection policy description.
        :type description: str
        :param snapshot_rule_ids: (optional) Snapshot rule identifiers that
                                  should replace the current list of snapshot
                                  rule identifiers in this policy.
        :type snapshot_rule_ids: list[str]
        :param replication_rule_ids: (optional) Replication rule identifiers
                                     that should replace the current list of
                                     replication rule identifiers in this
                                     policy
        :type replication_rule_ids: list[str]
        :param add_snapshot_rule_ids: (optional) Snapshot rule identifiers to
                                      be added to this policy.
        :type add_snapshot_rule_ids: list[str]
        :param add_replication_rule_ids: (optional) Replication rule
                                         identifiers to be added to this
                                         policy.
        :type add_replication_rule_ids: list[str]
        :param remove_snapshot_rule_ids: (optional) Snapshot rule identifiers
                                         to be removed from this policy.
        :type remove_snapshot_rule_ids: list[str]
        :param remove_replication_rule_ids: (optional) Replication rule
                                            identifiers to be removed from this
                                            policy.
        :type remove_replication_rule_ids: list[str]
        :return: Protection policy details.
        :rtype: dict
        """
        LOG.info("Modifying policy: '%s'" % policy_id)
        payload = self._prepare_create_modify_protection_policy_payload(
            name=name, description=description,
            snapshot_rule_ids=snapshot_rule_ids,
            replication_rule_ids=replication_rule_ids,
            add_snapshot_rule_ids=add_snapshot_rule_ids,
            add_replication_rule_ids=add_replication_rule_ids,
            remove_snapshot_rule_ids=remove_snapshot_rule_ids,
            remove_replication_rule_ids=remove_replication_rule_ids
        )
        self.rest_client.request(
            constants.PATCH,
            constants.PROTECTION_POLICY_OBJECT_URL.format(self.server_ip,
                                                          policy_id),
            payload
        )
        return self.get_protection_policy_details(policy_id)

    def delete_protection_policy(self, policy_id):
        """Delete a protection policy. Before the deletion of a protection
        policy, ensure that the relevant storage resources are no longer using
        the policy.

        :param policy_id: Protection policy unique identifier.
        :type policy_id: str
        :return: None if success else raise exception
        :rtype: None
        """
        LOG.info("Deleting policy: '%s'" % policy_id)
        return self.rest_client.request(
            constants.DELETE,
            constants.PROTECTION_POLICY_OBJECT_URL.format(self.server_ip,
                                                          policy_id)
        )

    # FS Snapshot Methods

    def get_filesystem_snapshot_details_by_name(
            self, snapshot_name, filesystem_id=None, nas_server_id=None):
        """Get details of a particular filesystem snapshot.

        :param snapshot_name: The name of the filesystem snapshot
        :type snapshot_name: str
        :param filesystem_id: (optional) The ID of the filesystem
        :type filesystem_id: str
        :param nas_server_id: (optional) The ID of the NAS server
        :type nas_server_id: str
        :return: Filesystem snapshot details
        :rtype: list
        """

        if filesystem_id is None and nas_server_id is None:
            raise ValueError('Provide filesystem_id or nas_server_id.')

        if filesystem_id is not None and nas_server_id is not None:
            raise ValueError('Provide filesystem_id or nas_server_id, '
                             'but not both.')

        if filesystem_id:
            LOG.info("Getting filesystem snapshot: '%s' details by fs_id: '%s'"
                     % (snapshot_name, filesystem_id))
            return self.rest_client.request(
                constants.GET,
                constants.GET_FILESYSTEM_DETAILS_BY_NAME_URL.format(
                    self.server_ip),
                querystring=helpers.prepare_querystring(
                    constants.SELECT_ALL_FILESYSTEM,
                    name=constants.EQUALS + snapshot_name,
                    parent_id=constants.EQUALS + filesystem_id))
        else:
            LOG.info("Getting filesystem snapshot: '%s' details by "
                     "nasserver id: '%s'" % (snapshot_name, nas_server_id))
            return self.provisioning.get_filesystem_by_name(
                filesystem_name=snapshot_name, nas_server_id=nas_server_id)

    def get_filesystem_snapshot_details(self, snapshot_id):
        """Get details of a particular filesystem snapshot.

        :param snapshot_id: Filesystem snapshot unique identifier
        :type snapshot_id: str
        :return: Filesystem snapshot details
        :rtype: dict
        """
        return self.provisioning.get_filesystem_details(
            filesystem_id=snapshot_id)

    def create_filesystem_snapshot(self, filesystem_id, **kwargs):
        """Create a snapshot of a file system.

        :param filesystem_id: File system unique identifier.
        :type filesystem_id: str
        :param kwargs: Other file system snapshot parameters. It includes
                       description, access_type and expiration_timestamp.
        :type kwargs: dict
        :return: The dict containing file system snapshot ID if successful
                 else error.
        :rtype: dict
        """
        LOG.info("Creating filesystem: '%s' snapshot with param: '%s'"
                 % (filesystem_id, kwargs))
        return self.rest_client.request(
            constants.POST, constants.CREATE_FILESYSTEM_SNAPSHOT_URL.format(
                self.server_ip, filesystem_id), payload=kwargs)

    def modify_filesystem_snapshot(self, snapshot_id, **kwargs):
        """Modify a snapshot of a file system.

        :param snapshot_id: File system unique identifier.
        :type snapshot_id: str
        :param kwargs: Other file system snapshot parameters. It includes
                       description and expiration_timestamp.
        :type kwargs: dict
        """
        LOG.info("Modifying filesystem snapshot: '%s' with param: '%s'"
                 % (snapshot_id, kwargs))
        return self.rest_client.request(
            constants.PATCH, constants.MODIFY_FILESYSTEM_URL.format(
                self.server_ip, snapshot_id), payload=kwargs)

    def delete_filesystem_snapshot(self, snapshot_id):
        """Delete a filesystem snapshot.

        :param snapshot_id: File system unique identifier.
        :type snapshot_id: str
        """
        LOG.info("Deleting filesystem snapshot: '%s'" % snapshot_id)
        return self.rest_client.request(constants.DELETE,
                                        constants.DELETE_FILESYSTEM_URL.
                                        format(self.server_ip, snapshot_id))
    # FS Snapshot Methods end

    @staticmethod
    def _prepare_create_modify_snapshot_payload(**kwargs):
        """Prepare a create/modify volume/volume group snapshot request body
        using provided arguments.

        :return: Request body.
        :rtype: dict
        """
        payload = dict()
        for argname in ('name', 'description', 'performance_policy_id',
                        'expiration_timestamp'):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload

    @staticmethod
    def _prepare_create_modify_snapshot_rule_payload(**kwargs):
        """Prepare a create/modify snapshot rule request body using provided
        arguments.

        :return: Request body.
        :rtype: dict
        """
        payload = dict()
        for argname in ('name', 'desired_retention', 'interval', 'time_of_day',
                        'days_of_week'):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload

    @staticmethod
    def _prepare_create_modify_protection_policy_payload(**kwargs):
        """Prepare a create/modify protection policy request body using
        provided arguments.

        :return: Request body.
        :rtype: dict
        """
        payload = dict()
        for argname in ('name', 'description', 'snapshot_rule_ids',
                        'replication_rule_ids', 'add_snapshot_rule_ids',
                        'remove_snapshot_rule_ids', 'add_replication_rule_ids',
                        'remove_replication_rule_ids'):
            if kwargs.get(argname) is not None:
                payload[argname] = kwargs[argname]
        return payload
