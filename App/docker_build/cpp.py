from time import sleep, time
import docker
import os
import json

client = docker.from_env()

def build(filename):
    data = json.load(open("Data/set.json", 'r'))

    build_start = time() # 컨테이너 빌드 시간
    
    # 컨테이너 종류 / 컨테이너 실행
    docker_contalner = str(client.containers.create(data['cpp']).id) 
    os.system(f"docker cp Data/user_file/{filename} {docker_contalner}:home/run.cpp") # 컨테이너에 파일 전송
    
    build_end = time() # 컨테이너 빌드 종료 시간

    data = client.containers.get(docker_contalner)
    
    data.restart() # 컨테이너 재시작
    
    run_start = time() # 프로그램 실행 시간
    
    data.wait() # 프로그램 실행 동작확인
    
    return_date = data.logs() # 프로그램 실행 결과

    run_end = time() # 프로그램 종료 시간

    data.remove() # 컨테이너 삭제

    return {
        "test build language" : "cpp/gcc", 
        "container build time" : round(build_end - build_start, 3), 
        "file execution time" : round(run_end - run_start, 3), 
        "file result" : return_date
    }