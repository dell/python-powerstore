"""Unit tests for Job"""

# pylint: disable=no-member, unused-import

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils.exception import PowerStoreException


class TestJob(TestBase):
    """
    Unit tests for Job
    """

    def test_get_job_details(self):
        """
        Test get job details
        
        Validates that the returned job details matches the expected job details
        """
        job_details = self.provisioning.get_job_details(self.data.job_id1)
        self.assertEqual(job_details, self.data.job_details)

    def test_get_invalid_job_details(self):
        """
        Test get invalid job details
        
        Verifies that an exception is raised when trying to get details of an invalid job
        """
        self.assertRaisesRegex(
            PowerStoreException,
            "HTTP code: 404, Not Found",
            self.provisioning.get_job_details,
            self.data.job_does_not_exist,
        )
