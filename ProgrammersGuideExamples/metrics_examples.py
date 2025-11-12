# Copyright: (c) 2025, Dell Technologies

"""Local User Operations"""

# pylint: disable=invalid-name,assignment-from-none,duplicate-code

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username="<username>",
    password="<password>",
    server_ip="<IP>",
    verify=False,
    application_type="<Application>",
    timeout=180.0,
)

pprint ((CONN.metrics.get_performance_metrics(
    entity="performance_metrics_by_appliance", entity_id="A1",
                                     interval="Five_Sec")))
