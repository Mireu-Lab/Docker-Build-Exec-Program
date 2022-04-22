from time import sleep, time
import docker
import os
import json

client = docker.from_env()

def build(filename):
    data = json.load(open("Data/set.json", 'r'))

    build_start = time() # 컨테이너 빌드 시간
    docker_contalner = str(client.containers.create(data['golang']).id) # 컨테이너 종류 / 컨테이너 실행

    os.system(f"docker cp Data/user_file/{filename} {docker_contalner}:home/run.cpp") # 컨테이너에 파일 전송
    build_end = time() # 컨테이너 빌드 종료 시간

    data = client.containers.get(docker_contalner)
    data.restart() # 컨테이너 재시작

    sleep(1) # 1초 딜레이

    run_start = time() # 프로그램 실행 시간
    
    return_data = data.logs() # 프로그램 실행
    
    run_end = time() # 프로그램 종료 시간
    
    data.remove() # 컨테이너 삭제
    
    return {"test build language" : "python", "container build time" : build_end - build_start, "file execution time" : run_end - run_start, "file result" : return_data}