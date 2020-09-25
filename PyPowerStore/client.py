# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Client module for PowerStore"""

import json
import base64
import socket
import requests
from requests.exceptions import SSLError
from requests.exceptions import ConnectionError
from requests.exceptions import TooManyRedirects
from requests.exceptions import Timeout
from PyPowerStore.utils.exception import PowerStoreException
from PyPowerStore.utils import constants, helpers

requests.packages.urllib3.disable_warnings()

# TODO: kept LOG as global for now will improve it to avoid overriding
LOG = helpers.get_logger(__name__)

# Codes
VALID_CODES = [200, 201, 202, 204, 206, 207]


class Client():
    """Client class for PowerStore"""
    def __init__(self, username, password, verify, application_type,
                 timeout=None, enable_log=False):
        """ Initializes Client Class

        :param username: array username
        :type username: str
        :param password: array password
        :type password: str
        :param verify: Whether the SSL cert will be verified
        :type verify: bool
        :param application_type: Application Type
        :type application_type: str
        :param timeout: (optional) How long to wait for the server to send data
                        before giving up
        :param enable_log: (optional) Whether to enable log or not
        :type enable_log: bool
        :type timeout: float
        """
        global LOG
        self.username = username
        self.password = password
        self.verify = verify
        self.application_type = application_type
        """Setting default timeout"""
        self.timeout = timeout if timeout else constants.TIMEOUT
        LOG = helpers.get_logger(__name__, enable_log=enable_log)

    def fetch_response(self, http_method, url, payload=None, querystring=None,
                       myrange=None):
        """ Fetch & return the response based on request parameters.

        :param http_method: HTTP Method
        :type http_method: str
        :param url: Service Endpoint
        :type url: str
        :param payload: (optional) Request payload
        :type payload: dict
        :param querystring: (optional) Request querystring
        :type querystring: dict
        :param myrange: (optional) element's offset & limit. e.g. 100-199
        :type myrange: str
        :return: Request's response.
        :rtype: requests.models.Response object
        """
        credentials = base64.b64encode(
            "{username}:{password}".format(
                username=self.username, password=self.password).encode())

        headers = {
            'authorization': "Basic " + credentials.decode(),
            'content-type': "application/json",
            'Application-Type': self.application_type,
        }

        LOG.debug("Request's http_method: '%s' url: '%s' payload: '%s' "
                  "querystring: '%s' myrange: '%s'"
                  % (http_method, url, payload, querystring, myrange))
        if myrange:
            headers["Range"] = myrange

        if payload:
            response = requests.request(
                http_method, url, data=json.dumps(payload), headers=headers,
                verify=self.verify, timeout=self.timeout)
        elif querystring:
            response = requests.request(
                http_method, url, headers=headers, params=querystring,
                verify=self.verify, timeout=self.timeout)
        else:
            response = requests.request(
                http_method, url, headers=headers, verify=self.verify,
                timeout=self.timeout)
        return response

    def is_valid_response(self, response):
        """ Check whether response is valid or not

        :param response: Request's response.
        :type response: requests.models.Response
        :return: bool
        """
        if response.status_code in VALID_CODES:
            return True
        return False

    def raise_http_exception(self, response):
        """ Raises PowerStoreException

        :param response: Request's response.
        :type response: requests.models.Response
        """
        if response.status_code == 500:
            error_msg = "PowerStore internal server error. Error " \
                        "details: " + str(response.json())
        elif response.status_code == 401:
            error_msg = "Access forbidden: Authentication required."
        elif response.status_code == 403:
            error_msg = "Not allowed - authorization failure. " \
                        "Error details: " + str(response.json())
        elif response.status_code == 404:
            error_msg = "Requested resource not found. " \
                        "Error details: " + str(response.json())
        elif response.status_code == 405:
            error_msg = "The HTTP method is not supported on that URL. " \
                        "Error details: " + str(response.json())
        elif response.status_code == 406:
            error_msg = "Not acceptable - the server cannot satisfy the " \
                        "Accept: header in the request. Either the format " \
                        "or version requested is not supported. " \
                        "Error details: " + str(response.json())
        elif response.status_code == 415:
            error_msg = "Invalid request Content-Type. " \
                        "Error details: " + str(response.json())
        elif response.status_code == 416:
            error_msg = "Range Not Satisfiable. The client requested a " \
                        "starting offset (using the ?offset URL parameter, " \
                        "or the first value in Range header) that was " \
                        "larger than the number of instances in the queried "\
                        "result set. Error details: " + str(response.json())
        elif response.status_code == 422:
            error_msg = "Request could not be completed. " \
                        "Error details: " + str(response.json())
        elif response.status_code == 503:
            error_msg = "The service is temporarily unavailable. "\
                        "Error details: " + str(response.json())
        else:
            error_msg = str(response.json())
        LOG.error(error_msg)
        raise PowerStoreException(PowerStoreException.HTTP_ERR,
                                  "HTTP code: " +
                                  str(response.status_code) +
                                  ", " + response.reason +
                                  " [" + error_msg + "]",
                                  str(response.status_code))

    def get_total_size_from_content_range(self, content_range):
        """ Extract & return total_size from content_range

        :param http_method: HTTP Method
        :type http_method: str
        :return: total_size
        :rtype: int
        """
        total_size = content_range.split("/")[-1]
        total_size = int(total_size)
        return total_size

    def request(self, http_method, url, payload=None, querystring=None,
                all_pages=None):
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
                http_method, url, payload=payload, querystring=querystring)
            try:
                if self.is_valid_response(response):
                    response_json = None
                    if response.status_code != 204:
                        response_json = response.json()
                    # check 'all_pages' required, response received is
                    # partial(code 206) and contains info about total size of
                    # the collection
                    content_range = response.headers.get('content-range')
                    if all_pages and response.status_code == 206 and\
                       content_range:
                        # 'content-range': '0-99/789'
                        total_size = self.get_total_size_from_content_range(
                                         content_range)
                        myranges = [
                            "{0}-{1}".format(i, i + constants.MAX_LIMIT)
                            for i in range(constants.OFFSET, total_size,
                                           constants.MAX_LIMIT)]
                        for myrange in myranges:
                            response = self.fetch_response(
                                http_method, url, payload=payload,
                                querystring=querystring, myrange=myrange)
                            if self.is_valid_response(response):
                                response_json.extend(response.json())
                            else:
                                self.raise_http_exception(response)

                    return response_json
                else:
                    self.raise_http_exception(response)

            except ValueError as ex:
                # its low-level or response level error caused by
                # response.json() and not in requests.exceptions
                error_msg = "ValueError: '{0}' for Method: '{1}' URL: '{2}'"\
                    " PayLoad: '{3}' QueryString: '{4}'".format(
                        str(ex), http_method, url, payload, querystring)
                LOG.error(error_msg)
                raise PowerStoreException(PowerStoreException.VALUE_ERROR,
                                          error_msg)
        except socket.error as exception:
            LOG.error(str(exception))
            raise PowerStoreException(PowerStoreException.SOCKET_ERR,
                                      str(exception))
        except SSLError as exception:
            LOG.error(str(exception))
            raise PowerStoreException(PowerStoreException.SSL_ERROR,
                                      str(exception))
        except ConnectionError as exception:
            LOG.error(str(exception))
            raise PowerStoreException(PowerStoreException.CONNECTION_ERROR,
                                      str(exception))
        except TooManyRedirects as exception:
            LOG.error(str(exception))
            raise PowerStoreException(
                PowerStoreException.TOO_MANY_REDIRECTS_ERROR, str(exception))
        except Timeout as exception:
            LOG.error(str(exception))
            raise PowerStoreException(PowerStoreException.TIMEOUT_ERROR,
                                      str(exception))
