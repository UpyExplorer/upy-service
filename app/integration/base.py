# coding=utf-8

"""
Module Docstring
"""

import json
from requests import request, HTTPError
from app.integration.errors import ApiRequestError


class BaseIntegration(object):
    """Defines the basic functions for communicating with the API.
    """

    def __init__(self):
        """Initial Operations
        """
        self.url = None
        self.headers = None      
        self.params = None  
        self.token = None

        self.setup()

    def setup_url(self):
        """Setup URL
        """
        self.url = None

    def setup_headers(self):
        """Setup Headers
        """
        self.setup_headers = {'Content-Type': 'application/json'}

    def setup_params(self):
        """Setup Params
        """
        self.params = None

    def setup_token(self):
        """Setup Token
        """
        self.token = None

    def setup(self):
        """Setup
        """
        self.setup_url()
        self.setup_params() 
        self.setup_token()
        self.setup_headers()

    def make_get(self, url=None, params=None, headers=None):
        """Sends a GET request to the API.

        Args:
            url (str, optional): Defaults to None.
            params (dict, optional): Defaults to None.
            headers (dict, optional): Defaults to None.

        Returns:
            json: Data returned
        """

        if url is None:
            url = self.url

        if params is None:
            params = {}

        result = self.make_request(
            url=url,
            method='GET',
            params=params,
            headers=headers
        )

        return json.loads(result)

    def make_post(self, data, url=None, headers=None, params=None):
        """Sends a POST request to the API.

        Args:
            data (dict): [description]
            url (str, optional): Defaults to None.
            headers (dict, optional): Defaults to None.
            params (dict, optional): Defaults to None.

        Returns:
            json: Data returned
        """

        if url is None:
            url = self.url

        if params is None:
            params = self.params

        if headers is None:
            headers = self.headers

        result = self.make_request(
            url=url,
            method='POST',
            params=params,
            headers=headers,
            body=json.dumps(data)
        )

        return json.loads(result)
    
    def make_delete(self, url=None, headers=None):
        """Sends a DELETE request to the API.

        Args:
            url ([type], optional): Defaults to None.
            headers ([type], optional): Defaults to None.

        Returns:
            json: Data returned
        """
        if url is None:
            url = self.url
        
        if headers is None:
            headers = self.headers
            
            result = self.make_request(
                url=url,
                method='DELETE',
                headers=headers
            )
            
            return json.loads(result)

    def make_put(self, data, url=None, headers=None):
        """Sends a PUT request to the API.

        Returns:
            json: Data returned
        """
        if url is None:
            url = self.url

        if headers is None:
            headers = self.headers

        result = self.make_request(
            method='PUT',
            url=url,
            headers=headers,
            body=json.dumps(data)
        )

        return json.loads(result)

    def make_request(self, method, url, headers=None, params=None, body=None):
        """Sends a request to the API.

        Raises:
            ApiRequestError: [description]

        Returns:
            [type]: [description]
        """
        if headers is None:
            headers = self.headers

        if params is None:
            params = {}
        
        if body is None:
            body = ''

        kwargs = {
            'method': method,
            'url': url,
            'params': params,
            'headers': headers,
            'data': body
        }

        with request(**kwargs) as response:
            try:
                response.raise_for_status()

            except HTTPError as error:
                raise ApiRequestError(
                    url=error.request.url,
                    response_status=error.response.status_code,
                    response_body=error.response.text
                )
            return response.text
