echo "---------- BETA SCRIPT DEPLOY ----------"
echo "transfert .env"
scp -i /Users/florian/.ssh/greenit-aws-beta.pem .env.beta ubuntu@13.38.18.186:/var/www/greenit-backend
scp -i /Users/florian/.ssh/greenit-aws-beta.pem /Users/florian/Desktop/greenit-webapp/.env.beta.front ubuntu@13.38.18.186:/var/www/greenit-backend
echo "---------- Run docker deploy ----------"
ssh -ti /Users/florian/.ssh/greenit-aws-beta.pem ubuntu@13.38.18.186 "./docker-deploy-beta.sh"
echo "---------- END SCRIPT BETA DEPLOY ----------"
