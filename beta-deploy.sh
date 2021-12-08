echo "---------- BETA SCRIPT DEPLOY ----------"
echo "Start deploy script for BETA"
scp -i /Users/florian/.ssh/greenit-aws-beta.pem .env.beta ubuntu@13.38.18.186:/var/www/greenit-backend
scp -i /Users/florian/.ssh/greenit-aws-beta.pem /Users/florian/Desktop/greenit-webapp/.env.beta.front ubuntu@13.38.18.186:/var/www/greenit-backend

echo "---------- END SCRIPT BETA DEPLOY ----------"
