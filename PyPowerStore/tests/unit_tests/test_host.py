"""Unit Tests for Host"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestHost(TestBase):
    """
    Unit tests for Host
    """

    def test_get_hosts(self):
        """
        Test get hosts

        Validates that the host list retrieved from the provisioning matches the expected host list
        """
        host_list = self.provisioning.get_hosts()
        self.assertListEqual(host_list, self.data.host_list)

    def test_get_host_with_filter(self):
        """
        Test get host with filter

        Validates that the request to get hosts with a filter is sent with the correct querystring
        """
        querystring = {"name": "ilike.*test*"}
        querystring.update(constants.SELECT_ID_AND_NAME)
        with mock.patch.object(self.provisioning.client, "request") as mock_request:
            self.provisioning.get_hosts(filter_dict=querystring, all_pages=True)
            mock_request.assert_called_with(
                constants.GET,
                constants.GET_HOST_LIST_URL.format(self.provisioning.server_ip),
                all_pages=True,
                payload=None,
                querystring=querystring,
            )

    def test_get_host_details(self):
        """
        Test get host details

        Verifies that the host details retrieved from the provisioning match
        the expected host details
        """
        host = self.provisioning.get_host_details(self.data.host_id1)
        self.assertEqual(host, self.data.host1)

    def test_get_host_by_name(self):
        """
        Test get host by name

        Confirms that the host retrieved from the provisioning by name matches the expected host
        """
        host = self.provisioning.get_host_by_name(self.data.host_name1)
        self.assertEqual(host, [self.data.host1])

    def test_create_host(self):
        """
        Test create host

        Validates that the host created through the provisioning matches
        the expected host creation result
        """
        host = self.provisioning.create_host(
            self.data.host_name1,
            os_type="Linux",
            initiators=[{"port_name": self.data.initiator1, "port_type": "iSCSI"}],
        )
        self.assertEqual(host, self.data.create_host)

    def test_modify_host(self):
        """
        Test modify host

        Verifies that the response is None
        """
        host = self.provisioning.modify_host(
            self.data.host_id1, description="modify host description",
        )
        self.assertIsNone(host)

    def test_add_invalid_initiator_to_host(self):
        """
        Test add invalid initiator to host

        Validates that adding an invalid initiator to a host through the
        provisioning raises a PowerStoreException
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.add_initiators_to_host,
            self.data.host_id1,
            add_initiators=self.data.invalid_initiator,
        )

    def test_remove_invalid_initiator_from_host(self):
        """
        Test remove invalid initiator from host

        Confirms that removing an invalid initiator from a host through the
        provisioning raises a PowerStoreException
        """
        self.assertRaises(
            PowerStoreException,
            self.provisioning.remove_initiators_from_host,
            self.data.host_id1,
            remove_initiators=[self.data.invalid_initiator["name"]],
        )

    def test_delete_host(self):
        """
        Test delete host

        Verifies that the response is None
        """
        host = self.provisioning.delete_host(self.data.host_id1)
        self.assertIsNone(host)
