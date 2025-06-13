"""Unit Tests for Auth Manager"""

import time
from unittest.mock import MagicMock, patch

import pytest
import requests

from PyPowerStore.client import AuthenticationManager


class TestAuthenticationManager:
    """
    Unit tests for Authentication Manager
    """

    @pytest.fixture
    def auth_manager(self):
        """
        Initializes an instance of AuthenticationManager for testing
        """
        return AuthenticationManager(
            username="test_user",
            password="test_password",
            verify=False,
            application_type="test_app",
            timeout=10,
        )

    def test_set_host(self, auth_manager):
        """
        Test set host

        Validates the host is set correctly
        """
        auth_manager.set_host("test_host")
        assert auth_manager.host == "test_host"

    def test_get_authorization(self, auth_manager):
        """
        Test get authorization

        Verifies the authorization header is generated correctly
        """
        auth_header = auth_manager.get_authorization()
        assert auth_header == {
            "authorization": "Basic dGVzdF91c2VyOnRlc3RfcGFzc3dvcmQ=",
        }

    def test_set_session_timeout_and_creation_time(self, auth_manager):
        """
        Test set session timeout and creation time

        Confirms the idle timeout and creation time are set from the login response
        """
        login_response_mock = MagicMock()
        login_response_mock.status_code = 200
        login_response_mock.json = MagicMock(return_value=[{"idle_timeout": 3600}])
        auth_manager.set_session_timeout_and_creation_time(login_response_mock)
        assert auth_manager.idle_timeout == 3600

    def test_is_session_alive(self, auth_manager):
        """
        Test is session alive

        Verifies the session is considered alive based on the creation time and idle timeout
        """
        auth_manager.creation_time = 1
        auth_manager.idle_timeout = 10
        with patch.object(time, "time", return_value=5):
            assert auth_manager.is_session_alive()

    def test_login(self, auth_manager):
        """
        Test login

        Validates the login method sets the dell_emc_token and cookie
        """
        with patch.object(requests, "request"):
            auth_manager.login()
            assert auth_manager.dell_emc_token is not None
            assert auth_manager.cookie is not None

    def test_get_token_and_cookie(self, auth_manager):
        """
        Test get token and cookie

        Verifies the get_token_and_cookie method returns the dell_emc_token and cookie
        """
        with patch.object(requests, "request"):
            auth_manager.login()
            tokens = auth_manager.get_token_and_cookie()
            assert tokens["DELL-EMC-TOKEN"] is not None
            assert tokens["Cookie"] is not None

    def test_logout_session(self, auth_manager):
        """
        Test logout session

        Confirms the logout_session method clears the dell_emc_token and cookie
        """
        with patch.object(requests, "request"):
            auth_manager.login()
            auth_manager.logout_session()
            assert auth_manager.dell_emc_token is None
            assert auth_manager.cookie is None
