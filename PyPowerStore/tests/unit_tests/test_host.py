from PyPowerStore.utils import constants
from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException
import mock


class TestHost(TestBase):

    def test_get_hosts(self):
        host_list = self.provisioning.get_hosts()
        self.assertListEqual(host_list, self.data.host_list)

    def test_get_host_with_filter(self):
        querystring = {'name': 'ilike.*test*'}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client,
                               'request') as mock_request:
            self.provisioning.get_hosts(filter_dict=querystring,
                                        all_pages=True)
            mock_request.assert_called_with(
                constants.GET, constants.GET_HOST_LIST_URL.format(
                    self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring)

    def test_get_host_details(self):
        host = self.provisioning.get_host_details(self.data.host_id1)
        self.assertEqual(host, self.data.host1)

    def test_get_host_by_name(self):
        host = self.provisioning.get_host_by_name(self.data.host_name1)
        self.assertEqual(host, [self.data.host1])

    def test_create_host(self):
        host = self.provisioning.create_host(
            self.data.host_name1, os_type='Linux',
            initiators=[{"port_name": self.data.initiator1,
                         "port_type": "iSCSI"}])
        self.assertEqual(host, self.data.create_host)

    def test_modify_host(self):
        host = self.provisioning.modify_host(self.data.host_id1,
                                             description="modify host "
                                                         "description")
        self.assertIsNone(host)

    def test_add_invalid_initiator_to_host(self):
        self.assertRaises(PowerStoreException,
                          self.provisioning.add_initiators_to_host,
                          self.data.host_id1,
                          add_initiators=self.data.invalid_initiator)

    def test_remove_invalid_initiator_from_host(self):
        self.assertRaises(PowerStoreException,
                          self.provisioning.remove_initiators_from_host,
                          self.data.host_id1,
                          remove_initiators=[self.data.invalid_initiator[
                                                 'name']])

    def test_delete_host(self):
        host = self.provisioning.delete_host(self.data.host_id1)
        self.assertIsNone(host)
