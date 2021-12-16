#!/usr/bin/env bash


git fetch
git checkout develop

echo -e "Start pull"
git pull origin develop;
# Docker
echo -e "Run docker"

docker stop core_web
docker stop core_app
docker-compose -f docker-compose.prod.yml up -d --build
until [ "`docker inspect -f {{.State.Running}} core_app`"=="true" ]; do
    sleep 0.1;
done;
exit 0;