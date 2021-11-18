#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_DB_HOST $POSTGRES_DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#python manage.py flush --no-input
python manage.py migrate

exec "$@"