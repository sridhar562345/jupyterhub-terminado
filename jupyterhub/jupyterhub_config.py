import os
import json
import logging
import sys
import requests
from tornado import gen
from jupyterhub.auth import Authenticator
import tmpauthenticator
# import awsspawner

c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': 'python3 cull_idle_servers.py --timeout=360'.split(),
    }
]

# General
c.JupyterHub.authenticator_class = tmpauthenticator.TmpAuthenticator
# c.Authenticator.admin_users = {'root'}
c.JupyterHub.spawner_class = 'awsspawner.EcsTaskSpawner'
c.DockerSpawner.image = os.environ['DOCKER_NOTEBOOK_IMAGE']
c.DockerSpawner.debug = True
# c.Spawner.base_url = ''


# Networking
c.Spawner.strategy = 'ECSxEC2SpawnerHandler'
c.Spawner.strategy_parms = {
    'cluster_name': 'notebook-cluster',
    'ec2_instance_template': 'jupyterhub-launch-template',
    'ecs_task_definition': 'terminado',
    'port': 8000
}
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8080

