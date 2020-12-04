# needed by dockerspawner -> jupyterhub-config
docker network create jupyterhub-network

# if it fails after this point, we should know about it
set -e

# terminado image to spawn for every user
docker build --no-cache -t terminado:latest ./terminado/

# set up jupyterhub server
docker-compose build --no-cache
docker-compose up -d

sleep 10s

# python create_users.py
