#!/usr/bin/env bash


git fetch
git checkout develop

echo -e "Start pull"
git pull origin develop;
# Docker
echo -e "Run docker"

docker stop core_web
docker stop core_app
echo -e "RUN DOCKER COMPOSE SUR LE SERVEUR POUR QUE CA MARCHE"
df . -h
exit 0;