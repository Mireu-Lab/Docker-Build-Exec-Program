# Docker Build Exec Program

## 실행방법

이 프로그램은 아래와 같은 순서대로 작동을 시켜주세요
```shell
# 기본 설치 프로그램 세팅
sudo sh Install/install.sh

# API 코드 실행
sudo python3 App/main.py 
```

해당 프로그램들은 관리자 권한이 반드시 필요하며 
실행전 sudo 을 안빠져있는지 확인후 세팅 해주세요.

## 사용법

- CURL 파이썬 요청

```
curl -X 'POST' \
  'http://testing.mireu.xyz/check' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@main.py;type=application/x-python'
```



- CURL 자바스크립트 요청

```
curl -X 'POST' \
  'http://testing.mireu.xyz/check' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@main.js;type=application/x-javascript'
```



## 도커 컨테이너 이미지

| 언어       | 도커 허브 URL                    | 구현 형태 (T/F) |      |
| ---------- | -------------------------------- | --------------- | ---- |
| Python     | https://hub.docker.com/_/python  | True            |      |
| Javascript | https://hub.docker.com/_/node    | True            |      |
| Golang     | https://hub.docker.com/_/golang  | True            |      |
| Ruby       | https://hub.docker.com/_/ruby    | False           |      |
| Java       | https://hub.docker.com/_/openjdk | False           |      |
| Php        | https://hub.docker.com/_/php     | False           |      |
| Gcc        | https://hub.docker.com/_/gcc     | True            |      |
| Rust       | https://hub.docker.com/_/rust    | False           |      |
| R          | https://hub.docker.com/_/r-base  | False           |      |
