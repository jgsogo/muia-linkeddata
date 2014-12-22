#!/bin/bash
set -e
LOGFILE=/home/javi/projects/muia_linkeddata/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)

# user/group to run as
USER=javi
GROUP=javi
cd /home/javi/projects/muia_linkeddata/webapp/
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn -c gunicorn.conf.py \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE linkeddata.wsgi:application

