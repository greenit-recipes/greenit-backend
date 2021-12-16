echo "---------- PROD SCRIPT DEPLOY ----------"
echo "Build on local machine - BACK NEED TO BE RUN TO WORK"
set -e

echo "Tu va mettre en production c'est good pour toi ? (y/n)? "
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    echo "pd"
else
    echo "pas bon"
fi