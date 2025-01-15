from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestVirtualVolume(TestBase):

    def test_get_virtual_volumes(self):
        virtual_volume_list = self.configuration.get_virtual_volume_list()
        self.assertListEqual(
            virtual_volume_list, self.virtual_volume_data.virtual_volume_list,
        )
