# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Helper module for PowerStore"""


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
