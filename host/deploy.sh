#! /usr/bin/env bash

sudo systemctl stop gunicorn.service
sudo docker stop nginx-nginx-1

cd /srv/nginx/tuxTech/src
source ./venv/bin/activate

./venv/bin/python3 ./manage.py makemigrations
./venv/bin/python3 ./manage.py migrate
./venv/bin/python3 ./manage.py collectstatic

cd /srv/nginx/tuxTech/src/website/src/

npm install
npm run build

cd /srv/nginx/

sudo docker start nginx-nginx-1
sudo systemctl start gunicorn.service
