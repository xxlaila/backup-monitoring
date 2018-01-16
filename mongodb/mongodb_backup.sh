#!/bin/bash
# sco mongodb database backup
# This script backup is a backup mongodb copy mode, three nodes, A is primary, BC is secondary
# mongodb in the backup copy set will automatically select an available secondary backup
# In the backup copy set is the need to add --oplog
# --oplog Specific please refer to: Https://Docs.Mongodb.Com/v3.4/Reference/program/mongodump/

# Define mongodb information
MONG_HOST="1.1.1.1:27011,1.2.2.2:27011,1.3.3.3:27011"
MONG_USER=""
MONG_PASS=""
MONG_REP="test01"

# Get mongodb shell information
MONGODUMP="$(which mongodump)"
GZIP="$(which gzip)"

# Get system time
NOW="$(date +"%Y%m%d_%H%M%S")"

# How many days old files must be to be removed
DAYS=7

# Define mongodb backup directory
BACKUP_DIR="/data/mongodb"

# Get the current system time
NEW_TIME="$(date +"%Y%d%m_%H%M%S")"

MDBS="${BACKUP_DIR}/${NOW}"
install -d ${MDBS}

# Start backup
${MONGODUMP} -h "${MONG_REP}/${MONG_HOST}" -u${MONG_USER} -p${MONG_PASS} --oplog -o ${MDBS}

# Compress the current backup database
cd ${BACKUP_DIR}
tar -zcf mongodb_${NOW}.tar.gz ${NOW}
$GZIP -9 mongodb_$NOW.tar

rm -rf $NOW

# Remove old files
find $BACKUP_DIR -mtime +$DAYS -exec rm -f {} \;
