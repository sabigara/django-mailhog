#!/usr/bin/env bash

while ! mysqladmin ping -h"db:3306" --silent; do
    sleep 1
done

python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000