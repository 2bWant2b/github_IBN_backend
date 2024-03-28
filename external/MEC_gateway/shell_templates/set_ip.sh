#!/bin/bash
#arg1: 连接名称, arg2:网卡名称, arg3: 连接方式, arg4: ipv4地址
echo "running $0"
#nmcli connection add con-name test ifname enp9s0 type ethernet ipv4.method manual ipv4.addresses 192.168.168.199/24
nmcli connection add con-name "$1" ifname "$2" type "$3" ipv4.method manual ipv4.addresses "$4"
nmcli connection up test
