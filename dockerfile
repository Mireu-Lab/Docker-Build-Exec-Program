FROM python:3

RUN mkdir app
WORKDIR /app

COPY ../../ .

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y docker docker.io

RUN pip3 install -r Install/requirements.txt

CMD [ "python3", "App/main.py" ]