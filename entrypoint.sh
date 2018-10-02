#!/usr/bin/env bash
sleep 5s
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:9000
