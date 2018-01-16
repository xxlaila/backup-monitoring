#!/bin/bash
# Shell script to backup MySQL database
# bin-log is not currently

# Set these variables
MyUSER=""
MyPASS=""
MyHOST="localhost"

# mysql-bin directory
HISBINLOGS=/opt/data

# Backup Dest directory
DEST="/data/mysql/mysql_backup"
BINLOGS="/data/mysql/mysql_binlogs"

# Email for notifications
EMAIL=""

# How many days old files must be to be removed
DAYS=7

# Linux bin paths
MYSQL="$(which mysql)"
MYSQLDUMP="$(which mysqldump)"
GZIP="$(which gzip)"

# Get date in dd-mm-yyyy format
NOW="$(date +"%Y%m%d_%H%M%S")"

# Create Backup sub-directories
MBD="$DEST/$NOW"
install -d $MBD

# DB skip list
# SKIP="performance_schema mysql information_schema"

# Get all databases
DBS=`$MYSQL -h $MyHOST -u $MyUSER -p$MyPASS -Bse "show databases;"| grep -Ev "(Database|information_schema|performance_schema|mysql)"`

# Archive database dumps
for db in $DBS
do
        FILE="$MBD/$db.sql"
        $MYSQLDUMP -h $MyHOST -u $MyUSER -p$MyPASS --single-transaction $db >$FILE
done

# Archive the directory, send mail and cleanup
cd $DEST
tar -cf mysql_$NOW.tar $NOW
$GZIP -9 mysql_$NOW.tar

$echo "MySQL backup is completed! Backup name is mysql_$NOW.tar.gz" | mail -s "MySQL backup" $EMAIL
rm -rf $NOW

# Remove old files
find $DEST -mtime +$DAYS -exec rm -f {} \;

