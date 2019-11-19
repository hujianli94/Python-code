#!/usr/bin/env bash
#usage:xxx
#scripts_name:xxx.sh
# author：xiaojian
IP=$1
SOFT=$2
OS=$3
if [ -z `/usr/bin/nmap -p 22 $IP | grep open | awk '{print $1}'` ]; then
    exit 1
fi
if [ ! -z `/usr/bin/nmap -p 80 $IP | grep open | awk '{print $1}'` ]; then
    exit 2
fi
if [ ! -z `/usr/bin/nmap -p 3306 $IP | grep open | awk '{print $1}'` ]; then
     exit 3
fi
exit 0