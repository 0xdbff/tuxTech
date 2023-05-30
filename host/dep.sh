#!/usr/bin/env bash

# Node and python should be installed on the server system
sudo apt update
sudo apt install gdal-bin libgdal-dev libpq-dev python3-dev build-essential postgis 

# TODO! latex dependencies... installation...

# Website server
sudo apt install certbot python3-certbot-nginx nginx certbot

# Email server
# sudo apt-get install postfix postfix-pgsql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-pgsql certbot

# Setup postgres (naive)
sudo -u postgres psql -d postgres -c "CREATE DATABASE djangodev;"
sudo -u postgres psql -d postgres -c "CREATE EXTENSION postgis;"    # READ THIS COMMENTS!
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '123';" # please CHANGE password for production.
								    # !PLEASE!
								    # DID you read the comments?
