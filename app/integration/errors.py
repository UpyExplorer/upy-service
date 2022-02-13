# coding=utf-8

"""
Module Docstring
"""

__all__ = ['ApiRequestError']


class ApiRequestError(Exception):
    """
    Definition of communication errors with an API.
    """

    def __init__(self, url, response_status, response_body):
        message = 'url=%s, response_status=%s, response_body=%s' \
            % (url, response_status, response_body)

        self.url = url
        self.response_status = response_status
        self.response_body = response_body

        super(Exception, self).__init__(message)
