"""Mock requests module for PowerStore Unit Tests"""

import json

from PyPowerStore.tests.unit_tests.entity.ads import AdsResponse
from PyPowerStore.tests.unit_tests.entity.appliance import ApplianceResponse
from PyPowerStore.tests.unit_tests.entity.certificate import CertificateResponse
from PyPowerStore.tests.unit_tests.entity.chap_config import ChapConfigResponse
from PyPowerStore.tests.unit_tests.entity.cluster import ClusterResponse
from PyPowerStore.tests.unit_tests.entity.discovered_appliances import (
    DiscoveredApplianceResponse,
)
from PyPowerStore.tests.unit_tests.entity.dns import DnsResponse
from PyPowerStore.tests.unit_tests.entity.email import EmailResponse
from PyPowerStore.tests.unit_tests.entity.file_dns import FileDNSResponse
from PyPowerStore.tests.unit_tests.entity.file_interface import FileInterfaceResponse
from PyPowerStore.tests.unit_tests.entity.file_nis import FileNISResponse
from PyPowerStore.tests.unit_tests.entity.file_system import FileSystemResponse
from PyPowerStore.tests.unit_tests.entity.host import HostResponse
from PyPowerStore.tests.unit_tests.entity.host_group import HostGroupResponse
from PyPowerStore.tests.unit_tests.entity.ip_pool_address import IPPoolAddressResponse
from PyPowerStore.tests.unit_tests.entity.ip_port import IPPortResponse
from PyPowerStore.tests.unit_tests.entity.job import JobResponse
from PyPowerStore.tests.unit_tests.entity.ldap import LdapResponse
from PyPowerStore.tests.unit_tests.entity.ldap_account import LDAPAccountResponse
from PyPowerStore.tests.unit_tests.entity.ldap_domain import LDAPDomainResponse
from PyPowerStore.tests.unit_tests.entity.local_user import LocalUserResponse
from PyPowerStore.tests.unit_tests.entity.nas_server import NASServerResponse
from PyPowerStore.tests.unit_tests.entity.network import NetworkResponse
from PyPowerStore.tests.unit_tests.entity.nfs_export import NFSExportResponse
from PyPowerStore.tests.unit_tests.entity.nfs_server import NFSServerResponse
from PyPowerStore.tests.unit_tests.entity.ntp import NtpResponse
from PyPowerStore.tests.unit_tests.entity.policy import PolicyResponse
from PyPowerStore.tests.unit_tests.entity.remote_support import RemoteSupportResponse
from PyPowerStore.tests.unit_tests.entity.remote_support_contact import (
    RemoteSupportContactResponse,
)
from PyPowerStore.tests.unit_tests.entity.remote_system import RemoteSystemResponse
from PyPowerStore.tests.unit_tests.entity.rep_rule import RepRuleResponse
from PyPowerStore.tests.unit_tests.entity.rep_session import RepSessionResponse
from PyPowerStore.tests.unit_tests.entity.replication_group import (
    ReplicationGroupResponse,
)
from PyPowerStore.tests.unit_tests.entity.role import RoleResponse
from PyPowerStore.tests.unit_tests.entity.security_config import SecurityConfigResponse
from PyPowerStore.tests.unit_tests.entity.service_config import ServiceConfigResponse
from PyPowerStore.tests.unit_tests.entity.service_user import ServiceUserResponse
from PyPowerStore.tests.unit_tests.entity.smb_server import SMBServerResponse
from PyPowerStore.tests.unit_tests.entity.smb_share import SMBShareResponse
from PyPowerStore.tests.unit_tests.entity.smtp_config import SmtpConfigResponse
from PyPowerStore.tests.unit_tests.entity.snap_rule import SnapRuleResponse
from PyPowerStore.tests.unit_tests.entity.snmp_server import SNMPServerResponse
from PyPowerStore.tests.unit_tests.entity.software_installed import SoftwareResponse
from PyPowerStore.tests.unit_tests.entity.storage_container import (
    StorageContainerResponse,
)
from PyPowerStore.tests.unit_tests.entity.storage_container_destination import (
    StorageContainerDestinationResponse,
)
from PyPowerStore.tests.unit_tests.entity.tree_quota import TreeQuotaResponse
from PyPowerStore.tests.unit_tests.entity.user_quota import UserQuotaResponse
from PyPowerStore.tests.unit_tests.entity.vcenter import VcenterResponse
from PyPowerStore.tests.unit_tests.entity.virtual_volume import VirtualVolumeResponse
from PyPowerStore.tests.unit_tests.entity.volume import VolumeResponse
from PyPowerStore.tests.unit_tests.entity.volume_group import VolumeGroupResponse

# map the entity class name with the url resource name
ENTITY_CLASS_MAPPING = {
    "volume": VolumeResponse,
    "volume_group": VolumeGroupResponse,
    "host_volume_mapping": HostResponse,
    "host": HostResponse,
    "host_group": HostGroupResponse,
    "policy": PolicyResponse,
    "snapshot_rule": SnapRuleResponse,
    "nas_server": NASServerResponse,
    "nfs_export": NFSExportResponse,
    "smb_share": SMBShareResponse,
    "file_system": FileSystemResponse,
    "file_tree_quota": TreeQuotaResponse,
    "file_user_quota": UserQuotaResponse,
    "replication_rule": RepRuleResponse,
    "replication_session": RepSessionResponse,
    "network": NetworkResponse,
    "software_installed": SoftwareResponse,
    "job": JobResponse,
    "vcenter": VcenterResponse,
    "virtual_volume": VirtualVolumeResponse,
    "ip_pool_address": IPPoolAddressResponse,
    "ip_port": IPPortResponse,
    "local_user": LocalUserResponse,
    "role": RoleResponse,
    "appliance": ApplianceResponse,
    "cluster": ClusterResponse,
    "service_user": ServiceUserResponse,
    "service_config": ServiceConfigResponse,
    "chap_config": ChapConfigResponse,
    "x509_certificate": CertificateResponse,
    "security_config": SecurityConfigResponse,
    "remote_system": RemoteSystemResponse,
    "file_ftp": AdsResponse,
    "file_ldap": LdapResponse,
    "email_notify_destination": EmailResponse,
    "smtp_config": SmtpConfigResponse,
    "dns": DnsResponse,
    "ntp": NtpResponse,
    "remote_support": RemoteSupportResponse,
    "remote_support_contact": RemoteSupportContactResponse,
    "ldap_domain": LDAPDomainResponse,
    "ldap_account": LDAPAccountResponse,
    "storage_container": StorageContainerResponse,
    "storage_container_destination": StorageContainerDestinationResponse,
    "replication_group": ReplicationGroupResponse,
    "discovered_appliance": DiscoveredApplianceResponse,
    "file_interface": FileInterfaceResponse,
    "smb_server": SMBServerResponse,
    "nfs_server": NFSServerResponse,
    "file_dns": FileDNSResponse,
    "file_nis": FileNISResponse,
    "snmp_server": SNMPServerResponse,
}


class FakeResponse:
    """
    A class used to simulate an HTTP response.
    """

    def __init__(self, data, status_code):
        """
        Initializes the FakeResponse object.

        Args:
        ----
        data (dict): The response data in JSON format.
        status_code (int): The status code of the HTTP response.
        """
        self.headers = {}
        self.reason = self.get_reason(status_code)
        self.status_code = status_code
        self.data = data

    @staticmethod
    def get_reason(status_code):
        """
        Returns the reason phrase for a given status code.

        Args:
        ----
        status_code (int): The status code of the HTTP response.

        Returns:
        -------
        str: The reason phrase for the given status code.
        """
        status_code_reason_mapping = {
            200: "OK",
            201: "Created",
            202: "Accepted",
            204: "No Content",
            206: "Partial Content",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            416: "Range Not Satisfiable",
            422: "Unprocessable Entity",
            500: "Internal Server Error",
            503: "Service Unavailable",
        }
        return status_code_reason_mapping.get(status_code, "OK")

    def json(self):
        """
        Returns the response data in JSON format.

        Returns:
        -------
        dict: The response data in JSON format.
        """
        return self.data


def get_entity_class(url):
    """
    Returns the entity class based on the given URL.

    Args:
    ----
    url (str): The URL for which the entity class is to be determined.

    Returns:
    -------
    str: The entity class corresponding to the given URL.
    """
    klass = ""
    url_split = url.split("/")
    if ENTITY_CLASS_MAPPING.get(url_split[-1]):
        # generic request .i.e. '/<entity>'
        klass = ENTITY_CLASS_MAPPING.get(url_split[-1])
    elif ENTITY_CLASS_MAPPING.get(url_split[-2]):
        # request for specific id. i.e. '/<entity>/{id}'
        klass = ENTITY_CLASS_MAPPING.get(url_split[-2])
    elif ENTITY_CLASS_MAPPING.get(url_split[-3]):
        # request for specific id. i.e. '/<entity>/{id}/clone'
        klass = ENTITY_CLASS_MAPPING.get(url_split[-3])
    return klass


def get_factory_obj(method, url, **kwargs):
    """
    Returns an object of the entity class based on the given URL.

    Args:
    ----
    method (str): The HTTP method.
    url (str): The URL for which the entity class object is to be created.
    **kwargs: Additional keyword arguments.

    Returns:
    -------
    object: An object of the entity class corresponding to the given URL.
    """
    klass = get_entity_class(url)
    obj = klass(method, url, **kwargs)
    return obj


def request(method, url, **kwargs):
    """
    Sends a request to the server and returns the response.

    Args:
    ----
    method (str): The HTTP method to use (e.g. GET, POST, PUT, DELETE).
    url (str): The URL of the request.
    **kwargs: Additional keyword arguments.

    Returns:
    -------
    FakeResponse: The response from the server.
    """
    if kwargs.get("data"):
        kwargs["data"] = json.loads(kwargs["data"])
    obj = get_factory_obj(method, url, **kwargs)
    api_name = obj.get_api_name()
    status_code, response = obj.execute_api(api_name)
    response = FakeResponse(response, status_code)
    return response
