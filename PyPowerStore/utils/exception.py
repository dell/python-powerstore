# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""PowerStore exceptions"""


class PowerStoreException(Exception):
    """Class for PowerStore exceptions"""
    HTTP_ERR = 1
    SOCKET_ERR = 2
    SSL_ERROR = 3
    CONNECTION_ERROR = 4
    TOO_MANY_REDIRECTS_ERROR = 5
    TIMEOUT_ERROR = 6
    VALUE_ERROR = 7

    def __init__(self, err_code, err_text, status_code=None):
        Exception.__init__(self)
        self.err_code = err_code
        self.err_text = err_text
        self.status_code = status_code

    def __str__(self):
        return self.err_text
