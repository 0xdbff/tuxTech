#!/usr/bin/env bash

TIMESTAMP=$(date +"%F")
BACKUP_DIR="/srv/nginx/tuxTech/backup"
DJANGO_DIR="/srv/nginx/tuxTech/src"

source /srv/nginx/tuxTech/src/env/bin/activate

cd $DJANGO_DIR

python manage.py dumpdata > $BACKUP_DIR/db-$TIMESTAMP.json
gzip $BACKUP_DIR/db-$TIMESTAMP.json
