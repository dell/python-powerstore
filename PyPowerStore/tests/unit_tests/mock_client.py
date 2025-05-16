"""Mock Client for PowerStore Unit Tests"""

# pylint: disable=duplicate-code,too-many-arguments,too-many-positional-arguments,too-many-nested-blocks

import base64
import json

from PyPowerStore.tests.unit_tests import myrequests
from PyPowerStore.utils import constants

# from myrequests.exceptions import SSLError
# from myrequests.exceptions import ConnectionError
# from myrequests.exceptions import TooManyRedirects
# from myrequests.exceptions import Timeout
from PyPowerStore.utils.exception import PowerStoreException

VALID_CODES = [200, 201, 202, 204, 206, 207]


class MockClient:
    """
    Mock Client for PowerStore Unit Tests
    """
    def __init__(
        self,
        username,
        password,
        verify,
        application_type,
        timeout=None,
        enable_log=False,
    ):
        self.username = username
        self.password = password
        self.verify = verify
        self.application_type = application_type
        self.timeout = timeout
        self.enable_log = enable_log

    def fetch_response(
        self, http_method, url, payload=None, querystring=None, myrange=None,
    ):
        """Fetch & return the response based on request parameters.

        :param http_method: HTTP Method
        :type http_method: str
        :param url: Service Endpoint
        :type url: str
        :param payload: Request payload
        :type payload: dict
        :param querystring: Request querystring
        :type querystring: dict
        :param myrange: element's offset & limit. e.g. 100-199
        :type myrange: str

        :return: Request's response.
        :rtype: requests.models.Response object

        """
        credentials = base64.b64encode(
            f"{self.username}:{self.password}".encode(),
        )

        headers = {
            "authorization": "Basic " + credentials.decode(),
            "content-type": "application/json",
            "Application-Type": self.application_type,
        }

        if myrange:
            headers["Range"] = myrange

        if payload:
            response = myrequests.request(
                http_method,
                url,
                data=json.dumps(payload),
                headers=headers,
                verify=self.verify,
                timeout=self.timeout,
            )
        elif querystring:
            response = myrequests.request(
                http_method,
                url,
                headers=headers,
                params=querystring,
                verify=self.verify,
                timeout=self.timeout,
            )
        else:
            response = myrequests.request(
                http_method,
                url,
                headers=headers,
                verify=self.verify,
                timeout=self.timeout,
            )
        return response

    def is_valid_response(self, response):
        """Check whether response is valid or not

        :param response: Request's response.
        :type response: requests.models.Response

        :return: bool

        """
        if response.status_code in VALID_CODES:
            return True
        return False

    def get_total_size_from_content_range(self, content_range):
        """Extract & return total_size from content_range

        :param http_method: HTTP Method
        :type http_method: str

        :return: total_size
        :rtype: int
        """
        total_size = content_range.split("/")[-1]
        total_size = int(total_size)
        return total_size

    def raise_http_exception(self, response):
        """Raises PowerStoreException

        :param response: Request's response.
        :type response: requests.models.Response
        """
        if response.status_code == 500:
            error_msg = "PowerStore internal server error. Error details: " + str(
                response.json(),
            )
        elif response.status_code == 401:
            error_msg = "Access forbidden: Authentication required."
        elif response.status_code == 403:
            error_msg = "Not allowed - authorization failure. Error details: " + str(
                response.json(),
            )
        elif response.status_code == 404:
            error_msg = "Requested resource not found. Error details: " + str(
                response.json(),
            )
        elif response.status_code == 405:
            error_msg = (
                "The HTTP method is not supported on that URL. "
                "Error details: " + str(response.json())
            )
        elif response.status_code == 406:
            error_msg = (
                "Not acceptable - the server cannot satisfy the "
                "Accept: header in the request. Either the format "
                "or version requested is not supported. "
                "Error details: " + str(response.json())
            )
        elif response.status_code == 415:
            error_msg = "Invalid request Content-Type. Error details: " + str(
                response.json(),
            )
        elif response.status_code == 416:
            error_msg = (
                "Range Not Satisfiable. The client requested a "
                "starting offset (using the ?offset URL parameter, "
                "or the first value in Range header) that was "
                "larger than the number of instances in the queried "
                "result set. Error details: " + str(response.json())
            )
        elif response.status_code == 422:
            error_msg = "Request could not be completed. Error details: " + str(
                response.json(),
            )
        elif response.status_code == 503:
            error_msg = (
                "The service is temporarily unavailable. "
                "Error details: " + str(response.json())
            )
        else:
            error_msg = str(response.json())
        raise PowerStoreException(
            PowerStoreException.HTTP_ERR,
            "HTTP code: "
            + str(response.status_code)
            + ", "
            + response.reason
            + " ["
            + error_msg
            + "]",
        )

    def request(self, http_method, url, payload=None, querystring=None, all_pages=None):
        """Method which serves requests to PowerStore.

        :param http_method: HTTP Method
        :type http_method: str
        :param url: Service Endpoint
        :type url: str
        :param payload: (optional) Request payload
        :type payload: dict
        :param querystring: (optional) Request querystring
        :type querystring: dict
        :param all_pages: (optional) Indicates whether to return all available
                          entities on the storage system
        :type all_pages: If not given default is None, else bool
        :return: Request's response.
        :rtype: dict or list of dict
        """
        try:
            response = self.fetch_response(
                http_method, url, payload=payload, querystring=querystring,
            )

            try:
                if self.is_valid_response(response):
                    response_json = None
                    if response.status_code != 204:
                        response_json = response.json()

                    content_range = response.headers.get("content-range")
                    if all_pages and response.status_code == 206 and content_range:
                        # 'content-range': '0-99/789'
                        total_size = self.get_total_size_from_content_range(
                            content_range,
                        )
                        myranges = [
                            f"{i}-{i + constants.MAX_LIMIT}"
                            for i in range(
                                constants.OFFSET, total_size, constants.MAX_LIMIT,
                            )
                        ]
                        for myrange in myranges:
                            response = self.fetch_response(
                                http_method,
                                url,
                                payload=payload,
                                querystring=querystring,
                                myrange=myrange,
                            )
                            if self.is_valid_response(response):
                                response_json.extend(response.json())
                            else:
                                self.raise_http_exception(response)

                    return response_json
                self.raise_http_exception(response)
                return None
            except ValueError as ex:
                # its low-level or response level error caused by
                # response.json() and not in requests.exceptions
                error_msg = (
                    f"ValueError: '{ex!s}' for Method: '{http_method}' URL: '{url}'"
                    f" PayLoad: '{payload}' QueryString: '{querystring}'"
                )
                raise PowerStoreException(PowerStoreException.VALUE_ERROR, error_msg) from ex
        except Exception as err:
            raise err
