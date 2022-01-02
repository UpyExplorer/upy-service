# coding=utf-8

"""
Module Docstring
"""

from flask import Blueprint, jsonify
from app.api.decorators import BaseDecorator

mod_upy = Blueprint('', __name__, url_prefix='')


class UpyView(object):
    """
    BaseUpyView
    """
    def __init__(self):
        super().__init__()

    @mod_upy.route('/', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token
    def initial(data):
        return jsonify(
                {
                    "data": {
                        "status": "success",
                        "message": "Successful Request",
                        "limit": 1,
                        "total": 1
                    },
                    "result": None
                }
            ), 200
