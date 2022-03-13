from time import sleep
import docker
import os
import json

client = docker.from_env()

def build(filename):
    data = json.load(open("Data/set.json", 'r'))

    docker_contalner = str(client.containers.create(data['javascript']).id)

    os.system(f"docker cp Data/user_file/{filename} {docker_contalner}:home/run.js")

    data = client.containers.get(docker_contalner)
    data.restart()

    sleep(1)

    return_data = data.logs()
    data.remove()
    return return_data