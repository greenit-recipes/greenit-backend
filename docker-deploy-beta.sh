#!/usr/bin/env bash

TARGET='test'

# cd ~/app || exit à changer avec un repo qui sera au dessus

ACTION='\033[1;90m'
NOCOLOR='\033[0m'

echo "Start script"
git checkout test 
git fetch
# If that's not the case, we pull the latest changes and we build a new image

echo "Start pull"
git pull origin main;

# We pull front
FILE=react/build
if [ -f "$FILE" ]; then
    rm -rf react/build
    mkdir react/
else 
    mkdir react/
fi
echo "Pull Front"
git clone https://github.com/greenit-recipes/greenit-webapp
cp .env.beta.front greenit-webapp/.env
cd greenit-webapp/
git checkout develop
yarn install --frozen-lockfile
npm run build
mv build ../react/
cd ..
rm -rf greenit-webapp/

# Docker
echo "Run docker"

docker-compose -f docker-compose.beta.yml up -d --build

exit 0;