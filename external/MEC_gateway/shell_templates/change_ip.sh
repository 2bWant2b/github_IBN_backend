#!/bin/bash
# arg1: 连接名称, arg2: ipv4地址
# echo "Running $0"
# nmcli connection modify test ipv4.address 192.168.168.30/24
nmcli connection modify "$1" ipv4.address "$2"
nmcli connection up "$1"