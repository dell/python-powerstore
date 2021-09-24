# -*- coding: utf-8 -*-
# Copyright: (c) 2019-2021, Dell EMC

"""Helper module for PowerStore"""
import logging
from pkg_resources import parse_version

provisioning_obj = None


def set_provisioning_obj(val):
    global provisioning_obj
    provisioning_obj = val


def prepare_querystring(*query_arguments, **kw_query_arguments):
    """Prepare a querystring dict containing all query_arguments and
    kw_query_arguments passed.

    :return: Querystring dict.
    :rtype: dict
    """
    querystring = dict()
    for argument_dict in query_arguments:
        if isinstance(argument_dict, dict):
            querystring.update(argument_dict)
    querystring.update(kw_query_arguments)
    return querystring


def get_logger(module_name, enable_log=False):
    """Return a logger with the specified name

    :param module_name: Name of the module
    :type module_name: str
    :param enable_log: (optional) Whether to enable log or not
    :type enable_log: bool
    :return: Logger object
    :rtype: logging.Logger
    """
    LOG = logging.getLogger(module_name)
    LOG.setLevel(logging.DEBUG)
    if enable_log:
        LOG.disabled = False
    else:
        LOG.disabled = True
    return LOG


def is_foot_hill_or_higher():
    """Return a true if the array version is foot hill or higher.

    :return: True if foot hill or higher
    :rtype: bool
    """
    foot_hill_version = '2.0.0.0'
    array_version = provisioning_obj.get_array_version()
    if array_version and (
            parse_version(array_version) >= parse_version(foot_hill_version)):
        return True
    return False


def filtered_details(filterable_keys, filter_dict, resource_list,
                     resource_name):
    """
    Get the filtered output.
    :filterable_keys: Keys on which filters are supported.
    :type filterable_keys: list
    :filter_dict: Dict containing the filters, operators and value.
    :type filter_dict: dict
    :resource_list: The response of the REST api call on which
                    filter_dict is to be applied.
    :type resource_list: list
    :resource_name: Name of the resource
    :type resource_name: str
    :return: Dict, containing filtered values.
    :rtype: dict
    """
    err_msg = "Entered key {0} is not supported for filtering. " \
              "For {1}, filters can be applied only on {2}. "
    response = list()

    for resource in resource_list:
        count = 0
        for key in filter_dict:
            # Check if the filters can be applied on the key or not
            if key not in filterable_keys:
                raise Exception(err_msg.format(
                    key, resource_name, str(filterable_keys)))
            count = apply_operators(filter_dict, key, resource, count)
            if count == len(filter_dict):
                temp_dict = dict()
                temp_dict['id'] = resource['id']
                # check if resource has 'name' parameter or not.
                if resource_name not in ["CHAP config", "service config"]:
                    temp_dict['name'] = resource['name']
                response.append(temp_dict)
    return response


def apply_operators(filter_dict, key, resource, count):
    """
    Returns the count for the filters applied on the keys
    """
    split_list = filter_dict[key].split(".")
    if split_list[0] == 'eq' and str(resource[key]) == str(split_list[1]):
        count += 1
    elif split_list[0] == 'neq' and str(resource[key]) != str(split_list[1]):
        count += 1
    elif split_list[0] == 'ilike':
        if not isinstance(resource[key], str):
            raise Exception('like can be applied on string type'
                            ' parameters only. Please enter a valid operator'
                            ' and parameter combination')
        search_val = split_list[1].replace("*", "")
        value = resource[key]
        if split_list[1].startswith("*") and \
                split_list[1].endswith("*") and \
                value.count(search_val) > 0:
            count += 1
        elif split_list[1].startswith("*") and \
                value.endswith(search_val):
            count += 1
        elif value.startswith(search_val):
            count += 1
    elif split_list[0] == 'gt':
        if not isinstance(resource[key], (int, float)):
            raise Exception('greater can be applied on int type'
                            ' parameters only. Please enter a valid operator'
                            ' and parameter combination')
        if isinstance(resource[key], int) and\
                int(split_list[1]) < resource[key]:
            count += 1
        if isinstance(resource[key], float) and \
                float(split_list[1]) < resource[key]:
            count += 1
    elif split_list[0] == 'lt':
        if not isinstance(resource[key], (int, float)):
            raise Exception('lesser can be applied on int type'
                            ' parameters only. Please enter a valid operator'
                            ' and parameter combination')
        if isinstance(resource[key], int) and\
                int(split_list[1]) > resource[key]:
            count += 1
        if isinstance(resource[key], float) and \
                float(split_list[1]) > resource[key]:
            count += 1
    return count
