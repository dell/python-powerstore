"""Mock volume Api for Volume Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity
from PyPowerStore.utils import constants


class VolumeResponse(Entity):
    """
    This class is used to handle Volume related responses.

    It provides methods to get volume list, create volume, modify volume, 
    get volume details, get volume by name, map volume, unmap volume, 
    delete volume, create snapshot, clone volume, refresh volume, 
    restore volume, configure metro volume and end metro volume configuration.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the VolumeResponse object.

        Args:
            method (str): The HTTP method.
            url (str): The URL of the request.
            **kwargs: Additional keyword arguments.
        """
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.data = CommonData()
        self.status_code = 200

    def get_post_api_name(self):
        """
        Returns the API function name based on the POST request URL.

        Returns:
            function: The API function.
        """
        if self.url.endswith("/volume"):
            return self.create_volume
        if self.url.endswith("/attach"):
            return self.map_volume
        if self.url.endswith("/detach"):
            return self.unmap_volume
        if self.url.endswith("/snapshot"):
            return self.create_snap
        if self.url.endswith("/clone"):
            return self.clone_volume
        if self.url.endswith("/refresh"):
            return self.refresh_volume
        if self.url.endswith("/restore"):
            return self.restore_volume
        if self.url.endswith("/configure_metro"):
            return self.configure_metro_volume
        if self.url.endswith("/end_metro"):
            return self.end_volume_metro_config
        return None

    def get_api_name(self):
        """
        Returns the API function name based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "PATCH":
            return self.modify_volume
        if self.method == "POST":
            return self.get_post_api_name()

        if self.method == "GET":
            # its a GET request
            if self.url.endswith("/volume"):
                if self.kwargs.get("params", {}).get(
                    "select",
                ) == constants.FHP_VOLUME_DETAILS_QUERY.get("select"):
                    return self.get_volume_by_name
                return self.get_volume_list
            return self.get_volume_details
        if self.method == "DELETE":
            return self.delete_volume
        return None

    def execute_api(self, api_name):
        """
        Executes the API function and returns the result.

        Args:
            api_name (function): The API function to execute.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        status_code, response = api_name()
        return status_code, response

    def get_volume_list(self):
        """
        Returns the list of volumes.

        Returns:
            tuple: A tuple containing the status code and the list of volumes.
        """
        return self.status_code, self.data.volume_list

    def create_volume(self):
        """
        Creates a new volume.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 201, self.data.create_volume

    def get_volume_details(self):
        """
        Returns the details of a volume.

        Returns:
            tuple: A tuple containing the status code and the volume details.
        """
        return self.status_code, self.data.volume1

    def get_volume_by_name(self):
        """
        Returns the volume by name.

        Returns:
            tuple: A tuple containing the status code and the volume.
        """
        return self.status_code, [self.data.volume1]

    def modify_volume(self):
        """
        Modifies a volume.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "protection_policy_id" in self.kwargs["data"]
            and self.kwargs["data"]["protection_policy_id"] == self.data.invalid_pol_id
        ):
            return 404, self.data.policy_error[404]
        return 204, None

    def map_volume(self):
        """
        Maps a volume.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def unmap_volume(self):
        """
        Unmaps a volume.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def delete_volume(self):
        """
        Deletes a volume.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def create_snap(self):
        """
        Creates a snapshot.

        Returns:
            tuple: A tuple containing the status code and the volume snapshot.
        """
        return 200, self.data.create_vol_snap

    def clone_volume(self):
        """
        Clones a volume.

        Returns:
            tuple: A tuple containing the status code and the volume id.
        """
        return self.status_code, self.data.vol_id2

    def refresh_volume(self):
        """
        Refreshes a volume.

        Returns:
            tuple: A tuple containing the status code and the snapshot id.
        """
        return self.status_code, self.data.snapshot_id

    def restore_volume(self):
        """
        Restores a volume.

        Returns:
            tuple: A tuple containing the status code and the snapshot id.
        """
        return self.status_code, self.data.snapshot_id

    def configure_metro_volume(self):
        """
        Configures metro volume.

        Returns:
            tuple: A tuple containing the status code and the metro replication session id.
        """
        return 200, self.data.metro_replication_session_id

    def end_volume_metro_config(self):
        """
        Ends metro volume configuration.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
