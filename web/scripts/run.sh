#!/usr/bin/env bash

scripts/wait-for-it.sh db:3306
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000