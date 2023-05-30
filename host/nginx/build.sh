#! /usr/bin/env bash

sudo systemctl stop gunicorn.service
sudo docker stop nginx-nginx-1

cd /srv/nginx/tuxTech/src

git pull origin main
source ./venv/bin/activate

cd /srv/nginx/tuxTech/src
# makemigrations
./venv/bin/python3 ./manage.py collectstatic

cd /srv/nginx/

sudo docker rm nginx-nginx-1
sudo docker build --no-cache -t nginx-container .
sudo docker compose up -d
sudo systemctl daemon-reload
sudo systemctl start gunicorn.service
