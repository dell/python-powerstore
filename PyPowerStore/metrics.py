
from collections import namedtuple

from PyPowerStore.utils import constants, helpers

LOG = helpers.get_logger(__name__)


class MetricsFunctions:
    """Metric related functionality for PowerStore."""
    def __init__(self, provisioning, enable_log=False):
        """Initializes ProtectionFunctions Class

        :param provisioning: Provisioning class object
        :type provisioning: Provisioning
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        """
        self.provisioning = provisioning
        self.server_ip = provisioning.server_ip
        self.rest_client = provisioning.client
        global LOG # Reset LOG based on param
        LOG = helpers.get_logger(__name__, enable_log=enable_log)


    def get_performance_metrics(self, entity, entity_id, interval):
        """Get performance metrics for the given entity.

        entity: The entity to get metrics for see documentation for Entity
        class https://developer.dell.com/apis/3898/versions/{
        version}/reference/openapi.json/paths/~1metrics~1generate/post
        entity_id: The ID of the entity - str
        entity_id: The ID of the entity - str
        interval: The interval to get metrics for, Best_Available
                  Five_Sec, Twenty_Sec, Five_Mins, One_Hour, One_Day - str
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
