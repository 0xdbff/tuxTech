#!/bin/bash
echo "Creating config files"
mkdir -p /tmp/docker-mailserver/
touch /tmp/docker-mailserver/postfix-accounts.cf
echo "Configuring mail server"
sudo docker compose up -d mailserver
