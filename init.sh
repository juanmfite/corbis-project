#!/bin/bash

docker-compose up -d db

echo "Esperando a Postgres..."

sleep 2

docker cp corbis-stock.dump $(docker-compose ps -q db):corbis-stock.dump

docker exec -i $(docker-compose ps -q db) psql -U postgres postgres < corbis-stock.dump

docker-compose up -d web
