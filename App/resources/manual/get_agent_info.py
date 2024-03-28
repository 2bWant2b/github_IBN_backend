from App.exts import Resource
from flask import request
from external.MEC_gateway.api.IBN_proxy_local import get_agent_info
from App.models.router import RouterModel


class GetAgentInfo(Resource):
    @classmethod
    def post(cls):
        # json = request.get_json()
        # device_id = json["device_id"]
        # try:
        #     device_ip = RouterModel.find_by_id(device_id).ip
        # except:
        #     return {"message": f"agent {device_id} not found."}, 404

        info = get_agent_info()
        return {"message": [info]}
