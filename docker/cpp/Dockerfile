FROM gcc:latest

WORKDIR /home
COPY ./info.cpp ./run.cpp
COPY ./run.sh ./run.sh

RUN "ls" 

RUN cat run.cpp

CMD ["sh","run.sh"]