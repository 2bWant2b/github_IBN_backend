from App.exts import Resource
from App.models.router import RouterModel
from flask import request
from external.MEC_gateway.api.IBN_proxy_local import change_agent_ip


class ChangeAgentIP(Resource):
    @classmethod
    def post(cls):
        json = request.get_json()
        device_id = json["device_id"]
        net_card = json["net_card"]
        ip = json["ip"]
        # try:
        #     device_ip = RouterModel.find_by_id(device_id).ip
        # except:
        #     return {"message": f"agent {device_id} not found."}, 404

        # shutdown_con(device_ip)
        # set_ip(device_ip, json["net_card"], json["ip"])
        change_agent_ip(net_card, ip)
