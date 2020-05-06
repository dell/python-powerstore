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
from PyPowerStore.utils import constants

requests.packages.urllib3.disable_warnings()


# Codes
VALID_CODES = [200, 201, 202, 204, 206, 207]


class Client():
    """Client class for PowerStore"""
    def __init__(self, username, password, verify, application_type,
                 timeout=None):
        self.username = username
        self.password = password
        self.verify = verify
        self.application_type = application_type
        """Setting default timeout"""
        self.timeout = timeout if timeout else constants.TIMEOUT


    def request(self, http_method, url, payload=None, querystring=None):
        """Method which serves requests to PowerStore.
        """
        credentials = base64.b64encode(
            "{username}:{password}".format(username=self.username,
                                           password=self.password).encode()
        )

        headers = {
            'authorization': "Basic " + credentials.decode(),
            'content-type': "application/json",
            'Application-Type': self.application_type,
        }

        try:
            if payload is not None:
                response = requests.request(http_method, url,
                                            data=json.dumps(payload),
                                            headers=headers,
                                            verify=self.verify,
                                            timeout=self.timeout)

            elif querystring is not None:
                response = requests.request(http_method, url, headers=headers,
                                            params=querystring,
                                            verify=self.verify,
                                            timeout=self.timeout)
            else:
                response = requests.request(http_method, url, headers=headers,
                                            verify=self.verify,
                                            timeout=self.timeout)
            try:
                response_json = response.json()
            except ValueError:
                response_json = None
            if response.status_code in VALID_CODES:
                return response_json
            else:
                if response.status_code == 500:
                    error_msg = "PowerStore internal server error. Error " \
                                "details: " + \
                                str(response.json())
                elif response.status_code == 401:
                    error_msg = "Access forbidden: Authentication " \
                                "required."
                elif response.status_code == 403:
                    error_msg = "Not allowed - authorization failure. " \
                                "Error details: " + str(response.json())
                elif response.status_code == 404:
                    error_msg = "Requested resource not found. " \
                                "Error details: " + str(response.json())
                elif response.status_code == 405:
                    error_msg = "The HTTP method is not supported " \
                                "on that URL. Error details: " \
                                + str(response.json())
                elif response.status_code == 406:
                    error_msg = "Not acceptable - the server " \
                                "cannot satisfy the Accept: header " \
                                "in the request. Either the format " \
                                "or version requested is not supported. " \
                                "Error details: " + str(response.json())
                elif response.status_code == 415:
                    error_msg = "Invalid request Content-Type. " \
                                "Error details: " + str(response.json())
                elif response.status_code == 416:
                    error_msg = "Range Not Satisfiable. The client " \
                                "requested a starting offset " \
                                "(using the ?offset URL parameter, " \
                                "or the first value in Range header) " \
                                "that was larger than the number of " \
                                "instances in the queried result set. " \
                                "Error details: " + str(response.json())
                elif response.status_code == 422:
                    error_msg = "Request could not be completed. " \
                                "Error details: " + str(response.json())
                elif response.status_code == 503:
                    error_msg = "The service is temporarily " \
                                "unavailable. Error details: " + \
                                str(response.json())
                else:
                    error_msg = str(response.json())
                raise PowerStoreException(PowerStoreException.HTTP_ERR,
                                          "HTTP code: " +
                                          str(response.status_code) +
                                          ", " + response.reason +
                                          " [" + error_msg + "]")
        except socket.error as exception:
            raise PowerStoreException(PowerStoreException.SOCKET_ERR,
                                      str(exception))
        except SSLError as exception:
            raise PowerStoreException(PowerStoreException.SSL_ERROR,
                                      str(exception))
        except ConnectionError as exception:
            raise PowerStoreException(PowerStoreException.CONNECTION_ERROR,
                                      str(exception))
        except TooManyRedirects as exception:
            raise PowerStoreException(
                PowerStoreException.TOO_MANY_REDIRECTS_ERROR, str(exception))
        except Timeout as exception:
            raise PowerStoreException(PowerStoreException.TIMEOUT_ERROR,
                                      str(exception))
