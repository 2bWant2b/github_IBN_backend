from external.MEC_gateway.api.IBN_proxy_local import get_agent_info
import re


def get_topology():
    info = get_agent_info("nmcli")
    matches = re.findall(r'enp7s0\s+ethernet\s+connected\s+enp7s0\s+[\S]+', info)


    topology = {"data": [
        {"name": "意图驱动代理", "x": 500, "y": 500},
        {"name": "自组织网节点1", "x": 700, "y": 600},
        {"name": "自组织网节点1", "x": 800, "y": 600},
        {"name": "集群网络设备1", "x": 200, "y": 700},
        {"name": "卫星网络设备", "x": 600, "y": 100}

    ], "links": [{"source": "意图驱动代理", "target": "自组织网节点node40"},
                 {"source": "意图驱动代理", "target": "集群网络设备1"},
                 {"source": "意图驱动代理", "target": "卫星网络设备"},
                 ]}
    if matches != "192.168.30.1/32":
        topology = {"ok": "1"}

    print(topology)
    return topology


if __name__ == "__main__":
    get_topology()
