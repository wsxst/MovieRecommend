#!/bin/bash
docker rm -f $(docker ps -q)
docker-compose up -d
