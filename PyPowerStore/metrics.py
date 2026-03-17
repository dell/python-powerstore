"""Metric related functionality for PowerStore."""

from PyPowerStore.utils import constants, helpers

LOG = helpers.get_logger(__name__)


class MetricsFunctions:
    """Metric related functionality for PowerStore.
    
    This class provides methods to retrieve performance metrics
    from PowerStore appliances.
    """
    def __init__(self, provisioning, enable_log=False):
        """Initializes MetricsFunctions Class

        :param provisioning: Provisioning class object
        :type provisioning: Provisioning
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        """
        self.provisioning = provisioning
        self.server_ip = provisioning.server_ip
        self.rest_client = provisioning.client
        global LOG  # Reset LOG based on param
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    def get_performance_metrics(self, entity, entity_id, interval):
        """Get performance metrics for the given entity.

        :param entity: The entity to get metrics for see documentation for Entity
        class https://developer.dell.com/apis/3898/versions/{
        version}/reference/openapi.json/paths/~1metrics~1generate/post
        :type entity: str
        :param entity_id: The ID of the entity
        :type entity_id: str
        :param interval: The interval to get metrics for, Best_Available
                  Five_Sec, Twenty_Sec, Five_Mins, One_Hour, One_Day
        :type interval: str
        :return: Performance metrics data
        :rtype: dict
        """
        payload = {
            "entity": entity,
            "entity_id": entity_id,
            "interval": interval
        }
        return self.rest_client.request(
                   constants.POST,
               constants.GET_PERFORMANCE_METRICS_URL.format(
                       self.server_ip),
               payload=payload
               )
