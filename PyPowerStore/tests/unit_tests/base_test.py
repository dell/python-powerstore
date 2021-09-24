from testtools import TestCase
from PyPowerStore.tests.unit_tests.mock_client import MockClient
from PyPowerStore.tests.unit_tests.config import PowerStoreConfig
from PyPowerStore.provisioning import Client
from PyPowerStore.provisioning import Provisioning
from PyPowerStore.protection import ProtectionFunctions
from PyPowerStore.powerstore_conn import PowerStoreConn
from PyPowerStore.tests.unit_tests.common_data import CommonData

from unittest import mock

class TestBase(TestCase):
    def setUp(self):
        super(TestBase, self).setUp()
        self.data = CommonData()
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