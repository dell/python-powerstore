from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestNetwork(TestBase):
    def test_get_job_details(self):
        job_details = self.provisioning.get_job_details(self.data.job_id1)
        self.assertEqual(job_details, self.data.job_details)

    def test_get_invalid_job_details(self):
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.get_job_details,
            self.data.job_does_not_exist)
