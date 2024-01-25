from testtools import TestCase
from PyPowerStore.tests.unit_tests.mock_client import MockClient
from PyPowerStore.tests.unit_tests.config import PowerStoreConfig
from PyPowerStore.powerstore_conn import PowerStoreConn
from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.data.certificate_data import CertificateData
from PyPowerStore.tests.unit_tests.data.security_config_data import SecurityConfigData
from PyPowerStore.tests.unit_tests.data.remote_system_data import RemoteSystemData
from PyPowerStore.tests.unit_tests.data.ads_data import AdsData
from PyPowerStore.tests.unit_tests.data.ldap_data import LdapData
from PyPowerStore.tests.unit_tests.data.email_data import EmailData
from PyPowerStore.tests.unit_tests.data.smtp_config_data import SmtpConfigData
from PyPowerStore.tests.unit_tests.data.dns_data import DnsData
from PyPowerStore.tests.unit_tests.data.ntp_data import NtpData
from PyPowerStore.tests.unit_tests.data.remote_support_data import RemoteSupportData
from PyPowerStore.tests.unit_tests.data.remote_support_contact_data import RemoteSupportContactData
from PyPowerStore.tests.unit_tests.data.ldap_account_data import LdapAccountData
from PyPowerStore.tests.unit_tests.data.vcenter_data import VcenterData
from PyPowerStore.tests.unit_tests.data.virtual_volume_data import VirtualVolumeData
from PyPowerStore.tests.unit_tests.data.file_system_data import FileSystemData
from PyPowerStore.tests.unit_tests.data.storage_container_data import StorageContainerData
from PyPowerStore.tests.unit_tests.data.storage_container_destination_data import StorageContainerDestinationData
from PyPowerStore.tests.unit_tests.data.replication_group_data import ReplicationGroupData
from PyPowerStore.tests.unit_tests.data.discovered_appliances import DiscoveredApplianceData
from PyPowerStore.tests.unit_tests.data.file_interface_data import FileInterfaceData
from PyPowerStore.tests.unit_tests.data.smb_server_data import SMBServerData
from PyPowerStore.tests.unit_tests.data.nfs_server_data import NFSServerData
from PyPowerStore.tests.unit_tests.data.file_dns_data import FileDNSData
from PyPowerStore.tests.unit_tests.data.file_nis_data import FileNISData
from unittest import mock

class TestBase(TestCase):
    def setUp(self):
        super(TestBase, self).setUp()
        self.data = CommonData()
        self.certificate_data = CertificateData()
        self.security_config_data = SecurityConfigData()
        self.remote_system_data = RemoteSystemData()
        self.ads_data = AdsData()
        self.ldap_data = LdapData()
        self.email_data = EmailData()
        self.smtp_config_data = SmtpConfigData()
        self.dns_data = DnsData()
        self.ntp_data = NtpData()
        self.remote_support_data = RemoteSupportData()
        self.remote_support_contact_data = RemoteSupportContactData()
        self.ldap_account_data = LdapAccountData()
        self.storage_container_data = StorageContainerData()
        self.storage_container_destination_data = StorageContainerDestinationData()
        self.replication_group_data = ReplicationGroupData()
        self.vcenter_data = VcenterData()
        self.virtual_volume_data = VirtualVolumeData()
        self.file_system_data = FileSystemData()
        self.discovered_appliance_data = DiscoveredApplianceData()
        self.file_interface_data = FileInterfaceData()
        self.smb_server_data = SMBServerData()
        self.nfs_server_data = NFSServerData()
        self.file_dns_data = FileDNSData()
        self.file_nis_data = FileNISData()
        self.conf = PowerStoreConfig()
        self.mock_client = mock.patch('PyPowerStore.provisioning.Client',
                                      new=MockClient)
        self.mock_client = self.mock_client.start()
        self.conn = PowerStoreConn(
            self.conf.username, self.conf.password, self.conf.server_ip,
            verify=self.conf.verify, timeout=self.conf.timeout,
            application_type=self.conf.application_type,
            enable_log=self.conf.enable_log)
        self.provisioning = self.conn.provisioning
        self.protection = self.conn.protection
        self.configuration = self.conn.config_mgmt
        self.file_interface = self.conn.file_interface
        self.file_dns = self.conn.file_dns
        self.file_nis = self.conn.file_nis
        self.smb_server = self.conn.smb_server
        self.nfs_server = self.conn.nfs_server
