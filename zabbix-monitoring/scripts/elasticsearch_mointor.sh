#!/bin/bash
# date 2018-11-21
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
#
CURL="$(which curl)"
PORT=9200
case $1 in
  Alls)
    all=$("${CURL}" -s -XGET 'http://127.0.0.1:9200/_cluster/health?pretty' |grep "$2"|awk -F '[ "|,]+' '{print $4}')
    echo ${all}
    ;;
  status)
    pid=$(ps -ef |grep elasticsearch|grep -v grep|wc -l)
    echo ${pid}
    ;;
  *)
  echo "Usage:$0(Alls|status)"
esac
