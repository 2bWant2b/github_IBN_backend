from external.MEC_gateway.api.IBN_proxy_local import get_agent_info
import re


def get_topology():
    info = get_agent_info("ifconfig")
    network_cards = {}
    # 使用正则表达式匹配每个网卡信息块
    pattern = re.compile(r'(?P<card>\S+): flags=\d+<(?P<flags>[^>]*)>\s+mtu\s+\d+\s+(?P<other_info>.+?)\n(?=\S|$)',
                         re.DOTALL)
    matches = pattern.finditer(info)

    for match in matches:
        card = match.group('card')
        flags = match.group('flags')
        other_info = match.group('other_info')
        network_cards[card] = []

        if 'RUNNING' in flags.split(','):
            network_cards[card].append('on')
        else:
            network_cards[card].append('off')

        network_cards[card].append('none')
        match_ip = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', other_info)
        if match_ip:
            network_cards[card][1] = match_ip.group(1)

    topology = {"data": [
        {"name": "意图驱动代理", "x": 500, "y": 500},
        {"name": "自组织网设备1", "x": 700, "y": 600},  # enp8s0
        {"name": "自组织网设备2", "x": 800, "y": 600},  # enp10s0
        {"name": "集群网络设备", "x": 200, "y": 700},   # enp9s0
        {"name": "卫星网络设备", "x": 600, "y": 100}    # enp7s0

    ], "links": []}

    if network_cards["enp8s0"][0] == "on":
        topology["links"].append({"source": "意图驱动代理", "target": "自组织网设备1"})
    if network_cards["enp10s0"][0] == "on":
        topology["links"].append({"source": "意图驱动代理", "target": "自组织网设备2"})
    if network_cards["enp9s0"][0] == "on":
        topology["links"].append({"source": "意图驱动代理", "target": "集群网络设备"})
    if network_cards["enp7s0"][0] == "on":
        topology["links"].append({"source": "意图驱动代理", "target": "卫星网络设备"})

    return topology


if __name__ == "__main__":
    get_topology()
