#!/usr/bin/env bash

while ! mysqladmin ping -h db --silent; do
    echo 'Waiting for mysql startup...'
    sleep 3
done

python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000