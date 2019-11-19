#!/usr/bin/env bash
#usage:xxx
#scripts_name:xxx.sh
# author：xiaojian
IP=$1
SOFT=$2
OS=$3
COUNT=2
if [ ! -z `/usr/bin/nmap -p 80 $IP | grep open | awk '{print $1}'` ]; then
    COUNT=$[$COUNT - 1]
fi
if [ ! -z `/usr/bin/nmap -p 3306 $IP | grep open | awk '{print $1}'` ]; then
    COUNT=$[$COUNT - 1]
fi
exit $COUNT
