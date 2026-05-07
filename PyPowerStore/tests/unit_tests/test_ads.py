"""Unit tests for Ads."""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestAds(TestBase):
    """
    Unit tests for ads.
    """

    def test_get_ads(self):
        """
        Test get ads.

        Validates that ads are successfully retrieved.
        """
        ads_list = self.provisioning.get_file_ads()
        self.assertListEqual(ads_list, self.ads_data.ads_list)
