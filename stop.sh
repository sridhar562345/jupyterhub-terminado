## Shut down all services, keep network
docker-compose down

# Kill containers of people who logged out without stopping their servers
docker kill $(docker ps -q)

## Tidy up everything
docker system prune --all

