# Copyright: (c) 2024, Dell Technologies

"""Module for establishing connection with PowerStore"""

from PyPowerStore.configuration import Configuration
from PyPowerStore.objects.file_dns import FileDNS
from PyPowerStore.objects.file_interface import FileInterface
from PyPowerStore.objects.file_nis import FileNIS
from PyPowerStore.objects.nfs_server import NFSServer
from PyPowerStore.objects.smb_server import SMBServer
from PyPowerStore.objects.snmp_server import SNMPServer
from PyPowerStore.protection import ProtectionFunctions
from PyPowerStore.provisioning import Provisioning


class PowerStoreConn:
    """Class for establishing connection with PowerStore"""

    def __init__(
        self,
        username,
        password,
        server_ip,
        verify=False,
        application_type=None,
        timeout=None,
        enable_log=False,
        port_no=None,
    ):
        """Initializes PowerStoreConn Class

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
        self.provisioning = Provisioning(
            server_ip,
            username,
            password,
            verify,
            application_type,
            timeout,
            enable_log=enable_log,
            port_no=port_no,
        )
        self.protection = ProtectionFunctions(self.provisioning, enable_log=enable_log)
        self.config_mgmt = Configuration(self.provisioning, enable_log=enable_log)
        self.file_interface = FileInterface(self.provisioning, enable_log=enable_log)
        self.smb_server = SMBServer(self.provisioning, enable_log=enable_log)
        self.nfs_server = NFSServer(self.provisioning, enable_log=enable_log)
        self.file_dns = FileDNS(self.provisioning, enable_log=enable_log)
        self.file_nis = FileNIS(self.provisioning, enable_log=enable_log)
        self.snmp_server = SNMPServer(self.provisioning, enable_log=enable_log)
