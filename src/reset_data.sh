#!/usr/bin/env bash

rm -rf ./product/migrations/0* && echo "Removed product migrations" || echo "Failed to remove product migrations"
rm -rf ./cart/migrations/0* && echo "Removed cart migrations" || echo "Failed to remove cart migrations"
rm -rf ./favourites/migrations/0* && echo "Removed favourites migrations" || echo "Failed to remove favourites migrations"
rm -rf ./users/migrations/0* && echo "Removed users migrations" || echo "Failed to remove users migrations"
rm -rf ./blog/migrations/0* && echo "Removed blog migrations" || echo "Failed to remove blog migrations"
rm -rf ./enterpriseStore/migrations/0* && echo "Removed ES migrations" || echo "Failed to remove ES migrations"
rm -rf ./store/migrations/0* && echo "Removed Store migrations" || echo "Failed to remove Store migrations"
rm -rf ./support/migrations/0* && echo "Removed support migrations" || echo "Failed to remove support migrations"
rm -rf ./supply/migrations/0* && echo "Removed supply migrations" || echo "Failed to remove supply migrations"
rm -rf ./order/migrations/0* && echo "Removed order migrations" || echo "Failed to remove order migrations"

sudo -u postgres dropdb djangodev && echo "Dropped database djangodev" || echo "Failed to drop database djangodev"
sudo -u postgres createdb djangodev && echo "Created database djangodev" || echo "Failed to create database djangodev"

# check if venv exists, if not create it and install requirements
if [ ! -d "venv" ]; then
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
else
  source venv/bin/activate
fi

python manage.py makemigrations
python manage.py migrate

# import cities
# python manage.py cities --import=country
# python manage.py cities --import=city
