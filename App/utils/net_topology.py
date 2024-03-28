def get_topology():
    return {"data": [
        {"name": "意图驱动代理", "x": 500, "y": 500},
        {"name": "自组织网节点node40", "x": 700, "y": 600},
        {"name": "集群网络设备1", "x": 200, "y": 700},
        {"name": "卫星网络设备", "x": 600, "y": 100}

    ], "links": [{"source": "意图驱动代理", "target": "自组织网节点node40"},
                 {"source": "意图驱动代理", "target": "集群网络设备1"},
                 {"source": "意图驱动代理", "target": "卫星网络设备"},
                 ]}