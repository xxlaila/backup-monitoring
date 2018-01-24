#!/bin/bash
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/mysql/bin'
# mysql master or slave monitor
# MySQL details
# My.cnf catalog designated storage
MYSQL_ACCESS="/usr/local/zabbix/scripts/my.cnf"
MYSQL="$(which mysql)"
#MYSQL="$MYSQL_BIN --defaults-extra-file=$MYSQL_ACCESS --skip-column"
MYSQL_BIN="$MYSQL --defaults-extra-file=$MYSQL_ACCESS"
# Linux bin paths
ARGS=1
# No mysql access file to read login info from
if [ $# -ne "$ARGS" ];then
    echo "Please input one arguement:"
fi
case $1 in
  Slave_Running)
    slave_is=$(${MYSQL_BIN} -e 'show slave status\G'|egrep -E "\bSlave_.*_Running\b"|awk '{print $2}'|grep -c Yes)
    echo "$slave_is"
    ;;
  Seconds_Behind)
    result=$(${MYSQL_BIN} -e 'show slave status\G'|egrep "\bSeconds_Behind_Master\b"|awk '{print $2}')
    echo $result
    ;;
  *)
    echo "Usage:$0(Slave_Running|Seconds_Behind)"
    ;;
esac
