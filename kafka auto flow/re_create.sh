#!/bin/sh 

docker-compose stop 
docker-compose rm -y 
docker-compose up -d --build