import re


def text_to_intention(text):
    """将前端输入的文本转化为抽象意图与意图参数"""
    pattern = r'^将1号意图驱动代理的enp9s0网卡的ip设置为'
    pattern2 = r'节点(\w+).*?的(\w+).*?修改为(\d+)'
    matched_text1 = re.search(pattern, text)
    matched_text2 = re.search(pattern2, text)
    if matched_text1:
        ip_pattern = "(?:(?:1[0-9][0-9]\.)|(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))"
        matched_ips = re.findall(ip_pattern, text)
        intent = "set_ip"
        semantic_slot = {
            "device_type": "意图驱动代理",
            "device_id": "1",
            "net_card": "enp9s0",
            "ipv4_address": matched_ips[0]
        }
        intention_dic = {
            "intent": intent,
            "kwargs": semantic_slot
        }
        return intention_dic
    elif text == "查看1号意图驱动代理的网络信息":
        intent = "get_net_info"
        semantic_slot = {
            "device_type": "意图驱动代理",
            "device_id": "1",
        }
        intention_dic = {
            "intent": intent,
            "kwargs": semantic_slot
        }
        return intention_dic
    elif text == "关闭1号意图驱动代理的connection1连接":
        intent = "shutdown_con"
        semantic_slot = {
            "device_type": "意图驱动代理",
            "device_id": "1",
            "con_name": "connection1"
        }
        intention_dic = {
            "intent": intent,
            "kwargs": semantic_slot
        }
        return intention_dic
    # elif text == "将自组织网节点node40的音频麦克风增益修改为50":
    elif matched_text2:
        device_name = matched_text2.group(1)
        param = matched_text2.group(2)
        value = int(matched_text2.group(3))
        intent = "config"
        param_dic = {
            "音频麦克风增益": "audioMicGain",
            "天线1的发射功率衰减值": "pwAtten1",
            "天线2的发射功率衰减值": "pwAtten2",
            "RS485波特率": "baudrateRs485",
            "串口0的波特率": "uartBaudrate0",
            "串口1的波特率": "uartBaudrate1",
            "串口2的波特率": "uartBaudrate2",
        }
        semantic_slot = {
            "device_type": "AdHoc",
            "device_name": device_name,
            "param": param_dic[param],
            "value": value
        }
        intention_dic = {
            "intent": intent,
            "kwargs": semantic_slot
        }
        return intention_dic
    else:
        return None
