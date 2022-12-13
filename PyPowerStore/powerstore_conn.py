# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell Technologies

"""Module for establishing connection with PowerStore"""

from PyPowerStore.protection import ProtectionFunctions
from PyPowerStore.provisioning import Provisioning
from PyPowerStore.configuration import Configuration


class PowerStoreConn():
    """Class for establishing connection with PowerStore"""
    def __init__(self, username, password, server_ip, verify=False,
                 application_type=None, timeout=None, enable_log=False,
                 port_no=None):
        """ Initializes PowerStoreConn Class

        :param username: array username
        :type username: str
        :param password: array password
        :type password: str
        :param server_ip: The array IP
        :type server_ip: str
        :param port_no: The port number
        :type port_no: int
        :param verify: (optional) Whether the SSL cert will be verified
        :type verify: bool
        :param application_type: (optional) Application Type
        :type application_type: str
        :param timeout: (optional) How long to wait for the server to send data
                        before giving up
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        :type timeout: float
        """
        self.provisioning = Provisioning(server_ip, username, password,
                                         verify, application_type, timeout,
                                         enable_log=enable_log,
                                         port_no=port_no)
        self.protection = ProtectionFunctions(self.provisioning,
                                              enable_log=enable_log)
        self.config_mgmt = Configuration(self.provisioning,
                                         enable_log=enable_log)