"""Unit Tests for Host"""

from unittest import mock

from PyPowerStore.tests.unit_tests.base_test import TestBase
from PyPowerStore.utils import constants
from PyPowerStore.utils.exception import PowerStoreException


class TestMetrics(TestBase):
    """Unit Tests for Metrics"""

    def test_metrics(self):
        """Unit test for metrics"""
        metric_result = self.metrics.get_performance_metrics(
            entity="performance_metrics_by_appliance", entity_id="A1",
            interval="Five_Sec")
        self.asssertIsNotNone(metric_result)
