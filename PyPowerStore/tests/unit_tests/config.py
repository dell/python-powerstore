"""Configuration for unit tests"""

# pylint: disable=too-few-public-methods

class PowerStoreConfig:
    """
    Configuration class for PowerStore.

    This class holds the configuration parameters for the PowerStore connection.
    """
    username = "user"
    password = "pass"
    server_ip = "1.1.1.1"
    verify = False
    application_type = None
    timeout = None
    enable_log = False
