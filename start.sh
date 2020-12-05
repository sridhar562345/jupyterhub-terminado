# needed by dockerspawner -> jupyterhub-config
sudo docker network create jupyterhub-network

# if it fails after this point, we should know about it
set -e

# terminado image to spawn for every user
sudo docker build -t terminado:latest ./terminado/

# set up jupyterhub server
sudo docker-compose build
sudo docker-compose up -d

sleep 10s

# python create_users.py
