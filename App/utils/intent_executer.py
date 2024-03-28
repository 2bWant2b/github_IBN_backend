from pytorch_models.api.basic_api import text_to_intention
from external.MEC_gateway.api.IBN_proxy import *
from ..models.router import RouterModel
from ..utils.param_config import param_config


def intent_execute(user_text):
    intent_dic = text_to_intention(user_text)
    if intent_dic is None:
        return "意图获取失败！"
    intent = intent_dic["intent"]
    if intent == "set_ip":
        device_id = intent_dic["kwargs"]["device_id"]
        device_ipv4 = RouterModel.find_by_id(device_id).ip
        net_card = intent_dic["kwargs"]["net_card"]
        con_type = "ethernet"
        ip_v4 = intent_dic["kwargs"]["ipv4_address"]+"/24"
        set_ip(device_ipv4, "connection1", net_card, con_type, ip_v4)
        return f"{device_id}号意图驱动代理的{net_card}网卡的ip已被设置为{ip_v4}"
    elif intent == "get_net_info":
        device_id = intent_dic["kwargs"]["device_id"]
        device_ipv4 = RouterModel.find_by_id(device_id).ip
        net_info = get_brief_net_info(device_ipv4)
        return net_info
    elif intent == "shutdown_con":
        device_id = intent_dic["kwargs"]["device_id"]
        device_ipv4 = RouterModel.find_by_id(device_id).ip
        con_name = intent_dic["kwargs"]["con_name"]
        shutdown_con(device_ipv4, con_name)
        return f"{device_id}号意图驱动代理的{con_name}连接已关闭"
    elif intent == "config":
        device_name = intent_dic["kwargs"]["device_name"]
        data = {
            intent_dic["kwargs"]["param"]: intent_dic["kwargs"]["value"]
        }
        param_config(device_name, data)
        return "配置已修改"
