#!/bin/bash
#return: 网卡，连接方式，连接状态，连接名，ipv4地址
echo "kc304@KC304" | sudo -S su -c

if [ "$1" = "nmcli" ]; then
    nmcli device | awk 'NR>=2' | while read -r line
    do
      net_card=($line)
      ipv4_address=$(nmcli d show ${net_card[0]} | awk '$1=="IP4.ADDRESS[1]:" {print $2}')
      printf "%s\t    %s\n" "$line" "$ipv4_address"
      done
elif [ "$1" = "ifconfig" ]; then
    ifconfig
fi


