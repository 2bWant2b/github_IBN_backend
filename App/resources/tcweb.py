from ..exts import Resource
from external.MEC_gateway.api.IBN_proxy import tcweb_post
from flask import request


class Tcweb(Resource):
    @classmethod
    def post(cls):
        res = request.get_json()
        print(res)
        tcweb_post(res["device_ipv4"], res["dev"], *res["param"])


