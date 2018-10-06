#!/usr/bin/env bash
sleep 6s

echo 'Starting Django-API application, with db:'
echo $DB_POSTGRES_DATABASE_NAME

python3 manage.py runserver 0.0.0.0:9000
