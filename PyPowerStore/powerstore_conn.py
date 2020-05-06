# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Module for establishing connection with PowerStore"""

from PyPowerStore.protection import ProtectionFunctions
from PyPowerStore.provisioning import Provisioning


class PowerStoreConn():
    """Class for establishing connection with PowerStore"""
    def __init__(self, username, password, server_ip, verify=False,
                 application_type=None, timeout=None):
        self.provisioning = Provisioning(server_ip, username, password,
                                         verify, application_type, timeout)
        self.protection = ProtectionFunctions(self.provisioning)
