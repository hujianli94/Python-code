#!/usr/bin/env bash
#usage:xxx
#scripts_name:xxx.sh
# author：xiaojian
IP=$1
SOFT=$2
OS=$3

ssh root@$IP "yum -y install httpd mysql mysql-server php php-mysql php-mbstring php-mcrypt php-xml php-xmlrpc php-gd"
ssh root@$IP "/sbin/chkconfig httpd on; /bin/sleep 1 && /sbin/chkconfig mysqld on; /bin/sleep 1 && /sbin/service httpd start; /bin/sleep 1 && /sbin/service mysqld start"