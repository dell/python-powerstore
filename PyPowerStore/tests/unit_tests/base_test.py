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
