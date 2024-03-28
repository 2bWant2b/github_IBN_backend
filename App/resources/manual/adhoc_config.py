from App.exts import Resource
from flask import request
from App.utils.param_config import param_config


class AdhocConfig(Resource):
    @classmethod
    def post(cls):
        json = request.get_json()
        name = json.pop("name")
        data = json
        param_config(name, data)
