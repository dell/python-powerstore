# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Helper module for PowerStore"""
import logging


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
