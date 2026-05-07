"""Mock rep_session Api for Replication Session Unit Tests"""

# pylint: disable=too-many-return-statements,duplicate-code

from PyPowerStore.tests.unit_tests.data.common_data import CommonData
from PyPowerStore.tests.unit_tests.entity.base_abstract import Entity


class RepSessionResponse(Entity):
    """
    This class is used to handle Replication Session related responses.
    
    It provides methods to get replication sessions, get replication session details,
    sync replication session, pause replication session, resume replication session,
    failover replication session, reprotect replication session, and modify replication session.
    """

    def __init__(self, method, url, **kwargs):
        """
        Initializes the RepSessionResponse object.
        
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
            if self.url.endswith("/replication_session"):
                return self.get_replication_sessions
            return self.get_replication_session_details
        if self.method == "POST":
            if self.url.endswith("/sync"):
                return self.sync_replication_session
            if self.url.endswith("/pause"):
                return self.pause_replication_session
            if self.url.endswith("/resume"):
                return self.resume_replication_session
            if self.url.endswith("/failover"):
                return self.failover_replication_session
            if self.url.endswith("/reprotect"):
                return self.reprotect_replication_session
        elif self.method == "PATCH":
            return self.modify_replication_session
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

    def get_replication_sessions(self):
        """
        Returns a list of replication sessions.
        
        Returns:
            tuple: A tuple containing the status code and the list of replication sessions.
        """
        return self.status_code, self.data.rep_session_list

    def get_replication_session_details(self):
        """
        Returns the details of a replication session.
        
        Returns:
            tuple: A tuple containing the status code and the replication session details.
        """
        if self.url.endswith(
            f"/replication_session/{self.data.nas_id_not_exist}",
        ):
            return 404, self.data.rep_session_error[404]
        return 200, self.data.rep_session_details_1

    def sync_replication_session(self):
        """
        Synchronizes the replication session.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def pause_replication_session(self):
        """
        Pauses the replication session.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def resume_replication_session(self):
        """
        Resumes the replication session.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def failover_replication_session(self):
        """
        Fails over the replication session.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        data = self.kwargs.get("data", {})
        param = list(data.keys())
        if set(param) - set(self.data.rep_session_valid_param):
            # invalid param given
            return 400, self.data.rep_session_error[400]
        if self.url.endswith(
            f"/replication_session/{self.data.rep_session_id_not_exist}",
        ):
            return 404, self.data.rep_session_error[404]
        return 204, None

    def reprotect_replication_session(self):
        """
        Reprotects the replication session.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None

    def modify_replication_session(self):
        """
        Modifies the replication session.
        
        Returns:
            tuple: A tuple containing the status code and the response.
        """
        return 204, None
