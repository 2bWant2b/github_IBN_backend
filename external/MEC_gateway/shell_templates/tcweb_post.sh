#!/bin/bash
# arg1: 网卡名称, arg2: 参数名称, arg3: 参数值
echo "kc304@KC304" | sudo tc qdisc del dev "$1" root netem
echo "kc304@KC304" | sudo tc qdisc add dev "$1" root netem "${@:2}"
