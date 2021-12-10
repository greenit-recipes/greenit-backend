echo "---------- BETA SCRIPT DEPLOY ----------"
echo "Build on local machine - BACK NEED TO BE RUN TO WORK"
cd /Users/florian/Desktop/greenit-webapp
git checkout develop
git pull
yarn install
npm run build:beta
scp -ri /Users/florian/.ssh/greenit-aws-beta.pem /Users/florian/Desktop/greenit-webapp/build ubuntu@13.38.18.186:/var/www/greenit-backend/react

echo "transfert .env"
scp -i /Users/florian/.ssh/greenit-aws-beta.pem /Users/florian/Desktop/greenit-backend/.env.beta ubuntu@13.38.18.186:/var/www/greenit-backend
echo "---------- Run docker deploy ----------"
ssh -ti /Users/florian/.ssh/greenit-aws-beta.pem ubuntu@13.38.18.186 "pwd && cd /var/www/greenit-backend && ./docker-deploy-beta.sh"
echo "---------- END SCRIPT BETA DEPLOY ----------"
