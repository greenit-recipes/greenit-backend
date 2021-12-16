echo "---------- PROD SCRIPT DEPLOY ----------"
echo "Build on local machine - BACK NEED TO BE RUN TO WORK"
set -e

echo "Tu va mettre en production c'est good pour toi ? (y/n)? "
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    cd /Users/florian/Desktop/greenit-webapp
    git checkout develop
    git pull
    if [ -z "$(git status -uno --porcelain)" ]; then 
        echo "Le dossier est clean (front)"
    else 
        echo "Il reste des fichiers pas commit"
        exit 0
    fi
    reslog=$(git log HEAD..origin/develop --oneline)
    if [[ "${reslog}" != "" ]] ; then
        echo "Il reste des fichiers pas push ou pull (front)"
        exit 0
    fi
    yarn install
    npm run build:prod
    scp -ri /Users/florian/.ssh/aws_prod.pem /Users/florian/Desktop/greenit-webapp/build ubuntu@15.188.47.157:/var/www/greenit-backend/react

    if [ $1 ]
    then
        exit 0
    fi
    echo "transfert .env"
    scp -i /Users/florian/.ssh/aws_prod.pem /Users/florian/Desktop/greenit-backend/.env.prod ubuntu@15.188.47.157:/var/www/greenit-backend
    echo "---------- Run docker deploy ----------"
    ssh -ti /Users/florian/.ssh/aws_prod.pem ubuntu@15.188.47.157 "pwd && cd /var/www/greenit-backend && ./docker-deploy-prod.sh"
    echo "---------- END SCRIPT PROD DEPLOY ----------"
else
    echo "Exit"
fi