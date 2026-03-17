"""Unit Tests for Metrics"""

from PyPowerStore.tests.unit_tests.base_test import TestBase


class TestMetrics(TestBase):
    """Unit Tests for Metrics"""

    def test_metrics(self):
        """Unit test for metrics"""
        metric_result = self.metrics.get_performance_metrics(
            entity="performance_metrics_by_appliance", entity_id="A1",
            interval="Five_Sec")
        self.assertIsNotNone(metric_result)
