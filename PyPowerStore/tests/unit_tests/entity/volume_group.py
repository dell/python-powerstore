"""Mock volume_group Api for Volume Group Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class VolumeGroupResponse(Entity):
    """
    This class is used to handle Volume Group related responses.

    It provides methods to get volume groups, create volume groups, get volume group details,
    add members to volume groups, modify volume groups, delete volume groups, clone volume groups,
    refresh volume groups, and restore volume groups.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the VolumeGroupResponse object.

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

    def get_api_name(self):
        """
        Returns the name of the API based on the HTTP method and URL.

        Returns:
            function: The API function.
        """
        if self.method == "GET":
            if self.url.endswith("/volume_group"):
                if self.kwargs.get("params", {}).get("name"):
                    return self.get_volume_group_by_name
                return self.get_volume_group_list
            return self.get_volume_group_details
        if self.method == "POST":
            if self.url.endswith("/add_members"):
                return self.add_members_to_volume_group
            if self.url.endswith("/clone"):
                return self.clone_volume_group
            if self.url.endswith("/restore"):
                return self.restore_volume_group
            if self.url.endswith("/refresh"):
                return self.refresh_volume_group
            return self.create_volume_group
        if self.method == "PATCH":
            return self.modify_volume_group
        if self.method == "DELETE":
            return self.delete_volume_group
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

    def get_volume_group_list(self):
        """
        Returns a list of volume groups.

        Returns:
            tuple: A tuple containing the status code and the list of volume groups.
        """
        return self.status_code, self.data.volumegroup_list

    def get_volume_group_details(self):
        """
        Returns the details of a volume group.

        Returns:
            tuple: A tuple containing the status code and the volume group details.
        """
        return self.status_code, self.data.volume_group1

    def get_volume_group_by_name(self):
        """
        Returns a volume group by name.

        Returns:
            tuple: A tuple containing the status code and the volume group.
        """
        return self.status_code, [self.data.volume_group1]

    def create_volume_group(self):
        """
        Creates a new volume group.

        Returns:
            tuple: A tuple containing the status code and the volume group ID.
        """
        return 201, self.data.vg_id1

    def add_members_to_volume_group(self):
        """
        Adds members to a volume group.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "volume_ids" in self.kwargs["data"]
            and self.kwargs["data"]["volume_ids"][0] == self.data.invalid_vol_id
        ):
            return 404, self.data.volume_error[404]
        return 201, None

    def modify_volume_group(self):
        """
        Modifies a volume group.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        if (
            "protection_policy_id" in self.kwargs["data"]
            and self.kwargs["data"]["protection_policy_id"] == self.data.invalid_pol_id
        ):
            return 404, self.data.policy_error[404]
        return 204, None

    def delete_volume_group(self):
        """
        Deletes a volume group.

        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def clone_volume_group(self):
        """
        Clones a volume group.

        Returns:
            tuple: A tuple containing the status code and the volume group ID.
        """
        return self.status_code, self.data.vg_id2

    def refresh_volume_group(self):
        """
        Refreshes a volume group.

        Returns:
            tuple: A tuple containing the status code and the snapshot ID.
        """
        return self.status_code, self.data.snapshot_id

    def restore_volume_group(self):
        """
        Restores a volume group.

        Returns:
            tuple: A tuple containing the status code and the snapshot ID.
        """
        return self.status_code, self.data.snapshot_id
