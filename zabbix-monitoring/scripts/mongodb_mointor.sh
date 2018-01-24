#!/bin/bash
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
# zabbix monitors mongodb
# mongodb enabled account authentication
# Define account connection information
# This script is for monitoring mongodb 3.4 version, zabbix version is 3.2.9
# mongodb is to set up a replica set (replica set) shard shard if later used in the introduction of the update。Part of the parameters optimization
MoUser=""
MoPwd=""
MoDb="admin"
# Define mongodb command variables
MONG="$(which mongo)"
#######
#echo "db.serverStatus().$1" | mongo -u "${MoUser}" -p "${MoPwd}" --authenticationDatabase "${MoDb}"|awk 'NR==4'
case $1 in
  Single)
    single=$(echo "db.serverStatus().$2" | mongo -u "${MoUser}" -p "${MoPwd}" --authenticationDatabase "${MoDb}"|awk 'NR==4')
    echo ${single}
    ;;
  Alls)
    all=$(echo "db.serverStatus().$2" | mongo -u "${MoUser}" -p "${MoPwd}" --authenticationDatabase "${MoDb}"|egrep -E "\b$3\b"|awk -F "" '{for (i=1;i<=NF;i++){if ($i ~ /[0-9]/){str=$i;str1=(str1 str)}} print str1}')
    echo ${all}
    ;;
  *)
    echo "Usage:$0(Alls|Single)"
esac
