## Shut down all services, keep network
sudo docker-compose down

# Kill containers of people who logged out without stopping their servers
sudo docker kill $(sudo docker ps -q)

## remove stopped containers
sudo docker rm $(sudo docker ps -aq)

