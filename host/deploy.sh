#! /usr/bin/env bash

# export DJANGO_SETTINGS_MODULE=storeServer.settings.prod

sudo systemctl stop gunicorn.service
sudo docker stop nginx-nginx-1

cd /srv/nginx/tuxTech/src

git pull origin main
source ./venv/bin/activate

cd /srv/nginx/tuxTech/src/website
source ~/.nvm/nvm.sh
nvm use --lts
npm install
npm run build

cd /srv/nginx/tuxTech/src
# makemigrations
# ./venv/bin/python3 ./manage.py collectstatic
DJANGO_SETTINGS_MODULE=storeServer.settings.prod ./venv/bin/python3 ./manage.py collectstatic

cd /srv/nginx/

sudo docker rm nginx-nginx-1
sudo docker build  -t nginx-container .

sudo docker compose up -d
sudo systemctl daemon-reload
sudo systemctl start gunicorn.service
