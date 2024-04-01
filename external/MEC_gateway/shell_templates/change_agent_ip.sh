#!/bin/bash
# arg1: 连接名称, arg2: ipv4地址
# echo "Running $0"
# nmcli connection modify test ipv4.address 192.168.168.30/24
echo "kc304@KC304" | sudo su
sudo nmcli connection delete "$1"
sudo nmcli connection add type ethernet con-name "$1" ifname "$1" ip4 "$2"
sudo nmcli connection up "$1"