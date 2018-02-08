#!/bin/bash
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/mysql/bin'
# This script is mainly used to monitor mysql innodb
# Define the mysql environment variable
# zabbix version 3.2.9
MYSQL_ACCESS="/usr/local/zabbix/scripts/my.cnf"
MYSQL="$(which mysql)"
#MYSQL="$MYSQL_BIN --defaults-extra-file=$MYSQL_ACCESS --skip-column"
MYSQL_BIN="$MYSQL --defaults-extra-file=$MYSQL_ACCESS"
vars=$2
######
case $1 in
  mysql_status)
    result=$(${MYSQL_BIN} -e "show status like '%${vars}%';"|tail -1|awk '{print $2}')
    echo ${result}
    ;;
  var)
    result=$(${MYSQL_BIN} -e "show variables like '%${vars}%';"|tail -1|awk '{print $2}')
    echo ${result}
    ;;
esac
