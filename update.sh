#!/usr/bin/env bash

echo "1/5 Pulling updates..."
git pull

echo "2/5 re-Building containers"
docker-compose build --no-cache

echo "3/5 Restarting containers"
docker-compose up -d

echo "4/5 Cleaning system"
docker system prune -f

echo "5/5 Applying migrations"
docker exec -it ${DB_HOST} python3 ./marriage_agency/manage.py migrate

