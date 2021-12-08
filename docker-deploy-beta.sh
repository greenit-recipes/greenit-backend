#!/usr/bin/env bash


# cd ~/app || exit à changer avec un repo qui sera au dessus

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
pwd
until [ "`docker inspect -f {{.State.Running}} core_app`"=="true" ]; do
    sleep 0.1;
done;
# We pull front
FILE=./react/build
if [ -f "$FILE" ]; then
    echo -e "${ACTION}Service, it's not running."
    rm -rf ./react
    mkdir react
else 
    mkdir react
fi
echo -e "${ACTION}Pull Front"
FILE_WEB_APP= ./greenit-webapp
if [ -f "$FILE_WEB_APP" ]; then
    echo "------ FILE EXIST DELETE ------"
    rm -rf FILE_WEB_APP
fi
git clone https://github.com/greenit-recipes/greenit-webapp
cp .env.beta.front greenit-webapp/.env
cd greenit-webapp/
git checkout develop
yarn install --frozen-lockfile
echo -e "${ACTION}Run build front"
npm run build
mv build ../react/
cd ..
rm -rf greenit-webapp/
exit 0;