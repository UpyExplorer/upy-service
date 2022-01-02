# coding=utf-8

"""
Module Docstring
"""

from flask import current_app as app
from flask import request, jsonify
from functools import wraps


class BaseDecorator(object):
    """ 
    BaseDecorator
    """

    def validate_token(f):
        @wraps(f)
        def decorated(data, *args, **kwargs):

            if data['access_token'] == app.config['SECRET_KEY']:
                return f(data, *args, **kwargs)

            return jsonify(
                {
                    "data": {
                        "status": "fail",
                        "message": "Permission Denied",
                        "limit": 1,
                        "total": 1
                    },
                    "result": None
                }), 401
        
        return decorated

    def system(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            body = request.data.decode("UTF-8")
            params = request.args.to_dict(flat=False)
            access_token = request.headers.get('access_token', None)

            data = {
                "body": body,
                "params": params,
                "access_token": access_token
            }

            return f(data, *args, **kwargs)
        
        return decorated