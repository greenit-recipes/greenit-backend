#!/usr/bin/env bash

ACTION='\033[0;31m'
NOCOLOR='\033[0m'

git fetch
git checkout develop
# If that's not the case, we pull the latest changes and we build a new image

echo -e "${ACTION}Start pull"
git pull origin develop;

# Docker
echo -e "${ACTION}Run docker"

docker stop core_web
docker stop core_app
docker-compose -f docker-compose.beta.yml up -d --build
until [ "`docker inspect -f {{.State.Running}} core_app`"=="true" ]; do
    sleep 0.1;
done;
exit 0;