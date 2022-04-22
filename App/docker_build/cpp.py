from time import sleep, time
import docker
import os
import json

client = docker.from_env()

def build(filename):
    data = json.load(open("Data/set.json", 'r'))

    build_start = time()
    docker_contalner = str(client.containers.create(data['cpp']).id)

    os.system(f"docker cp Data/user_file/{filename} {docker_contalner}:home/run.cpp")

    data = client.containers.get(docker_contalner)
    data.restart()
    build_end = time()

    sleep(1)

    run_start = time()
    return_data = data.logs()
    data.remove()
    run_end = time()
    
    return {"test build language" : "cpp/gpp", "container build time" : build_end - build_start, "file execution time" : run_end - run_start, "file result" : return_data}