#!/bin/bash
# arg1: 连接名称
echo "running $0"
# nmcli connection delete test
nmcli connection delete "$1"