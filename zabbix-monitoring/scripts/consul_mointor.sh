#!/bin/bash
# consul unit price simple installation script
# data: 2018-03-08
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/mysql/bin'
CONSUL="$(which consul)"
CURL="$(which curl)"
IP=`ifconfig |sed -n 2p |awk '{print $1$2}'|sed 's/^.*[^0-9]\([0-9]\{1,3\}\)\.\([0-9]\{1,3\}\)\.\([0-9]\{1,3\}\)\.\([0-9]\{1,3\}\)$/\1\.\2\.\3\.\4/g'`
PORT=8500
case $1 in
  leader)
    result=$($CURL -s http://${IP}:${PORT}/v1/status/leader)
    echo ${result}
    ;;
  peers)
    result=$($CURL -s http://${IP}:${PORT}/v1/status/peers|awk -F'"' '{print $2 "\n" $4 "\n" $6}'|wc -l)
    echo ${result}
    ;;
  *)
    echo "Usage:$0(leader|peers)"
    ;;
esac
