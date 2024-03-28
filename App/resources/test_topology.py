from ..exts import Resource
from ..utils.net_topology import *
from flask import request


class TestTopology(Resource):
    @classmethod
    def get(cls):
        return get_topology()
