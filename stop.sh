## Shut down all services, keep network
sudo docker-compose down

# Kill containers of people who logged out without stopping their servers
sudo docker kill $(sudo docker ps -q)

## Tidy up everything
sudo docker system prune --all

