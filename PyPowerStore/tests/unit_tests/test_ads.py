from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestAds(TestBase):

    def test_get_ads(self):
        ads_list = self.provisioning.get_file_ads()
        self.assertListEqual(ads_list, self.ads_data.ads_list)
