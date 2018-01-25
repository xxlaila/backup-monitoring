#!/bin/bash
# This script is for a single port
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
REDISPATH="$(which redis-cli)"
HOST="127.0.0.1"
PORT=""
PWD=""
REDIS_INFO="$REDISPATH -h $HOST -p $PORT -a ${PWD} info"
case $1 in
  cluster)
    result=$($REDIS_INFO|/usr/bin/egrep -E "\b$2\b"|awk -F":" '{print $NF}'|awk -F "" '{for (i=1;i<=NF;i++){if ($i ~ /[0-9.]/){str=$i;str1=(str1 str)}} print str1}')
    echo $result
    ;;
esac
