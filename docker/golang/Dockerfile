FROM golang:1.17

WORKDIR /home
COPY ./info.go ./run.go

RUN "ls" 

RUN cat run.go

CMD [ "go","run","run.go" ]