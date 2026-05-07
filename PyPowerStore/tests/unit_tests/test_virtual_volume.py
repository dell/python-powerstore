"""Unit tests for Virtual Volume"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestVirtualVolume(TestBase):
    """
    Unit tests for Virtual Volume
    """

    def test_get_virtual_volumes(self):
        """
        Test Get Virtual Volumes

        Validates that the list of virtual volumes matches the expected list.
        """
        virtual_volume_list = self.configuration.get_virtual_volume_list()
        self.assertListEqual(
            virtual_volume_list, self.virtual_volume_data.virtual_volume_list,
        )
